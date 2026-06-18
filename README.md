# Aerial-Sketch

![Python](https://img.shields.io/badge/python-3.11-blue)
![OpenCV](https://img.shields.io/badge/opencv-computer%20vision-green)
![Status](https://img.shields.io/badge/status-phase%201-orange)

An interactive computer vision project that allows users to draw in the air using their webcam and hand gestures.

**Currently in Phase 1:** The program uses AI to track the user's hand in real-time, isolates the index finger, and projects a tracking marker onto a mirrored video canvas.

---

## Tech Stack

* **Python** (Recommended: v3.11)
* **OpenCV** — Computer vision and canvas mapping
* **MediaPipe** — AI hand-tracking model

---

## How to Run Locally

You'll need Python installed. Each command below builds a virtual environment, installs dependencies, and launches the app in one step.

### Mac & Linux

```bash
python3 -m venv cv-env && source cv-env/bin/activate && pip install -r requirements.txt && python3 air_canvas.py
```

### Windows

```bat
python -m venv cv-env && cv-env\Scripts\activate && pip install -r requirements.txt && python air_canvas.py
```

---

## Controls

| Action | Key |
|---|---|
| Quit the application | `q` |

More drawing controls and gestures are planned for Phase 2.