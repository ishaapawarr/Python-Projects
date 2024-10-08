# pip install cmake
# pip install face_recognition
# pip install opencv-python
# pip install numpy

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime  # Fixed the typo 'daatetime' to 'datetime'

# Initialize webcam video capture
video_capture = cv2.VideoCapture(0)

# Load known faces and their encodings
isha_image = face_recognition.load_image_file("faces/isha.jpg")
isha_encoding = face_recognition.face_encodings(isha_image)[0]

rahul_image = face_recognition.load_image_file("faces/rahul.jpg")
rahul_encoding = face_recognition.face_encodings(rahul_image)[0]

# List of known face encodings and names
known_face_encodings = [isha_encoding, rahul_encoding]
known_face_names = ["Isha", "Rahul"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Open a CSV file to write the attendance
f = open(f"{current_date}.csv", "w+", newline="")  # Fixed 'newLine' to 'newline'
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()
    # Resize the frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)  # Fixed 'face_location' to 'face_locations'
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # Fixed 'face_encoding' typo

    for face_encoding in face_encodings:
        # Compare faces and calculate distances
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  # Fixed 'mathes' to 'matches'
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Display the recognized person's name on the frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            # Mark the student as present and log it in the CSV file
            if name in students:
                students.remove(name)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])

    # Display the video feed
    cv2.imshow("Attendance", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):  # Fixed 'cv2.waitKet' to 'cv2.waitKey'
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
f.close()