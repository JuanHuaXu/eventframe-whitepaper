"""Check imported evidence, headline arithmetic, failure labels, and scope."""

from pathlib import Path
import hashlib
import json
import math
import statistics
import unittest


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "observation-research-2026-10"
SOURCE = "\n".join((ROOT / "src" / name).read_text() for name in [
    "09_experimental_evaluation.md", "15_observation_research_appendix.md"
])


def load(name):
    return json.loads((EVIDENCE / name).read_text())


class ObservationResearchTests(unittest.TestCase):
    def test_import_integrity_and_published_origin(self):
        provenance = load("provenance.json")
        self.assertEqual(provenance["revision"], "7a7b9357c06ce855795b947ffcde2fd61a82d3ca")
        self.assertEqual(len(provenance["files"]), 24)
        self.assertFalse(provenance["wholeResearchGoalsComplete"])
        for record in provenance["files"]:
            raw = (EVIDENCE / record["name"]).read_bytes()
            self.assertEqual(len(raw), record["bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), record["sha256"])
        for line in (EVIDENCE / "SHA256SUMS").read_text().splitlines():
            digest, name = line.split()
            self.assertEqual(hashlib.sha256((EVIDENCE / name).read_bytes()).hexdigest(), digest)

    def test_expected_brier_identity_including_endpoints(self):
        for q in [0, .01, .2, .5, .99, 1]:
            for p in [0, .01, .2, .5, .99, 1]:
                realized_expectation = p * (q - 1) ** 2 + (1 - p) * q ** 2
                self.assertAlmostEqual(realized_expectation, (q - p) ** 2 + p * (1 - p))
                self.assertGreaterEqual((q - p) ** 2 + p * (1 - p), p * (1 - p))
        self.assertIn("generator's known clean-outcome probability used only for evaluation", SOURCE)

    def test_fresh_control_table_is_consumed_not_confirmation(self):
        report, selection = load("baseline-controls.json"), load("baseline-selection.json")
        self.assertFalse(report["UntouchedConfirmation"])
        self.assertTrue(selection["consumedDevelopmentOnly"])
        self.assertEqual(report["IndependentLossChecks"], 576000)
        self.assertEqual(len(report["Cells"]), 240)
        for arm, label in [("adaptive", "Adaptive accuracy reference"), ("full", "Full speed control")]:
            rows = [r for r in report["Cells"] if r["Arm"] == arm]
            self.assertEqual(len(rows), 120)
            self.assertEqual(len({(r["Geometry"], r["Regime"], r["Schedule"]) for r in rows}), 120)
            risk = statistics.mean(r["Risk"] for r in rows)
            mean_cost = statistics.mean(r["CoreMS"] for r in rows)
            worst = max(r["CoreMS"] for r in rows)
            self.assertLess(worst, 400)
            self.assertIn(f"| {label} | 0 / 120 | {risk:.9f} | {mean_cost:.3f} | {worst:.3f} |", SOURCE)
            old = next(r for r in selection["historicalCandidates"] if r["name"] == arm)
            self.assertAlmostEqual(risk, old["expected_brier"], places=12)
        risks = {r["name"]: r["expected_brier"] for r in selection["freshControls"]}
        self.assertIn(f"{100 * (risks['full'] - risks['adaptive']) / risks['full']:.2f}% lower loss", SOURCE)
        self.assertIn("not one request, its p99", SOURCE)

    def test_preserved_rescue_table_and_retained_verdicts(self):
        report = load("preserved-v3-summary.json")
        self.assertTrue(report["OverallPass"])
        cases = [("stable", "Stable, full stream", "FullBrier", "Harm below frozen 0.01 ceiling, not zero"),
                 ("member_shift", "Member shift, post-change", "PostBrier", "Rescue criterion passed"),
                 ("common_shift", "Common shift, post-change", "PostBrier", "Rescue criterion passed"),
                 ("recurring", "Recurring, after first change", "PostBrier", "Improved over frozen and matched observation controls")]
        for scenario, label, metric, verdict in cases:
            rows = {r["Arm"]: r for r in report["Summaries"]
                    if r["Split"] == "confirmation" and r["Scenario"] == scenario}
            self.assertIn(f"| {label} | {rows['frozen_mmm'][metric]:.6f} | {rows['mix_mmm_ap'][metric]:.6f} | {verdict} |", SOURCE)
        verdicts = {r["Arm"]: r["Pass"] for r in load("retained-v8-summary.json")["Verdicts"]}
        self.assertEqual(verdicts, {"replacement_mmm": False, "adaptive_retained": True, "static_retained": True})

    def test_gate_coverage_is_not_forecast_gain(self):
        report = load("member-fit-summary.json")
        self.assertTrue(report["coveragePass"])
        self.assertFalse(report["pilotPass"])
        self.assertEqual(len(report["falseRevocations"]), 12)
        for row in report["falseRevocations"]:
            self.assertEqual((row["k"], row["n"]), (0, 512))
            self.assertAlmostEqual(row["upper"], 1 - row["alpha"] ** (1 / row["n"]), places=12)
            self.assertLess(row["upper"], .02)
        row = next(r for r in report["comparisons"] if r["split"] == "confirmation" and r["scenario"] == "member_shift")
        self.assertLess(row["postBrierGain"]["mean"], 0)
        self.assertFalse(row["pilotCellPass"])
        self.assertIn(f"{row['delayGainPercent']:.2f}% reduction", SOURCE)

    def test_broad_quality_failures_are_preserved(self):
        v72, v75 = load("native-v72-readback.json"), load("native-v75-readback.json")
        self.assertEqual(v72["arms"], 2160)
        self.assertTrue(v72["allArmsBitwiseEqual"])
        self.assertEqual(len(v72["summaries"]), 16)
        for row in v72["summaries"].values():
            self.assertFalse(row["gates"]["gain01"])
            self.assertFalse(row["gates"]["noAdaptiveHarm01"])
            self.assertFalse(row["gates"]["recovery"])
            self.assertTrue(row["gates"]["completeLoop400"])
        self.assertEqual(v75["arms"], 3600)
        self.assertFalse(v75["allNewArmsEquivalent"])
        self.assertEqual(len(v75["equivalence"]["failed"]), 160)
        new = [v for k, v in v75["summaries"].items() if k.startswith("mean")]
        self.assertEqual(len(new), 12)
        for row in new:
            self.assertEqual(row["over400MS"], 120)
            self.assertFalse(any(row["gates"].values()))

    def test_support_and_numeric_components_do_not_promote_quality(self):
        screen = load("protected-v81-readback.json")
        self.assertEqual((screen["forecasts"], screen["attempts"]), (115200, 172800))
        self.assertEqual(screen["screen"]["shiftedPositiveCases"], 36)
        self.assertFalse(screen["scientificAdoption"])
        audit, completion = load("summary-v83-audit.json"), load("summary-v83-completed.json")
        self.assertTrue(audit["LongLogRescue"] and audit["MemberOddsRescue"])
        self.assertEqual(audit["SummaryParityChecks"], 48780)
        self.assertEqual(audit["Checks"], 193613)
        self.assertLess(audit["MaxSummaryParity"], 1e-14)
        self.assertGreater(audit["MaxEnvelopeActualTV"], .69)
        self.assertFalse(completion["scientificQualityRescueEstablished"])
        self.assertFalse(completion["wholeCohortTested"])
        self.assertFalse(completion["loadedServingEstablished"])
        self.assertTrue(completion["allChecksPass"])

    def test_new_claim_rows_are_synchronized(self):
        claims = (ROOT / "src" / "01a_claims_register.md").read_text()
        spec = (ROOT / "spec" / "claims.md").read_text()
        labels = ["The tested small recurrent", "Preserving the incumbent", "Retained short-window/tree",
                  "Faster member-split", "Native v72", "Expanded v75", "Protected support",
                  "Log-state and summary", "Frozen source-only", "Durable feedback stays",
                  "Adaptive is the best recorded"]
        for label in labels:
            row = next(line for line in claims.splitlines() if line.startswith("|") and label in line)
            self.assertIn(row, spec)
        self.assertIn("Falsified for v2 policy", claims)
        self.assertIn("All seven whole research directions", (ROOT / "src" / "00_abstract.md").read_text())


if __name__ == "__main__":
    unittest.main()
