import spacy
import textstat
from typing import Dict

nlp = spacy.load("en_core_web_sm")

def score_grammar(doc) -> int:
    errors = sum(1 for token in doc if token.pos_ == "X")
    return max(10 - errors, 2)

def score_clarity(prompt: str) -> int:
    reading_score = textstat.flesch_reading_ease(prompt)
    if reading_score >= 60:
        return 10
    elif reading_score >= 40:
        return 7
    else:
        return 4

def score_relevance(doc) -> int:
    good_words = [t for t in doc if t.pos_ in ["NOUN", "VERB", "ADJ"]]
    return min(int((len(good_words) / len(doc)) * 10), 10) if len(doc) > 0 else 2

def score_creativity(prompt: str) -> int:
    unique_words = len(set(prompt.lower().split()))
    total_words = len(prompt.split())
    ratio = unique_words / total_words if total_words else 0
    return min(int(ratio * 15), 10) if ratio > 0 else 2

def score_completeness(doc) -> int:
    if any(token.dep_ == "ROOT" for token in doc):
        return 10 if len(doc) > 10 else 7
    return 5

def analyze_prompt(prompt: str) -> Dict[str, int]:
    doc = nlp(prompt)
    clarity = score_clarity(prompt)
    relevance = score_relevance(doc)
    creativity = score_creativity(prompt)
    grammar = score_grammar(doc)
    completeness = score_completeness(doc)
    total = clarity + relevance + creativity + grammar + completeness
    return {
        "clarity": clarity,
        "relevance": relevance,
        "creativity": creativity,
        "grammar": grammar,
        "completeness": completeness,
        "total_score": total
    }
