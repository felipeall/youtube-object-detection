import uvicorn
from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI(title="YouTube Object Detector")
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
