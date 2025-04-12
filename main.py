import logging
import sys
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout
)

logging.info("testapp started")

app = FastAPI()

@app.get("/sayhi")
def say_hi():
    logging.info("testapp said hi")
    return {"message": "Hello World"}

@app.get("/badhi")
def bad_hi():
    logging.error("testapp said bad hi")
    return {"message": "Hello BAD World"}

