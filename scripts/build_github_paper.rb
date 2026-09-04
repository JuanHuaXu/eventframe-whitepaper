#!/usr/bin/env ruby
# frozen_string_literal: true

require "cgi"

# GitHub stops rendering math after a page-scale request ceiling. Keep every
# display equation, typeset selected inline expressions, and render the rest as
# semantic HTML with Unicode mathematical symbols and real sub/superscripts.

SOURCE = File.expand_path("../build/paper.md", __dir__)
TARGET = File.expand_path("../paper.md", __dir__)
MAX_MATH_NODES = 191
MAX_INLINE_MATH = 0
FRONT_MATTER_INLINE_MATH = 0
NATIVE_DISPLAY_MATH = 191

# Keep the governing promotion, descent, and point-composition equations native.
# The indexed semantic fallbacks are simple definitions or already summarized
# in nearby prose; their count preserves GitHub's page-scale math-node budget.
SEMANTIC_DISPLAY_INDICES = [0, 2, 4, 5, 8, 9, 12, 13, 139, 140, 141, 142, 143, 144, 145, 198, 199, 200, 201, 202].freeze
SEMANTIC_DISPLAY_MATH = [
  '<div align="center"><i>e</i><sub>t</sub> = (<i>w</i><sub>t</sub>, <i>a</i><sub>t</sub>, τ<sub>t</sub>, ℓ<sub>t</sub>, <i>m</i><sub>t</sub>, <i>h</i><sub>t</sub>, <i>x</i><sub>t</sub>, <i>c</i><sub>t</sub>).</div>',
  '<div align="center"><i>e</i><sub>t</sub> = Γ<sub>Δ<sub>τ</sub></sub>(ω<sub><i>A</i><sub>t</sub></sub>).</div>',
  '<div align="center"><i>E</i><sub>1:<i>T</i></sub> = (<i>e</i><sub>1</sub>, <i>e</i><sub>2</sub>, …, <i>e</i><sub><i>T</i></sub>).</div>',
  '<div align="center"><i>C</i><sub>t</sub> = <i>e</i><sub><i>t</i>−<i>k</i>+1:<i>t</i></sub>.</div>',
  '<div align="center"><i>Q</i><sub>Δ<sub>τ</sub></sub>: ℝ → 𝒯<sub>Δ<sub>τ</sub></sub>.</div>',
  '<div align="center"><i>C</i><sub>t</sub> = <i>e</i><sub><i>t</i>−<i>k</i>+1:<i>t</i></sub> ∈ ℰ<sup><i>k</i></sup>.</div>',
  '<div align="center">𝖰<sub>θ</sub>(· | <i>C</i><sub>t</sub>) ∈ 𝒫(𝒵<sub><i>H</i></sub>).</div>',
  '<div align="center"><i>d</i><sub><i>H</i></sub>: 𝒫(𝒵<sub><i>H</i></sub>) → 𝒵<sub><i>H</i></sub>.</div>',
  '<div align="center"><i>E</i><sub><i>A</i></sub><sup>(<i>b</i>)</sup> = (<i>e</i><sub><i>A</i>,0</sub><sup>(<i>b</i>)</sup>, …, <i>e</i><sub><i>A</i>,<i>m</i><sub>ch</sub>−1</sub><sup>(<i>b</i>)</sup>), &nbsp; <i>E</i><sub><i>B</i></sub><sup>(<i>b</i>)</sup> defined likewise, &nbsp; <i>b</i> ∈ {0,1}.</div>',
  '<div align="center"><i>T</i><sub><i>j</i></sub>(φ<sub><i>A</i>,<i>j</i></sub>(<i>e</i><sub><i>A</i>,<i>j</i></sub><sup>(<i>b</i>)</sup>)) = φ<sub><i>B</i>,<i>j</i></sub>(<i>e</i><sub><i>B</i>,<i>j</i></sub><sup>(<i>b</i>)</sup>), &nbsp; <i>b</i> ∈ {0,1}.</div>',
  '<div align="center"><i>J</i><sub>prop</sub> = ∏<sub><i>j</i>=0</sub><sup><i>m</i><sub>ch</sub>−1</sup><i>J</i><sub><i>j</i></sub><sup>map</sup>, &nbsp; <i>J</i><sub>erase</sub> = 1{<i>J</i><sub><i>m</i><sub>ch</sub>−1</sub><sup>map</sup> = 0},<br><i>J</i><sub>pred</sub> = 1{∏<sub><i>j</i></sub><i>J</i><sub><i>j</i></sub><sup>loc</sup> = 1 ∧ (<i>J</i><sub>prop</sub> = 1 ∨ <i>J</i><sub>erase</sub> = 1)}.</div>',
  '<div align="center">δ<sub><i>A</i>,<i>j</i></sub> = <i>p</i><sub><i>A</i>,<i>j</i></sub><sup>(1)</sup> − <i>p</i><sub><i>A</i>,<i>j</i></sub><sup>(0)</sup>, &nbsp; δ<sub><i>B</i>,<i>j</i></sub> defined likewise.</div>',
  '<div align="center"><i>M</i><sub><i>A</i></sub> = ½∑<sub><i>j</i></sub>|δ<sub><i>A</i>,<i>j</i></sub>|, &nbsp; <i>M</i><sub><i>B</i></sub> = ½∑<sub><i>j</i></sub>|δ<sub><i>B</i>,<i>j</i></sub>|, &nbsp; <i>D</i><sub>tr</sub> = ½∑<sub><i>j</i></sub>|δ<sub><i>A</i>,<i>j</i></sub> − δ<sub><i>B</i>,<i>j</i></sub>|.</div>',
  '<div align="center"><i>C</i><sub>chain</sub> = invariant under locality, terminal erasure, and bounded movement; translation under locality, full propagation, and bounded effect defect; divergence otherwise.</div>',
  '<div align="center"><i>T</i><sub><i>j</i>+1</sub> ∘ <i>K</i><sub><i>A</i>,<i>j</i></sub> ≈ <i>K</i><sub><i>B</i>,<i>j</i></sub> ∘ <i>T</i><sub><i>j</i></sub>.</div>',
  '<div align="center"><i>d</i><sub>t</sub>(<i>h</i>) = max({0} ∪ {<i>r</i><sub>1</sub>, …, <i>r</i><sub><i>N</i><sub>t</sub></sub>}).</div>',
  '<div align="center"><i>T</i><sub>comp</sub> = O(∑<sub><i>e</i>∈<i>E</i><sub>Δ</sub></sub> <i>C</i><sub><i>D</i><sub><i>e</i></sub></sub>),</div>',
  '<div align="center"><i>T</i><sub>snap</sub> ≤ <i>T</i><sub>generate</sub> + ∑<sub>Ξ′∈𝔖<sub>t</sub></sub>[<i>T</i><sub>refit</sub>(Ξ′) + ∑<sub><i>e</i>∈<i>E</i><sub>Δ</sub>(Ξ′)</sub><i>C</i><sub><i>D</i><sub><i>e</i></sub></sub> + <i>T</i><sub>obl</sub>(Ξ′) + <i>T</i><sub>score</sub>(Ξ′)] + <i>T</i><sub>confirm</sub> + <i>T</i><sub>publish</sub>.</div>',
  '<div align="center"><i>e</i><sub>t</sub> = (<i>w</i><sub>t</sub>, <i>a</i><sub>t</sub>, τ<sub>t</sub>, ℓ<sub>t</sub>, <i>m</i><sub>t</sub>, <i>h</i><sub>t</sub>, <i>x</i><sub>t</sub>, <i>c</i><sub>t</sub>).</div>',
  '<div align="center"><i>S</i><sub>g</sub> = min(1, Δ<sub>g</sub> / η<sub>g</sub>).</div>'
].freeze

