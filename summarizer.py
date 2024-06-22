import re


def load_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def sentence_tokenize(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 10]


def word_tokenize(text):
    return re.findall(r'\b[a-zA-Z]+\b', text.lower())


STOPWORDS = set([
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'have',
    'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
    'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from', 'as',
    'and', 'but', 'or', 'not', 'so', 'if', 'when', 'where', 'how',
    'what', 'which', 'who', 'this', 'that', 'these', 'those',
    'i', 'me', 'my', 'we', 'you', 'he', 'she', 'it', 'they', 'them',
    'its', 'his', 'her', 'our', 'their', 'than', 'more', 'very',
])

def remove_stopwords(tokens):
    return [t for t in tokens if t not in STOPWORDS]
