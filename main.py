from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "我的第一个 AI 应用接口"}


@app.get("/hello/{name}")
def say_hello(name: str, times: int = 1):
    return {"greeting": f"你好，{name}！" * times}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)