SEMANTIC_DISPLAY_BY_INDEX = SEMANTIC_DISPLAY_INDICES.zip(SEMANTIC_DISPLAY_MATH).to_h.freeze
abort "Semantic display index/value mismatch" unless
  SEMANTIC_DISPLAY_BY_INDEX.length == SEMANTIC_DISPLAY_INDICES.length

class InlineMathHTML
  SYMBOLS = {
    "Delta" => "Δ", "Gamma" => "Γ", "Lambda" => "Λ", "Omega" => "Ω",
    "Phi" => "Φ", "Pi" => "Π", "Psi" => "Ψ", "Sigma" => "Σ",
    "Theta" => "Θ", "Xi" => "Ξ",
    "alpha" => "α", "beta" => "β", "gamma" => "γ", "delta" => "δ",
    "epsilon" => "ε", "varepsilon" => "ϵ", "zeta" => "ζ", "eta" => "η",
    "theta" => "θ", "kappa" => "κ", "lambda" => "λ", "mu" => "μ",
    "nu" => "ν", "xi" => "ξ", "pi" => "π", "rho" => "ρ",
    "sigma" => "σ", "tau" => "τ", "upsilon" => "υ", "phi" => "φ",
    "chi" => "χ", "psi" => "ψ", "omega" => "ω", "ell" => "ℓ",
    "approx" => "≈", "equiv" => "≡", "ge" => "≥", "le" => "≤",
    "ne" => "≠", "neq" => "≠", "in" => "∈", "mid" => "|",
    "ll" => "≪", "sim" => "∼", "subset" => "⊂", "subseteq" => "⊆",
    "to" => "→", "rightarrow" => "→", "mapsto" => "↦",
    "cap" => "∩", "cup" => "∪", "cdot" => "·", "circ" => "∘", "oplus" => "⊕",
    "partial" => "∂", "prod" => "∏", "sqcup" => "⊔", "sum" => "∑",
    "times" => "×", "star" => "⋆", "varnothing" => "∅",
    "infty" => "∞", "langle" => "⟨", "rangle" => "⟩",
    "ldots" => "…", "arg" => "arg", "inf" => "inf", "ker" => "ker",
    "log" => "log", "max" => "max", "min" => "min", "quad" => " ",
    "qquad" => " "
  }.freeze

  SCRIPT_CAPITALS = {
    "A" => "𝒜", "B" => "ℬ", "C" => "𝒞", "D" => "𝒟", "E" => "ℰ",
    "F" => "ℱ", "G" => "𝒢", "H" => "ℋ", "I" => "ℐ", "J" => "𝒥",
    "K" => "𝒦", "L" => "ℒ", "M" => "ℳ", "N" => "𝒩", "O" => "𝒪",
    "P" => "𝒫", "Q" => "𝒬", "R" => "ℛ", "S" => "𝒮", "T" => "𝒯",
    "U" => "𝒰", "V" => "𝒱", "W" => "𝒲", "X" => "𝒳", "Y" => "𝒴",
    "Z" => "𝒵"
  }.freeze

  FRAKTUR_CAPITALS = {
    "A" => "𝔄", "B" => "𝔅", "C" => "ℭ", "D" => "𝔇", "E" => "𝔈",
    "F" => "𝔉", "G" => "𝔊", "H" => "ℌ", "I" => "ℑ", "J" => "𝔍",
    "K" => "𝔎", "L" => "𝔏", "M" => "𝔐", "N" => "𝔑", "O" => "𝔒",
    "P" => "𝔓", "Q" => "𝔔", "R" => "ℜ", "S" => "𝔖", "T" => "𝔗",
    "U" => "𝔘", "V" => "𝔙", "W" => "𝔚", "X" => "𝔛", "Y" => "𝔜",
    "Z" => "ℨ"
  }.freeze

  DOUBLE_STRUCK_CAPITALS = {
    "A" => "𝔸", "B" => "𝔹", "C" => "ℂ", "D" => "𝔻", "E" => "𝔼",
    "F" => "𝔽", "G" => "𝔾", "H" => "ℍ", "I" => "𝕀", "J" => "𝕁",
    "K" => "𝕂", "L" => "𝕃", "M" => "𝕄", "N" => "ℕ", "O" => "𝕆",
    "P" => "ℙ", "Q" => "ℚ", "R" => "ℝ", "S" => "𝕊", "T" => "𝕋",
    "U" => "𝕌", "V" => "𝕍", "W" => "𝕎", "X" => "𝕏", "Y" => "𝕐",
    "Z" => "ℤ"
  }.freeze

  SANS_SERIF_CAPITALS = Hash[("A".."Z").each_with_index.map do |character, index|
    [character, (0x1D5A0 + index).chr(Encoding::UTF_8)]
  end].freeze

  ACCENTS = {
    "bar" => "̄", "overline" => "̄", "hat" => "̂", "widehat" => "̂",
    "tilde" => "̃", "widetilde" => "̃"
  }.freeze

  def self.render(source)
    rendered = new(source).render
    if rendered.match?(/[\\$^]/)
      raise "Raw TeX survived semantic inline conversion: #{source.inspect} -> #{rendered.inspect}"
    end
    rendered
  end

  def initialize(source)
    @source = source
    @index = 0
  end

  def render
    result = parse_until(nil)
    raise "Unconsumed inline TeX: #{@source.inspect}" unless @index == @source.length
    result
  end

  private

  def parse_until(terminator)
    output = +""
    while @index < @source.length
      character = @source[@index]
      if terminator && character == terminator
        @index += 1
        return output
      end

      case character
      when "\\"
        output << parse_command
      when "{"
        @index += 1
        output << parse_until("}")
      when "}"
        raise "Unexpected closing brace in #{@source.inspect}"
      when "_", "^"
        @index += 1
        tag = character == "_" ? "sub" : "sup"
        output << "<#{tag}>#{parse_atom}</#{tag}>"
      else
        @index += 1
        output << escape_character(character)
      end
    end
    raise "Unclosed group in #{@source.inspect}" if terminator
    output
  end

  def parse_atom
    skip_spaces
    raise "Missing command argument in #{@source.inspect}" if @index >= @source.length

    case @source[@index]
    when "{"
      @index += 1
      parse_until("}")
    when "\\"
      parse_command
    else
      character = @source[@index]
      @index += 1
      escape_character(character)
    end
  end

  def parse_command
    @index += 1
    raise "Trailing backslash in #{@source.inspect}" if @index >= @source.length

    unless @source[@index].match?(/[A-Za-z]/)
      character = @source[@index]
      @index += 1
      return "" if character == "!"
      return " " if [",", ";", ":"].include?(character)
      return escape_character(character)
    end

    start = @index
    @index += 1 while @index < @source.length && @source[@index].match?(/[A-Za-z]/)
    command = @source[start...@index]

    return SYMBOLS.fetch(command) if SYMBOLS.key?(command)
    return apply_accent(parse_atom, ACCENTS.fetch(command)) if ACCENTS.key?(command)

    case command
    when "mathrm"
      parse_atom
    when "mathsf"
      stylize(parse_atom, SANS_SERIF_CAPITALS, 0x1D5BA, 0x1D7E2)
    when "mathbf"
      "<b>#{parse_atom}</b>"
    when "mathcal", "mathscr"
      stylize(parse_atom, SCRIPT_CAPITALS)
    when "mathfrak"
      stylize(parse_atom, FRAKTUR_CAPITALS, 0x1D51E)
    when "mathbb"
      stylize(parse_atom, DOUBLE_STRUCK_CAPITALS, 0x1D552, 0x1D7D8)
    when "underline"
      "<u>#{parse_atom}</u>"
    when "sqrt"
      "√(#{parse_atom})"
    else
      raise "Unsupported inline TeX command \\#{command} in #{@source.inspect}"
    end
  end

  def stylize(rendered, capitals, lowercase_start = nil, digit_start = nil)
    rendered.split(/(<[^>]+>)/).map do |fragment|
      next fragment if fragment.start_with?("<")
      fragment.each_char.map do |character|
        if capitals.key?(character)
          capitals.fetch(character)
        elsif lowercase_start && character.match?(/[a-z]/)
          (lowercase_start + character.ord - "a".ord).chr(Encoding::UTF_8)
        elsif digit_start && character.match?(/[0-9]/)
          (digit_start + character.ord - "0".ord).chr(Encoding::UTF_8)
        else
          character
        end
      end.join
    end.join
  end

  def apply_accent(rendered, accent)
    "#{rendered}#{accent}"
  end

  def skip_spaces
    @index += 1 while @index < @source.length && @source[@index].match?(/\s/)
  end

  def escape_character(character)
    return "−" if character == "-"
    CGI.escapeHTML(character)
  end
