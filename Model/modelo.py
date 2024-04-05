
class Compuertas:
    def __init__(self, nombre= None, axioma= None, tabla=None ,simbolo=None):
        self.nombre = nombre 
        self.axioma = axioma   
        self.tabla = tabla
        self.simbolo= simbolo 
    

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre=nombre

    def getAxioma(self):
        return self.axioma
    
    def setAxioma(self, axioma):
        self.axioma=axioma

    def getTabla(self):
        return self.tabla
    
    def setTabla(self, tabla):
        self.tabla=tabla
    
    def getSimbolo(self):
        return self.simbolo
    
    def setSimbolo(self, simbolo):
        self.simbolo=simbolo