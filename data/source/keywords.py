import yake  # Yet Another Keyword Extractor - finds important words/phrases in text

# Extract keywords from text ---
def extract_keywords(text, top_n=5):  
    # text: The input string to analyze
    # top_n: How many keywords to return (default is 5)
    
    if len(text.strip()) == 0:  
        return []  
        # If text is empty or just spaces, return an empty list immediately
    
    # Create a keyword extractor
    kw_extractor = yake.KeywordExtractor(lan="en", top=top_n)
    
    return kw_extractor.extract_keywords(text)  
    # Returns a list of (keyword, score) pairs
