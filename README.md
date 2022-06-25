# example-nlp-project

This is an example NER service using Spacy and was built to show Data Scientists & Analysts a quick way to turn their models into deployable services.

## How to run

- download poetry `brew install poetry`
- `poetry init` to initialize a project
- download [poppler](https://macappstore.org/poppler/) for mac to process PDF `brew install poppler`. Other [Os install ref](https://pdf2image.readthedocs.io/en/latest/installation.html)
  - Test if the install run sucessfully by running `pdftoppm -h`
  - `pdftoppm -png fargo.pdf fargo` - This will convert pdf pages to images
  - Available [tools](https://www.xpdfreader.com/about.html) from poppler:
    - some examples are pdfimages, pdftotext, pdftohtml, pdfinfo, pdftopng, pdffonts.
- `poetry shell` - This will initiate a venv enviroment
- uvicorn src.main:app --reload
  or
- `bash runDocker.sh` to run the docker command

### with docker

`docker build -t kiri23/fast-api-nlp:latest . `

`docker run -p 80:80 kiri23/fast-api-nlp:latest`

### FAQ

- Using `opencv-python-headless` fixed error on docker about not file found for opencv
- The image window for opencv only work locally and then it never close
  - The image window does not want to work on docker.
- To select intepreter on vs code https://user-images.githubusercontent.com/18028544/175776994-36b20dda-3a4b-42dc-9df3-35aa106968e0.mov

[The YouTube video for the run through can be found here.](https://youtu.be/Maj9v-Ev7-4)

[Swagger doc for the project can be seen & tested here.](http://34.86.252.161/docs)
