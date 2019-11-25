from fastapi import FastAPI

from pydantic import BaseModel


class PageSearchRequest(BaseModel):
    word: str
    urls: List[str]


class SearchResult(BaseModel):
    word: str
    url: str


class PageSearchResponse(BaseModel):
    search: List[SearchResult]


app = FastAPI()


@app.get("/alive", status_code=200)
async def alive():
    return {"text": "RUNNING"}

@app.post("/", status_code=200)
async def crawler(req: PageSearchRequest):
    
    return {
        "rsarch"
    }
