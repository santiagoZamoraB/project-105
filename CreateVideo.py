import os
import cv2 as cv

#creando el path de las imagenes
path = "Images/"

#lista para contener las imagenes
images =[]

#bucle for para separar los archivos por nombre y extension
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    #condición para agregar las imagenes a la lista Images
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file

        print(file_name)

        images.append(file_name)
        count = len(images)

        #creando el frame y sus parametros para reproducir el video
        frame =cv.imread(images[0])
        height,width,channels = frame.shape
        size =(width, height)
        print(size)
        out = cv.VideoWriter('project.avi',cv.VideoWriter_fourcc(*'DIVX'), 0.8, size)

        #bucle for para hacer el video agregando las imagenes de Images a out usando frame
        for i in range(0, count-1):
            frame = cv.imread(images[i])
            out.write(frame)
        
        out.release
        print("video terminado")

