import os

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"message": "我的第一个 AI 应用接口"}


@app.post("/chat")
def chat(req: ChatRequest):
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": req.message}],
    )
    return {"reply": resp.choices[0].message.content}
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)