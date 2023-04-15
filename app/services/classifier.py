from dataclasses import dataclass

import cv2
from cvlib import detect_common_objects
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear


@dataclass
class YTVideoClassifier:
    yt_url: str
    yt_resolution: str = "360p"
    model: str = "yolov4-tiny"
    confidence: float = 0.2

    def run(self):
        stream = CamGear(
            source=self.yt_url,
            stream_mode=True,
            logging=True,
            STREAM_RESOLUTION=self.yt_resolution,
        ).start()

        while True:
            frame = stream.read()

            if frame is None:
                break

            bbox, label, conf = detect_common_objects(frame, confidence=self.confidence, model=self.model)
            frame_output = draw_bbox(frame, bbox, label, conf)

            _, frame_encoded = cv2.imencode(".jpg", frame_output)
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + bytearray(frame_encoded) + b"\r\n")

        stream.stop()
