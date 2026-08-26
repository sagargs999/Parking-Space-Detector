import cv2
import pickle
import cvzone
import numpy as np

VIDEO_PATH = "carPark.mp4"
POSITIONS_PATH = "CarParkPos"

PARKING_WIDTH = 107
PARKING_HEIGHT = 48
OCCUPANCY_LIMIT = 900

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    raise FileNotFoundError(f"Could not open video: {VIDEO_PATH}")

with open(POSITIONS_PATH, "rb") as file:
    position_list = pickle.load(file)


def check_parking_spaces(processed_image, output_image):
    free_spaces = 0

    for x, y in position_list:
        cropped_space = processed_image[
            y:y + PARKING_HEIGHT,
            x:x + PARKING_WIDTH
        ]

        pixel_count = cv2.countNonZero(cropped_space)

        if pixel_count < OCCUPANCY_LIMIT:
            color = (0, 255, 0)
            thickness = 5
            free_spaces += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(
            output_image,
            (x, y),
            (x + PARKING_WIDTH, y + PARKING_HEIGHT),
            color,
            thickness
        )

        cvzone.putTextRect(
            output_image,
            str(pixel_count),
            (x, y + PARKING_HEIGHT - 3),
            scale=1,
            thickness=2,
            offset=0,
            colorR=color
        )

    cvzone.putTextRect(
        output_image,
        f"Free: {free_spaces}/{len(position_list)}",
        (100, 50),
        scale=3,
        thickness=5,
        offset=20,
        colorR=(0, 200, 0)
    )


while True:
    success, frame = cap.read()

    # Restart the video when it finishes
    if not success:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)

    threshold = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        25,
        16
    )

    median = cv2.medianBlur(threshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(median, kernel, iterations=1)

    check_parking_spaces(dilated, frame)

    cv2.imshow("Parking Space Detector", frame)

    # Press Q to close the application
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()