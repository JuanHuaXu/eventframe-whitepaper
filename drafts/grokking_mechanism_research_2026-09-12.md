# Grokking-informed background abstraction: research correction

Status: research proposal, not implemented or validated. This note replaces the earlier conversational claim that adding fuzz and compatibility penalties constitutes a grokking mechanism. It does not change the published specification or its claim register.

## Sources and evidence boundary

Read the primary papers' methods, mechanism sections, and relevant experimental appendices. This is a focused mechanism review, not an exhaustive literature survey or an independent reproduction of their experiments.

1. [Power et al., 2201.02177v1](https://arxiv.org/html/2201.02177v1), sections 2-3 and Appendix A.1: masked binary-operation tables with abstract tokens; delayed held-out generalization after fitting training examples. Their default uses a two-layer transformer and AdamW. Importantly, the dramatic late-generalization experiment uses Adam without weight decay. Explicit decay is therefore not a universal prerequisite. This motivates a fixed-data replay experiment, not a guarantee that replay discovers rules.
2. [Nanda et al., 2301.05217v3](https://arxiv.org/html/2301.05217v3), sections 3-5, Appendices C, D, E: reverse-engineered modular-addition computation; restricted/excluded logit ablations expose circuit development before the visible improvement. Excluded training loss rises during circuit formation. The interpretation of composition-driven emergence in Appendix E.2 is a hypothesis, not a theorem. Final-model frequency selection makes the reported diagnostic retrospective, not automatically a deployable early-warning certificate.
3. [Varma et al., 2309.02390v1](https://arxiv.org/html/2309.02390v1), sections 3-5 and 7: competing memorizing/generalizing circuits, different learning speeds, and parameter-norm efficiency; experimental partial generalization and reversal. Their minimal simulation supplies the successful circuit in advance, so reproducing that simulation alone cannot demonstrate discovery. Its norm-based argument does not prove an analogous claim about graph size, latency, or description length.

Source caution: Nanda section 3.1 prints a cosine product with the first operand repeated. The resolved identity is cos(A+B)=cos(A)cos(B)-sin(A)sin(B), also consistent with its later analysis. Do not mechanically copy the typo. Appendix D.1's numerical decay/time ordering conflicts with the surrounding prose; no timing law is imported from that sentence.

## Correction audit

- Confirmed: the previous static objective did not define learning dynamics or identify competing contributions to the forecast.
- Confirmed: a publication threshold can create a step-shaped performance curve without delayed learning.
- Confirmed: current section 7's nomination-law sensitivity diagnostic is not a learned terminal-outcome predictor.
- Recommendation only: introduce a separate, bounded experimental rule learner with explicit ablations. No production change is authorized by this note.
- Unsupported: identifying neural Fourier components with graph neighbors, or claiming that sheaf compatibility implies generalization.

## Proposed executable mathematical family

Everything below is our proposed adaptation, not a result proved by the cited papers.

### Fixed task, state, and information boundary

Start with a finite terminal outcome alphabet Y of size d, including an explicit no-event category when relevant. This categorical experiment is not the full continuous marked-time law. Freeze a published state v, extraction/encoding, candidate grammar, and baseline Q_v. Use fitting data D_fit, development data D_dev, and untouched confirmation data D_conf, split by complete trajectories and source lineage, not individual adjacent frames.

Background iteration n counts optimization steps over this fixed information, not new observations. Replaying one outcome does not increment production evidence counts, posterior support, or source independence. Generated perturbations are audit inputs, not newly observed truths.

Let b_v(C)=log Q_v(.|C), with a declared positive floor for Q_v. A candidate has an abstraction contribution A_phi,G(C) and an exemplar contribution M_psi(C), both in R^d. Center each vector over labels to remove the softmax offset ambiguity. Define

\[
z_n(C)=b_v(C)+A_{\phi_n,G_n}(C)+M_{\psi_n}(C),
\qquad
Q_n(.\mid C)=\varepsilon u+(1-\varepsilon)\operatorname{softmax}(z_n(C)),
\]

where u is uniform on Y and 0<epsilon<1 is frozen. Thus every probability is at least epsilon/d and log loss is finite. Use exactly this normalization for all controls and ablations.

M_psi is a declared finite exemplar model, for example sum_i k(C,C_i) psi_i with a fixed bounded retrieval kernel k and training-only exemplars C_i. Its capacity, retrieval cap, and behavior away from examples must be specified. It is not assumed incapable of generalization. A_phi,G must be learned without the hidden answer-generating rule.

### Make snapping a computation, not an unnamed assembler

A minimal admissible rule graph is a bounded directed chain with finite state spaces X_0,...,X_L=Y. Each stage supplies a learned row-stochastic matrix K_j. Context gives a normalized input law p_0(C), and

\[
q_G(.\mid C)=p_0(C)K_0K_1\cdots K_{L-1}.
\]

Smooth q_G with epsilon*u, and define A_phi,G as the centered log ratio log(q_G^epsilon)-log(Q_v). Then b_v+A_phi,G, before the outer smoothing, decodes to q_G^epsilon exactly. This gives the abstraction an actual connection to the scored law.

Learn transition matrices from available training transitions or terminal likelihood; hidden stages are latent, not supplied invented labels. A finite search grammar proposes aligned stages, bounded joins, splits, and rewires. Fitting and identifiability remain experimental questions. General graphs require an explicit normalized joint model; agreement of pairwise marginals alone is insufficient.

For domain-A and domain-B chains, let T_j:X_A,j -> X_B,j be a declared deterministic correspondence on its valid domain. Its row-stochastic matrix R_j permits the typed compatibility defect

\[
D_{\mathrm{snap}}=
\sum_j w_j\,\mathbb E_{x\sim\nu_j}
\operatorname{TV}\left(
K_{A,j}(x,.)R_{j+1},\ (R_jK_{B,j})(x,.)
\right).
\]

Weights sum to one; nu_j and the required interfaces are frozen. Both distributions live on X_B,j+1. Missing required interfaces cannot silently remove terms. A stochastic R_j instead of a deterministic correspondence needs a separately declared interpretation. These commuting-square tests remain sheaf-inspired; they neither instantiate sheaf gluing laws nor identify real-world causation.

Fuzzing supplies valid context transformations T_a and proposed outcome transformations U_a:

\[
D_{\mathrm{fuzz}}=
\mathbb E_{(C,a)\sim\nu_f}
\operatorname{TV}\left(Q_n(.\mid T_aC),(U_a)_\#Q_n(.\mid C)\right).
\]

Identity U_a tests invariance; nonidentity U_a tests a proposed translation. Specify validity and independently justify or learn the correspondence using fitting data. Do not derive test labels by assuming the hypothesis being evaluated. Preserve section 7's non-target-field and terminal-effect checks; consistency never substitutes for observed terminal accuracy.

### Learning dynamics and competition

For a fixed candidate topology, take actual iterative optimization steps on

\[
F(\phi,\psi,G)=\widehat L_{\mathrm{fit}}(Q)
+\lambda_fD_{\mathrm{fuzz}}+\lambda_sD_{\mathrm{snap}}
+\lambda_A\|\phi\|_2^2/2+\lambda_M\|\psi\|_2^2/2
+\lambda_G c(G).
\]

L_fit is mean negative log probability of observed outcomes. For this finite experiment c(G) is the number of free transition parameters plus a fixed code cost for topology and correspondence tables; the alphabet, parameterization, precision, and coding scheme are frozen. It measures representation cost, not execution latency. Norms are parameterization-dependent. Equalize or ablate regularization choices; do not assume the abstraction is more efficient by assigning it a cheaper arbitrary coefficient.

An explicit optimizer can use projected gradient steps on stochastic matrices and bounded exemplar parameters; proposal search makes discrete topology changes. A resource-capped beam retains partial compositions, including candidates that do not yet beat the baseline individually. The beam policy and cap must be measured: there is no guarantee it retains the needed pieces. No production confidence is awarded to an unfinished candidate.

Record F, component losses, prediction margins, parameter norms, topology size, and unthresholded held-out performance versus n. Do not implement a scripted delay, automatic exemplar deletion, or hardcoded successful rule to manufacture a grokking curve. Unlike neural AdamW, this explicit regularized optimizer is a new method; no equivalence is asserted.

### Measure the mechanism with ablations

Define Q_A,n using b_v+A only, and Q_M,n using b_v+M only. At each checkpoint, without refitting after ablation, evaluate

\[
L_{\mathrm{full},n}=\widehat L(Q_n),\quad
L_{\mathrm{A},n}=\widehat L(Q_{A,n}),\quad
L_{\mathrm{M},n}=\widehat L(Q_{M,n}).
\]

These are structural ablations, not the paper's Fourier projections. The removal penalty L_M-L_full estimates how much this fixed system relies on the abstraction. A positive L_full-L_A indicates that exemplar contribution is harmful on that evaluation distribution. Neither quantity alone proves generalization or causal truth.

Measure all three separately on fitting, development, and locked confirmation trajectories. Development diagnostics may steer search but lose confirmatory status. Confirmation checkpoint curves can be analyzed only under a frozen protocol, with no feedback into the run; adaptive publication needs fresh blocks or a valid sequential/multiple-testing procedure.

Joint component ablations test whether snapping contributes more than ordinary standalone-rule selection. Include equally sized random-component ablations, no-fuzz, no-snap, no-complexity-pressure, and no-abstraction controls. If a newly composed rule works but no prior hidden improvement or change in competing contributions is measured, call it successful abstraction learning, not demonstrated grokking dynamics.

### Publication and cleanup are separate hypotheses

Search returns a candidate, not a production update. Paired confirmation must show complete-law gain and protected-group non-inferiority; retain Anti-Pigeon, evidence, snapshot-dependency, and runtime gates. Evaluate the candidate against both the active baseline and the same baseline plus an ordinary learner under matched data and compute budgets.

Any reduced exemplar influence is reversible and applies to serving parameters, not deletion of source observations or exception records. Gate partial cleanup separately on exceptions. Publication atomically installs a bounded representation only while the dependency versions still match. Discovery, optimization, and audits stay off the hot path; matrix application must itself pass the hot-path budget. No sub-100ms claim follows from the equations.

## Experiment that could falsify the adaptation

1. Reproduce a small neural modular-addition baseline separately, using the authors' setup as a reference. Measure actual training and held-out curves. This validates the laboratory, not EventFrame.
2. Give the external learner a fixed table of opaque symbols and observed event transitions. Keep hidden operation and test outcomes outside its grammar, extraction, and search inputs. A supplied arithmetic oracle is an upper-bound control only.
3. Sweep unique-data coverage and background compute independently across frozen seeds. Repeated rows do not create additional independent evidence. Measure new combinations, not renamed copies leaking through retrieval.
4. Track component-only and full predictions throughout discovery before any publication threshold. If only publication creates the jump, reject the mechanistic-grokking claim.
5. Add noncomposable/random labels, exceptions, changed regimes, and narrowed replay coverage. Report partial gains and regression rather than forcing a universal-success criterion.
6. Charge discovery and application costs separately. Compare the combined method with simpler predictors; a complex mechanism that loses to ordinary fitting has not earned integration.

## Integration decision

Keep the existing published sensitivity/snapping claims unchanged. The missing research component is a learned, scored compositional predictor plus component-level progress measurements. Fuzzing and snapping can propose and constrain that predictor, but are not by themselves its learning mechanism. This draft is sufficient to specify the next prototype's boundaries; no empirical grokking, convergence, or continuous-learning superiority claim is established.
