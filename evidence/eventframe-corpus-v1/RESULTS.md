# Contract-12 EventFrame-Corpus Results

Date: 2026-08-30

## Representation boundary

Canonical `eventframe-5w1h-v1` text supplied embedding, nomination, reranking,
and diversity calculations. Raw transcript text remained opaque metadata and
was hydrated only after ranking and packing.

## Codex retrospective confirmation split

The block contained 138 cases in three trajectories. It is a reserved split,
not prospective independent replication.

| Metric | Baseline | EventFrame | Difference |
| --- | ---: | ---: | ---: |
| Brier loss | 0.26117 | 0.24121 | -0.01996 |
| Recall@10 | 0.36192 | 0.46087 | +0.09895 |
| Recall@50 | 0.88811 | 0.96363 | +0.07552 |
| Packed recall | 0.27585 | 0.37200 | +0.09615 |
| MRR | 0.76147 | 0.91418 | +0.15271 |
| ECE | 0.14072 | 0.17976 | +0.03904, worse |

Trajectory-cluster 95% intervals were [0.00978, 0.04238] for Brier gain,
[0.04617, 0.32637] for Recall@10 gain, and [0.06700, 0.32637] for packed-recall
gain. High-priority misses did not increase. Shuffled feedback reduced
Recall@10 to 0.34194 and packed recall to 0.24266.

## Evidence shortages

- ChatGPT: 29 design cases in eight clusters, one confirmation case in one
  cluster; inconclusive.
- OpenClaw replay extraction: five design cases and no confirmation case;
  inconclusive.
- Isolated OpenClaw boundary: nine of nine synthetic answers in both arms; the
  five-case organic smoke test had identical candidate order and zero rank
  deltas, so its 0/5 versus 1/5 answer difference is not reranking evidence.

## Runtime

- Corrected local SQ8, 1,000 events: p99 range 9.988--11.014 ms over five runs.
- Corrected in-memory, 10,000 events: p99 range 7.981--8.513 ms.
- Embedded 16-worker mixed workload: 3,219 operations, zero errors, recall p95
  130.13 ms and p99 218.75 ms.
- Remote one-writer/overlapping-read mixed workload: 1,484 operations, zero
  EventFrame request errors, recall p95 176.68 ms and p99 219.85 ms.

The sequential target passed; the concurrent sub-100 ms p99 target failed.

## Explicit feedback durability

Ten exact-journal useful outcomes moved Beta(1,1) to Beta(11,1), probability
0.916667, and rank delta +0.067814. Restart reproduced the posterior exactly;
rank-delta and score drift were below 1e-8.
