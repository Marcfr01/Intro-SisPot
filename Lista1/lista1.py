from Circuito import Circuito
from Linha import Linha
import constantes as cte
import numpy as np
from itertools import product

# Instancia as linhas de transmissão
linha1 = Linha(cte.L1, cte.Z_P1, None)
linha2 = Linha(cte.L2, cte.Z_P2, cte.Z_M2)

# Instancia os circuitos com base nos grupos definidos anteriormente
fontes = [cte.FONTE1, cte.FONTE2]
linhas = [linha1, linha2]
cargas = [cte.Z1, cte.Z2, cte.Z3]

casos = []

# ============= Questão 1. ============= 

for fonte, linha, carga in product(fontes, linhas, cargas):
    c = Circuito(fonte= fonte, linha= linha, carga= carga, nome= f"G{linhas.index(linha) + 1}{cargas.index(carga) + 1}")
    casos.append(c)

for i in casos:
    i.resolver_circuito()
    i.salvar_dados("dados_lista1.txt")

casos.clear() # limpa o vetor de casos para o próximo exercício

# ============= Questão 2. =============
#                                           ----- carga 1
# Circiuito I: fonte 1 ----- linha 1 ----- |
#                                           ----- carga 3

casos.append(Circuito(fonte= fontes[0], linha= linhas[0], carga1= cargas[0], carga2= cargas[2], nome= "2.I")) 
casos[0].resolver_cargas_paralelas()

#                                            ----- carga 1
# Circiuito II: fonte 2 ----- linha 2 ----- |
#                                            ----- carga 3

casos.append(Circuito(fonte= fontes[1], linha= linhas[1], carga1= cargas[0], carga2= cargas[2], nome= "2.II")) 
casos[1].resolver_cargas_paralelas()

#                                             ----- carga 1
# Circiuito III: fonte 1 ----- linha 2 ----- |----- carga 2
#                                             ----- carga 3

casos.append(Circuito(fonte= fontes[0], linha= linhas[0], carga1= cargas[0], carga2= cargas[1], carga3= cargas[2], nome = "2.III")) 
casos[2].resolver_cargas_paralelas()