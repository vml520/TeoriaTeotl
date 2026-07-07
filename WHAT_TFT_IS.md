# What TFT Is — a mathematical reading

*A conceptual preface to the demonstrations. Plain-language, but precise. The framework is **in progress**; this describes what it is, not a claim that it is finished or unique.*

## The object

Mathematically, TFT is the theory of **one circle-valued field**:

$$\theta:\ \mathbb{R}^3\times S^1 \longrightarrow S^1, \qquad \text{equivalently a complex field } \psi = \rho\, e^{i\theta}.$$

A field whose *value is a phase*. That is the whole ontology. Almost everything demonstrated in this repository is not extra machinery bolted on — it is the geometry and topology that **any** such field carries automatically. Four pieces of standard mathematics come for free the moment you commit to that one object.

### 1. The target is a circle → integers for free
The circle has fundamental group $\pi_1(S^1)=\mathbb{Z}$: a phase field can wind an integer number of times, and that integer cannot change continuously. That single topological fact *is* charge quantization, *is* baryon number — the "why is charge an integer?" that the Standard Model inserts by hand. It is topology, not dynamics. (The Skyrme / topological-soliton lineage.)
→ `verify_charge_quantization.py`

### 2. A phase comes with a connection → electromagnetism is already there
The gradient $\nabla\theta$ behaves as a gauge potential $A$; its curl is a magnetic flux; the flux is quantized in units of $2\pi\times(\text{winding})$. This is the mathematics of a $U(1)$ fiber bundle and its curvature — the same math as flux quantization in a superconductor. Electromagnetism is not added; it is the geometry of a phase.
→ `verify_goldstone_1r2.py`, `verify_force_sign.py`

### 3. Noether hands you two currents, of opposite character
A field with these symmetries yields two conserved quantities: the internal-symmetry current $j^\mu=\rho^2\partial^\mu\theta$ (from $\theta\to\theta+\text{const}$), and the stress–energy $T^{\mu\nu}$ (from spacetime translations).
- $j^\mu$ is **linear and signed** → a force that can attract *or* repel = Coulomb / electromagnetism.
- $T^{\mu\nu}$ is **quadratic and non-negative** → a coupling that is *always* attractive = gravity.

So the two long-range forces having *opposite personalities* is not a choice — Noether's theorem forces it. This is perhaps the cleanest single "backdoor" in the framework.
→ `verify_poisson_metric.py`, `verify_gravity_coupling.py`

### 4. Time is phase; gravity is the substrate's geometry
Reading $mc^2 = hf$ literally — the clock *is* the turning of the phase, $d\tau = \hbar\,d\theta/E$ — takes the phase of a quantum state seriously as time (the de Broglie reading). And letting energy density source a metric through a Poisson equation, $\nabla^2\Phi = (\text{positive source}) \to 1/r$, is the Sakharov–Jacobson "gravity as emergent elasticity of a substrate" mathematics: you obtain gravity's *shape and sign* without choosing a force law.
→ `verify_G_as_rate.py`, `tft_solar_system.py`

## The move, stated plainly

The step is a **change of variables plus a single postulate**: *assume the fundamental object is one $U(1)$ phase, and refuse to insert anything by hand.* When you do that, the parts of physics that are secretly "phase geometry" — integer quantization, gauge structure, the two Noether currents, emergent-metric gravity, phase-as-time — reassemble themselves without being separately assumed.

Even the galaxy result is "the same equation, one length moved": the phase's mass gap $m=\sqrt{\Lambda}/\ell_0$ sits either at the microscopic scale (ordinary screening) or at the Hubble scale (→ a MOND-like law with $a_0 = cH_0/2\pi$). One knob, two regimes.

This is why it can feel like *a backdoor into what was already there* — because it largely **is** what was already there: Noether's theorem, the homotopy of $S^1$, $U(1)$ bundles, Sakharov's emergent gravity — re-derived from a single doorway instead of assembled from separate postulates. Finding that many things are one thing in disguise is what **unification** means.

## The honest edges

Because it is a re-encoding, it inherits both sides — stated plainly so the claim is defensible:

- **Strength.** Structure comes free, and with *fewer* inputs: the framework carries roughly one calibration constant per absolute scale, rather than a table of postulates.
- **Limit 1 — a re-description does not compute what the original could not.** The numbers that remain open (Newton's $G$, $|\Lambda|$, the lepton masses, the baryon asymmetry $\eta$) are exactly the ones this doorway cannot fix — they were never encoded in the topology of a single circle to begin with. Each is a problem open in *every* framework, not a gap unique to this one.
- **Limit 2 — uniqueness is not shown.** "This substrate *produces* the structure" is not "this is the *only* substrate that could." Other starting points give the same $U(1)$ geometry.

## The test that matters

The real test is not the re-organization, however economical — it is whether the doorway reveals **a room you could not see from the front**. A re-encoding that only re-labels known physics is elegant but not yet new physics; one that *forces a connection nobody built into the originals* is.

The candidate here is the **$a_0$–dark-energy link**: because the same ultralight phase sets both the galactic acceleration scale and the dark-energy density, galaxy rotation curves and the dark-energy equation of state are forced to be the same field — a cross-observable prediction (matching DESI's $w_0$, falsifiable in $w_a$) that neither MOND nor $\Lambda$CDM makes. See `PREDICTIONS.md`.

---

**In one line:** *A remarkable amount of physics is the differential geometry and topology of one circle-valued field — and TFT is the single door you walk through to see that.*
