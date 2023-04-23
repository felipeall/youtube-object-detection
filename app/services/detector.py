from dataclasses import dataclass
from typing import Generator

import cv2
import numpy as np
from cvlib.object_detection import detect_common_objects, draw_bbox
from vidgear.gears import CamGear


@dataclass
class YTObjectDetector:
    video_url: str
    video_resolution: str = "360p"
    model: str = "yolov4-tiny"
    confidence: float = 0.2

    def run(self):

        for frame in self._get_video_frames_generator():

            # Detect objects in frame
            bbox, label, conf = detect_common_objects(frame, confidence=self.confidence, model=self.model)

            # Draw boxes for detected objects
            frame_output = draw_bbox(frame, bbox, label, conf)

            # Encode frame as .jpg
            _, frame_encoded = cv2.imencode(".jpg", frame_output)

            # Yield encoded frame to web application
            yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + bytearray(frame_encoded) + b"\r\n"

    def _get_video_frames_generator(self) -> Generator[np.ndarray, None, None]:

        # Instantiate YouTube video stream
        options = {"STREAM_RESOLUTION": self.video_resolution}

        video = CamGear(
            source=self.video_url,
            stream_mode=True,
            logging=True,
            **options,
        ).start()

        frame = video.read()

        while True:
            if frame is None:
                break

            yield frame
            frame = video.read()

        video.stop()
