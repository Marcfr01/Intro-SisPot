from Circuito import Circuito
from Linha import Linha
import constantes as cte
import numpy as np
from itertools import product
import pandas as pd

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

casos.append(Circuito.questao_2_cIII(fonte= fontes[0], linha= linhas[0], carga1= cargas[0], carga2= cargas[1], carga3= cargas[2], nome = "2.III")) 
casos[2].resolver_cargas_paralelas()
circuito_III = casos[2].get_incognitas()
modulo2 = np.abs(circuito_III)
fase2 = np.angle(circuito_III, deg=True) 

questao2 = pd.DataFrame(columns=["Circuito I", "Circuito II", "Circuito III"], index= ["Ia", "Ib", "Ic", "Vnn / In"])
m0_flat = np.array(modulo0).flatten()
f0_flat = np.array(fase0).flatten()

m1_flat = np.array(modulo1).flatten()
f1_flat = np.array(fase1).flatten()

m2_flat = np.array(modulo2).flatten()
f2_flat = np.array(fase2).flatten()

questao2["Circuito I"]   = [f"{m:.4f} ∠ {f:.2f}°" for m, f in zip(m0_flat, f0_flat)]
questao2["Circuito II"]  = [f"{m:.4f} ∠ {f:.2f}°" for m, f in zip(m1_flat, f1_flat)]
questao2["Circuito III"] = [f"{m:.4f} ∠ {f:.2f}°" for m, f in zip(m2_flat, f2_flat)]

print("\n",questao2["Circuito I"])
print("\n",questao2["Circuito II"])
print("\n",questao2["Circuito III"])
print()

modulo0_l = np.abs(casos[0].get_tensoes_linha())
fase0_l = np.angle(casos[0].get_tensoes_linha(), deg= True)
print(f"Vaa':   {casos[0].get_tensoes_linha()[0]} = {modulo0_l[0][0]:.4f} ∠ {fase0_l[0][0]:.2f}°")
print(f"Vbb':   {casos[0].get_tensoes_linha()[1]} = {modulo0_l[1][0]:.4f} ∠ {fase0_l[1][0]:.2f}°")
print(f"Vcc':   {casos[0].get_tensoes_linha()[2]} = {modulo0_l[2][0]:.4f} ∠ {fase0_l[2][0]:.2f}°\n")

modulo1_l = np.abs(casos[1].get_tensoes_linha())
fase1_l = np.angle(casos[1].get_tensoes_linha(), deg= True)
print(f"Vaa':   {casos[1].get_tensoes_linha()[0]} = {modulo1_l[0][0]:.4f} ∠ {fase1_l[0][0]:.2f}°")
print(f"Vbb':   {casos[1].get_tensoes_linha()[1]} = {modulo1_l[1][0]:.4f} ∠ {fase1_l[1][0]:.2f}°")
print(f"Vcc':   {casos[1].get_tensoes_linha()[2]} = {modulo1_l[2][0]:.4f} ∠ {fase1_l[2][0]:.2f}°\n")

modulo2_l = np.abs(casos[2].get_tensoes_linha())
fase2_l = np.angle(casos[2].get_tensoes_linha(), deg= True)
print(f"Vaa':   {casos[2].get_tensoes_linha()[0]} = {modulo2_l[0][0]:.4f} ∠ {fase2_l[0][0]:.2f}°")
print(f"Vbb':   {casos[2].get_tensoes_linha()[1]} = {modulo2_l[1][0]:.4f} ∠ {fase2_l[1][0]:.2f}°")
print(f"Vcc':   {casos[2].get_tensoes_linha()[2]} = {modulo2_l[2][0]:.4f} ∠ {fase2_l[2][0]:.2f}°\n")
