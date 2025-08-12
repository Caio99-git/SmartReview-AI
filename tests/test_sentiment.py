from src.sentiment import get_sentiment

def test_basic_sentiment():
    text = "This product is amazing!"
    result = get_sentiment(text)
    assert isinstance(result, str)
    assert len(result) > 0