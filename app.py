import sys, os
import streamlit as st

# Ensure repo root is importable (esp. on Streamlit Cloud)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
if APP_ROOT not in sys.path:
    sys.path.insert(0, APP_ROOT)

st.set_page_config(page_title="SmartReview AI", layout="centered")
st.title("Text Toolkit & Daily Utilities")
st.caption("Summarize • Sentiment • Translate • Keywords • NER • Daily Brief")

# Import app tools
from src.summarizer import summarize
from src.sentiment import get_sentiment
from src.translator import translate
from src.keywords import extract_keywords
from src.ner import get_entities
from src.daily_brief import get_weather, get_news

mode = st.sidebar.selectbox(
    "Select mode",
    ["Summarize Text", "Sentiment Analysis", "Translate Text",
     "Keyword Extraction", "Named-Entity Recognition", "Daily Brief"]
)

# Summarization
if mode == "Summarize Text":
    st.header("Summarization")
    text = st.text_area("Enter text to summarize", height=200)
    min_len, max_len = st.slider("Summary length", 10, 500, (30, 120), step=10)
    if st.button("Summarize"):
        if not text.strip():
            st.warning("Please enter some text first."); st.stop()
        with st.spinner("Summarizing…"):
            try:
                result = summarize(text, min_len=min_len, max_len=max_len)
                st.success(result)
            except Exception as e:
                st.error(f"Summarization failed: {e}")

# Sentiment
elif mode == "Sentiment Analysis":
    st.header("Sentiment Analysis")
    text = st.text_area("Enter text to analyze sentiment", height=200)
    if st.button("Analyze"):
        if not text.strip():
            st.warning("Please enter some text first."); st.stop()
        with st.spinner("Analyzing…"):
            try:
                result = get_sentiment(text)
                st.success(result)
            except Exception as e:
                st.error(f"Sentiment analysis failed: {e}")

# Translate
elif mode == "Translate Text":
    st.header("Translator")
    text = st.text_area("Enter text to translate", height=200)
    cols = st.columns(2)
    src_lang = cols[0].selectbox("From", ["auto","en","es","pt","fr","de"], index=0)
    tgt_lang = cols[1].selectbox("To", ["en","es","pt","fr","de"], index=1)
    if st.button("Translate"):
        if not text.strip():
            st.warning("Please enter text to translate."); st.stop()
        with st.spinner("Translating…"):
            try:
                result = translate(text, source=src_lang, target=tgt_lang)
                st.success(result)
            except Exception as e:
                st.error(f"Translation failed: {e}")

# Keywords
elif mode == "Keyword Extraction":
    st.header("Keyword Extraction")
    text = st.text_area("Enter text to extract keywords from", height=200)
    n = st.slider("Number of keywords", 3, 20, 5)
    if st.button("Extract"):
        if not text.strip():
            st.warning("Please enter some text first."); st.stop()
        try:
            keywords = extract_keywords(text, top_n=n)
            if not keywords:
                st.info("No keywords found.")
            else:
                for kw, score in keywords:
                    st.write(f"- {kw} (score: {score:.2f})")
        except Exception as e:
            st.error(f"Keyword extraction failed: {e}")

# NER
elif mode == "Named-Entity Recognition":
    st.header("Named-Entity Recognition")
    text = st.text_area("Enter text for NER", height=200)
    if st.button("Detect Entities"):
        if not text.strip():
            st.warning("Please enter some text first."); st.stop()
        try:
            ents = get_entities(text)
            if ents:
                st.table({"Entity": [e[0] for e in ents], "Label": [e[1] for e in ents]})
            else:
                st.info("No entities found.")
        except Exception as e:
            st.error(f"NER failed: {e}")

# Daily Brief
elif mode == "Daily Brief":
    st.header("Your Daily Brief")
    city = st.text_input("City for weather (e.g. London)", "Los Angeles")
    if st.button("Get Brief"):
        try:
            with st.spinner("Fetching weather…"):
                weather = get_weather(city)

            st.subheader("Weather")
            if isinstance(weather, dict) and "error" in weather:
                st.error(weather["error"])
            else:
                place = weather.get("resolved_city", city)
                temp = weather.get("temperature")
                wind = weather.get("windspeed")
                st.write(f"**{place}**")
                st.write(f"{temp}°C, wind {wind} km/h")

            with st.spinner("Fetching headlines…"):
                news = get_news()
            st.subheader("Top Headlines")
            for entry in news:
                title = getattr(entry, "title", "Untitled")
                link  = getattr(entry, "link", "#")
                st.write(f"- [{title}]({link})")
        except Exception as e:
            st.error(f"Daily brief failed: {e}")

