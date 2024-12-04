import cv2
import os
import time
import subprocess


def getDateTime():
    fecha_hora = time.localtime()
    fecha_hora = time.strftime("%Y-%m-%d %H:%M:%S", fecha_hora)
    return fecha_hora


def openLoggedIn(empleado, dateTime):
    subprocess.Popen(
        ['python', 'deteccionRostro\\interfazG\\registrado.py', empleado, dateTime])


recognitionCounter = 0
ruta = 'deteccionRostro\\empleadosGaleria'
imagen = os.listdir(ruta)
print('imagen=', imagen)
modelo = cv2.face.EigenFaceRecognizer_create()
# modelo = cv2.face.LBPHFaceRecognizer_create()
# Leyendo el modelo
modelo.read('deteccionRostro\\modelo.xml')


# cap = cv2.VideoCapture('/home/miltonpaz/Desktop/IA_OpenCv/Tarea 1/DuaLipa.mp4')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
faceClassif = cv2.CascadeClassifier(
    'deteccionRostro\\haarcascade_frontalface_default.xml')
while True:

    ret, frame = cap.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = modelo.predict(rostro)
        cv2.putText(frame, '{}'.format(result), (x, y-5),
                    1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

        # EigenFaces
        if result[1] < 5700:

            cv2.putText(frame, '{}'.format(
                imagen[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            recognitionCounter += 1
            if recognitionCounter > 15:
                empleado = imagen[result[0]]
                dateTime = getDateTime()

                cap.release()
                cv2.destroyAllWindows()
                time.sleep(1)
                openLoggedIn(empleado, dateTime)

        else:
            cv2.putText(frame, 'Intruso', (x, y-20), 2,
                        0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Prueba Deteccion de Rostro (ESC para SALIR)', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
