import cv2
import mediapipe as mp
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = 2560, 1440

def get_eyes_position():
    global cam, face_mesh, screen_w, screen_h
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    blink_eye, screen_x, screen_y = False, 0, 0
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            if id == 1:
                screen_x = 2560 * landmark.x
                screen_y = 1440 * landmark.y
        left = [landmarks[145], landmarks[159]]
        if (left[0].y - left[1].y) < 0.01:
            blink_eye = True
    key = cv2.waitKey(1)
    if key == ord("s"):
        screen_w, screen_h = 2560, 1440
    return (blink_eye, screen_x, screen_y)