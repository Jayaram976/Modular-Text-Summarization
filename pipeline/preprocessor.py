import re

def preprocess(text):
    text=re.sub(r'\s+',' ',text).strip()
    return text.strip()