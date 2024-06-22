import re


def load_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def sentence_tokenize(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def word_tokenize(text):
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())
