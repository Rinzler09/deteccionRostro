import cv2
import os
import numpy as np
# Cambia a la ruta donde hayas almacenado la fotos para entrenar
empleado = "JonathanMarley"
# dataPath = os.path.join('deteccionRostro\\empleadosGaleria', empleado)
dataPath = os.path.join('deteccionRostro\\empleadosGaleria')
peopleList = os.listdir(dataPath)
print('Lista de rostros: ', peopleList)
labels = []
facesData = []
label = 0
for nameDir in peopleList:
    personPath = dataPath + '\\' + nameDir
    # personPath = dataPath
    print('Leyendo las imagenes')
    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '\\' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'\\'+fileName, 0))
        image = cv2.imread(personPath+'\\'+fileName, 0)
        cv2.imshow('Entrenando Deteccion de Rostros', image)
        cv2.waitKey(10)
    label = label + 1
print('labels= ', labels)
print('Numero de etiquetas 0: ', np.count_nonzero(np.array(labels) == 0))
print('Numero de etiquetas 1: ', np.count_nonzero(np.array(labels) == 1))
face_recognizer = cv2.face.EigenFaceRecognizer_create()
print('Entrenando....')
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido
face_recognizer.write('deteccionRostro\\modelo.xml')
