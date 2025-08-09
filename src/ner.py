import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def get_entities(text):
    if len(text.strip()) == 0:
        return []
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
