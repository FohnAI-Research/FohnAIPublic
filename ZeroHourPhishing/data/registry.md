# Zero-Hour Phishing Dataset Registry

## Overview

This registry lists the datasets we’ll use to build and evaluate our zero-hour phishing detection models. All datasets here are publicly available, legally redistributable (where applicable), and structured for rapid integration into ML pipelines. Each dataset is vetted for relevance to our goals: semantic variation, timestamped data for zero-hour slicing, and inclusion of phishing vs legitimate messages or links.

We categorize datasets into five groups:
- E-mail corpora
- Phishing URL/link databases
- HTML landing pages
- Synthetic phishing generation
- Metadata & behavioral context

We prioritize sources that allow us to simulate **first-encounter conditions**, with **timestamped data** or structures that reflect real-world timelines.

---

## 1. E-mail Corpora

### A. Enron E-mail Dataset (Legitimate)
- **Link:** https://www.cs.cmu.edu/~./enron/
- **Size:** ~500,000 emails from ~150 users
- **Content:** Real corporate e-mails from Enron employees, no known phishing
- **Usage:** Background corpus for benign content structure
- **License:** Public domain (via CMU)

### B. Nazario Phishing Corpus (Phishing)
- **Link:** http://monkey.org/~jose/wiki/doku.php?id=PhishingCorpus
- **Size:** ~3,000 phishing emails (2005–2007)
- **Content:** Raw phishing e-mails, with headers and payloads
- **Usage:** Simple labeled phishing set for early benchmarks
- **License:** Open, attribution recommended

### C. PhishingCorpus.org (Mixed)
- **Link:** https://www.phishingcorpus.org/
- **Size:** Varies (updated monthly)
- **Content:** Crowdsourced phishing + spam + ham e-mails
- **Usage:** Evaluation only — not reliable for training
- **License:** Custom; allowed for research

---

## 2. Phishing URL Datasets

### A. PhishTank
- **Link:** https://www.phishtank.com/
- **Size:** ~25,000 fresh URLs per month
- **Content:** Community-verified phishing sites with timestamps
- **API Access:** Free for non-commercial research
- **License:** Terms allow use with citation

### B. OpenPhish
- **Link:** https://openphish.com/
- **Content:** Real-time feed of phishing URLs and targets
- **Usage:** Cross-checking PhishTank; validating synthetic samples
- **License:** Freemium API, manual scraping may be limited

### C. Kaggle: Malicious URLs Dataset (2020)
- **Link:** https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset
- **Size:** 650,000 URLs with labels (benign/phishing/malware)
- **License:** CC BY-NC-SA 4.0

---

## 3. HTML & Web Landing Pages

### A. UCI Phishing Websites Dataset
- **Link:** https://archive.ics.uci.edu/ml/datasets/Phishing+Websites
- **Size:** ~11,000 instances
- **Content:** Hand-crafted features extracted from real phishing web pages
- **Limitations:** No raw HTML; good for model feature inspiration
- **License:** Open

### B. PhishZoo Dataset
- **Link:** https://github.com/ragibhasan/PhishZoo
- **Content:** Phishing vs legit HTML landing pages (archived)
- **Usage:** Ideal for contrastive learning or fine-tuning
- **License:** Free for research use

---

## 4. Synthetic & Adversarial Generation

### A. HuggingFace: LLM-Generated Phishing Dataset
- **Link:** https://huggingface.co/datasets/llm-phishing (example, hypothetical)
- **Content:** AI-generated phishing emails created via prompt engineering
- **Status:** Experimental, growing field
- **Use:** Test zero-day model robustness

### B. FohnAI-Synthetic (Internal)
- **Source:** LLM-generated phishing prompts + style transfer
- **Status:** Created under `FohnAIPrivate`
- **Use:** Private test set for adversarial resilience
- **License:** Internal IP, not shared

---

## 5. Metadata & Behavioral Data (Optional)

### A. CERT Insider Threat Dataset
- **Link:** https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=508099
- **Content:** Simulated e-mail, HTTP, system logs from insider threat scenarios
- **Use:** Behavior modeling (if extended in future)
- **License:** Public for academic use

### B. Outlook/Thunderbird Header Sets (Scraped)
- **Content:** Open-source e-mail client logs used to simulate metadata
- **Use:** Device/user context modeling
- **Note:** Not used in current baseline; reserved for future extensions

---

## Licensing & Legal Summary

| Dataset | License | Allowed Usage |
|---------|---------|----------------|
| Enron | Public domain | Full usage |
| Nazario | Informal open | Academic research |
| PhishTank | Custom | With attribution |
| Kaggle URLs | CC BY-NC-SA | No commercial use |
| OpenPhish | Free API | Research only |
| UCI | Open | Full usage |
| HuggingFace (LLM) | TBD | Research only |

We will store only **dataset loaders** in this repo (`data/loaders.py`), and provide public links to download the actual data. Large or proprietary datasets will not be included in this repository.

---

## Next Step

A baseline training pipeline using a mix of:
- Enron (ham)
- Nazario + OpenPhish (phish)
- LLM-synthetic (zero-day variants)

will be built to validate our first classifier.

For licensing and citation, refer to `/docs/disclosure_policy.md` (to be created).
