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
cargas = [cte.Z1, cte.Z2, cte.Z3, cte.Z4]

casos = []

'''
# ============= Questão 1. ============= 

# instancia o circuito 1 - fonte 1, linha 1, carga 1
casos.append(Circuito.questao_1cI(fonte= fontes[0], linha= linhas[0], carga= cargas[0], nome= "1.I"))
circuitoI = casos[0].correntes_linha()
modulo0 = np.abs(circuitoI)
fase0 = np.angle(circuitoI, deg=True)
print(f"Circuito I: Corrente na linha : Módulo = {modulo0[0][0]:.4f} A, Fase = {fase0[0][0]:.2f}°")
print(f"Circuito I: Corrente na linha : Módulo = {modulo0[1][0]:.4f} A, Fase = {fase0[1][0]:.2f}°")
print(f"Circuito I: Corrente na linha : Módulo = {modulo0[2][0]:.4f} A, Fase = {fase0[2][0]:.2f}°\n")

Sf1 = casos[0].get_potencia_fonte()
moduloSf1 = np.abs(Sf1)
faseSf1 = np.angle(Sf1, deg=True)
print(f"Circuito I: Potência na fonte = {moduloSf1[0][0]/1000:.4f} kVA, Fase = {faseSf1[0][0]:.2f}°")
print(f"Circuito I: Potência na fonte = {moduloSf1[1][0]/1000:.4f} kVA, Fase = {faseSf1[1][0]:.2f}°")
print(f"Circuito I: Potência na fonte = {moduloSf1[2][0]/1000:.4f} kVA, Fase = {faseSf1[2][0]:.2f}°\n")

Pl1 = casos[0].get_potencia_linha()
print(f"Circuito I: Potência na linha = {Pl1[0][0]/1000:.4f} kW, ")
print(f"Circuito I: Potência na linha = {Pl1[1][0]/1000:.4f} kW, ")
print(f"Circuito I: Potência na linha = {Pl1[2][0]/1000:.4f} kW, \n")

Sc1 = casos[0].get_potencia_carga()
moduloSc1 = np.abs(Sc1)
faseSc1 = np.angle(Sc1, deg=True)
print(f"Circuito I: Potência na carga = {moduloSc1[0][0]/1000:.4f} kVA, Fase = {faseSc1[0][0]:.2f}° | {Sc1[0][0]/1000:.4f} kVA")
print(f"Circuito I: Potência na carga = {moduloSc1[1][0]/1000:.4f} kVA, Fase = {faseSc1[1][0]:.2f}° | {Sc1[1][0]/1000:.4f} kVA")
print(f"Circuito I: Potência na carga = {moduloSc1[2][0]/1000:.4f} kVA, Fase = {faseSc1[2][0]:.2f}° | {Sc1[2][0]/1000:.4f} kVA\n")

C1, Xc1 = casos[0].capacitor()
print(f"Circuito I: Capacitor necessário para correção do fator de potência = {C1[0][0]*1e6:.4f} μF\n")

Pl1_1, Pl1_1t, i1 = casos[0].potencia_linha_capacitor()
print(f"Circuito I: Potência na linha com capacitor = {Pl1_1[0][0]/1000:.4f} kW,")
print(f"Circuito I: Potência na linha com capacitor = {Pl1_1[1][0]/1000:.4f} kW, ")
print(f"Circuito I: Potência na linha com capacitor = {Pl1_1[2][0]/1000:.4f} kW, \n")
print(f"Circuito I: Potência total na linha com capacitor = {Pl1_1t/1000:.4f} kW\n")

print("=====================================================\n")

# instancia o circuito 2 - fonte 2, linha 2, [carga 1 // carga 1] (paralelo)
casos.append(Circuito.questao_1cII(fonte= fontes[1], linha= linhas[1], carga1= cargas[0], carga2= cargas[0], nome= "1.II"))
circuitoII = casos[1].correntes_linha()
modulo1 = np.abs(circuitoII)
fase1 = np.angle(circuitoII, deg=True)
print(f"Circuito II: Corrente na linha : Módulo = {modulo1[0][0]:.4f} A, Fase = {fase1[0][0]:.2f}°")
print(f"Circuito II: Corrente na linha : Módulo = {modulo1[1][0]:.4f} A, Fase = {fase1[1][0]:.2f}°")
print(f"Circuito II: Corrente na linha : Módulo = {modulo1[2][0]:.4f} A, Fase = {fase1[2][0]:.2f}°\n")

Sf2 = casos[1].get_potencia_fonte()
moduloSf1 = np.abs(Sf2)
faseSf1 = np.angle(Sf2, deg=True)
print(f"Circuito II: Potência na fonte = {moduloSf1[0][0]/1000:.4f} kVA, Fase = {faseSf1[0][0]:.2f}°")
print(f"Circuito II: Potência na fonte = {moduloSf1[1][0]/1000:.4f} kVA, Fase = {faseSf1[1][0]:.2f}°")
print(f"Circuito II: Potência na fonte = {moduloSf1[2][0]/1000:.4f} kVA, Fase = {faseSf1[2][0]:.2f}°\n")

Pl2 = casos[1].get_potencia_linha()
print(f"Circuito II: Potência na linha = {Pl2[0][0]/1000:.4f} kW, ")
print(f"Circuito II: Potência na linha = {Pl2[1][0]/1000:.4f} kW, ")
print(f"Circuito II: Potência na linha = {Pl2[2][0]/1000:.4f} kW, \n")

Sc2 = casos[1].get_potencia_carga()
moduloSc2 = np.abs(Sc2)
faseSc2 = np.angle(Sc2, deg=True)
print(f"Circuito II: Potência na carga = {moduloSc2[0][0]/1000:.4f} kVA, Fase = {faseSc2[0][0]:.2f}° | {Sc2[0][0]/1000:.4f} kVA")
print(f"Circuito II: Potência na carga = {moduloSc2[1][0]/1000:.4f} kVA, Fase = {faseSc2[1][0]:.2f}° | {Sc2[1][0]/1000:.4f} kVA")
print(f"Circuito II: Potência na carga = {moduloSc2[2][0]/1000:.4f} kVA, Fase = {faseSc2[2][0]:.2f}° | {Sc2[2][0]/1000:.4f} kVA\n")

C2, Xc2 = casos[1].capacitor()
print(f"Circuito II: Capacitor necessário para correção do fator de potência = {C2[0][0]*1e6:.4f} μF\n")

Pl2_1, Pl2_1t, i2 = casos[1].potencia_linha_capacitor()
moduloPl2_1 = np.abs(Pl2_1)
fasePl2_1 = np.angle(Pl2_1, deg=True)
print(f"Circuito II: Potência na linha com capacitor = {moduloPl2_1[0][0]/1000:.4f} kW,") 
print(f"Circuito II: Potência na linha com capacitor = {moduloPl2_1[1][0]/1000:.4f} kW,")
print(f"Circuito II: Potência na linha com capacitor = {moduloPl2_1[2][0]/1000:.4f} kW,\n")
print(f"Circuito II: Potência total na linha com capacitor = {Pl2_1t/1000:.4f} kW\n")
print("=====================================================\n")

for i in casos: 
    del i # deleta cada caso

casos.clear() # limpa o vetor de casos para a proxima questao


# ============= Questão 2. =============

casos.append(Circuito.questao_2(fonte= fontes[0], linha= linhas[1], carga1= cargas[0], nome= "2.I"))
circuito2I = casos[0].correntes_linha2()
modulo2I = np.abs(circuito2I)
fase2I = np.angle(circuito2I, deg=True)
print(f"Circuito 2.I: Corrente na linha  : Módulo = {modulo2I[0][0]:.4f} A, Fase = {fase2I[0][0]:.2f}°")
print(f"Circuito 2.I: Corrente na linha  : Módulo = {modulo2I[1][0]:.4f} A, Fase = {fase2I[1][0]:.2f}°")
print(f"Tensão de deslocamento do neutro : Módulo = {modulo2I[2][0]:.4f} V, Fase = {fase2I[2][0]:.2f}°\n")

T2I = casos[0].get_tensoes_fase()
moduloT2I = np.abs(T2I)
faseT2I = np.angle(T2I, deg=True)
print(f"Circuito 2.I: Tensão na carga A  : Módulo = {moduloT2I[0][0]/1000:.4f} kV, Fase = {faseT2I[0][0]:.2f}°")
print(f"Circuito 2.I: Tensão na carga C  : Módulo = {moduloT2I[1][0]/1000:.4f} kV, Fase = {faseT2I[1][0]:.2f}°\n")

Sf2I = casos[0].get_potencia_fonte()
moduloSf2I = np.abs(Sf2I)
faseSf2I = np.angle(Sf2I, deg=True)
print(f"Circuito 2.I: Potência na fonte = {moduloSf2I[0][0]/1000:.4f} kVA, Fase = {faseSf2I[0][0]:.2f}°")
print(f"Circuito 2.I: Potência na fonte = {moduloSf2I[1][0]/1000:.4f} kVA, Fase = {faseSf2I[1][0]:.2f}°")
print(f"Circuito 2.I: Potência na fonte = {moduloSf2I[2][0]/1000:.4f} kVA, Fase = {faseSf2I[2][0]:.2f}°\n")

ScI = casos[0].get_potencia_carga()
moduloScI = np.abs(ScI)
faseScI = np.angle(ScI, deg=True)
print(f"Circuito 2.I: Potência na carga = {moduloScI[0][0]/1000:.4f} kVA, Fase = {faseScI[0][0]:.2f}° | {ScI[0][0]/1000:.4f} kVA")
print(f"Circuito 2.I: Potência na carga = {moduloScI[1][0]/1000:.4f} kVA, Fase = {faseScI[1][0]:.2f}° | {ScI[1][0]/1000:.4f} kVA")
print(f"Circuito 2.I: Potência na carga = {moduloScI[2][0]/1000:.4f} kVA, Fase = {faseScI[2][0]:.2f}° | {ScI[2][0]/1000:.4f} kVA\n")

print("=====================================================\n")

casos.append(Circuito.questao_2(fonte= fontes[0], linha= linhas[1], carga1 = cargas[2], nome= "2.II"))
circuito2II = casos[1].correntes_linha2()
modulo2II = np.abs(circuito2II)
fase2II = np.angle(circuito2II, deg=True)
print(f"Circuito 2.II: Corrente na Fase A : Módulo = {modulo2II[0][0]:.4f} A, Fase = {fase2II[0][0]:.2f}°")
print(f"Circuito 2.II: Corrente na Fase C : Módulo = {modulo2II[1][0]:.4f} A, Fase = {fase2II[1][0]:.2f}°")
print(f"Tensão de deslocamento do neutro  : Módulo = {modulo2II[2][0]:.4f} V, Fase = {fase2II[2][0]:.2f}°\n")

T2II = casos[1].get_tensoes_fase()
moduloT2II = np.abs(T2II)  
faseT2II = np.angle(T2II, deg=True)
print(f"Circuito 2.II: Tensão na carga A  : Módulo = {moduloT2II[0][0]/1000:.4f} kV, Fase = {faseT2II[0][0]:.2f}°")
print(f"Circuito 2.II: Tensão na carga C  : Módulo = {moduloT2II[1][0]/1000:.4f} kV, Fase = {faseT2II[1][0]:.2f}°\n")

Sf2II = casos[1].get_potencia_fonte()
moduloSf2II = np.abs(Sf2II)
faseSf2II = np.angle(Sf2II, deg=True)
print(f"Circuito 2.II: Potência na fonte = {moduloSf2II[0][0]/1000:.4f} kVA, Fase = {faseSf2II[0][0]:.2f}°")
print(f"Circuito 2.II: Potência na fonte = {moduloSf2II[1][0]/1000:.4f} kVA, Fase = {faseSf2II[1][0]:.2f}°")
print(f"Circuito 2.II: Potência na fonte = {moduloSf2II[2][0]/1000:.4f} kVA, Fase = {faseSf2II[2][0]:.2f}°\n")

ScII = casos[1].get_potencia_carga()
moduloScII = np.abs(ScII)   
faseScII = np.angle(ScII, deg=True)
print(f"Circuito 2.II: Potência na carga = {moduloScII[0][0]/1000:.4f} kVA, Fase = {faseScII[0][0]:.2f}° | {ScII[0][0]/1000:.4f} kVA")
print(f"Circuito 2.II: Potência na carga = {moduloScII[1][0]/1000:.4f} kVA, Fase = {faseScII[1][0]:.2f}° | {ScII[1][0]/1000:.4f} kVA")
print(f"Circuito 2.II: Potência na carga = {moduloScII[2][0]/1000:.4f} kVA, Fase = {faseScII[2][0]:.2f}° | {ScII[2][0]/1000:.4f} kVA\n")

print("=====================================================\n")

casos.append(Circuito.questao_2(fonte= fontes[0], linha= linhas[0], carga1 = cargas[1], nome= "2.III"))
circuito2III = casos[2].correntes_linha2()
modulo2III = np.abs(circuito2III)
fase2III = np.angle(circuito2III, deg=True)
print(f"Circuito 2.III: Corrente na Fase A : Módulo = {modulo2III[0][0]:.4f} A, Fase = {fase2III[0][0]:.2f}°")
print(f"Circuito 2.III: Corrente na Fase C : Módulo = {modulo2III[1][0]:.4f} A, Fase = {fase2III[1][0]:.2f}°")
print(f"Circuito 2.III: Corrente de neutro : Módulo = {modulo2III[2][0]:.4f} A, Fase = {fase2III[2][0]:.2f}°\n")

T2III = casos[2].get_tensoes_fase()
moduloT2III = np.abs(T2III)
faseT2III = np.angle(T2III, deg=True)
print(f"Circuito 2.III: Tensão na carga A  : Módulo = {moduloT2III[0][0]/1000:.4f} kV, Fase = {faseT2III[0][0]:.2f}°")
print(f"Circuito 2.III: Tensão na carga C  : Módulo = {moduloT2III[1][0]/1000:.4f} kV, Fase = {faseT2III[1][0]:.2f}°\n")

Sf2III = casos[2].get_potencia_fonte()
moduloSf2III = np.abs(Sf2III) 
faseSf2III = np.angle(Sf2III, deg=True)
print(f"Circuito 2.III: Potência na fonte = {moduloSf2III[0][0]/1000:.4f} kVA, Fase = {faseSf2III[0][0]:.2f}°")
print(f"Circuito 2.III: Potência na fonte = {moduloSf2III[1][0]/1000:.4f} kVA, Fase = {faseSf2III[1][0]:.2f}°")
print(f"Circuito 2.III: Potência na fonte = {moduloSf2III[2][0]/1000:.4f} kVA, Fase = {faseSf2III[2][0]:.2f}°\n")

ScIII = casos[2].get_potencia_carga()
moduloScIII = np.abs(ScIII)
faseScIII = np.angle(ScIII, deg=True)
print(f"Circuito 2.III: Potência na carga = {moduloScIII[0][0]/1000:.4f} kVA, Fase = {faseScIII[0][0]:.2f}° | {ScIII[0][0]/1000:.4f} kVA")
print(f"Circuito 2.III: Potência na carga = {moduloScIII[1][0]/1000:.4f} kVA, Fase = {faseScIII[1][0]:.2f}° | {ScIII[1][0]/1000:.4f} kVA")
print(f"Circuito 2.III: Potência na carga = {moduloScIII[2][0]/1000:.4f} kVA, Fase = {faseScIII[2][0]:.2f}° | {ScIII[2][0]/1000:.4f} kVA\n")

print("=====================================================\n")

for i in casos: 
    del i # deleta cada caso

casos.clear() # limpa o vetor de casos para a proxima questao

'''

