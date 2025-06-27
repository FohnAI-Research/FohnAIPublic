# Detecting Zero-Hour Phishing with Human-Level Context

## Objective

This research initiative explores the detection of phishing attacks at zero-hour — the moment they appear — by simulating a level of cognitive and contextual understanding that approximates human intuition. Traditional filters rely on known signatures, rule-based triggers, or static heuristics. We intend to build and evaluate a machine intelligence pipeline capable of identifying threats before threat intelligence reports catch up.

This effort is grounded in one of Cencori’s foundational promises: proactive defense for individuals, enterprises, and governments. The system will ultimately be integrated into CIE — the Cencori Intelligence Engine — as part of its real-time threat recognition layer.

## Hypothesis

> A system trained on diverse contextual signals — including semantic content, metadata relationships, behavioral priors, and real-world temporal anomalies — can detect phishing attempts with <1% false positives and >95% detection accuracy at first encounter, without requiring a threat signature update.

We hypothesize that phishing emails and messages can be detected *without prior exposure* to the exact attack, by using semantic generalization, URL reputation heuristics, metadata outlier detection, and structural embeddings of conversation patterns.

## Scope

This research will:
- Focus exclusively on **zero-hour phishing detection** via e-mail and browser input.
- Use **only publicly available datasets** and synthetic augmentation to simulate novel phishing attempts.
- Build a baseline detection model from established architectures.
- Design and test novel detection techniques using proprietary logic (kept in private repo).
- Evaluate performance on *time-sliced* datasets to test generalization over unseen samples.

We will not:
- Build response or remediation logic (e.g., auto-delete, quarantine).
- Train end-to-end models on private Cencori user data.
- Open-source the final model weights or internal scoring functions.

## Approach

The methodology is divided into five phases:

### 1. Literature and baseline replication
We’ll review existing open-source phishing detection models and replicate at least one in the public domain as a benchmark. This includes models trained on the Enron dataset, PhishTank, or datasets available through Kaggle or VirusTotal.

### 2. Dataset construction
We’ll compile a dataset composed of:
- Public e-mail corpora (e.g. Enron, Nazario phishing set)
- Open source phishing URLs and landing pages
- Publicly crawled HTML/JS of phishing campaigns
- Synthetic phishing content generated using LLMs to simulate novel styles

A portion of this data will be time-split to simulate a “true zero-hour” condition: the model must evaluate examples without prior exposure to structurally similar samples.

### 3. Model design
The baseline will use BERT-style embeddings on e-mail body, headers, and link features. Additional models will explore:
- Multi-modal attention over content + metadata
- Behavioral context scoring (i.e. user-device frequency, network anomaly)
- Light graph-based link reputation scoring (non-causal)

The full pipeline will include:
1. Content preprocessing
2. Embedding + multi-feature vectorization
3. Classifier ensemble (baseline + novel layers)
4. Scoring + interpretability layer

### 4. Evaluation
Performance will be judged on:
- Precision, recall, F1, ROC-AUC
- Time-to-detection (TtD)
- False-positive rate (must remain <1%)
- Detection rate for synthetic zero-day samples

All evaluations will be conducted in Jupyter and Python scripts, with replicable notebooks shared publicly.

### 5. Publication
Our outputs will include:
- A public whitepaper outlining methods and results
- A GitHub repo with the dataset registry and baseline code
- A Substack post explaining the findings in plain language
- An arXiv submission detailing the experimental framework

We will **mention** the Cencori Intelligence Engine (CIE) as the parent system, but will **not disclose proprietary architectures, feature engineering strategies, or live deployment mechanisms**.

## Risk & Disclosure

This research will not include:
- Any real Cencori user data
- Any personally identifiable information (PII)
- Any real-time internet scraping
- Any model or pipeline that could be directly weaponized by attackers

All research artifacts will be reviewed through a red-team disclosure gate prior to publication.

## Success Criteria

This project will be considered successful if:
- It demonstrates statistically meaningful detection performance on zero-day phishing messages using only public data.
- It produces a replicable pipeline and a clear publication.
- It lays the foundation for further work in adversarial robustness and generalizable cyber-threat cognition inside the CIE suite.

## Timeline

| Phase                | Milestone                                  | ETA         |
|---------------------|---------------------------------------------|-------------|
| Replication          | Baseline BERT phishing model reproduced     | Week 1      |
| Dataset              | Zero-hour dataset created and verified      | Week 2      |
| Modeling             | Novel feature extractor implemented         | Week 3–4    |
| Evaluation           | Benchmarking and stress tests completed     | Week 5      |
| Paper                | Whitepaper + arXiv + Substack published     | Week 6      |

---

This document defines the scope of research under the ZeroHourPhishing initiative. Updates, lab notes, results, and further technical documentation will be maintained within the repository. All rights, IP, and future extensions belong to FohnAI.
