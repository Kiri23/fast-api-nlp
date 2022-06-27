import spacy
from spacy import displacy

# download free templates on https://templatelab.com/bank-statement/#google_vignette or check for bank fake template like this https://templatearchive.com/bank-statement/#google_vignette
nlp = spacy.load("en_core_web_sm")
doc = nlp("")
html = displacy.render(doc, style="ent", page=True)
displacy.serve(doc, style="ent")
