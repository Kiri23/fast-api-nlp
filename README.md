# example-nlp-project
This is an example NER service using Spacy and was built to show Data Scientists & Analysts a quick way to turn their models into deployable services.

## How to run 
download poetry `brew install poetry` 
`poetry shell` - This will initiate a venv enviroment

### with docker 
`docker build -t kiri23/fast-api-nlp:latest . `

`docker run -p 80:80 kiri23/fast-api-nlp:latest`

[The YouTube video for the run through can be found here.](https://youtu.be/Maj9v-Ev7-4)

[Swagger doc for the project can be seen & tested here.](http://34.86.252.161/docs)
