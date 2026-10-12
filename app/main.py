from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
  return {"message":"Hi, Welcome to FastAPI!", "status": "success", "code": 200, "data": None,"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}