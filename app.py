import streamlit as st
from datetime import date
from src.summarizer import summarize
from src.sentiment import get_sentiment
from src.translator import translate
from src.keywords import extract_keywords
from src.ner import get_entities
from src.daily_brief import get_weather, get_news

# App title
st.title("Text Toolkit & Daily Utilities")

# Sidebar mode selector lets user pick what tool to use
mode = st.sidebar.selectbox("Select mode", [
    "Summarize Text", "Sentiment Analysis", "Translate Text",
    "Keyword Extraction", "Named-Entity Recognition", "Daily Brief"
])

# Summarization tool 
if mode == "Summarize Text":
    st.header("Summarization")
    text = st.text_area("Enter text to summarize", height=200)
    min_len, max_len = st.slider("Summary length", 10, 500, (30, 120), step=10)
    if st.button("Summarize"):
        with st.spinner("Summarizing…"):  # Show spinner during processing
            result = summarize(text, min_len=min_len, max_len=max_len)
        st.success(result)  # Show result when done

# Sentiment Analysis tool
elif mode == "Sentiment Analysis":
    st.header("Sentiment Analysis")
    text = st.text_area("Enter text to analyze sentiment", height=200)
    if st.button("Analyze"):
        with st.spinner("Analyzing…"):
            result = get_sentiment(text)
        st.success(result)

# Translation tool
elif mode == "Translate Text":
    st.header("Translator")
    text = st.text_area("Enter text to translate", height=200)
    cols = st.columns(2)
    src = cols[0].selectbox("From", ["auto","en","es","pt","fr","de"], index=0)
    tgt = cols[1].selectbox("To", ["en","es","pt","fr","de"], index=1)
    if st.button("Translate"):
        with st.spinner("Translating…"):
            result = translate(text, source=src, target=tgt)
        st.success(result)

# Keyword Extraction tool
elif mode == "Keyword Extraction":
    st.header("Keyword Extraction")
    text = st.text_area("Enter text to extract keywords from", height=200)
    n = st.slider("Number of keywords", 3, 20, 5)
    if st.button("Extract"):
        keywords = extract_keywords(text, top_n=n)
        for kw, score in keywords:
            st.write(f"- {kw} (score: {score:.2f})")

# Named Entity Recognition tool
elif mode == "Named-Entity Recognition":
    st.header("Named-Entity Recognition")
    text = st.text_area("Enter text for NER", height=200)
    if st.button("Detect Entities"):
        ents = get_entities(text)
        if ents:
            st.table(ents)  # Show entities in a table
        else:
            st.info("No entities found.")

# Daily Brief tool (weather + news)
elif mode == "Daily Brief":
    st.header("Your Daily Brief")
    city = st.text_input("City for weather (e.g. London)", "Los Angeles")
    if st.button("Get Brief"):
        with st.spinner("Fetching weather…"):
            weather = get_weather(city)

        st.subheader("Weather")
        if "error" in weather:
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
            link = getattr(entry, "link", "#")
            st.write(f"- [{title}]({link})")

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.write("Built with Streamlit")