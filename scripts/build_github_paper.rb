#!/usr/bin/env ruby
# frozen_string_literal: true

# GitHub stops rendering math after a page-scale request ceiling. Keep every
# display equation, typeset operational inline expressions, and show repeated
# symbol-only references as exact monospace notation.

SOURCE = File.expand_path("../build/paper.md", __dir__)
TARGET = File.expand_path("../paper.md", __dir__)
MAX_INLINE_MATH = 150
FRONT_MATTER_INLINE_MATH = 20

source = File.read(SOURCE, encoding: "UTF-8")
inline_pattern = /(?<!\$)\$([^\n$]+)\$(?!\$)/

expressions = source.scan(inline_pattern).flatten
relation = /[=<>]|\\(?:le|ge|neq|in|notin|subset|supset|equiv|approx|propto|sim|mid|to|mapsto)(?![A-Za-z])/
selected_indices = (0...[FRONT_MATTER_INLINE_MATH, expressions.length].min).to_a
seen = expressions.first(FRONT_MATTER_INLINE_MATH).to_h { |expression| [expression, true] }
candidates = []
expressions.each_with_index do |expression, index|
  next if index < FRONT_MATTER_INLINE_MATH || seen.key?(expression)

  seen[expression] = true
  score = expression.length
  score += 60 if expression.match?(relation)
  score += 30 if expression.length > 35
  candidates << [score, index]
end
selected_indices.concat(
  candidates
    .sort_by { |score, index| [-score, index] }
    .first(MAX_INLINE_MATH - selected_indices.length)
    .map(&:last)
)
selected_indices = selected_indices.to_h { |index| [index, true] }
inline_index = 0
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
      keep = selected_indices.key?(inline_index)
      inline_index += 1
      if keep
        "$`#{expression}`$"
      else
        "`#{expression}`"
      end
    end
  end
end.join

abort "Unbalanced display-math delimiters" if inside_display

# GitHub appends a slash to a row break in this fenced cases expression. The
# TeX primitive row terminator avoids the resulting three-slash parse failure.
github = github.sub("1,&P_t=N_t,\\\\\n\\mathrm{clip}", "1,&P_t=N_t,\\cr\n\\mathrm{clip}")

note = <<~MARKDOWN

  _GitHub rendering note: display equations and selected inline expressions are typeset. Other inline references use exact monospace notation to keep this single-file edition below GitHub's per-page math-rendering ceiling. The PDF remains fully typeset._
MARKDOWN

scope = "_Public working paper. Initial implementation evidence is reported in Section 9; full real-world validation remains outstanding._\n"
abort "Paper scope marker not found" unless github.include?(scope)

github = github.sub(scope, scope + note)
File.write(TARGET, github, encoding: "UTF-8")

display_count = github.scan(/^```math$/).length
inline_count = github.scan(inline_pattern).length
total = display_count + inline_count
abort "GitHub math budget exceeded: #{total}" if total > 360

warn "GitHub paper: #{display_count} display + #{inline_count} inline = #{total} math nodes"
