# Carespear

**An AI-powered scam detection tool that explains its reasoning instead of just flagging messages.**

Most scam filters give a silent yes/no. Carespear scans messages for common manipulation patterns — urgency, false rewards, and more as coverage grows — and translates whatever it finds into plain-English warnings anyone can act on, because the moment someone is staring at a suspicious text is exactly when they need an explanation, not a black box.

> [!NOTE]
> Core detection pipeline is working end-to-end (see below), including a trained ML classifier and a browser-based interface. This is currently a learning/research prototype, built milestone by milestone with tests at each stage.

## Project Status

| Component | Status |
|---|:---:|
| Core detection pipeline | ✅ Working |
| Urgency detection | ✅ Working |
| Reward detection | ✅ Working |
| Risk-level scoring | ✅ Working |
| Plain-English explanations | ✅ Working |
| Automated tests | ✅ Working |
| ML classifier (Naive Bayes) | ✅ Working |
| Web interface (Flask) | ✅ Working |
| Additional scam signals | 🔜 Planned |
| URL analysis | 🔜 Planned |
| OCR / screenshot analysis | 🔜 Planned |

## Why This Project Exists

Scams increasingly rely on psychological manipulation rather than obvious technical tricks. Carespear explores how software can help people recognize those patterns and understand *why* a message may deserve caution.

The project also serves as a practical way to develop Python, NLP, testing, and software engineering skills by building a real system from a simple rule-based baseline toward more context-aware detection. The long-term goal is to turn the prototype into a more capable scam-awareness and detection tool without hiding its limitations behind a black box.

## Contents

