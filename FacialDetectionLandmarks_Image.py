import cv2
import mediapipe as mp


#Face Recognition
mp_face_meshing = mp.solutions.face_mesh
face_mesh = mp_face_meshing.FaceMesh()

#Image Path
image = cv2.imread("Brown-hair-girl-portrait-face_1280x800.jpg")
height, width, _ = image.shape
print("Height, width", height, width)

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Face Mesh Landmarks
result = face_mesh.process(rgb_image)

#Face Mesh Circles
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0, 468):
        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)

        cv2.circle(image, (x, y), 3, (232, 232, 2), -1)

#Image Showing
cv2.imshow("Image", image)
cv2.waitKey(0)