# ============= Questão 3. =============

casos.append(Circuito.questao_3(fonte= fontes[2], linha= linhas[1], carga= cargas[3], nome= "3.I"))
circuito3I = casos[0].correntes_linha3()
modulo3I = np.abs(circuito3I)
fase3I = np.angle(circuito3I, deg=True)
print(f"Circuito 3.I: Corrente na linha A     : Módulo = {modulo3I[0][0]:.4f} A, Fase = {fase3I[0][0]:.2f}°")
print(f"Circuito 3.I: Corrente na linha B     : Módulo = {modulo3I[1][0]:.4f} A, Fase = {fase3I[1][0]:.2f}°")
print(f"Circuito 3.I: Corrente na linha C     : Módulo = {modulo3I[2][0]:.4f} A, Fase = {fase3I[2][0]:.2f}°")
print(f"Circuito 3.I: Corrente de aterramento : Módulo = {modulo3I[3][0]:.4f} A, Fase = {fase3I[3][0]:.2f}°\n")

T3I = casos[0].get_tensoes_fase()
moduloT3I = np.abs(T3I)
faseT3I = np.angle(T3I, deg=True)
print(f"Circuito 3.I: Tensão na carga A  : Módulo = {moduloT3I[0][0]/1000:.4f} kV, Fase = {faseT3I[0][0]:.2f}°")
print(f"Circuito 3.I: Tensão na carga B  : Módulo = {moduloT3I[1][0]/1000:.4f} kV, Fase = {faseT3I[1][0]:.2f}°")
print(f"Circuito 3.I: Tensão na carga C  : Módulo = {moduloT3I[2][0]/1000:.4f} kV, Fase = {faseT3I[2][0]:.2f}°")
print(f"Circuito 3.I: Tensão de aterramento : Módulo = {moduloT3I[3][0]:.4f} kV, Fase = {faseT3I[3][0]:.2f}°\n")

