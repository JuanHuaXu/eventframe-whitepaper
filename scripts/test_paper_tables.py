"""Regression checks for source-derived PDF tables; also rebuilds the assembly."""

from pathlib import Path
import hashlib
import json
import math
import statistics
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]
builder = runpy.run_path(str(ROOT / "scripts" / "build_paper.py"))


class PaperTableTests(unittest.TestCase):
    def test_grid_evidence_and_table(self):
        directory = ROOT / "evidence" / "grid-belief-v1"
        for line in (directory / "SHA256SUMS").read_text().splitlines():
            digest, name = line.split()
            self.assertEqual(hashlib.sha256((directory / name).read_bytes()).hexdigest(), digest)
        source = (ROOT / "src" / "09_experimental_evaluation.md").read_text()
        names = ["Stationary .01", "Stationary .20", "Stationary .50", "Stationary .80",
                 "Stationary .99", "Abrupt .99 to .01", "Recurring .9/.1", "Gradual .1 to .9"]
        for split, seed in [("design", 2026090601), ("confirmation", 2026090602)]:
            report = json.loads((directory / f"grid-belief-{split}.json").read_text())
            self.assertEqual(report["Seed"], seed)
            self.assertEqual(len(report["Trajectories"]), 512)
            self.assertEqual(len(report["Summaries"]), 24)
            for summary in report["Summaries"]:
                rows = [r for r in report["Trajectories"] if r["Scenario"] == summary["Scenario"]]
                self.assertEqual({r["Trajectory"] for r in rows}, set(range(64)))
                metric = summary["Metric"]
                gain = [r["Old"][metric] - r["Grid"][metric] for r in rows]
                mean = statistics.mean(gain)
                error = statistics.stdev(gain) / math.sqrt(64)
                self.assertAlmostEqual(summary["Gain"], mean, places=13)
                self.assertAlmostEqual(summary["LowerSimultaneous"], mean-3.08*error, places=13)
                self.assertAlmostEqual(summary["UpperSimultaneous"], mean+3.08*error, places=13)
                if split == "confirmation" and metric == "Brier":
                    means = [statistics.mean(r[k][metric] for r in rows) for k in ["Old", "Grid", "Beta"]]
                    composed = statistics.mean(r["Old"]["ComposedBrier"]-r["Grid"]["ComposedBrier"] for r in rows)
                    row = (f"| {names[summary['Scenario']]} | {means[0]:.6f} | {means[1]:.6f} | "
                           f"{means[2]:.6f} | [{mean-3.08*error:.6f}, {mean+3.08*error:.6f}] | {composed:.6f} |")
                    self.assertIn(row, source)

    def test_claim_rows_are_not_a_hardcoded_snapshot(self):
        rows = [line for line in (ROOT / "src" / "01a_claims_register.md").read_text().splitlines()
                if line.startswith("|")]
        rendered = builder["render_table"](rows)
        for row in rows[2:]:
            for cell in builder["table_cells"](row):
                self.assertIn(builder["escape_text"](cell), rendered)
        self.assertEqual(rendered.count("2d &"), 3)
        self.assertEqual(rendered.count("2e &"), 3)

    def test_authenticated_timings_match_source_table(self):
        directory = ROOT / "evidence" / "authenticated-outcomes-v1"
        report = json.loads((directory / "timings.json").read_text())
        raw = (directory / "authenticated-evidence-benchmark.txt").read_bytes()
        self.assertEqual(report["input_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(len(report["runs"]), 45)
        summaries = {row["benchmark"]: row for row in report["summaries"]}
        source = (ROOT / "src" / "09_experimental_evaluation.md").read_text()
        cases = [
            ("Serial recall", "EvidenceInternalRequests", "/workers=1/mixed=false", "ms"),
            ("Four-worker recall", "EvidenceInternalRequests", "/workers=4/mixed=false", "ms/op"),
            ("Serial durable outcome", "AuthenticatedOutcome/disk=true", "", "ms"),
            ("Four-worker mixed traffic", "EvidenceInternalRequests", "/workers=4/mixed=true", "ms/op"),
        ]
        for label, benchmark, suffix, unit in cases:
            control = summaries[f"Benchmark{benchmark}/upgrade=false{suffix}-10"]
            upgrade = summaries[f"Benchmark{benchmark}/upgrade=true{suffix}-10"]
            low, high = upgrade["p99_range_ns"]
            row = (f"| {label} | {control['median_run_mean_ns_per_op']/1e6:.3f} {unit} | "
                   f"{upgrade['median_run_mean_ns_per_op']/1e6:.3f} {unit} | "
                   f"{low/1e6:.2f}-{high/1e6:.2f} ms |")
            self.assertIn(row, source)

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
