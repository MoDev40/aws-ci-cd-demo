from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
  return {"message":"Hi, Welcome to FastAPI!", "status": "success", "code": 200, "data": {
    "features": [
      "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
      "FastAPI is easy to use and learn, and it has automatic interactive API documentation.",
      "FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts."
    ]
  },"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}