Sf3I = casos[0].get_potencia_fonte()
moduloSf3I = np.abs(Sf3I)
faseSf3I = np.angle(Sf3I, deg=True)
print(f"Circuito 3.I: Potência na fonte = {moduloSf3I[0][0]/1000:.4f} kVA, Fase = {faseSf3I[0][0]:.2f}°")
print(f"Circuito 3.I: Potência na fonte = {moduloSf3I[1][0]/1000:.4f} kVA, Fase = {faseSf3I[1][0]:.2f}°")
print(f"Circuito 3.I: Potência na fonte = {moduloSf3I[2][0]/1000:.4f} kVA, Fase = {faseSf3I[2][0]:.2f}°\n")

Sc3I = casos[0].get_potencia_carga()
moduloSc3I = np.abs(Sc3I)
faseSc3I = np.angle(Sc3I, deg=True)
print(f"Circuito 3.I: Potência na carga = {moduloSc3I[0][0]/1000:.4f} kVA, Fase = {faseSc3I[0][0]:.2f}° | {Sc3I[0][0]/1000:.4f} kVA")
print(f"Circuito 3.I: Potência na carga = {moduloSc3I[1][0]/1000:.4f} kVA, Fase = {faseSc3I[1][0]:.2f}° | {Sc3I[1][0]/1000:.4f} kVA")
print(f"Circuito 3.I: Potência na carga = {moduloSc3I[2][0]/1000:.4f} kVA, Fase = {faseSc3I[2][0]:.2f}° | {Sc3I[2][0]/1000:.4f} kVA\n")

