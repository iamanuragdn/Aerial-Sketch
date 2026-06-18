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

# 1. Initialize MediaPipe Hand Tracking module
mp_hands = mp.solutions.hands
# Set confidence to 0.7 so it doesn't jitter too much
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) 
mp_draw = mp.solutions.drawing_utils

# 2. Start the webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
        
    # Flip the image horizontally so it acts like a mirror
    img = cv2.flip(img, 1)
    
    # OpenCV uses BGR colors, but MediaPipe requires RGB. We must convert it.
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 3. Send the frame to MediaPipe to find hands
    results = hands.process(img_rgb)
    
    # 4. If a hand is found, extract the data
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the cyan wireframe over the hand
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # 5. ISOLATE THE INDEX FINGER TIP (Landmark #8)
            index_finger = hand_landmarks.landmark[8]
            
            # The coordinates returned are decimals (e.g., 0.5, 0.2). 
            # We multiply by the screen width and height to get actual pixel coordinates.
            h, w, c = img.shape
            cx, cy = int(index_finger.x * w), int(index_finger.y * h)
            
            # Draw a solid red circle right on the tip of the index finger!
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)

    # Show the final image
    cv2.imshow("Air Canvas - Phase 1", img)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()