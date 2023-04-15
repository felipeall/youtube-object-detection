from dataclasses import dataclass

import cv2
from cvlib import detect_common_objects
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear


@dataclass
class YTObjectDetector:
    video_url: str
    video_resolution: str = "360p"
    model: str = "yolov4-tiny"
    confidence: float = 0.2

    def run(self):

        # Instantiate YouTube video stream
        video = CamGear(
            source=self.video_url,
            stream_mode=True,
            logging=True,
            STREAM_RESOLUTION=self.video_resolution,
        ).start()

        while True:

            # Read frame
            frame = video.read()

            # Break if frame is invalid
            if frame is None:
                break

            # Detect objects in frame
            bbox, label, conf = detect_common_objects(frame, confidence=self.confidence, model=self.model)

            # Draw boxes for detected objects
            frame_output = draw_bbox(frame, bbox, label, conf)

            # Encode frame as .jpg
            _, frame_encoded = cv2.imencode(".jpg", frame_output)

            # Yield encoded frame to web application
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + bytearray(frame_encoded) + b"\r\n")

        # Safely close video stream
        video.stop()
