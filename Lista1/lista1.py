from Circuito import Circuito
from Linha import Linha
import constantes as cte
import numpy as np
from itertools import product

def imprimir_vetor_polar(vetor):
    modulo = np.abs(vetor)
    fase = np.angle(vetor, deg=True)  # Converte fase para graus
    
    for i in range(len(vetor)):
        print(f"   {modulo[i][0]:.4f} ∠ {fase[i][0]:.2f}°")

# Instancia as linhas de transmissão
linha1 = Linha(cte.L1, cte.Z_P1, None)
linha2 = Linha(cte.L2, cte.Z_P2, cte.Z_M2)

# Instancia os circuitos com base nos grupos definidos anteriormente
fontes = [cte.FONTE1, cte.FONTE2]
linhas = [linha1, linha2]
cargas = [cte.Z1, cte.Z2, cte.Z3]

casos = []

for fonte, linha, carga in product(fontes, linhas, cargas):
    c = Circuito(fonte, linha, carga, f"G{linhas.index(linha) + 1}{cargas.index(carga) + 1}")
    casos.append(c)

#for i in casos: print(i.getNome())

# teste
caso1 = Circuito(cte.FONTE1, cte.Z_P1, cte.Z1, "G11")
caso1.tipos_parametros()
teste1 = caso1.resolver_circuito()
modulo1 = np.abs(teste1)
fase1 = np.angle(teste1, deg=True)  

print("\nCaso de teste 1:")
print(f"Ia:   {teste1[0]} = {modulo1[0][0]:.4f} ∠ {fase1[0][0]:.2f}°")
print(f"Ib:   {teste1[1]} = {modulo1[1][0]:.4f} ∠ {fase1[1][0]:.2f}°")
print(f"Ic:   {teste1[2]} = {modulo1[2][0]:.4f} ∠ {fase1[2][0]:.2f}°")
print(f"Vnn': {teste1[3]} = {modulo1[3][0]:.4f} ∠ {fase1[3][0]:.2f}°")

caso2 = Circuito(cte.FONTE2, cte.Z_P1, cte.Z2, "G11")
caso2.tipos_parametros()
teste2 = caso2.resolver_circuito()
modulo2 = np.abs(teste2)
fase2 = np.angle(teste2, deg=True) 

print("\nCaso de teste 2:")
print(f"Ia:   {teste2[0]} = {modulo2[0][0]:.4f} ∠ {fase2[0][0]:.2f}°")
print(f"Ib:   {teste2[1]} = {modulo2[1][0]:.4f} ∠ {fase2[1][0]:.2f}°")
print(f"Ic:   {teste2[2]} = {modulo2[2][0]:.4f} ∠ {fase2[2][0]:.2f}°")
print(f"In:   {teste2[3]} = {modulo2[3][0]:.4f} ∠ {fase2[3][0]:.2f}°")