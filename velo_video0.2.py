import cv2
import numpy as np
import datetime
import time

bgsMOG = cv2.createBackgroundSubtractorMOG2()
cap    = cv2.VideoCapture('video.avi')
#cap = cv2.VideoCapture('http://192.168.1.15:8080/video')
contador = 0

if cap:
    while True:
        ret, frame = cap.read()

        if ret:
            fgmask = bgsMOG.apply(frame, None, 0.1)
            cv2.line(frame,(450,0),(450,720),(320,550,0),1)
            # Encontrar contorno carro
            contorno, hierarchy = cv2.findContours(fgmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            try:
                hierarchy = hierarchy[0]

            except:
                hierarchy = []

            for contour, hier in zip(contorno, hierarchy):
                (x, y, w, h) = cv2.boundingRect(contour)

                if w > 20 and h > 20:
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 0)

                    #Encontrar centro carro
                    x1 = w/2
                    y1 = h/2

                    cx = x+x1
                    cy = y+y1
                    print "cy=", cy
                    print "cx=", cx
                    centrocar = (cx,cy)
                    print "Centro=", centrocar
                    # Desenha um circulo no meio do carro
                    cv2.circle(frame,(int(cx),int(cy)),2,(0,0,255),-1)

                    # Verifica se carro passou mesmo pela linha
                    dy = cy-108
                    print "dy", dy
                    if centrocar > (27, 38) and centrocar < (134, 108):
                        if (cx >= 120):
                            contador +=1
                            print "contador=", contador
                        #cv2.putText(frame, str(contador), (x,y-5),
                        #                cv2.FONT_HERSHEY_SIMPLEX,
                        #                0.5, (255, 0, 255), 2)

            # imprime status e data atual
            text = "0"
            if contador >= 3:
                text = "Trafego"
                print  contador

            #cv2.putText(frame, "Status: {}".format(text), (10, 20),
            #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)


            cv2.imshow('Output', frame)
            #cv2.imshow('FGMASK', fgmask)
            key = cv2.waitKey(60)
            if key == 27:
                break

cap.release()
cv2.destroyAllWindows()
