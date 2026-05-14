# Data Preprocessing - Email Spam Classifier

## Overview

This branch focuses on preprocessing and cleaning the email/text dataset before model training. Proper preprocessing improves model performance and helps convert raw text into machine-readable format.

---

## Objectives

- Clean raw email/text data
- Remove unwanted characters and symbols
- Perform NLP preprocessing
- Prepare dataset for feature extraction

---

## Preprocessing Steps

### 1. Lowercase Conversion
Convert all text into lowercase.

### 2. Remove Punctuation
Remove commas, symbols, and special characters.

### 3. Tokenization
Split sentences into individual words.

### 4. Stopword Removal
Remove common words like:
- the
- is
- and
- are

### 5. Stemming/Lemmatization
Convert words into root form.

Example:
- running → run
- playing → play

---

## Technologies Used

- Python
- Pandas
- NLTK
- Regular Expressions

---

## Output

The processed dataset is cleaned and ready for:
- TF-IDF Vectorization
- Model Training

---

## Conclusion

This preprocessing pipeline improves text quality and helps the machine learning model achieve better spam classification accuracy.
