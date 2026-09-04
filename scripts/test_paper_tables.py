"""Regression checks for source-derived PDF tables; also rebuilds the assembly."""

from pathlib import Path
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]
builder = runpy.run_path(str(ROOT / "scripts" / "build_paper.py"))


class PaperTableTests(unittest.TestCase):
    def test_claim_rows_are_not_a_hardcoded_snapshot(self):
        rows = [line for line in (ROOT / "src" / "01a_claims_register.md").read_text().splitlines()
                if line.startswith("|")]
        rendered = builder["render_table"](rows)
        for row in rows[2:]:
            for cell in builder["table_cells"](row):
                self.assertIn(builder["escape_text"](cell), rendered)
        self.assertEqual(rendered.count("2d &"), 3)

    def test_replay_table_has_six_body_rows(self):
        lines = (ROOT / "src" / "09_experimental_evaluation.md").read_text().splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith("| Source and historical block |"))
        block = lines[start:start + 8]
        rendered = builder["render_table"](block)
        self.assertIn("1,286", rendered)
        self.assertIn("0.446439", rendered)
        self.assertIn(r"\begin{longtable}", rendered)

    def test_math_pipe_is_not_a_column(self):
        self.assertEqual(builder["table_cells"]("| $|x|$ | plain |"), ["$|x|$", "plain"])

    def test_invalid_width_is_rejected(self):
        with self.assertRaises(ValueError):
            builder["render_table"](["| A | B |", "| --- | --- |", "| missing |"])


if __name__ == "__main__":
    unittest.main()
