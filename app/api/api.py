from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

from app.services.detector import YTObjectDetector

api_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@api_router.get("/detection")
def detection(video_url: str = "https://www.youtube.com/watch?v=7HaJArMDKgI"):
    yt_object_detector = YTObjectDetector(video_url=video_url)
    return StreamingResponse(yt_object_detector.run(), media_type="multipart/x-mixed-replace;boundary=frame")


@api_router.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
