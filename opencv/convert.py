import numpy as np
import cv2
import glob
import os

def faceCrop(imagePattern,boxScale=1):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    imgList=glob.glob(imagePattern)
    
    if len(imgList)<=0:
        print('No Images Found')
        return

    for img in imgList:
        #escalas/tamanhos crus
        pil_im = cv2.imread(img)
        height, width, channels = pil_im.shape

        img_scale = (width/256)
        #print("ESCALA : " + str(img_scale))

        scaled_height = round(height/(img_scale))
        #print("NOVA ALTURA: " + str(scaled_height))
        
        img_resize = cv2.resize(pil_im, (256,scaled_height), interpolation=cv2.INTER_LINEAR)
        
        img_cutting = DetectFace(img_resize, 256, face_cascade)
        
        FaceFileName = "fotosadm/" + img
        cv2.imwrite(FaceFileName, img_cutting)

        print(img)
        print("---------------------------------------------")

        # exibir quadrado da imagem
        # cv2.imshow('img',img_cutting)
        # cv2.waitKey(0)

def DetectFace(image, img_width, faceCascade, returnImage=False):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        y_acima_abaixo = round((img_width - h)/2)
        dif = y - y_acima_abaixo

        if dif < 0:
            y_inicial_crop = 0
            y_final_crop = y + h + y_acima_abaixo + (dif * -1)

        else:
            y_inicial_crop = dif
            y_final_crop = y + h + y_acima_abaixo


        # image = cv2.rectangle(image,(0,y_inicial_crop),(500,y_final_crop),(255,0,0),2)

        sub_face = image[y_inicial_crop:y_final_crop, 0:500]
        return sub_face


faceCrop('*.jpg',boxScale=1)