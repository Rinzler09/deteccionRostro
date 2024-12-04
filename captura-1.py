""" Script diseñado para la captura de rostros """

import os
import cv2
import imutils

personName = 'MiltonPaz'
# Cambia a la ruta donde hayas almacenado Data
dataPath = r'deteccionRostro\\empleadosGaleria'
personPath = os.path.join(dataPath, personName)

if not os.path.exists(personPath):
    print('Carpeta creada: ', personPath)
    os.makedirs(personPath)
# se utiliza la webcam para sacar las capturas de los rostros
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# videoPath = os.path.join(
#     'deteccionRostro\empleadosVideos', f'{personName}.mp4')
# se utiliza una ruta de video para detectar los rostros y sacar capturas
# cap = cv2.VideoCapture(videoPath)

if not cap.isOpened():
    print("Error: No se pudo abrir el video")
    exit()

faceClassif = cv2.CascadeClassifier(
    # cv2.data.haarcascades+'haarcascade_frontalface_default.xml'
    r'deteccionRostro\\haarcascade_frontalface_default.xml')

if faceClassif.empty():
    print("No se encontro el archivo xml de Deteccion")
    exit()

count = 0
while True:

    ret, frame = cap.read()
    if ret == False:
        break
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    # faces = faceClassif.detectMultiScale(gray, 1.3, 5)
    faces = faceClassif.detectMultiScale(gray, 1.2, 6)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + r'\\rostro_{}.jpg'.format(count), rostro)
        count = count + 1
    cv2.imshow('Captura de Rostro', frame)
    k = cv2.waitKey(1)
    if k == 27 or count >= 100:
        break
cap.release()
cv2.destroyAllWindows()