end

{
  'S_{\Theta,t^-}' => 'S<sub>Θ,t<sup>−</sup></sub>',
  '\mathbf r_t^{\mathrm{use}}' => '<b>r</b><sub>t</sub><sup>use</sup>',
  '\Delta_\tau' => 'Δ<sub>τ</sub>',
  '\mathrm{share}' => 'share'
}.each do |source, expected|
  actual = InlineMathHTML.render(source)
  abort "Semantic inline math regression: #{source.inspect}: #{actual.inspect}" unless actual == expected
end

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
semantic_inline_count = 0
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
        semantic_inline_count += 1
        InlineMathHTML.render(expression)
      end
    end
  end
end.join

abort "Unbalanced display-math delimiters" if inside_display

display_index = 0
semantic_display_count = 0
github = github.gsub(/^```math\n(.*?)^```$/m) do |block|
  replacement = SEMANTIC_DISPLAY_BY_INDEX[display_index]
  if replacement
    semantic_display_count += 1
  else
    replacement = block
  end
  display_index += 1
  replacement
end
abort "Semantic display fallback count changed: #{display_index}" unless
  display_index == NATIVE_DISPLAY_MATH + SEMANTIC_DISPLAY_MATH.length

# GitHub's client corrupts the row break in this particular fenced `cases`
# expression. Use an equivalent one-line conditional definition in this
# rendering target; the canonical assembly retains the piecewise form.
packing_cases = <<~'MATH'.strip
  c_t^{\mathrm{pack}}=
  \begin{cases}
  1,&P_t=N_t,\\
  \mathrm{clip}_{[0,1]}\!\left(
  \dfrac{s_{(P_t),t}^{\mathrm{ret}}-s_{(P_t+1),t}^{\mathrm{ret}}}
  {\max\{|s_{(P_t),t}^{\mathrm{ret}}|,
  |s_{(P_t+1),t}^{\mathrm{ret}}|,\varepsilon_s\}}
  \right),&P_t<N_t,
  \end{cases}
