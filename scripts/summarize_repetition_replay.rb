#!/usr/bin/env ruby
# frozen_string_literal: true

require "json"
require "digest"
require "fileutils"

root = ARGV.fetch(0)
target = File.expand_path("../evidence/repetition-gate-v1/replay-summary.json", __dir__)
metrics = %w[brier expected_calibration_error priority_weighted_brier recall_at_10 packed_recall mean_packed_count mean_used_tokens].freeze
rows = []
%w[openclaw codex chatgpt].each do |source|
  %w[design confirmation].each do |block|
    relative = "#{source}/#{block}-report.json"
    paths = [File.join(root, "control", relative), File.join(root, relative)]
    bytes = paths.map { |path| File.binread(path) }
    before, after = bytes.map { |value| JSON.parse(value) }
    %w[cases trajectories evaluation_block].each do |field|
      raise "Unmatched #{relative}: #{field}" unless before.fetch(field) == after.fetch(field)
    end
    raise "Unexpected case count" unless after.fetch("cases").is_a?(Integer)
    raise "Unmatched variants" unless before.fetch("variants").keys.sort == after.fetch("variants").keys.sort
    variants = after.fetch("variants").keys.sort.to_h do |variant|
      pairs = metrics.to_h do |metric|
        values = [before, after].map { |report| report.fetch("variants").fetch(variant).fetch(metric) }
        raise "Non-finite aggregate" unless values.all? { |value| value.is_a?(Numeric) && value.finite? }
        [metric, { "before" => values[0], "after" => values[1], "delta" => values[1] - values[0] }]
      end
      [variant, pairs]
    end
    rows << { "source" => source, "block" => block, "cases" => after.fetch("cases"),
              "trajectories" => after.fetch("trajectories"),
              "aggregate_report_sha256" => bytes.map { |value| Digest::SHA256.hexdigest(value) },
              "variants" => variants }
  end
end
summary = {
  "schema" => "eventframe.repetition-regression.v1",
  "replay_date" => "2026-09-02",
  "control_revision" => "aca468a",
  "guard_revision" => "74ccb92",
  "scope" => "Retrospective reused historical splits; local in-memory/hash-embedding replay, not live vector-store or LLM end-to-end evaluation. Zero-case rows are unevaluated, not perfect scores.",
  "inference" => "Descriptive paired aggregates; no preregistered poisoning-success test or new confirmation claim.",
  "privacy" => "Whitelist of aggregate metrics and report checksums only; no text, event IDs, session IDs, embeddings, or claim hashes.",
  "total_cases" => rows.sum { |row| row.fetch("cases") },
  "rows" => rows
}
FileUtils.mkdir_p(File.dirname(target))
File.write(target, JSON.pretty_generate(summary) + "\n")
puts "Wrote #{rows.length} aggregate rows, #{summary.fetch('total_cases')} cases"
