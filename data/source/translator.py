from deep_translator import GoogleTranslator

# Translate text from source language to target language 
def translate(text, source="auto", target="en"): # "auto" means detect automatically
    if len(text.strip()) == 0:
        return "Please enter text to translate."
        # Return message if input is empty or just spaces
    
    try:
        # Use GoogleTranslator to translate the text
        return GoogleTranslator(source=source, target=target).translate(text) # Tries to create a GoogleTranslator object with given source and target languages
    except Exception as e:
        return f"Translation failed: {e}"
        # Return error message if translation fails