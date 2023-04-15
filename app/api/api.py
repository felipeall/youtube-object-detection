from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

from app.services.classifier import YTVideoClassifier

api_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@api_router.get("/video_feed")
def video_feed(yt_url: str = "https://www.youtube.com/watch?v=7HaJArMDKgI"):
    classifier = YTVideoClassifier(yt_url=yt_url)
    return StreamingResponse(classifier.run(), media_type="multipart/x-mixed-replace;boundary=frame")


@api_router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