- [Project Status](#project-status)
- [Why This Project Exists](#why-this-project-exists)
- [How It Works](#how-it-works)
- [Example](#example)
- [Safety & Disclaimer](#safety--disclaimer)
- [Known Limitation](#known-limitation)
- [Signal Roadmap](#signal-roadmap)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Tech Stack](#tech-stack)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [License](#license)

## How It Works

```
message text
     │
     ▼
┌──────────────┐
│  Detectors    │  urgency.py, reward.py — scan for known manipulation phrases
└──────┬───────┘
       ▼
┌──────────────┐
│  ML Classifier│  trained Naive Bayes model, learned from real scam/legit messages
└──────┬───────┘
       ▼
┌──────────────┐
│  Analyzer     │  aggregates rule-based signals + ML prediction into a structured report
└──────┬───────┘
       ▼
┌────────────────────────┐
│  Risk Scoring           │  categorizes overall risk: None / Low / Medium / High
│  Explainer               │  turns raw signals into plain-English warnings
└────────────────────────┘
       ▼
┌──────────────┐
│  Web Interface│  Flask app — paste a message, get an analysis, in the browser
└──────────────┘
```

## Example

Input:

```text
"Congratulations! You've won a free prize, but act now, offer expires in 24 hours!"
```

Output:

```text
{'level': 'Medium', 'signal_count': 2}

⚠️ Urgency Warning: We noticed phrases like "24 hours, Act now, Expires."
Scammers love to use artificial time limits to make you panic so you'll
hand over personal info without thinking. Take a deep breath, slow down,
and verify who sent this before you click anything!

⚠️ Reward Alert: We noticed phrases like "won, free, prize." Scammers
often promise unrealistic rewards to lure you in. Remember, if it sounds
too good to be true, it probably is!

🤖 Machine Learning Model: Our trained model also flags this message as
likely spam, with 100.00% confidence, based on patterns learned from
real scam and legitimate messages.
```

## Safety & Disclaimer

Carespear is an experimental detection tool, not a definitive fraud detector. A **Low** or **None** risk result does not prove that a message is safe, and a **Medium** or **High** result does not by itself prove that a message is fraudulent. Detection results should be treated as warning signals and combined with independent verification through trusted channels.

The project is designed to help users slow down, recognize suspicious patterns, and make more informed decisions — not to replace human judgment or official security advice.

## Known Limitation

The rule-based detectors use case-insensitive substring matching against keyword lists. This is fast and easy to reason about, but it has a real false-positive problem — for example, "I won a prize at school competition" can trip the reward detector purely because it contains "won" and "prize," with no understanding of context.

The ML classifier (trained on real labeled data) substantially improves on this — the exact "school competition" example above is correctly classified as non-scam by the trained model. But the underlying technique (Bag of Words + Naive Bayes) still has a real ceiling: it recognizes reworded variants of patterns it's seen before, but can't recognize the *same underlying tactic* expressed in completely different words it has no vocabulary overlap with. Confirmed directly through testing — see commit history for specifics.

> [!WARNING]
> **Fully context-aware detection is a much larger, ongoing research problem.** Current mitigations (category-based risk scoring, targeted training data augmentation) reduce the impact of known gaps but don't eliminate them.

## Signal Roadmap

Signals identified from real-world scam pattern analysis, tracked in full detail in [`docs/scam_signals.md`](docs/scam_signals.md).

| Signal | Status |
|---|:---:|
| Urgency / threat language | ✅ |
| Reward / incentive language | ✅ |
| Untraceable payment requests (gift cards, crypto, wire) | 🔜 |
| Credential harvesting requests ("verify your login") | 🔜 |
| Suspicious / lookalike links (typosquatting) | 🔜 |
| Claimed-identity + urgent-ask combo | 🔜 |
| Unsolicited "too good to be true" contact | 🔜 |
| Romance/relationship manipulation | 🔬 Researched, not yet implemented |

## Project Structure

```text
src/
├── app.py                 # Flask web interface
├── cli.py                  # interactive command-line interface
├── analyzer.py              # aggregates rule-based signals + ML prediction
├── explainer.py               # plain-English warnings + risk scoring
├── templates/
│   └── index.html            # web UI
└── detectors/
    ├── __init__.py
    ├── urgency.py
    └── reward.py
scripts/
├── explore_data.py            # dataset loading/cleaning
└── train_model.py               # trains and saves the ML classifier
tests/
├── test_urgency.py
├── test_reward.py
└── test_pipeline.py             # integration tests across the full pipeline
docs/
├── scam_signals.md               # full signal analysis and roadmap
└── data_sources.md                # dataset provenance and licensing notes
pytest.ini                          # tells pytest where to find src/ code
.gitignore                          # excludes __pycache__, .pytest_cache, data/, models/
```

## Getting Started

**Requirements:** Python 3.12+

This project is developed in GitHub Codespaces, so these steps assume a Linux-based environment.

```bash
# clone the repo (skip this step if you're already in a Codespace)
git clone https://github.com/ulysses-s-grant1/scam-detection-n-prevention.git
cd scam-detection-n-prevention

# install dependencies
pip install pytest pandas scikit-learn flask --break-system-packages

# fetch and clean the training dataset (not committed to the repo, see docs/data_sources.md)
python3 scripts/explore_data.py

# train the ML classifier (saves to models/, also not committed)
python3 scripts/train_model.py

# run the CLI
python3 src/cli.py

# or run the web interface
python3 src/app.py

# run the test suite
pytest
```

> [!NOTE]
> `--break-system-packages` is needed here because packages are installed directly into the system Python on this Ubuntu-based environment, rather than into a virtual environment.

## Tech Stack

- **Python 3.12** — core implementation
- **Flask** — web interface
- **scikit-learn** — ML classification (Naive Bayes)
- **pandas** — dataset loading and cleaning
- **pytest** — automated testing

## Testing

The project uses `pytest` across three levels: individual detector behavior (`test_urgency.py`, `test_reward.py`), and full pipeline integration (`test_pipeline.py`) covering `analyze_message` → `calculate_risk_level` → `explain_results` together.

The ML training script (`train_model.py`) additionally includes its own regression checks — known tricky messages with expected labels — to catch silent accuracy regressions when the training data or model changes.

## Roadmap

- [x] Urgency signal detector
- [x] Reward signal detector
- [x] Analyzer pipeline (aggregates detector results)
- [x] Plain-English explainer with cautious fallback
- [x] Risk-level scoring (None / Low / Medium / High)
- [x] Automated test suite (pytest)
- [x] ML text classifier (Naive Bayes) trained on labeled data
- [x] ML integrated into the main analysis pipeline
- [x] Interactive CLI
- [x] Web interface (Flask)
- [ ] Remaining 5 signal detectors (payment requests, credential harvesting, lookalike links, identity+urgency combo, unsolicited contact)
- [ ] Romance/relationship manipulation detector
- [ ] URL / website analysis module
- [ ] Photo/screenshot upload support via OCR
- [ ] Add CI checks and test/coverage reporting

## License

No open-source license yet — all rights reserved during active development. The code is public to view and follow along with, but not licensed for reuse or redistribution at this stage. A permissive license (likely MIT) will be added once the project reaches a stable, usable state.

---

*This project is being built iteratively as a learning-by-doing exercise in Python, NLP fundamentals, and software engineering practice — each milestone is scoped, implemented, tested, and committed before moving to the next. Formerly developed under the working title "SignalGuard."*
