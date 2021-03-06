from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from typing import List
import spacy
from spacy import displacy
import cv2 as cv
print(cv.__version__)
from .models import Payload, Entities


app = FastAPI()

nlp = spacy.load("en_core_web_sm")

# test code cv2
#  nparr = np.fromstring(contents, np.uint8)
# img = cv.imdecode(nparr, cv.IMREAD_COLOR)
# cv.imshow('img',img)
# cv.waitKey(0)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f"{file.filename}", "wb+") as file_object:
        file_object.write(file.file.read())
    return FileResponse("img/fargo-1.png")

# https://codebeautify.org/text-minifier
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

@app.post('/ner-service-html',  response_class=HTMLResponse)
async def get_ner(payload: Payload):
    tokenize_content: List[spacy.tokens.doc.Doc] = [
        nlp(content.content) for content in payload.data
    ]
    html = displacy.render(tokenize_content, style="ent", page=True)
    return HTMLResponse(content=html, status_code=200)
