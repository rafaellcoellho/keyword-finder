from fastapi import FastAPI

app = FastAPI()


@app.get("/alive", status_code=200)
async def alive():
    return {"text": "RUNNING"}
