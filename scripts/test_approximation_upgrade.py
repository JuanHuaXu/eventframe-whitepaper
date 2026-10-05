"""Correction integrity, theorem boundary and prospective-inference checks."""

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import math
import re
import statistics
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "approximation-inference-v1"
APPENDIX = (ROOT / "src" / "16_error_and_inference_appendix.md").read_text()


def load(name):
    return json.loads((EVIDENCE / name).read_text())


class ApproximationUpgradeTests(unittest.TestCase):
    def test_imports_are_byte_pinned_not_published_confirmation(self):
        provenance = load("provenance.json")
        self.assertIsNone(provenance["candidateRevision"])
        self.assertFalse(provenance["untouchedConfirmation"])
        self.assertFalse(provenance["wholeGoalValidation"])
        self.assertFalse(provenance["privateRawDataIncluded"])
        for record in provenance["files"]:
            raw = (EVIDENCE / record["name"]).read_bytes()
            self.assertEqual(len(raw), record["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), record["sha256"])
        for line in (EVIDENCE / "SHA256SUMS").read_text().splitlines():
            digest, name = line.split()
            self.assertEqual(hashlib.sha256((EVIDENCE / name).read_bytes()).hexdigest(), digest)

    def test_large_joint_defect_is_not_repaired_or_promoted(self):
        report = load("audit.json")
        historical = json.loads((ROOT / "evidence" / "observation-research-2026-10" /
                                 "summary-v83-audit.json").read_text())
        self.assertEqual(report["MaxEnvelopeActualTV"], historical["MaxEnvelopeActualTV"])
        self.assertEqual(report["EnvelopeOracleChecks"], 280)
        self.assertEqual(report["SummaryParityChecks"], 48780)
        self.assertFalse(report["WholeGoalValidation"])
        self.assertIn(f"{report['MaxEnvelopeActualTV']:.9f}", APPENDIX)
        self.assertIn("historical-query evidence-ratio weights", APPENDIX)
        self.assertIn("does not synthesize one from audit parity", APPENDIX)

    def test_conditional_safe_region_and_rare_evidence_counterexample(self):
        a = (1 - Fraction(3, 4)) * Fraction(1) / Fraction(1, 2)
        limit, dropped = Fraction(1, 100), Fraction(1, 200)
        self.assertEqual((1 - a) * limit, dropped)
        error = Fraction(0)
        for _ in range(256):
            error = a * error + dropped
            self.assertLessEqual(error, limit)
        # Tiny omitted prior mass can dominate after rare evidence.
        posterior_mass = []
        for delta in [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)]:
            posterior_mass.append(delta / (delta + (1 - delta) * delta**2))
        self.assertEqual(posterior_mass, sorted(posterior_mass))
        self.assertGreater(posterior_mass[-1], Fraction(99, 100))

    def test_same_outcome_binary_brier_bound(self):
        for p in [Fraction(i, 20) for i in range(21)]:
            for q in [Fraction(i, 20) for i in range(21)]:
                for y in [0, 1]:
                    self.assertLessEqual(abs((p-y)**2 - (q-y)**2), min(1, 2*abs(p-q)))
        self.assertIn("two independently changed residual kernels", APPENDIX)
        self.assertIn("not a log-loss bound", APPENDIX)

    def test_cs_report_formula_and_planning_are_distinct(self):
        report = load("inference-utility.json")
        self.assertFalse(report["scientific_confirmation"])
        self.assertFalse(report["historical_verdicts_changed"])
        self.assertFalse(report["appendix_c"]["stronger_betting_method_used"])
        interval = report["synthetic_interval"]
        n, alpha, k = interval["stream_count"], interval["alpha_family"], interval["family_size"]
        halfwidth = math.sqrt(2 * math.log(2*k*n*(n+1)/alpha) / n)
        self.assertAlmostEqual(interval["halfwidth"], halfwidth)
        self.assertAlmostEqual(interval["lower"], interval["mean"] - halfwidth)
        self.assertAlmostEqual(interval["upper"], interval["mean"] + halfwidth)
        # Telescoping spending is below the frozen family budget at every finite horizon.
        spending = sum(Fraction(1, j*(j+1)) for j in range(1, 257))
        self.assertEqual(spending, Fraction(256, 257))
        ap = report["ap_member_planning"]
        self.assertEqual(ap["scenario"], "member_shift")
        planned = math.ceil(ap["pilot_units"] * (
            (ap["critical_z"] + ap["power_z"]) * ap["observed_se"] / ap["mean"])**2)
        self.assertEqual(planned, ap["approximate_total_fresh_units"])
        self.assertEqual(planned, 137)
        self.assertLess(report["ap_recurring_context"]["mean"], 0)
        self.assertIn("not a guaranteed requirement", APPENDIX)

    def test_matched_benchmarks_have_all_profiles_and_repeated_samples(self):
        report = load("benchmark-results.json")
        self.assertEqual(set(report["results"]), {"before", "after"})
        before, after = report["results"]["before"], report["results"]["after"]
        self.assertEqual(set(before), set(after))
        self.assertEqual(len(before), 12)
        for name in before:
            self.assertEqual(len(before[name]), 6)
            self.assertEqual(len(after[name]), 6)
            for rows in [before[name], after[name]]:
                self.assertGreater(statistics.median(r["ns"] for r in rows), 0)
                self.assertTrue(all(r["bytes"] >= 0 and r["allocs"] >= 0 for r in rows))
        self.assertIn("not serving latency", report["scope"])

    def test_component_timings_match_raw_samples(self):
        summary = load("timing-summary.json")
        low, high = summary["changePercentRange"]
        self.assertIn(f"{low:.2f}% to +{high:.2f}%", APPENDIX)
        values = summary["boundNSPerOperation"]
        self.assertIn(f"{min(values):.2f}--{max(values):.2f} ns/op", APPENDIX)
        frames = load("frame-benchmark-results.json")["results"]
        self.assertEqual(len(frames), 30)
        changes, candidate_us = [], []
        for name, before in frames.items():
            self.assertEqual(len(before), 6)
            if not name.endswith("/HEAD"):
                continue
            after = frames[name.replace("/HEAD", "/current")]
            a = statistics.median(r["ns"] for r in before)
            b = statistics.median(r["ns"] for r in after)
            changes.append((name, 100*(b/a-1)))
            candidate_us.append(b/1000)
        unquoted = [value for name, value in changes if not name.startswith("quoted/")]
        quoted = [value for name, value in changes if name.startswith("quoted/")]
        self.assertIn(f"{min(unquoted):.2f}--{max(unquoted):.2f}%", APPENDIX)
        self.assertIn(f"{min(quoted):.2f}--{max(quoted):.2f}%", APPENDIX)
        self.assertIn(f"{min(candidate_us):.3f} microseconds", APPENDIX)
        self.assertIn(f"{max(candidate_us)/1000:.3f} milliseconds", APPENDIX)
        raw = (EVIDENCE / "admission-benchmark.txt").read_text()
        runs = {}
        for line in raw.splitlines():
            match = re.match(r"BenchmarkBoundedIssue/M(\d+)/bounded=(false|true)\s+\d+\s+([\d.]+) ns/op", line)
            if match:
                runs.setdefault((int(match[1]), match[2]), []).append(float(match[3]))
        self.assertEqual(len(runs), 6)
        for values in runs.values():
            self.assertEqual(len(values), 3)
            self.assertIn(f"{statistics.median(values)/1000:.3f}", APPENDIX)
        self.assertIn("synthetic zero numerical witness", APPENDIX)

    def test_reading_order_and_claim_sync(self):
        abstract = (ROOT / "src" / "00_abstract.md").read_text()
        self.assertLess(len(abstract.split()), 350)
        main = (ROOT / "src" / "09_experimental_evaluation.md").read_text()
        self.assertLess(main.index("| Direction |"), main.index("## Initial Implementation Evidence"))
        self.assertIn("identityBySession", main)
        self.assertIn("neither a signature", main)
        self.assertIn("not independently adjudicated agent task success", main)
        builder = (ROOT / "scripts" / "build_paper.py").read_text()
        self.assertIn("15_observation_research_appendix.md", builder)
        self.assertIn("16_error_and_inference_appendix.md", builder)
        claims = (ROOT / "src" / "01a_claims_register.md").read_text()
        spec = (ROOT / "spec" / "claims.md").read_text()
        for phrase in ["Conditional capped-filter", "Prospective stream-level"]:
            row = next(line for line in claims.splitlines() if line.startswith("|") and phrase in line)
            self.assertIn(row, spec)


if __name__ == "__main__":
    unittest.main()
