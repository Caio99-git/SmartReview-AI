import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_classifier():
    return pipeline("sentiment-analysis")

def get_sentiment(text):
    if not text.strip(): return "Please enter some text to analyze."
    clf = get_classifier()
    out = clf(text)[0]
    return f"{out['label']} ({round(out['score']*100,2)}%)"



