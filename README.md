# Email Spam Classification Using NLP and Machine Learning

Predictive Analytics Group Project | Academic Year 2025–26

---

# Team Members

| Name |
|---|
| Fidal Govind |
| Arjun S |
| ANU GOPAL V |

---

# Problem Statement

Email spam remains a major challenge in modern digital communication. Spam messages waste user time, consume infrastructure resources, and often contain phishing links, malware, and fraudulent content. 

This project aims to build an intelligent Email Spam Classification system using Natural Language Processing (NLP) and Machine Learning techniques to automatically classify emails as:

- Spam
- Ham (Legitimate Email)

The project compares multiple machine learning algorithms and deploys the best-performing model using Streamlit.

---

# Project Motivation

The increasing volume of spam emails creates serious issues including:

- Phishing attacks
- Financial fraud
- Malware distribution
- Productivity loss
- Storage and bandwidth waste

An automated spam filtering system helps users and organizations improve security and communication efficiency.

---

# Dataset Description

## Dataset Used

SpamAssassin Public Dataset

## Dataset Features

| Feature | Description |
|---|---|
| label | Spam or Ham |
| message | Email text message |

## Dataset Characteristics

- Text-based email dataset
- Binary classification problem
- Contains spam and non-spam messages
- Used for NLP preprocessing and ML model training

---

# Methodology

The project follows a complete machine learning lifecycle workflow.

## 1. Exploratory Data Analysis (EDA)

Performed:
- Class distribution analysis
- Message length analysis
- Spam vs Ham visualization

## Spam vs Ham Distribution

![Spam vs Ham Distribution](results/Spam%20vs%20Ham.png)

## 2. Text Preprocessing

Applied preprocessing techniques such as:
- Lowercase conversion
- Tokenization
- Stopword removal
- Punctuation removal
- Stemming using Porter Stemmer

## 3. Feature Extraction

Used:
- TF-IDF Vectorization

to convert text into numerical feature vectors.

## 4. Model Training

The following machine learning models were trained and evaluated:

- Naive Bayes
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

## 5. Model Evaluation

Evaluation metrics used:
- Accuracy Score
- Classification Report
- Confusion Matrix

## 6. Deployment

The best-performing SVM model was deployed using:
- Streamlit

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Handling |
| NumPy | Numerical Operations |
| NLTK | NLP Preprocessing |
| Scikit-learn | Machine Learning |
| Matplotlib | Visualization |
| Seaborn | Visualization |
| Streamlit | Deployment |
| Pickle | Model Serialization |

---

# Project Structure

```text
Email-Spam-Classification/
│
├── models/
├── notebooks/
├── results/
├── screenshots/
├── app.py
├── requirements.txt
└── README.md
```

---

# Results Summary

## Best Performing Model

Support Vector Machine (SVM)

## Evaluation Metrics

The SVM model achieved the highest accuracy among all tested machine learning models.

Visualizations included:
- Confusion Matrix
- Model Comparison Graph

---

# Screenshots

## Application Homepage

Stored in:
```text
screenshots/
```

## Spam Prediction Example

Stored in:
```text
screenshots/
```

## Non-Spam Prediction Example

Stored in:
```text
screenshots/
```

---

# Deployment Link

[Open Streamlit App](https://email-spam-classification-erd32gzrsof4qto2zxkfz8.streamlit.app/)

---

# How to Run the Project Locally

## 1. Clone Repository

```bash
git clone https://github.com/fidalgovind/Email-Spam-Classification.git
```

## 2. Navigate to Project Folder

```bash
cd Email-Spam-Classification
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Streamlit App

```bash
streamlit run app.py
```

---

# Conclusion

This project demonstrates how NLP and Machine Learning can be effectively used for automated spam email detection. The deployed application provides real-time spam classification using an optimized SVM model.


