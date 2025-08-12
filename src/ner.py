import spacy

# Try to load the model, download if missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def get_entities(text: str):
    """
    Extract named entities from text.
    Returns a list of (entity text, entity label) tuples.
    """
    if not text.strip():
        return []

    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
