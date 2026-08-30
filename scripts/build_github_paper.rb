#!/usr/bin/env ruby
# frozen_string_literal: true

# GitHub stops rendering math after a page-scale request ceiling. Keep every
# display equation, typeset operational inline expressions, and show repeated
# symbol-only references as exact monospace notation.

SOURCE = File.expand_path("../build/paper.md", __dir__)
TARGET = File.expand_path("../paper.md", __dir__)
MAX_INLINE_MATH = 330

source = File.read(SOURCE, encoding: "UTF-8")
inline_pattern = /(?<!\$)\$([^\n$]+)\$(?!\$)/

operational = lambda do |expression|
  expression.length > 35 ||
    expression.match?(/[=<>]/) ||
    expression.match?(/\\(?:le|ge|neq|in|notin|subset|supset|equiv|approx|propto|sim|mid|to|mapsto)(?![A-Za-z])/)
end

expressions = source.scan(inline_pattern).flatten
required = expressions.count { |expression| operational.call(expression) }
if required > MAX_INLINE_MATH
  abort "GitHub inline-math budget is too small: #{required} required expressions"
end

optional_budget = MAX_INLINE_MATH - required
optional_seen = {}
optional_kept = 0
inside_display = false

github = source.each_line.map do |line|
  if line.strip == "$$"
    inside_display = !inside_display
    inside_display ? "```math\n" : "```\n"
  elsif inside_display
    line
  else
    line.gsub(inline_pattern) do
      expression = Regexp.last_match(1)
      keep = operational.call(expression)
      unless keep
        if !optional_seen.key?(expression) && optional_kept < optional_budget
          optional_seen[expression] = true
          optional_kept += 1
          keep = true
        end
      end
      if keep
        "$`#{expression}`$"
      else
        "`#{expression}`"
      end
    end
  end
end.join

abort "Unbalanced display-math delimiters" if inside_display

note = <<~MARKDOWN

  _GitHub rendering note: display equations and operational inline expressions are typeset. Repeated symbol-only references use exact monospace notation to keep this single-file edition below GitHub's per-page math-rendering ceiling. The PDF remains fully typeset._
MARKDOWN

scope = "_Public working paper. Initial implementation evidence is reported in Section 9; full real-world validation remains outstanding._\n"
abort "Paper scope marker not found" unless github.include?(scope)

github = github.sub(scope, scope + note)
File.write(TARGET, github, encoding: "UTF-8")

display_count = github.scan(/^```math$/).length
inline_count = github.scan(inline_pattern).length
total = display_count + inline_count
abort "GitHub math budget exceeded: #{total}" if total > 540

warn "GitHub paper: #{display_count} display + #{inline_count} inline = #{total} math nodes"
