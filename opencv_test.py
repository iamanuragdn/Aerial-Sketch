import cv2
import platform

# Detect the operating system
system = platform.system()

# Select camera backend based on OS
if system == "Windows":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
elif system == "Darwin":  # macOS
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
else:  # Linux and other systems
    cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print(f"Running on: {system}")
print("Camera started successfully. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    success, frame = cap.read()

    # Check if frame was captured
    if not success:
        print("Error: Failed to capture frame.")
        break

    # Display the video frame
    cv2.imshow("OpenCV Camera Test", frame)

    # Press q to exit the camera window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Closing camera...")
        break

# Release camera resources
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()