print("=====================================================\n")

casos.append(Circuito.questao_3(fonte= fontes[1], linha= linhas[1], carga= cargas[3], nome= "3.II"))
circuito3II = casos[1].correntes_linha3()
modulo3II = np.abs(circuito3II)
fase3II = np.angle(circuito3II, deg=True)
print(f"Circuito 3.II: Corrente na linha A     : Módulo = {modulo3II[0][0]:.4f} A, Fase = {fase3II[0][0]:.2f}°")
print(f"Circuito 3.II: Corrente na linha B     : Módulo = {modulo3II[1][0]:.4f} A, Fase = {fase3II[1][0]:.2f}°")
print(f"Circuito 3.II: Corrente na linha C     : Módulo = {modulo3II[2][0]:.4f} A, Fase = {fase3II[2][0]:.2f}°")
print(f"Circuito 3.II: Corrente de aterramento : Módulo = {modulo3II[3][0]:.4f} A, Fase = {fase3II[3][0]:.2f}°\n")

T3II = casos[1].get_tensoes_fase()
moduloT3II = np.abs(T3II)
faseT3II = np.angle(T3II, deg=True)
print(f"Circuito 3.II: Tensão na carga A  : Módulo = {moduloT3II[0][0]/1000:.4f} kV, Fase = {faseT3II[0][0]:.2f}°")
print(f"Circuito 3.II: Tensão na carga B  : Módulo = {moduloT3II[1][0]/1000:.4f} kV, Fase = {faseT3II[1][0]:.2f}°")
print(f"Circuito 3.II: Tensão na carga C  : Módulo = {moduloT3II[2][0]/1000:.4f} kV, Fase = {faseT3II[2][0]:.2f}°")
print(f"Circuito 3.II: Tensão de aterramento : Módulo = {moduloT3II[3][0]:.4f} kV, Fase = {faseT3II[3][0]:.2f}°\n")

