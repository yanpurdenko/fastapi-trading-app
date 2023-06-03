from fastapi import FastAPI

app = FastAPI(
    title="Trading APP"
)


@app.get("/")
def root():
    return {"ping": "pong!"}
