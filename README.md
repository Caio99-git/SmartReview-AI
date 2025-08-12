# 🧰 SmartReview AI — Text Toolkit & Daily Utilities

Welcome to **SmartReview AI**, an interactive Streamlit web application that combines multiple natural language processing (NLP) and utility tools into one seamless platform.  
Access the live app here: **[SmartReview AI on Streamlit Cloud](https://smartreview-ai-nzklupvzh39sxufo7uckno.streamlit.app/)** 🚀

---

## 🚀 Project Overview

The primary goal of SmartReview AI is to provide a simple yet powerful web interface where users can perform various NLP tasks without writing any code. The app integrates multiple features, including:

- **Text Summarization** with state-of-the-art transformer models
- **Sentiment Analysis** to determine emotional tone
- **Translation** between multiple languages
- **Keyword Extraction** using YAKE
- **Named-Entity Recognition (NER)** for identifying entities in text
- **Daily Brief** combining real-time weather and latest news headlines

---

## 🧠 Key Features

### 1️⃣ Text Summarization
- Uses a transformer-based summarization pipeline (`facebook/bart-large-cnn`) to condense long texts into concise summaries.
- Adjustable summary length via slider.

### 2️⃣ Sentiment Analysis
- Classifies text as positive, negative, or neutral with confidence scores.
- Built on Hugging Face's `pipeline("sentiment-analysis")`.

### 3️⃣ Translation
- Translates text between English, Spanish, Portuguese, French, and German.
- Auto language detection option available.
- Powered by `deep-translator`.

### 4️⃣ Keyword Extraction
- Extracts top N keywords from the text.
- Uses `yake` for unsupervised keyword extraction.

### 5️⃣ Named-Entity Recognition
- Identifies and classifies entities such as names, locations, and organizations.
- Uses `spacy` with the `en_core_web_sm` model.

### 6️⃣ Daily Brief
- Fetches current weather data for any city via Open-Meteo API.
- Displays top 5 news headlines from BBC News RSS feed.

---

## 🧰 Tools & Libraries Used

- **Python Libraries:**  
  `streamlit`, `transformers`, `torch`, `spacy`, `yake`, `feedparser`, `deep-translator`, `requests`
- **APIs:**  
  Open-Meteo (Weather), BBC RSS (News)
- **Models:**  
  Hugging Face Transformers (`facebook/bart-large-cnn`), SpaCy `en_core_web_sm`

---

## 📊 Outcome

This application empowers users to:
- Summarize large texts quickly and efficiently
- Understand sentiment in any given text
- Translate between multiple languages on the fly
- Extract important keywords for analysis
- Detect named entities for deeper insights
- Stay updated with weather and top news headlines

---

## 🚀 How to Run Locally

1. **Clone this repository or download it**  
   ```bash
   git clone https://github.com/your-username/SmartReview-AI.git
   cd SmartReview-AI

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # On Windows: .venv\Scripts\activate

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

4. **Run the app**  
   ```bash
   streamlit run app.py

5. **Open the local URL provided by Streamlit in your browser.**  
---

## 📞 Contact

Feel free to reach out if you want to discuss the project or collaborate!

📧 **Email:** [alcantaracaio99@gmail.com](mailto:alcantaracaio99@gmail.com)  
🔗 **LinkedIn:** https://www.linkedin.com/in/caio-alcântara/