Sf3II = casos[1].get_potencia_fonte()
moduloSf3II = np.abs(Sf3II)
faseSf3II = np.angle(Sf3II, deg=True)
print(f"Circuito 3.II: Potência na fonte = {moduloSf3II[0][0]/1000:.4f} kVA, Fase = {faseSf3II[0][0]:.2f}°")
print(f"Circuito 3.II: Potência na fonte = {moduloSf3II[1][0]/1000:.4f} kVA, Fase = {faseSf3II[1][0]:.2f}°")
print(f"Circuito 3.II: Potência na fonte = {moduloSf3II[2][0]/1000:.4f} kVA, Fase = {faseSf3II[2][0]:.2f}°\n")

Sc3II = casos[1].get_potencia_carga()
moduloSc3II = np.abs(Sc3II)
faseSc3II = np.angle(Sc3II, deg=True)
print(f"Circuito 3.II: Potência na carga = {moduloSc3II[0][0]/1000:.4f} kVA, Fase = {faseSc3II[0][0]:.2f}° | {Sc3II[0][0]/1000:.4f} kVA")
print(f"Circuito 3.II: Potência na carga = {moduloSc3II[1][0]/1000:.4f} kVA, Fase = {faseSc3II[1][0]:.2f}° | {Sc3II[1][0]/1000:.4f} kVA")
print(f"Circuito 3.II: Potência na carga = {moduloSc3II[2][0]/1000:.4f} kVA, Fase = {faseSc3II[2][0]:.2f}° | {Sc3II[2][0]/1000:.4f} kVA\n")

print("=====================================================\n")

for i in casos: 
    del i # deleta cada caso

casos.clear() # limpa o vetor de casos para a proxima questao