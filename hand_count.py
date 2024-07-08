import cv2
import numpy as np

def count_fingers(contour):
    try:
        if len(contour) < 3:
            return 0

        hull = cv2.convexHull(contour, returnPoints=False)

        if hull is None or len(hull) <= 3:
            return 0

        defects = cv2.convexityDefects(contour, hull)

        count_defects = 0
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])

                a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                angle = np.arccos((b**2 + c**2 - a**2) / (2*b*c))

                if angle <= np.pi/2:
                    count_defects += 1

        return count_defects + 1

    except Exception as e:
        print(f"Erro na contagem de dedos: {e}")
        return 0

try:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            blur = cv2.GaussianBlur(frame, (5, 5), 0)
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

            lower_skin = np.array([0, 20, 70], dtype=np.uint8)
            upper_skin = np.array([20, 255, 255], dtype=np.uint8)

            mask = cv2.inRange(hsv, lower_skin, upper_skin)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                max_contour = max(contours, key=cv2.contourArea)
                cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 2)
                fingers = count_fingers(max_contour)
                cv2.putText(frame, f'Dedos: {fingers}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow('Detecção de Dedos', frame)

        except Exception as e:
            print(f"Erro no pré-processamento da imagem: {e}")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Erro na captura de vídeo: {e}")

finally:
    try:
        if cap:
            cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Erro ao liberar a câmera ou fechar janelas: {e}")
