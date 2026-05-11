import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Download NLTK Resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Initialize Stemmer
ps = PorterStemmer()

# Text Cleaning Function
def transform_text(text):

    text = text.lower()

    text = nltk.word_tokenize(text)

    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]

    y.clear()

    for i in text:

        if i not in stopwords.words('english') and i not in string.punctuation:

            y.append(i)

    text = y[:]

    y.clear()

    for i in text:

        y.append(ps.stem(i))

    return " ".join(y)

# Load TF-IDF Vectorizer
tfidf = pickle.load(open('models/vectorizer.pkl', 'rb'))

# Load SVM Model
model = pickle.load(open('models/svm_model.pkl', 'rb'))

# Streamlit Title
st.title("Email Spam Classifier")

# User Input
input_sms = st.text_area("Enter the message")

# Prediction Button
if st.button('Predict'):

    # Convert Text to TF-IDF Features
    vector_input = tfidf.transform([input_sms]).toarray()

    # Prediction
    result = model.predict(vector_input)[0]

    # Display Result
    if result == 1:

        st.error("Spam Message")

    else:

        st.success("Not Spam Message")
