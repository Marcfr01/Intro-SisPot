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
    c = Circuito.questao_1(fonte= fonte, linha= linha, carga= carga, nome= f"G{linhas.index(linha) + 1}{cargas.index(carga) + 1}")
    casos.append(c)

for i in casos:
    i.resolver_circuito()
    #i.salvar_dados("dados_lista1.txt")

for i in casos: del i # limpa o vetor casos

# ============= Questão 2. =============
#                                           ----- carga 1
# Circiuito I: fonte 1 ----- linha 1 ----- |
#                                           ----- carga 3

casos.append(Circuito.questao_2_cI_cII(fonte= fontes[0], linha= linhas[0], carga1= cargas[0], carga2= cargas[2], nome= "2.I")) 
casos[0].resolver_cargas_paralelas()
teste0 = casos[0].get_incognitas()
modulo0 = np.abs(teste0)
fase0 = np.angle(teste0, deg=True) 
print(f"Ia:   {teste0[0]} = {modulo0[0][0]:.4f} ∠ {fase0[0][0]:.2f}°")
print(f"Ib:   {teste0[1]} = {modulo0[1][0]:.4f} ∠ {fase0[1][0]:.2f}°")
print(f"Ic:   {teste0[2]} = {modulo0[2][0]:.4f} ∠ {fase0[2][0]:.2f}°")
print(f"Vnn': {teste0[3]} = {modulo0[3][0]:.4f} ∠ {fase0[3][0]:.2f}°")
print("\n\n")

#                                            ----- carga 1
# Circiuito II: fonte 2 ----- linha 2 ----- |
#                                            ----- carga 3

casos.append(Circuito.questao_2_cI_cII(fonte= fontes[1], linha= linhas[1], carga1= cargas[0], carga2= cargas[2], nome= "2.II")) 
casos[1].resolver_cargas_paralelas()
teste1 = casos[1].get_incognitas()
modulo1 = np.abs(teste1)
fase1 = np.angle(teste1, deg=True) 
print(f"Ia:   {teste1[0]} = {modulo1[0][0]:.4f} ∠ {fase1[0][0]:.2f}°")
print(f"Ib:   {teste1[1]} = {modulo1[1][0]:.4f} ∠ {fase1[1][0]:.2f}°")
print(f"Ic:   {teste1[2]} = {modulo1[2][0]:.4f} ∠ {fase1[2][0]:.2f}°")
print(f"Vnn': {teste1[3]} = {modulo1[3][0]:.4f} ∠ {fase1[3][0]:.2f}°")
print("\n\n")

#                                             ----- carga 1
# Circiuito III: fonte 1 ----- linha 2 ----- |----- carga 2
#                                             ----- carga 3

casos.append(Circuito.questao_2_cIII(fonte= fontes[0], linha= linhas[0], carga1= cargas[0], carga2= cargas[1], carga3= cargas[2], nome = "2.III")) 
casos[2].resolver_cargas_paralelas()
teste2 = casos[2].get_incognitas()
modulo2 = np.abs(teste2)
fase2 = np.angle(teste2, deg=True) 
print(f"Ia:   {teste2[0]} = {modulo2[0][0]:.4f} ∠ {fase2[0][0]:.2f}°")
print(f"Ib:   {teste2[1]} = {modulo2[1][0]:.4f} ∠ {fase2[1][0]:.2f}°")
print(f"Ic:   {teste2[2]} = {modulo2[2][0]:.4f} ∠ {fase2[2][0]:.2f}°")
print(f"Vnn': {teste2[3]} = {modulo2[3][0]:.4f} ∠ {fase2[3][0]:.2f}°")
print("\n\n")