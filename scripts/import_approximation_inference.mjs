import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";

// Copy only explicit synthetic/aggregate reports; never traverse private corpora.
const software = process.argv[2];
if (!software) throw new Error("Usage: node scripts/import_approximation_inference.mjs /path/to/eventframed");
const output = path.resolve("evidence/approximation-inference-v1");
const files = [
  ["research/approximation-admission-2026-10-05/audit.json", "audit.json"],
  ["research/approximation-admission-2026-10-05/audit-tests.txt", "audit-tests.txt"],
  ["research/approximation-admission-2026-10-05/manifest.json", "source-manifest.json"],
  ["research/approximation-admission-2026-10-05/benchmark-results.json", "benchmark-results.json"],
  ["research/approximation-admission-2026-10-05/bounds-benchmark.txt", "bounds-benchmark.txt"],
  ["docs/experiments/inference-utility-2026-10-05-report.json", "inference-utility.json"],
  ["docs/experiments/inference-contract-2026-10-05.md", "inference-contract.md"],
  ["docs/experiments/turn-fallback-2026-10-05.md", "turn-fallback-audit.md"],
  ["research/approximation-admission-2026-10-05/admission-benchmark.txt", "admission-benchmark.txt"],
  ["research/approximation-admission-2026-10-05/frame-benchmark.txt", "frame-benchmark.txt"],
  ["research/approximation-admission-2026-10-05/frame-benchmark-results.json", "frame-benchmark-results.json"],
  ["docs/experiments/approximation-admission-2026-10-05.md", "approximation-correction.md"],
];
for (const arm of ["before", "after"]) for (const round of [0, 1]) {
  files.push([`research/approximation-admission-2026-10-05/${arm}-benchmark-${round}.txt`, `${arm}-benchmark-${round}.txt`]);
}
const utility = JSON.parse(fs.readFileSync(path.join(software, files[5][0])));
const manifest = JSON.parse(fs.readFileSync(path.join(software, files[2][0])));
const benches = JSON.parse(fs.readFileSync(path.join(software, files[3][0])));
if (utility.scientific_confirmation !== false || utility.private_raw_data_used !== false ||
    manifest.untouchedConfirmation !== false || manifest.syntheticMechanismsOnly !== true ||
    Object.values(benches.results).some(rows => Object.keys(rows).length !== 12 || Object.values(rows).some(r => r.length !== 6))) {
  throw new Error("Correction evidence has unexpected scope or incomplete benchmark data");
}
const imported = files.map(([source, name]) => {
  const bytes = fs.readFileSync(path.join(software, source));
  return { source, name, bytes, sha256: crypto.createHash("sha256").update(bytes).digest("hex") };
});
const median = values => {
  const sorted = [...values].sort((a,b) => a-b), middle = Math.floor(sorted.length/2);
  return sorted.length % 2 ? sorted[middle] : (sorted[middle-1]+sorted[middle])/2;
};
const operationProfiles = Object.entries(benches.results.before).map(([name, before]) => {
  const after = benches.results.after[name];
  const beforeMedianUS = median(before.map(r => r.ns))/1000;
  const afterMedianUS = median(after.map(r => r.ns))/1000;
  return { name, beforeMedianUS, afterMedianUS,
    changePercent: 100*(afterMedianUS/beforeMedianUS-1),
    beforeAllocations: before.map(r => r.allocs), afterAllocations: after.map(r => r.allocs) };
});
const primitives = fs.readFileSync(path.join(software, files[4][0]), "utf8")
  .split("\n").flatMap(line => {
    const match = line.match(/^BenchmarkStepTV\s+\d+\s+([\d.]+) ns\/op/);
    return match ? [Number(match[1])] : [];
  });
if (primitives.length !== 3) throw new Error("Incomplete scalar-bound benchmark");
const summary = {
  scope: "Prepared serial operations on one local M4; not loaded serving tails or scientific confirmation",
  repetitionsPerArmAndProfile: 6, operationProfiles,
  changePercentRange: [Math.min(...operationProfiles.map(r => r.changePercent)), Math.max(...operationProfiles.map(r => r.changePercent))],
  boundNSPerOperation: primitives,
};
const bytes = Buffer.from(JSON.stringify(summary, null, 2)+"\n");
imported.push({source: "derived from imported raw benchmark samples", name: "timing-summary.json",
  bytes, sha256: crypto.createHash("sha256").update(bytes).digest("hex")});
fs.mkdirSync(output, { recursive: true });
for (const record of imported) fs.writeFileSync(path.join(output, record.name), record.bytes);
fs.writeFileSync(path.join(output, "provenance.json"), JSON.stringify({
  scope: "Local uncommitted correction evidence; synthetic development checks and retrospective planning only",
  immutableControlRevision: manifest.controlRevision,
  candidateRevision: null,
  candidateSources: "SHA-256-pinned in source-manifest.json; not a published commit",
  untouchedConfirmation: false, wholeGoalValidation: false, privateRawDataIncluded: false,
  files: imported.map(({ bytes, ...record }) => ({ ...record, bytes: bytes.length })),
}, null, 2) + "\n");
fs.writeFileSync(path.join(output, "SHA256SUMS"), imported.map(r => `${r.sha256}  ${r.name}`).join("\n") + "\n");
console.log(JSON.stringify({ imported: imported.length, untouchedConfirmation: false }));
