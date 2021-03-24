import numpy as np
import pickle
import pandas as pd
import streamlit as st

#from PIL import image

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return prediction


def main():
    st.title("Bank Authenticator")
    st.markdown()


variance = st.text_input("variance", "type here")
skewness = st.text_input("skewness", "type here")
curtosis = st.text_input("curtosis", "type here")
entropy = st.text_input("entropy", "type here")

result = ""

if st.button("Predict"):
    result = predict_note_authentication(variance, skewness, curtosis, entropy)
st.success("The output is {}".format(result))

if __name__ == "__main__":
    main()
