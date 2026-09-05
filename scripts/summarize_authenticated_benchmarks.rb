#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"
require "digest"

root = File.expand_path("..", __dir__)
directory = File.join(root, "evidence", "authenticated-outcomes-v1")
input = File.join(directory, "authenticated-evidence-benchmark.txt")
raw = File.read(input)
abort "Incomplete benchmark campaign" unless raw.scan(/^PASS$/).length == 3 && !raw.match?(/^FAIL/)
rows = raw.lines.map do |line|
  next unless line.start_with?("Benchmark")
  name, iterations, *tokens = line.split
  abort "Invalid metric pairs" unless tokens.length.even?
  metrics = tokens.each_slice(2).to_h { |value, unit| [unit, Float(value)] }
  { "benchmark" => name, "iterations" => Integer(iterations), "metrics" => metrics }
end.compact
abort "Unexpected repetitions" unless rows.length == 45 && rows.all? { |row| row["iterations"] == 500 }
summary = rows.group_by { |row| row["benchmark"] }.map do |name, group|
  abort "Missing repeated run: #{name}" unless group.length == 3
  means = group.map { |row| row["metrics"].fetch("ns/op") }.sort
  p99 = group.map { |row| row["metrics"]["p99-ns"] }.compact
  maxima = group.map { |row| row["metrics"]["max-ns"] }.compact
  { "benchmark" => name, "median_run_mean_ns_per_op" => means[1],
    "p99_range_ns" => p99.empty? ? nil : p99.minmax,
    "max_reported_request_ns" => maxima.max }
end
report = {
  "schema" => "eventframe-authenticated-outcome-timing-v1",
  "runtime_commit" => "d5cda75",
  "date" => "2026-09-05", "machine" => "Apple M4 darwin/arm64",
  "go_version" => "go1.27.0", "corpus_events" => 50,
  "embedding" => "32-dimensional local hash", "recall_k" => 50, "pack_k" => 10,
  "mixed_recall_fraction" => 0.75,
  "boundary" => "Internal service calls; includes lock/storage waits, excludes observer signing and fixture setup. Not a production SLA or accuracy trial.",
  "input_sha256" => Digest::SHA256.hexdigest(raw), "runs" => rows, "summaries" => summary
}
File.write(File.join(directory, "timings.json"), JSON.pretty_generate(report) + "\n")
puts "Validated and summarized #{rows.length} benchmark rows"
