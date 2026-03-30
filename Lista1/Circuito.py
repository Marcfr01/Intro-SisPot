import constantes as cte 
from Linha import Linha
import numpy as np
import math

class Circuito: 
    # Questão 1.
    def __init__(self, fonte, linha: Linha, cargas, nome):
        self._fonte = fonte
        self._imp_prop = linha.getImp_prop()
        self._imp_mutua = linha.getImp_mutua()
        self._cargas = cargas # Recebe uma lista de cargas
        self._nome = nome

        self._carga = cargas[0]
        self._incognitas = None # calculada no resolver por I = Y * V
        self._caracteristicas_rede = None # Matriz das impedâncias
        self._valores_forcados = np.vstack([self._fonte, [0]]) # Vetor com tensões provenientes da 2 Lei de Kirchhoff
        self._tensoes_carga_fase = None
        self._tensoes_linha = None

    # "Construtor" para a Questão 1
    @classmethod
    def questao_1(cls, fonte, linha, carga, nome):
        return cls(fonte, linha, [carga], nome)

    # "Construtor" para a Questão 2 (Circuitos I e II)
    @classmethod
    def questao_2_cI_cII(cls, fonte, linha, carga1, carga2, nome):
        return cls(fonte, linha, [carga1, carga2], nome)

    # "Construtor" para a Questão 2 (Circuito III)
    @classmethod
    def questao_2_cIII(cls, fonte, linha, carga1, carga2, carga3, nome):
        return cls(fonte, linha, [carga1, carga2, carga3], nome)


    def get_fonte(self):
        return self._fonte
    
    def get_linha(self):
        return self._imp_prop
    
    def get_carga(self):
        return self._cargas[0]
    
    def get_nome(self):
        return self._nome
    
    def get_incognitas(self):
        return self._incognitas
    
    
    def get_carga1(self):
        return self._carga1
    
    def get_carga2(self):
        return self._carga2
    
    def get_carga3(self):
        return self._carga3
    

    def resolver_circuito(self):
        #Linhas sem mutuas
        if self._nome == "G11": # Linha sem mútua + Carga trifásica em estrela não aterrada
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._carga, 0, 0, 1],
                                                    [0, self._imp_prop + self._carga, 0, 1],
                                                    [0, 0, self._imp_prop + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, Vnn']

        elif self._nome == "G12": # Linha sem mútua + Carga trifásica em estrela aterrada
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._carga, 0, 0, 0],
                                                    [0, self._imp_prop + self._carga, 0, 0],
                                                    [0, 0, self._imp_prop + self._carga, 0],
                                                    [1, 1, 1, -1] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, In]

        elif self._nome == "G13": # Linha sem mútua + carga trifásica em delta
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._carga, 0, 0, 1],
                                                    [0, self._imp_prop + self._carga, 0, 1],
                                                    [0, 0, self._imp_prop + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, Vnn']

        # Linhas com mútuas
        elif self._nome == "G21": # Linha com mútua + carga trifásica em estrela não aterrada
            self._linha_eq = self._imp_prop - self._imp_mutua
            self._caracteristicas_rede = np.array([ [self._linha_eq + self._carga, 0, 0, 1],
                                                    [0, self._linha_eq + self._carga, 0, 1],
                                                    [0, 0, self._linha_eq + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, Vnn']

        elif self._nome == "G22": # Linha com mútua + carga trifásica em estrela aterrada
            self._linha_eq = self._imp_prop + (2* self._imp_mutua)
            self._caracteristicas_rede = np.array([ [self._linha_eq + self._carga, 0, 0, 0],
                                                    [0, self._linha_eq + self._carga, 0, 0],
                                                    [0, 0, self._linha_eq + self._carga, 0],
                                                    [1, 1, 1, -1] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, In]

        elif self._nome == "G23": # Linha com mútua + carga trifásica em delta
            self._linha_eq = self._imp_prop - self._imp_mutua
            self._caracteristicas_rede = np.array([ [self._linha_eq + self._carga, 0, 0, 1],
                                                    [0, self._linha_eq + self._carga, 0, 1],
                                                    [0, 0, self._linha_eq + self._carga, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, Vnn']

        return self._incognitas

    def get_tensoes_fase(self):
        if np.array_equal(self._incognitas, None): raise ValueError("Correntes da linha ainda não foram calculadas. Execute .resolver_circuito() primeiro")
        self._tensoes_carga_fase = self._incognitas[:3] * self._carga

        return self._tensoes_carga_fase
    
    def get_tensoes_linha(self):
        if np.array_equal(self._incognitas, None): raise ValueError("Correntes da linha ainda não foram calculadas. Execute .resolver_circuito() primeiro")

        if self._nome in ["G11", "G12", "G13"]: self._tensoes_linha = self._incognitas * self._imp_prop # Vaa' = Ia * Zf
        elif self._nome in ["G21", "G23"]: self._tensoes_linha = self._incognitas[:3] * (self._imp_prop - self._imp_mutua) # Vaa' = Ia * (Zf - Zm) : carga não aterrada      
        elif self._nome == "G22": self._tensoes_linha = self._incognitas[:3] * (self._imp_prop + 2 * self._imp_mutua) # Vaa' = Ia * (Zf + 2Zm) : carga aterrada

        if self._nome == "2.I": self._tensoes_linha = self._incognitas * self._imp_prop # Vaa' = Ia * Zf
        elif self._nome == "2.II": self._tensoes_linha = self._incognitas[:3] * (self._imp_prop - self._imp_mutua) # Vaa' = Ia * (Zf - Zm) : carga não aterrada
        elif self._nome == "2.III": self._tensoes_linha = self._incognitas[:3] * (self._imp_prop + 2 * self._imp_mutua) # Vaa' = Ia * (Zf + 2Zm) : carga aterrada

        return self._tensoes_linha
    
    def resolver_cargas_paralelas(self):
        if self._nome == "2.I":
            self._carga1 = self._cargas[0]
            self._carga2 = self._cargas[1]
            self._Zeq = (self._carga1 * self._carga2) / (self._carga1 + self._carga2)
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._Zeq, 0, 0, 1], 
                                                    [0, self._imp_prop + self._Zeq, 0, 1],
                                                    [0, 0, self._imp_prop + self._Zeq, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, Vnn_eq]
        
        elif self._nome == "2.II":
            self._carga1 = self._cargas[0]
            self._carga2 = self._cargas[1]
            self._linha_eq = self._imp_prop - self._imp_mutua
            self._Zeq = (self._carga1 * self._carga2) / (self._carga1 + self._carga2)
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._Zeq, self._imp_mutua, self._imp_mutua, 1], 
                                                    [self._imp_mutua, self._imp_prop + self._Zeq, self._imp_mutua, 1],
                                                    [self._imp_mutua, self._imp_mutua, self._imp_prop + self._Zeq, 1],
                                                    [1, 1, 1, 0] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, Vnn_eq]

        elif self._nome == "2.III":
            self._carga1 = self._cargas[0]
            self._carga2 = self._cargas[1]
            self._carga3 = self._cargas[2]
            self._Zeq = 1 / ((1/self.carga1) + (1/self.carga2) + (1/self.carga3))
            self._caracteristicas_rede = np.array([ [self._imp_prop + self._Zeq, self._imp_mutua, self._imp_mutua, 0], 
                                                    [self._imp_mutua, self._imp_prop + self._Zeq, self._imp_mutua, 0],
                                                    [self._imp_mutua, self._imp_mutua, self._imp_prop + self._Zeq, 0],
                                                    [1, 1, 1, -1] ])
            inversa = np.linalg.inv(self._caracteristicas_rede)
            self._incognitas = np.dot(inversa, self._valores_forcados) # I = Y * V | I = [Ia, Ib, Ic, In]

        return self._incognitas

    def tipos_parametros(self):
        print("\n============= Parâmetros do circuito =============")
        if np.array_equal(self._fonte, cte.FONTE1): print('A fonte do circuito é do tipo 1')
        elif np.array_equal(self._fonte, cte.FONTE2): print('A fonte do circuito é do tipo 2')

        if (self._imp_prop == cte.Z_P1): print('A linha do circuito é do tipo 1')
        elif (self._imp_prop == cte.Z_P2): print('A linha do circuito é do tipo 2')

        if (self._carga == cte.Z1): print('A carga do circuito é do tipo 1')
        elif (self._carga == cte.Z2): print('A carga do circuito é do tipo 2')
        elif (self._carga == cte.Z3): print('A carga do circuito é do tipo 3')

    def salvar_dados(self, arquivo):
        try:
            with open(arquivo, "a", encoding="utf-8") as f:
                f.write(f"============= Dados referentes ao {self._nome} =============\n")

                f.write("Parâmetros: \n")

                if np.array_equal(self._fonte, cte.FONTE1): f.write(f"Fonte: 1\n")
                elif np.array_equal(self._fonte, cte.FONTE2): f.write(f"Fonte: 2\n")

                if (self._imp_prop == cte.Z_P1): f.write(f'Linha: 1 | Z_p = {self._imp_prop} [Ω]\n')
                elif (self._imp_prop == cte.Z_P2): f.write(f'Linha: 2 | Z_p = {self._imp_prop} [Ω] e Z_m = {self._imp_mutua} [Ω]\n')

                if   (self._carga == cte.Z1): f.write(f'Carga : 1 | Z_f = {self._carga} [Ω]\n')
                elif (self._carga == cte.Z2): f.write(f'Carga : 2 | Z_f = {self._carga} [Ω]\n')
                elif (self._carga == cte.Z3): f.write(f'Carga : 3 | Z_f = {self._carga} [Ω]\n')

                f.write("\nResultados:\n")
                f.write("1a.\n")
                modulo = np.abs(self._incognitas)
                fase = np.angle(self._incognitas, deg=True)  
                f.write(f"Ia:   {self._incognitas[0]} = {modulo[0][0]:.4f} ∠ {fase[0][0]:.2f}°\n")
                f.write(f"Ib:   {self._incognitas[1]} = {modulo[1][0]:.4f} ∠ {fase[1][0]:.2f}°\n")
                f.write(f"Ic:   {self._incognitas[2]} = {modulo[2][0]:.4f} ∠ {fase[2][0]:.2f}°\n")
                f.write(f"In:   {self._incognitas[3]} = {modulo[3][0]:.4f} ∠ {fase[3][0]:.2f}°\n")

                f.write("\n1b.\n")
                if self._nome == "G13" or self._nome == "G23":
                    self.get_tensoes_fase()
                    Va_temp = self._tensoes_carga_fase[0]
                    Vb_temp = self._tensoes_carga_fase[1]
                    Vc_temp = self._tensoes_carga_fase[2]
                    self._tensoes_carga_fase1 = np.array([Va_temp - Vb_temp, Vb_temp - Vc_temp, Vc_temp - Va_temp])
                    modulo3_c = np.abs(self._tensoes_carga_fase1)
                    fase3_c = np.angle(self._tensoes_carga_fase1, deg=True) 
                    f.write(f"Vab:   {self._tensoes_carga_fase1[0]} = {modulo3_c[0][0]:.4f} ∠ {fase3_c[0][0]:.2f}°\n")
                    f.write(f"Vbc:   {self._tensoes_carga_fase1[1]} = {modulo3_c[1][0]:.4f} ∠ {fase3_c[1][0]:.2f}°\n")
                    f.write(f"Vca:   {self._tensoes_carga_fase1[2]} = {modulo3_c[2][0]:.4f} ∠ {fase3_c[2][0]:.2f}°\n")
                else:
                    self.get_tensoes_fase()
                    modulo3_c = np.abs(self._tensoes_carga_fase)
                    fase3_c = np.angle(self._tensoes_carga_fase, deg=True) 
                    f.write(f"Van':   {self._tensoes_carga_fase[0]} = {modulo3_c[0][0]:.4f} ∠ {fase3_c[0][0]:.2f}°\n")
                    f.write(f"Vbn':   {self._tensoes_carga_fase[1]} = {modulo3_c[1][0]:.4f} ∠ {fase3_c[1][0]:.2f}°\n")
                    f.write(f"Vcn':   {self._tensoes_carga_fase[2]} = {modulo3_c[2][0]:.4f} ∠ {fase3_c[2][0]:.2f}°\n")

                f.write("\n1c.\n")
                self.get_tensoes_linha()
                modulo3_l = np.abs(self._tensoes_linha)
                fase3_l = np.angle(self._tensoes_linha, deg=True) 
                f.write(f"Vaa':   {self._tensoes_linha[0]} = {modulo3_l[0][0]:.4f} ∠ {fase3_l[0][0]:.2f}°\n")
                f.write(f"Vbb':   {self._tensoes_linha[1]} = {modulo3_l[1][0]:.4f} ∠ {fase3_l[1][0]:.2f}°\n")
                f.write(f"Vcc':   {self._tensoes_linha[2]} = {modulo3_l[2][0]:.4f} ∠ {fase3_l[2][0]:.2f}°\n")
                f.write("\n")
        except Exception as e:
            print("Erro ao salvar o arquivo", e)