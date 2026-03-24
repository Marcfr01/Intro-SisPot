import constantes as cte 
from Linha import Linha
import numpy as np
import math

class Circuito: 
    def __init__(self, fonte, linha : Linha, carga, nome):
        self._fonte = fonte
        self._imp_prop = linha.getImp_prop()
        self._imp_mutua = linha.getImp_mutua()
        self._carga = carga
        self._nome = nome

        self._incognitas = None # calculada no resolver por I = Y * V
        self._caracteristicas_rede = None
        self._valores_forcados = np.vstack([self._fonte, [0]])

    def getFonte(self):
        return self._fonte
    
    def getLinha(self):
        return self._imp_prop
    
    def getCarga(self):
        return self._carga
    
    def getNome(self):
        return self._nome
    
    def tipos_parametros(self):
        print("\n============= Parâmetros do circuito =============")
        if np.array_equal(self._fonte, cte.FONTE1): print('A fonte do circuito é do tipo 1')
        elif np.array_equal(self._fonte, cte.FONTE2): print('A fonte do circuito é do tipo 2')

        if (self._imp_prop == cte.Z_P1): print('A linha do circuito é do tipo 1')
        elif (self._imp_prop == cte.Z_P2): print('A linha do circuito é do tipo 2')

        if (self._carga == cte.Z1): print('A carga do circuito é do tipo 1')
        elif (self._carga == cte.Z2): print('A carga do circuito é do tipo 2')
        elif (self._carga == cte.Z3): print('A carga do circuito é do tipo 3')

    def resolver_circuito(self):
        #Linhas sem mutuas
        if self._nome == "G11": # Linha sem mútua + Carga trifásica em estrela não aterrada
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._carga, 0, 0, 1],
                                                    [0, self._imp_prop + self._carga, 0, 1],
                                                    [0, 0, self._imp_prop + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V / I = [Ia, Ib, Ic, Vnn']

        elif self._nome == "G12": # Linha sem mútua + Carga trifásica em estrela aterrada
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._carga, 0, 0, 0],
                                                    [0, self._imp_prop + self._carga, 0, 0],
                                                    [0, 0, self._imp_prop + self._carga, 0],
                                                    [1, 1, 1, -1] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V / I = [Ia, Ib, Ic, In]

        elif self._nome == "G13": # Linha sem mútua + carga trifásica em delta
            self._carga = self._carga / 3
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._carga, 0, 0, 1],
                                                    [0, self._imp_prop + self._carga, 0, 1],
                                                    [0, 0, self._imp_prop + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V / I = [Ia, Ib, Ic, Vnn']

        # Linhas com mútuas
        elif self._nome == "G21": # Linha com mútua + carga trifásica em estrela não aterrada
            self._linha_eq = self._imp_prop - self._imp_mutua
            self._caracteristicas_rede = np.array([ [self._linha_eq + self._carga, 0, 0, 1],
                                                    [0, self._linha_eq + self._carga, 0, 1],
                                                    [0, 0, self._linha_eq + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V / I = [Ia, Ib, Ic, Vnn']

        elif self._nome == "G22": # Linha com mútua + carga trifásica em estrela aterrada
            self._linha_eq = self._imp_prop + (2* self._imp_mutua)
            self._caracteristicas_rede = np.array([ [self._linha_eq + self._carga, 0, 0, 0],
                                                    [0, self._linha_eq + self._carga, 0, 0],
                                                    [0, 0, self._linha_eq + self._carga, 0],
                                                    [1, 1, 1, -1] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V / I = [Ia, Ib, Ic, In]

        elif self._nome == "G23": # Linha com mútua + carga trifásica em delta
            self._linha_eq = self._imp_prop - self._imp_mutua
            self._carga = self._carga / 3
            self._caracteristicas_rede = np.array([ [self._linha_eq + self._carga, 0, 0, 1],
                                                    [0, self._linha_eq + self._carga, 0, 1],
                                                    [0, 0, self._linha_eq + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V / I = [Ia, Ib, Ic, Vnn']

        return self._incognitas
