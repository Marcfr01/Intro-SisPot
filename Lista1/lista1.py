from Circuito import Circuito, Circuito3
from Linha import Linha
import constantes as cte
import numpy as np
from itertools import product
import pandas as pd

# Instancia as linhas de transmissão
linha1 = Linha(cte.L1, cte.Z_P1, None)
linha2 = Linha(cte.L2, cte.Z_P2, cte.Z_M2)

# Instancia os circuitos com base nos grupos definidos anteriormente
fontes = [cte.FONTE1, cte.FONTE2, cte.FONTE3]
linhas = [linha1, linha2]
cargas = [cte.Z1, cte.Z2, cte.Z3]

casos = []


# ============= Questão 1. ============= 

for fonte, linha, carga in product(fontes, linhas, cargas):
    # Criados circuitos para cada combinação de fonte, linha e carga, nomeados de acordo com o grupo a que pertencem 
    c = Circuito.questao_1(fonte= fonte, linha= linha, carga= carga, nome= f"G{linhas.index(linha) + 1}{cargas.index(carga) + 1}") 
    casos.append(c)

for i in casos:
    i.resolver_circuito()
    i.salvar_dados_q1("dados_lista1_q1.txt")

for i in casos: 
    del i # deleta cada caso

casos.clear() # limpa o vetor de casos para a proxima questao


# ============= Questão 2. =============
#                                           ----- carga 1
# Circiuito I: fonte 1 ----- linha 1 ----- |
#                                           ----- carga 2

casos.append(Circuito.questao_2_cI_cII(fonte= fontes[0], linha= linhas[0], carga1= cargas[0], carga2= cargas[1], nome= "2.I")) 
casos[0].resolver_cargas_paralelas()
circuito_I = casos[0].get_incognitas()
modulo0 = np.abs(circuito_I)
fase0 = np.angle(circuito_I, deg=True) 

#                                            ----- carga 1
# Circiuito II: fonte 2 ----- linha 2 ----- |
#                                            ----- carga 3

casos.append(Circuito.questao_2_cI_cII(fonte= fontes[1], linha= linhas[1], carga1= cargas[0], carga2= cargas[2], nome= "2.II")) 
casos[1].resolver_cargas_paralelas()
circuito_II = casos[1].get_incognitas()
modulo1 = np.abs(circuito_II)
fase1 = np.angle(circuito_II, deg=True) 

#                                             ----- carga 1
# Circiuito III: fonte 1 ----- linha 2 ----- |----- carga 2
#                                             ----- carga 3

casos.append(Circuito.questao_2_cIII(fonte= fontes[0], linha= linhas[1], carga1= cargas[0], carga2= cargas[1], carga3= cargas[2], nome = "2.III")) 
casos[2].resolver_cargas_paralelas()
circuito_III = casos[2].get_incognitas()
modulo2 = np.abs(circuito_III)
fase2 = np.angle(circuito_III, deg=True) 

for i in casos:
    i.salvar_dados_q2("dados_lista1_q2.txt")

for i in casos:
    del i # deleta cada caso

casos.clear() # limpa o vetor de casos para a proxima questao


# ============= Questão 3. ============= 

casos.append(Circuito3(fonte1= fontes[0], fonte2= fontes[2], linha1= linhas[0], linha2= linhas[1], carga= cargas[0], nome= "3."))
casos[0].resolver_2fontes()
casos[0].salvar_q3("dados_lista1_q3.txt")

for i in casos:
    del i # deleta cada caso

casos.clear() # limpa o vetor de casos para a proxima questao