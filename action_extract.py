# action_extract.py
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_action_items(text):
    """
    Extract sentences containing keywords like 'will', 'to', 'by', 'deadline'
    """
    doc = nlp(text)
    actions = []
    for sent in doc.sents:
        if any(word in sent.text.lower() for word in ["will", "to", "by", "deadline"]):
            actions.append(sent.text)
    return actions