MATH
packing_conditions = <<~'MATH'.strip
  c_t^{\mathrm{pack}}=1\quad\text{when }P_t=N_t;\qquad
  c_t^{\mathrm{pack}}=\mathrm{clip}_{[0,1]}\!\left(
  \dfrac{s_{(P_t),t}^{\mathrm{ret}}-s_{(P_t+1),t}^{\mathrm{ret}}}
  {\max\{|s_{(P_t),t}^{\mathrm{ret}}|,
  |s_{(P_t+1),t}^{\mathrm{ret}}|,\varepsilon_s\}}
  \right)\quad\text{when }P_t<N_t.
MATH
abort "Packing-boundary cases expression not found" unless github.include?(packing_cases)
github = github.sub(packing_cases, packing_conditions)

note = <<~MARKDOWN

  _GitHub rendering note: equations use native typesetting or semantic HTML with Unicode mathematical symbols and real sub/superscripts. This keeps the single-file edition within GitHub's per-page math-rendering budget. The PDF remains fully typeset._
MARKDOWN

scope = "_Public working paper. Initial implementation evidence is reported in Section 11; full real-world validation remains outstanding._\n"
abort "Paper scope marker not found" unless github.include?(scope)

github = github.sub(scope, scope + note)
File.write(TARGET, github, encoding: "UTF-8")

raw_tex_code = github.scan(/(?<!\$)`[^`\n]*\\[A-Za-z]+[^`\n]*`(?!\$)/)
abort "Raw inline TeX code fallback survived: #{raw_tex_code.first}" unless raw_tex_code.empty?

display_count = github.scan(/^```math$/).length
inline_count = github.scan(inline_pattern).length
total = display_count + inline_count
abort "GitHub math budget exceeded: #{total}" if total > MAX_MATH_NODES

warn "GitHub paper: #{display_count} display + #{inline_count} inline = #{total} math nodes; #{semantic_display_count} semantic displays; #{semantic_inline_count} semantic inline expressions"
