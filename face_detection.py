import cv2
import face_recognition
import numpy as np

def detect_faces_and_analyze(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    expressions = []
    ages = []

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        face_locations = face_recognition.face_locations(face)
        if face_locations:
            face_encoding = face_recognition.face_encodings(face, face_locations)[0]
            expression = predict_expression(face_encoding)
            expressions.append(expression)

        age = predict_age(face)
        ages.append(age)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        label = f'Idade: {age}, Expressão: {expression}'
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame, expressions, ages

def predict_expression(face_encoding):
    return "Feliz"  

def predict_age(face):
    return np.random.randint(20, 60) 

try:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, expressions, ages = detect_faces_and_analyze(frame)

        cv2.imshow('Análise Facial', frame)

        # Sair com 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Erro: {e}")

finally:
    try:
        if cap:
            cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Erro ao liberar a câmera ou fechar janelas: {e}")
