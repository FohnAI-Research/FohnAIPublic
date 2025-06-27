# Literature Review – Zero-Hour Phishing Detection

## Introduction

Zero-hour phishing detection refers to the ability to detect and flag phishing messages at the moment they are first encountered, before threat intelligence feeds, blacklists, or user reports have been updated. This is a challenging problem because phishing attacks constantly evolve, often using novel templates, URL cloaking, and adversarial prompts to evade detection systems trained on past data.

This literature review surveys state-of-the-art approaches in phishing detection across academic papers, open-source tools, and commercial baselines. We categorize the work into five domains: content-based detection, link and metadata analysis, graph and reputation modeling, machine learning pipelines, and adversarial robustness.

## 1. Content-Based Detection

Early systems relied heavily on handcrafted rules and keyword matching. However, recent advancements in NLP and transformer models have made content-based detection more sophisticated and context-aware.

### Key papers and systems:
- **Bahnsen et al. (2017)** – Used TF-IDF and logistic regression to detect phishing in e-mails with ~95% accuracy, but vulnerable to paraphrasing and template manipulation.
- **Huang et al. (2020)** – Introduced a BERT-based phishing classifier trained on email bodies and subject lines. It significantly outperformed older statistical models.
- **OpenPhish NLP stack** – Uses sentence-level parsing to look for emotional manipulation, urgency, and financial bait.

### Limitations:
- Pure content analysis struggles with synthetic and generative attacks.
- Cannot account for external context like sender behavior or unusual time-of-day.

## 2. Link and Metadata-Based Detection

URLs embedded in messages are common phishing vectors. Some research has focused solely on URL-based classifiers, while others integrate them as secondary features.

### Representative works:
- **Ma et al. (2009)** – Classic paper on classifying URLs using lexical and host-based features via online learning (AUC > 0.98).
- **Choi et al. (2011)** – Incorporated WHOIS data and URL lifespan into phishing classifiers.
- **URLNet (2018)** – Deep-learning model using character-level CNNs on URLs.

### Industry tools:
- **VirusTotal** – Aggregates antivirus and URL scanner results.
- **Google Safe Browsing API** – Frequently used to enrich URL data, but not zero-hour.

### Weaknesses:
- Heavy reliance on third-party lookups delays real-time performance.
- Many phishing URLs are short-lived (less than 2 hours) and bypass known blacklists.

## 3. Graph & Reputation-Based Modeling

Some models treat phishing detection as a graph problem — mapping sender relationships, domain reputation, or clickstream traces.

### Research insights:
- **SenderGraph (Microsoft Research, 2016)** – Built dynamic graphs of sender-recipient relationships to identify anomalies.
- **PhishSentry (2020)** – Used a bipartite graph of email senders and URLs to compute PageRank-like scores on domain trustworthiness.
- **FastPhish (USENIX 2021)** – Modeled email+URL+attachment relations as a temporal graph for real-time scoring.

### Benefits:
- Enables detection of coordinated phishing campaigns across users.
- More resilient to template churn or phrasing changes.

### Limitations:
- Requires large-scale infrastructure.
- Not practical for lightweight, on-device defense without serious compression or summarization.

## 4. End-to-End Machine Learning Pipelines

Full-stack phishing detection systems use multiple modalities: content, metadata, attachments, time, and user behavior.

### Benchmarks:
- **CANTINA++** – Hybrid feature-based system combining content with source reputation.
- **CIC-Phishing-Email 2021 Dataset** – Multi-feature dataset containing email text, headers, links, and attachments. Widely used to benchmark end-to-end models.
- **PhishBench** – A multi-model evaluation suite for phishing detection using standard ML frameworks.

### Limitations of prior pipelines:
- Many models are trained on outdated datasets (e.g., Enron).
- They often assume access to user interaction data (e.g., whether a link was clicked), which violates zero-hour constraints.
- Few address adversarial robustness.

## 5. Adversarial & Synthetic Phishing

The most difficult problem is detecting phishing messages designed specifically to bypass known filters — including those crafted by LLMs.

### Emerging research:
- **PhishLLM (2023)** – Demonstrated how GPT-3.5 can generate phishing e-mails that bypass popular detectors. Included benchmark prompts and performance degradation scores.
- **PromptShield (2024)** – Created synthetic adversarial prompts using LLMs and fine-tuned classifiers to defend against them.
- **HuggingFace Dataset: LLM-generated phishing** – Contains synthetic phishing samples designed to test robustness.

### Opportunity:
- Most open-source detectors fail on LLM-generated phishing samples.
- There’s no widely adopted benchmark for zero-hour, LLM-originating threats — a research gap we can exploit.

## Key Takeaways

- There is **no dominant open-source model** for zero-hour phishing that integrates content, metadata, and contextual behavior.
- Most systems depend on **external threat intelligence**, making them vulnerable to first-encounter failure.
- Graph-based and transformer-based models hold promise, but are often siloed and lack interpretability.
- **Adversarial resilience is underdeveloped**, especially against synthetic phishing from LLMs.
- A system that **fuses lightweight content embeddings, behavioral context, and threat priors — all without calling external APIs — is still missing from public research.**

## Strategic Implication for FohnAI

This literature survey affirms that our approach — detecting phishing at zero-hour using context-aware modeling, without dependence on blacklists or past examples — is still largely uncharted in public research. By positioning our detection pipeline as a modular component of the CIE suite, we will demonstrate not just technical depth, but a differentiated design philosophy centered on preemptive cognition.
