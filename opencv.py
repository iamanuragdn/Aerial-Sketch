import cv2

# 1. Turn on the Mac's default camera (Camera 0)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

print("Camera warming up... Press 'q' on your keyboard to quit!")

while True:
    # 2. Read the video feed frame-by-frame
    success, frame = cap.read()
    
    # 3. If the frame was read successfully, show it in a window
    if success:
        cv2.imshow('My First OpenCV Window', frame)
    
    # 4. Wait for 1 millisecond. If the 'q' key is pressed, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. Clean everything up when you quit
cap.release()
cv2.destroyAllWindows()