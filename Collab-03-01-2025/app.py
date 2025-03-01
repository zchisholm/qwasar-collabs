from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserQuery(BaseModel):
    query: str

@app.post("/ask")
async def ask(query: UserQuery):
    return {"response": f"You asked: {query.query}"}

@app.get("/")
async def root():
    return {"message": "API is running"}