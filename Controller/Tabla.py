import cv2
import os
from Controller.controlador import Controller

class Imagen:

    def __init__(self):
        self.controller = Controller()

    def addImage(self, value):

        data=self.controller.get_compuerta(value)
        if data is not None:
            url=data.simbolo
        else:
            pass

        script_dir = os.path.dirname(__file__)
        imagen_path = os.path.join(script_dir, url)

        imagen = cv2.imread(imagen_path)

        if imagen is not None:
           cv2.imshow('SIMBOLO', imagen)
           cv2.waitKey(0)  
           cv2.destroyAllWindows()  
        else:
            print('No se pudo cargar la imagen.')