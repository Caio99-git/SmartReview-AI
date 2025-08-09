from transformers import pipeline

# Load a summarization pipeline using the BART model fine-tuned for summarization
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Summarize a given text 
def summarize(text, min_len=30, max_len=120):
    if len(text.strip()) == 0:
        return "Please enter some text to summarize."
        # Return a message if input is empty or just spaces
    
    # Calls the summarization model with specific parameters:
    try:
        result = summarizer(
            text,
            max_length=max_len, 
            min_length=min_len, # max_length & min_length control summary length
            do_sample=False, # do_sample=False uses deterministic decoding (greedy search)
            length_penalty=2.0, # length_penalty discourages too short summaries
            early_stopping=True, # early_stopping stops generation once summary quality is good
            no_repeat_ngram_size=3 # no_repeat_ngram_size avoids repeating phrases
        )
        
        return result[0]["summary_text"]
        # Returns the generated summary text from the first result
    
    except Exception as e:
        return f"Error during summarization: {e}"
        # Return error message if something goes wrong
