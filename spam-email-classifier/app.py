import streamlit as st
import pickle
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def transformText(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    ps = PorterStemmer()
    y = []
    for i in text:
        if i.isalnum():
             y.append(i)

    text = y.copy()
    y.clear()
    for i in text:
        if i not in stopwords.words('english'):
            y.append(i)

    text = y.copy()
    y.clear()

    for i in text:
        y.append(ps.stem(i))
        
    return ' '.join(y)

st.title('Email spam classifier')

input_sms = st.text_input('Enter the message')

if st.button('Predict'):

    # Steps to get output :

    # 1) preprocess the data
    transform_input = transformText(input_sms)
    # 2) vectorize
    vector = tfidf.transform([transform_input])

    # 3) predict
    result = model.predict(vector)[0]

    # 4) display

    if result == 1:
        st.header('Spam')
    else:
        st.header('Ham')
