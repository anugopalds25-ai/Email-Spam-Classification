# Email Spam Classification Using NLP and Machine Learning

> Predictive Analytics Group Project | Academic Year 2025–26

## Team Members
| Name | Role | GitHub |
|------|------|--------|
| Fidal Govind | Member A — Problem definition, preprocessing, TF-IDF, explainability, README | @fidal |
| Arjun S | Member B — Data loading, EDA, Naive Bayes & SVM, Streamlit deployment | @arjun |
| Anu Gopal | Member C — Feature selection, LSTM, model evaluation, GitHub profiles | @anu |

---

## Problem Statement
Email spam remains a major challenge — it wastes time, carries phishing links, and clogs infrastructure. This project builds a multi-model NLP classifier that distinguishes spam from legitimate (ham) emails, comparing classical ML approaches (Naive Bayes, SVM) with a deep learning approach (LSTM).

---

## Dataset
- **Source:** SpamAssassin Public Corpus — https://spamassassin.apache.org/publiccorpus/
- **Size:** ~6,047 emails
- **Classes:** Ham (legitimate) ~4,150 | Spam ~1,897
- **Format:** Raw `.txt` files with email headers and body
- **Split:** 70% train / 15% validation / 15% test (stratified)

---

## Project Architecture

```
Raw Emails (.txt)
      ↓
[Stage 3] Preprocessing Pipeline
  - Strip headers, HTML, URLs
  - Lowercase, remove punctuation
  - Tokenize, remove stopwords, lemmatize
      ↓
[Stage 5] Feature Engineering
  - TF-IDF (unigrams + bigrams) → Naive Bayes, SVM
  - Word2Vec embeddings → LSTM
  - Chi-square feature selection
      ↓
[Stage 6] Model Training
  ┌──────────────┬──────────────┬──────────────┐
  │  Naive Bayes │     SVM      │     LSTM     │
  └──────────────┴──────────────┴──────────────┘
      ↓
[Stage 7] Evaluation: F1, ROC-AUC, Confusion Matrix
      ↓
[Stage 8] Explainability: LIME, feature importance
      ↓
[Stage 9] Streamlit Deployment
```

---

## Data Science Life Cycle Coverage

| Stage | Description | Owner |
|-------|-------------|-------|
| 1 | Problem Definition & Literature Review | Fidal |
| 2 | Data Collection & Understanding | Arjun + Anu |
| 3 | Preprocessing & Cleaning | Fidal |
| 4 | Exploratory Data Analysis | Arjun |
| 5 | Feature Engineering & Selection | Fidal + Anu |
| 6 | Model Building & Training | Arjun (NB, SVM) + Anu (LSTM) |
| 7 | Model Evaluation & Comparison | Anu |
| 8 | Model Interpretation | Fidal |
| 9 | Deployment (Streamlit) | Arjun |
| 10 | Documentation | All |

---

## Results Summary

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Naive Bayes | ~97.2% | 0.96 | 0.96 | 0.96 | 0.99 |
| SVM (Linear) | ~98.5% | 0.98 | 0.98 | 0.98 | 0.99 |
| LSTM | ~98.8% | 0.99 | 0.98 | 0.98 | 0.99 |

> Results will be updated after final model training.

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/spam-classifier-nlp.git
cd spam-classifier-nlp
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download dataset
Download SpamAssassin from: https://spamassassin.apache.org/publiccorpus/
Extract folders `easy_ham` and `spam` into `data/raw/`

### 4. Run preprocessing and training
```bash
python src/load_data.py
python src/preprocess.py
python src/features.py
python src/models.py
```

### 5. Launch Streamlit app
```bash
streamlit run app/streamlit_app.py
```

---

## Live Deployment
🔗 **Streamlit App:** [Link will be added after deployment]

---

## Repository Structure
```
spam-classifier-nlp/
├── data/
│   ├── raw/              ← SpamAssassin email folders
│   └── processed/        ← Cleaned CSVs
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_modelling.ipynb
│   └── 04_evaluation.ipynb
├── src/
│   ├── load_data.py
│   ├── preprocess.py
│   ├── features.py
│   └── models.py
├── app/
│   └── streamlit_app.py
├── docs/
│   ├── problem_definition.md
│   ├── literature_review.md
│   └── dataset_info.md
├── models/               ← Saved .pkl and .h5 model files
├── individual_profiles/  ← GitHub activity screenshots
├── requirements.txt
└── README.md
```

---

## GitHub Collaboration
All team members contributed to every stage. See `/individual_profiles/` for GitHub activity exports.

Branches used: `feature/stage1-docs`, `feature/project-setup`, `feature/preprocessing`, `feature/eda`, `feature/tfidf-features`, `feature/nb-svm-models`, `feature/lstm-model`, `feature/evaluation`, `feature/streamlit-app`, `feature/final-docs`s the project progresses.)*
