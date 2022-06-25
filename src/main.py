from fastapi import FastAPI, File, UploadFile
from typing import List
import spacy
import numpy as np
import cv2 as cv
print(cv.__version__)
from .models import Payload, Entities


app = FastAPI()

nlp = spacy.load("en_core_web_sm")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv.imdecode(nparr, cv.IMREAD_COLOR)
    cv.imshow('img',img)
    cv.waitKey(0)
    return {"filename": file.filename, "imgShape": img.shape}

@app.post('/ner-service')
async def get_ner(payload: Payload):
    tokenize_content: List[spacy.tokens.doc.Doc] = [
        nlp(content.content) for content in payload.data
    ]
    document_enities = []
    for doc in tokenize_content:
        document_enities.append([ {'text': ent.text, 'entity_type': ent.label_} for ent in doc.ents ])
    return [
        Entities(post_url=post.post_url, entities=ents)
        for post, ents in zip(payload.data, document_enities)
    ]