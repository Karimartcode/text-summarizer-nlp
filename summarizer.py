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


from collections import Counter

def word_frequency(tokens):
    freq = Counter(tokens)
    max_freq = max(freq.values()) if freq else 1
    return {word: count / max_freq for word, count in freq.items()}


def score_sentences(sentences, word_freq):
    scores = {}
    for i, sentence in enumerate(sentences):
        words = word_tokenize(sentence)
        words = remove_stopwords(words)
        score = sum(word_freq.get(w, 0) for w in words)
        if len(words) > 0:
            score /= len(words)
        scores[i] = score
    return scores


def select_top_sentences(sentences, scores, n):
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_indices = sorted([idx for idx, _ in ranked[:n]])
    return [sentences[i] for i in top_indices]


def summarize(text, num_sentences=3):
    sentences = sentence_tokenize(text)
    if len(sentences) <= num_sentences:
        return text
    all_words = word_tokenize(text)
    filtered_words = remove_stopwords(all_words)
    freq = word_frequency(filtered_words)
    scores = score_sentences(sentences, freq)
    summary_sentences = select_top_sentences(sentences, scores, num_sentences)
    return ' '.join(summary_sentences)


def evaluate_summary(original, summary):
    orig_words = set(word_tokenize(original))
    summ_words = set(word_tokenize(summary))
    overlap = len(orig_words & summ_words)
    precision = overlap / len(summ_words) if summ_words else 0
    recall = overlap / len(orig_words) if orig_words else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    compression = len(summary) / len(original)
    return {
        "compression_ratio": compression,
        "word_overlap_precision": precision,
        "word_overlap_recall": recall,
        "f1": f1,
        "original_sentences": len(sentence_tokenize(original)),
        "summary_sentences": len(sentence_tokenize(summary))
    }
