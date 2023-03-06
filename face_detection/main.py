import cv2 # Install this module use this command pip install opencv-python 
face_cap = cv2.CascadeClassifier("C:/Users/HP/AppData/Roaming/Python/Python311/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0) 
while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale( #these are some are factors that helps in face detection 
        col,
        scaleFactor = 1.1,
        minNeighbors =  5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data, (x,y), (x+w, y+h), (0, 255, 0),2)
    cv2.imshow("Video_Camera", video_data)
    if cv2.waitKey(10) == ord("a"): #for closing the camera screen you can a
        break
video_cap.release() #This function release the video_cap function that plays live video
