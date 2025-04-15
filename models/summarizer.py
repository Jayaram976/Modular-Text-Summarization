from transformers import pipeline

class Summarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.pipeline = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=130, min_length=30):
        result = self.pipeline(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]["summary_text"]