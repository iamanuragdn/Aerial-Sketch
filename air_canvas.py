# import cv2 # openCV
# import mediapipe as mp # mediapipe(mp)

# mp_hand = mp.solution.hand # choses the AI model that is hand (here solution is menu)
# hand = mp_hand.Hand(max_num_hands=1,min_detection_confidence=0.7) # rules given to model
# mp_draw = mp.solution.drawing_utils # Automatic Paintbrush

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read() # success = Boolean, It asks, "Did the camera successfully take a picture?"
#                               # img = Variable, that hold actual image data
#     if not success: # if camera disconnect thn loop breaks so prog. dont crash
#         break

# img = cv2.flip(img,1) # 0: Flips vertically, 1: Flips horizontally, -1: Flips both vertically and horizontally
# img_rgb = cv2.cvtColor( img, cv2.COLOR_BGR2RGB) # cvtColor means "Convert Color"

# results = hands.process(img_rgb) #process : send img_rgb to model, it scans pixels and return mathematical coordinates of my hand in result(variable)

# if results.multi_hand_landmarks: # .multi_hand_landmarks : is property build in Mediapipe
#                                  # Only run the code below IF this property actually contains data

#     for hand_landmarks in results.multi_hand_landmarks: # hand_landmarks : custom variable name
#                                                         # in results.multi_hand_landmarks, model detects multiple hand same time, so pakages the data as a List(an array)
#                                                         # Because the data is a List, we cannot process all hands at the exact same time. The loop reaches into the List, grabs Hand #1, temporarily names it hand_landmarks, runs the math, and then goes back to grab Hand #2.
#         # paintbrush                                                
#         mp_draw.draw_landmarks(img, hand_landmarks, mp_hand.HAND_CONNECTIONS) # mp_draw : is a alias we made for drawing utility ; draw_landmards() : is a function built in that utility that draw circle on joints
#                               #img : 1st argument, where we pass our video frame  so that fuction knows where to draw ; hand_landmarks : 2nd argument that passes data of the current hand so fuction knows the coordinate ; mp_hand.HAND_CONNECTIONS : 3rd argument, This is a built-in constant (a hardcoded list inside MediaPipe). 

#         index_finger = hand_landmarks.landmarks[8] # index_finger : custom variable ; landmark : A built-in property containing an array of exactly 21 points.
#                                              # [8]: The index of the array ; Google's 3D hand model maps the wrist as [0], the thumb as [4], and the index finger tip specifically as [8].

#         h,w,c = img.shape # h, w, c: Custom variables ; shape : OpenCV treats images as a massive matrix of numbers using a library called Numpy. .shape is a built-in Numpy property that asks the matrix for its exact dimensions. It always returns three numbers: Height, Width, and Channels (colors).
        
#         cx, cy = int(index_finger.x *w), int(index_finger.y*h) # cx, cy: Custom variables standing for "Center X" and "Center Y"
#                      #   
#         cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)





import cv2
import mediapipe as mp
import platform

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=4,
    min_detection_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils


# Select camera backend based on operating system
system = platform.system()

if system == "Windows":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# elif system == "Darwin":  # macOS
#     cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
else:  # Linux
    cap = cv2.VideoCapture(0)

# Check if camera opened
if not cap.isOpened():
    print("❌ Error: Could not open camera.")
    exit()

print(f"✅ Air Canvas started on {system}")
print("Press 'q' to exit")


while True:
    # Capture frame
    success, img = cap.read()

    if not success:
        print("❌ Failed to capture frame.")
        break

    # Flip image for mirror effect
    img = cv2.flip(img, 1)

    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(img_rgb)

    # Draw landmarks and track index finger
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand skeleton
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # # Get index finger tip (landmark 8)
            # index_finger = hand_landmarks.landmark[8]
            fingertips_ids=[4,8,12,16,20]

            for id in fingertips_ids:
                finger_landmarks = hand_landmarks.landmark[id]

                # Convert normalized coordinates to pixels
                h, w, c = img.shape
                cx = int(finger_landmarks.x * w)
                cy = int(finger_landmarks.y * h)

                # Draw red circle on index fingertip
                cv2.circle(
                    img,
                    (cx, cy),
                    15,
                    (0, 0, 255),
                    cv2.FILLED
                )

    # Show the camera output
    cv2.imshow("Air Canvas - Phase 1", img)

    # Press q to stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("👋 Closing Air Canvas...")
        break


# Release resources
cap.release()
cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# import numpy as np  # NEW: We need numpy to create our blank canvas!

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) 
# mp_draw = mp.solutions.drawing_utils

# cap = cv2.VideoCapture(0)

# # --- NEW: Initialize Memory Variables ---
# xp, yp = 0, 0
# imgCanvas = None # We will create this once the camera turns on

# while True:
#     success, img = cap.read()
#     if not success:
#         break
        
#     img = cv2.flip(img, 1)
    
#     # --- NEW: Create the Invisible Glass ---
#     # We only do this on the very first frame so it exactly matches your webcam's size
#     if imgCanvas is None:
#         imgCanvas = np.zeros_like(img)

#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(img_rgb)
    
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS) # (Optional: You can comment this out to hide the skeleton!)
            
#             index_finger = hand_landmarks.landmark[8]
#             h, w, c = img.shape
#             cx, cy = int(index_finger.x * w), int(index_finger.y * h)
            
#             # --- NEW: The Drawing Logic ---
#             # If this is the first frame we see your hand, start the line right exactly where you are
#             if xp == 0 and yp == 0:
#                 xp, yp = cx, cy
                
#             # Draw a thick neon pink line from the PAST point to the CURRENT point
#             cv2.line(imgCanvas, (xp, yp), (cx, cy), (255, 0, 255), 15)
            
#             # Update the past points to become the current points for the next loop
#             xp, yp = cx, cy

#             # Draw the circle on the tip of the finger
#             cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
    
#     # --- NEW: Reset Memory if Hand Disappears ---
#     else:
#         # If we don't do this, putting your hand down and raising it again will draw a massive line across the screen!
#         xp, yp = 0, 0

#     # --- NEW: Blend the Glass and the Webcam ---
#     # This adds the glowing lines from the canvas directly onto your live video feed
#     img = cv2.addWeighted(img, 1, imgCanvas, 1, 0)

#     cv2.imshow("Aerial-Sketch", img)
#     # Optional: You can also show the raw canvas in a separate window to see what the computer is actually doing!
#     # cv2.imshow("The Invisible Glass", imgCanvas) 
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()