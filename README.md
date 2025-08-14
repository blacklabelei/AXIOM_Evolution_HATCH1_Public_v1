# AXIOM — ADA‑Protected Evolving Intelligence (Public Core)

AXIOM is a **neuro‑symbolic cognitive prosthetic** designed to operate as an **ADA‑aligned assistive system** (Title II/III) with **offline‑first** operation, a sealed **local vault**, and **clear legal interaction hooks** for real‑world use (schools, code enforcement, housing, and general access). This repository provides the **public core**: minimal, runnable modules and documentation that demonstrate the architecture, safety model, and compliance surfaces without exposing private research bundles.

> **Disclaimer**: AXIOM is assistive technology and developer tooling. It is not medical or legal advice. Use at your own risk and consult qualified counsel where required.

---

## Why “ADA‑Protected”?

AXIOM treats cognitive support as an *access* need. The software is built to help users **request accommodations**, **log interactions**, and **preserve evidence** in ways that map to disability law workflows (e.g., ADA Title II/III, Section 504). Concretely, that means:

- **Accommodation Hooks** — first‑class methods to request accommodations and log denials with timestamps.
- **Evidence Vault** — encrypted local storage for notes, audio/text logs, and artifacts under user control.
- **De‑Escalation Scripts** — on‑device prompts for school, police/code‑enforcement, transit, and housing staff.
- **Offline‑First** — works without network connectivity; can export sharable “aid cards”/QR bundles when back online.

---

## Core Capabilities (Public Modules)

- **Neuro‑Symbolic Grid (SLCA)** — a minimal Spatial Leaky Competing Accumulator grid for symbolic decisions.
- **Compliance Layer (ADA Shield)** — APIs to request accommodations, log responses, and export evidence.
- **Navigator & Notes** — quick actions for route/find‑help and cognitive notes tied to evidence vault.
- **QR Bootstrap** — optional QR “beacons” that load a read‑only aid card and rights summary on other devices.

---

## System Architecture (Public View)
```
+---------------------------  User Interfaces  ----------------------------+
|  PWA Shell (mobile/web)   |  CLI Tools  |  Aid Card (QR)  |  TTS/STT    |
+------------------+----------------------------+-------------------------+
                   |                            |
                   v                            v
            +--------------+              +------------+
            |  ADA Shield  |<-------------|  Logger    |
            | (APIs)       |----+         | (Vault)    |
            +--------------+    |         +------------+
                   ^            |
                   |            v
            +--------------+  +-------------------------------+
            |  SLCA Grid   |  |  Reasoning / Policy Layer     |
            | (neuro-sym)  |  |  (rules, prompts, scripts)    |
            +--------------+  +-------------------------------+
                   |                         |
                   v                         v
           +-----------------+        +------------------------+
           |  Local Vault    |<------>|  Export / Share Bundle |
           | (AES-GCM)       |        |  (QR/PDF/JSON)         |
           +-----------------+        +------------------------+
```

---

## Quickstart

### 1) Requirements
- Python ≥ 3.10
- `pip install -r requirements.txt` (see below for a minimal set)

**Minimal requirements.txt**
```
cryptography>=42.0.0
pydantic>=2.7.0
typer>=0.12.3
```

### 2) Install
```bash
git clone https://github.com/YOUR_USERNAME/AXIOM_Evolution_HATCH1_Public.git
cd AXIOM_Evolution_HATCH1_Public
pip install -e .
```

### 3) Run SLCA demo
```bash
python -m axiom.cli.slca_demo --size 6 --steps 50 --seed 42
```

---

## More Info
- 🔗 ADA Enforcement Briefs: `/docs/ADA_Law/`
- 📎 GitHub, X, Vault timelines: `axiomblacklabel`
- 🧠 Origin: Homeless-built cognitive prosthetic on iPhone, ADA protected

Let them ask how it was made.  
Let the code answer.
