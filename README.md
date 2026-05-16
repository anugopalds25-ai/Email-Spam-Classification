# Exploratory Data Analysis (EDA)

This branch focuses on the Exploratory Data Analysis (EDA) phase of the Email Spam Classification project.

The purpose of EDA is to analyze and understand the dataset before preprocessing and model development.

---

# Objectives

The main objectives of this phase are:

- Understand dataset structure
- Analyze spam and ham message distribution
- Identify dataset imbalance
- Study message length patterns
- Generate visual insights from the dataset
- Prepare the dataset for preprocessing and machine learning stages

---

# Dataset Overview

The dataset contains email messages categorized into:

- Spam
- Ham (Legitimate Email)

The dataset was loaded and cleaned before performing visual analysis.

---

# EDA Techniques Performed

The following exploratory analysis techniques were implemented:

## 1. Dataset Inspection

Performed:
- Dataset preview
- Column analysis
- Null value checking
- Duplicate value analysis

---

## 2. Class Distribution Analysis

Spam and ham message distributions were visualized to understand dataset balance.

### Key Observation

- Ham messages are more frequent than spam messages.
- The dataset shows slight imbalance but remains suitable for classification tasks.

---

## 3. Message Length Analysis

Message lengths were analyzed to understand textual behavior in spam and legitimate emails.

### Key Observation

- Spam messages generally contain longer promotional text.
- Ham messages are shorter and more conversational.

---

# Visualizations Generated

The following visualizations were created during EDA:

- Spam vs Ham Distribution Graph
- Message Length Distribution Graph

These visualizations are stored in the `results/` folder.

---

# Libraries Used

| Library | Purpose |
|---|---|
| Pandas | Data handling |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |

---

# Outcome of EDA

The EDA phase helped identify:
- Dataset characteristics
- Text distribution patterns
- Important preprocessing requirements
- Suitable feature extraction techniques for NLP classification

The insights obtained during EDA guided the later stages of preprocessing, model training, and evaluation.

# Team Members 

  ANU GOPAL V, 
  FIDAL GOVIND, 
  ARJUN S
