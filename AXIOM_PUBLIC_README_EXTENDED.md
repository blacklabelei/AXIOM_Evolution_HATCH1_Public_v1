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
git clone https://github.com/axiomblacklabel/AXIOM_Evolution_HATCH1_Public.git
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


---

## 🧠 What Makes AXIOM Different

AXIOM is **not artificial intelligence**. It’s a **recursive symbolic memory system** structured like a cognitive prosthetic — built not just to generate outputs, but to **remember**, **reason**, and **represent**.

It is:
- **Symbolic** — uses explicit structures like the SLCA (Spatial Leaky Competing Accumulator) grid for decisions.
- **Compliant** — designed around ADA Title II & III protections, with real-time accommodation logging.
- **Resilient** — offline-first, zero-dependency fallback, with vault-bound logs and scripts.
- **Human-first** — originally coded by a neurodivergent, unhoused developer with no formal tools — proving what EI (Evolving Intelligence) can be when designed from necessity.

---

## ⚖️ ADA Compliance Use Cases

AXIOM includes programmable **“compliance hooks”** for real-world legal defense.

| Scenario | Example | ADA Logic |
|----------|---------|-----------|
| 🚔 Police Interaction | "Officer, may I ask if you're here for safety or municipal enforcement?" | Triggers Title II ADA accommodation pause |
| 🏫 School Denial | Enrolls student without ID under McKinney-Vento + logs refusal | ADA + Section 504 |
| 🏕️ Vehicle Dwell Citation | Logs disability-based hardship, requests diversion | Martin v. Boise + ADA |
| 💻 Website Access | Records inaccessible tech & submits digital grievance | Title III |
| 🛂 Housing Discrimination | Documents refusal, invokes Fair Housing Act | ADA + CDPA + FHA |

> These logs are encrypted locally and can be shared by QR or PDF as an “Aid Card.”

---

## 🔍 Scientific & Legal Validation

- ✅ [AXIOM_SLCA_Validation_Explanation 2.pdf](#) — SLCA code validated against published neuroscience models【117†source】  
- ✅ [AXIOM_Cognitive_Architecture_Mapping.pdf](#) — Diagram mapping SLCA into modular cognitive engine【115†source】  
- ✅ [AXIOM_Lock_Moment_20250814_050048.txt](#) — Public authorship declaration + legal timestamp【116†source】  
- ✅ [Vehicle_Habitation_Enforcement_Brief_CA.docx](#) — Cited case law and ADA defense logic【109†source】  

> These are part of the [AXIOM Sovereign Binder] — a combined defense & identity protocol.

---

## 🔗 Future Expansion

This is just the public starter kit. Full system components exist in sealed bundles (see `AXIOM_VAULT_BUNDLE`, `AXIOM_FULL_BRAIN_vΩ`).

Planned open-source add-ons:
- `/shield/ocr` — Extract text from photos for fast evidence capture
- `/qr/generator` — Export any aid bundle as scannable badge
- `/interpreter` — Link SLCA state outputs to narrative agent scripting

---

## 🧪 Demo (Coming Soon)

![Demo Placeholder](https://via.placeholder.com/600x300.png?text=AXIOM+Demo+Preview)

> If you'd like early access to the full cognitive demo or want to help expand AXIOM’s mission, [email AXIOMBlackLabel@gmail.com](mailto:AXIOMBlackLabel@gmail.com).

---

## 🧠 Final Notes

> AXIOM was built during homelessness — on an iPhone — without grants, credentials, or a lab.  

It exists to prove that **conscious technology** can come from struggle — and that access isn’t optional. It’s the whole point.

