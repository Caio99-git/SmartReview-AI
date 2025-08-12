from src.summarizer import summarize

def test_basic_summary():
    text = "Machine learning is a field of AI that enables computers to learn from data."
    result = summarize(text)
    assert isinstance(result, str)
    assert len(result) > 0