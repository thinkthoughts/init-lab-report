# init-lab-report

Minimal scaffold for reproducible lab reports using:

* Residue Manifold Learning (RML)
* Constraint-Guided Coherence Scoring (CGCS)
* bridge figures
* runnable notebooks
* report artifacts
* configurable domain translation layers

The repository is designed as a reusable initialization surface for future lab-specific collaborations.

---

## Structure

```text
init-lab-report/
├── README.md
├── Makefile
├── requirements.txt
│
├── site/
│   └── index.html
│
├── src/
│   └── general/
│       ├── __init__.py
│       ├── cgcs.py
│       ├── zabcd.py
│       ├── admissible.py
│       ├── persistence.py
│       ├── deescalation.py
│       ├── bridges.py
│       ├── reports.py
│       └── configs.py
│
├── configs/
│   └── init.json
│
├── notebooks/
│   ├── init.ipynb
│   └── mod30/
│       ├── 01.ipynb
│       ├── 07.ipynb
│       ├── 11.ipynb
│       ├── 13.ipynb
│       ├── 17.ipynb
│       ├── 19.ipynb
│       ├── 23.ipynb
│       └── 29.ipynb
│
├── figures/
├── reports/
└── results/
```

---

## Design

The repository separates:

```text
general framework
≠
domain-specific reports
```

The `src/general/` modules provide reusable structure:

* CGCS scoring
* admissible-state logic
* persistence/recovery operations
* bridge-figure generation
* report exports
* configuration loading

The `configs/` layer provides domain translation constraints and report context.

The `notebooks/` layer generates runnable report artifacts.

---

## Notebook Structure

### `init.ipynb`

Initialization notebook:

```text
initial report surface
→ bridge figure
→ key points
→ generated artifacts
```

This notebook functions as the initial collaboration/report scaffold.

---

### `mod30/`

Canonical admissible-lane demonstrations:

```text
{1,7,11,13,17,19,23,29}
```

These notebooks provide constrained examples using modulo-30 residue structure.

---

## Generated Artifacts

Typical outputs:

```text
figures/
reports/
results/
```

Artifacts may include:

* bridge figures (`.svg`, `.png`)
* markdown reports (`.md`)
* structured results (`.json`, `.csv`)

---

## Workflow

```text
site
→ report
→ notebook
→ figure
→ results
→ next-step collaboration
```

The goal is to reduce organizational noise and generate reusable continuation surfaces for scientific collaboration.

---

## Example Future Forks

```text
biofrontiers-allen-lab
climate-lab-report
watershed-lab-report
```

Each fork reuses the same general framework while changing:

* configs
* reports
* notebooks
* figures
* domain-specific datasets
