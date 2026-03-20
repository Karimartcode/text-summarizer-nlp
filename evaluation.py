from collections import Counter


def _ngrams(tokens: list, n: int) -> Counter:
    return Counter(tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1))


def rouge_n(hypothesis: str, reference: str, n: int = 1) -> dict:
    """Compute ROUGE-N precision, recall, and F1."""
    hyp_tokens = hypothesis.lower().split()
    ref_tokens = reference.lower().split()
    hyp_ng = _ngrams(hyp_tokens, n)
    ref_ng = _ngrams(ref_tokens, n)
    overlap = sum((hyp_ng & ref_ng).values())
    precision = overlap / max(sum(hyp_ng.values()), 1)
    recall    = overlap / max(sum(ref_ng.values()), 1)
    f1 = 2 * precision * recall / max(precision + recall, 1e-9)
    return {"precision": round(precision, 4),
            "recall":    round(recall, 4),
            "f1":        round(f1, 4)}
