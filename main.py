import cv2
import mediapipe as mp
import pyautogui
import time

# Mediapipe modullari
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
hands_model = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

cap = cv2.VideoCapture(0)

# Chap ko'z indekslari
LEFT_EYE = [362, 385, 387, 263, 373, 380]

def get_ear(landmarks, eye_points):
    p1, p5 = landmarks[eye_points[1]], landmarks[eye_points[5]]
    p2, p4 = landmarks[eye_points[2]], landmarks[eye_points[4]]
    p0, p3 = landmarks[eye_points[0]], landmarks[eye_points[3]]
    v_dist = (((p1.x - p5.x)**2 + (p1.y - p5.y)**2)**0.5 + ((p2.x - p4.x)**2 + (p2.y - p4.y)**2)**0.5) / 2
    h_dist = ((p0.x - p3.x)**2 + (p0.y - p3.y)**2)**0.5
    return v_dist / h_dist

# Holatni saqlash uchun o'zgaruvchilar
eye_closed_start_time = None
is_proper_blink = False
UP_THRESHOLD = 0.4 

print("Tizim ishga tushdi!")
print("- Ko'zni 0.4s yumib turing va oching: PASTGA (Down)")
print("- Barmoqni chiziqdan tepaga ko'taring: TEPAGA (Up)")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    face_results = face_mesh.process(rgb_frame)
    hand_results = hands_model.process(rgb_frame)

    # Vizual chegara chizig'i
    cv2.line(frame, (0, int(h * UP_THRESHOLD)), (w, int(h * UP_THRESHOLD)), (0, 255, 255), 2)

    # 1. KO'Z LOGIKASI (0.4s sharti bilan)
    if face_results.multi_face_landmarks:
        landmarks = face_results.multi_face_landmarks[0].landmark
        ear = get_ear(landmarks, LEFT_EYE)

        if ear < 0.20:  # Ko'z yumilgan
            if eye_closed_start_time is None:
                eye_closed_start_time = time.time()
            
            # Qancha vaqt yumilib turganini hisoblash
            duration = time.time() - eye_closed_start_time
            if duration >= 0.4:
                is_proper_blink = True
                cv2.putText(frame, "TAYYOR (Oching!)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                cv2.putText(frame, f"Kuting: {round(duration, 1)}s", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:  # Ko'z ochildi
            if eye_closed_start_time is not None:
                if is_proper_blink:
                    pyautogui.press("down")
                    print(">>> BUYRUQ: DOWN <<<")
                    cv2.putText(frame, "DOWN!", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
                
                # Holatni nollash
                eye_closed_start_time = None
                is_proper_blink = False

    # 2. QO'L HARAKATI (TEPAGA)
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            finger_tip_y = hand_landmarks.landmark[8].y 
            if finger_tip_y < UP_THRESHOLD:
                pyautogui.press("down")
                cv2.putText(frame, "UP!", (w-150, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
                time.sleep(0.15) 

    cv2.imshow('Smart Control v3', frame)
    if cv2.waitKey(1) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()