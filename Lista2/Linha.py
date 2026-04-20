class Linha:
    def __init__(self, distancia: float, p: complex, m: complex):
        self._distancia = distancia
        self._Z_p = p 
        self._Z_m = m 

    def getImp_prop(self):
        return self._Z_p 
       
    def getImp_mutua(self):
        return self._Z_m 
      
    def getDistancia(self):
        return self._distancia