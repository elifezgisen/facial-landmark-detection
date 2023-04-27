import cv2
import mediapipe as mp

# Face Mesh

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# The "mp_face_mesh" and "face_mesh" variables are used to access the MediaPipe face mesh model.

webcam = cv2.VideoCapture(0)

while True:
    # Real Time
    success, frame = webcam.read() 
            
    h, w, c = frame.shape
    
    print("Height, Width", h, w)

    rgb_image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # The "cv2.cvtColor()" function converts RGB images to BGR images. 
    # This conversion is the default format of OpenCV.
   
    # Facial Landmark

    results = face_mesh.process(rgb_image)
    LIPS = [ 61, 146, 91, 181, 84, 17, 314, 405, 321, 375,291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95,185, 40, 39, 37,0 ,267 ,269 ,270 ,409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78 ]

    # The "face_mesh.process()" function performs the face tracking functionality and stores the results in the "results" variable.

    for facial_landmarks in results.multi_face_landmarks:
        for i in list (LIPS):
            pt1 = facial_landmarks.landmark[i] 
            x = int(pt1.x * w)
            y = int(pt1.y * h)

    # "facial_landmarks.landmark" holds the position of the dots. 
    # It is used in this code to visualize each point by marking it as a circle.

            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1) # Shape of landmarks

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break # Exit the loop, turn off the webcam.

    # We use a specific letter to turn off the webcam.(Q)
    # Ascii code of the letter 'Q/q' => Q:81 or q:113
