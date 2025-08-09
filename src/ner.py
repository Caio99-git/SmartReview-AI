import spacy ## Load the small English language model for NLP tasks like tokenization and Named Entity Recognition (NER)

# Load English model with tokenization, POS tagging, and Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")  

# Extract named entities from text 
def get_entities(text):
    if len(text.strip()) == 0:
        return []  
        # Return empty list if input is empty or just spaces
    
    doc = nlp(text)  
    # Process the text to identify entities
    
    return [(ent.text, ent.label_) for ent in doc.ents]  
    # Return a list of (entity text, entity type) tuples
