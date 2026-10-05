import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const repository = process.argv[2];
assert(repository, 'Provide the local reference implementation repository');
const revision = '7a7b9357c06ce855795b947ffcde2fd61a82d3ca';
const destination = path.join(root, 'evidence', 'observation-research-2026-10');
const sources = [
  ['preserved-v3-results.md', 'docs/experiments/mmm-preserved-v3-results.md'],
  ['preserved-v3-summary.json', 'docs/experiments/mmm-preserved-v3-summary.json'],
  ['retained-v8-results.md', 'docs/experiments/mmm-retained-v8-results.md'],
  ['retained-v8-summary.json', 'docs/experiments/mmm-retained-v8-summary.json'],
  ['member-fit-results.md', 'docs/experiments/mmm-member-fit-breadth-v1-results.md'],
  ['member-fit-summary.json', 'docs/experiments/mmm-member-fit-breadth-v1-summary.json'],
  ['native-v72-results.md', 'docs/experiments/mmm-dynvarcache-v72-results.md'],
  ['native-v72-readback.json', 'research/dynvarcache-v72-diagnostic/readback.json'],
  ['native-v75-results.md', 'docs/experiments/mmm-mean-anchor-v75-cohort-results.md'],
  ['native-v75-readback.json', 'research/mean-anchor-v75-diagnostic/readback.json'],
  ['protected-v81-results.md', 'docs/experiments/mmm-regime-protected-v81-screen-results.md'],
  ['protected-v81-readback.json', 'research/regime-protected-v81-screen-initial/readback.json'],
  ['log-v82-results.md', 'docs/experiments/mmm-regime-log-v82-results.md'],
  ['summary-v83-audit.json', 'research/regime-logsummary-v83-initial/audit.json'],
  ['summary-v83-benchmark.log', 'research/regime-logsummary-v83-initial/benchmark.log'],
  ['summary-v83-completed.json', 'research/regime-logsummary-v83-initial/completed.json'],
  ['scifact-calibration-results.md', 'docs/experiments/scifact-native-calibration-v4-results.md'],
  ['nfcorpus-transfer-results.md', 'docs/experiments/nfcorpus-transfer-v4-results.md'],
  ['durable-freshness-results.md', 'docs/experiments/mmm-durable-live-freshness-v2-results.md'],
  ['recurrent-pilot-results.md', 'research/recurrent-discovery/RESULTS.md'],
  ['baseline-protocol.md', 'research/publication-2026-10-05/BASELINE-PROTOCOL.md'],
  ['baseline-selection.json', 'research/publication-2026-10-05/selection-results.json'],
  ['baseline-controls.json', 'research/publication-2026-10-05/baseline-run/control-results.json'],
  ['baseline-completed.json', 'research/publication-2026-10-05/baseline-run/completed.json'],
];
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');
const put = (name, bytes) => {
  const target = path.join(destination, name);
  if (fs.existsSync(target)) assert.deepEqual(fs.readFileSync(target), bytes, `Existing evidence differs: ${name}`);
  else fs.writeFileSync(target, bytes, { flag: 'wx' });
};
fs.mkdirSync(destination, { recursive: true });
const records = [];
for (const [name, source] of sources) {
  // Import immutable Git blobs, never mutable working-tree data or a private archive.
  const bytes = execFileSync('git', ['show', `${revision}:${source}`], {
    cwd: repository, maxBuffer: 20 * 1024 * 1024,
  });
  assert(!bytes.includes(0));
  assert(!/\/Users\/clawdius|\/Volumes\/Data\/eventframed|BEGIN .*PRIVATE KEY/.test(bytes.toString('utf8')));
  put(name, bytes);
  records.push({ name, source, sha256: hash(bytes), bytes: bytes.length });
}
put('provenance.json', Buffer.from(JSON.stringify({
  repository: 'https://github.com/JuanHuaXu/eventframed', revision,
  scope: 'Selected published synthetic summaries, public-task reports and serial timings; no raw chats or owned databases',
  byteIdenticalToPublishedBlobs: true, historicalVerdictsPreserved: true,
  nativeBaselineReplicationIsConsumedDevelopment: true,
  wholeResearchGoalsComplete: false, files: records,
}, null, 2) + '\n'));
const names = [...records.map(r => r.name), 'provenance.json'].sort();
put('SHA256SUMS', Buffer.from(names.map(name => `${hash(fs.readFileSync(path.join(destination, name)))}  ${name}`).join('\n') + '\n'));
console.log(JSON.stringify({ revision, files: records.length, bytes: records.reduce((n, r) => n + r.bytes, 0) }));
