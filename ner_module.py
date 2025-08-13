
import spacy
from config import NER_MODEL

nlp = spacy.load(NER_MODEL)

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
