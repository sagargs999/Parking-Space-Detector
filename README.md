# Parking Space Detector

A computer vision project that detects free and occupied parking spaces from a video using Python and OpenCV.

## Features

* Detects available and occupied parking spaces
* Displays free spaces with green rectangles
* Displays occupied spaces with red rectangles
* Shows the number of free spaces
* Automatically restarts the video when it ends
* Press `Q` to close the program

## Technologies Used

* Python
* OpenCV
* NumPy
* CVZone
* Pickle

## Project Structure

```text
Parking-Space-Detector/
├── main.py
├── carPark.mp4
├── CarParkPos
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sagargs999/Parking-Space-Detector.git
```

### 2. Open the project folder

```bash
cd Parking-Space-Detector
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

## Run the Project

Ensure that `carPark.mp4` and `CarParkPos` are inside the project folder.

Run:

```bash
python main.py
```

Press `Q` to close the program.

## How It Works

1. Reads frames from the parking-area video.
2. Converts every frame to grayscale.
3. Applies Gaussian blur to reduce noise.
4. Uses adaptive thresholding to detect objects.
5. Applies median blur and dilation to improve detection.
6. Crops each predefined parking space.
7. Counts the non-zero pixels in each parking space.
8. Classifies each space as free or occupied.

A parking space is considered free when its pixel count is below the configured limit.

## Configuration

The parking-space size and detection limit can be changed in `main.py`:

```python
width, height = 107, 48
```

```python
if count < 900:
```

Different videos may require different width, height, and pixel-count values.

## Requirements

```text
opencv-python
cvzone
numpy
```

## Important Note

GitHub does not accept individual files larger than 100 MB. If `carPark.mp4` is larger than 100 MB, add the following line to `.gitignore`:

```gitignore
*.mp4
```

Then upload the video to Google Drive and add its download link to this README.

## Author

**GS Sagar**

* GitHub: [sagargs999](https://github.com/sagargs999)
* LinkedIn: [GS Sagar](https://www.linkedin.com/in/gs-sagar999)
