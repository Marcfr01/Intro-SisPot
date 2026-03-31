import numpy as np
import math

# ============= Definicao do número complexo α =============
α = complex(np.cos(2*np.pi/3), np.sin(2*np.pi/3))
#print(f'O número complexo α é: {α:.3f}')
#print()

# ============= Definicao das sequências positivas e negativas ============= 
np.set_printoptions(precision=3)
SEQ_POS = np.array([[1], 
                    [α ** 2], 
                    [α]])

SEQ_NEG = np.array([[1], 
                    [α], 
                    [α ** 2]])
#print('A sequência positiva é:')
#print(SEQ_POS)
#print()

#print('A sequência negativa é:')
#print(SEQ_NEG)
#print()

# ============= Valores Constantes =============
# Fonte
# Fonte 1: sequencia positiva, em estrela e V_an = 6350 ∠ 10
V1 = complex(6350 * np.cos(np.deg2rad(10)), 6350 * np.sin(np.deg2rad(10)))
FONTE1 = V1 * SEQ_POS
#print('A matriz que determina a fonte 1 é: ')
#print(FONTE1)
#print()
#print(f'A tensão V_an da fonte 1 é: {FONTE1[0]} [V]')
#print(f'A tensão V_bn da fonte 1 é: {FONTE1[1]} [V]')
#print(f'A tensão V_cn da fonte 1 é: {FONTE1[2]} [V]')
#print()

# Fonte 2: sequencia negativa, em delta e V_ab = 13800 ∠ 50
V2 = complex((13800 / math.sqrt(3)) * np.cos(np.deg2rad(50 - 30)), (13800 / math.sqrt(3)) * np.sin(np.deg2rad(50 - 30))) # já transformada em estrela
FONTE2 = V2 * SEQ_NEG
FONTE2_DELTA = complex((13800) * np.cos(np.deg2rad(50)), (13800) * np.sin(np.deg2rad(50))) * SEQ_NEG
#print('A matriz que determina a fonte 2 é: ')
#print(FONTE2)
#print()
#print(f'A tensão V_an da fonte 2 é: {FONTE2[0]} [V]')
#print(f'A tensão V_bn da fonte 2 é: {FONTE2[1]} [V]')
#print(f'A tensão V_cn da fonte 2 é: {FONTE2[2]} [V]')
#print()

# Fonte 3: sequencia positiva, em estrela e V_an = 6600 ∠ 15
V3 = complex(6600 * np.cos(np.deg2rad(15)), 6600 * np.sin(np.deg2rad(15)))
FONTE3 = V3 * SEQ_POS

# Linhas 
# Linha 1: sem mútuas
L1 = 2.5 
Z_P1 = (0.15 + 1j*0.2) * L1
#print(f'A distância da linha 1 é: {L1} [Km]')
#print(f'A impedância própria da linha 1 é: {Z_P1} [Ω]')
#print()

# Linha 2: mútuas iguais entre fases
L2   = 4 
Z_P2 = (0.15 + 1j*0.2) * L2
Z_M2 = (0.09 * 1j) * L2
#print(f'A distância da linha 2 é: {L2} [Km]')
#print(f'A impedância própria da linha 2 é: {Z_P2} [Ω]')
#print(f'A indutância mútua da linha 2 é: {Z_M2} [Ω]')
#print()

# Impedância por Fase
# Carga 1: ligação estrela isolada
Z1 = 18 + 6 *1j
#print(f'A impedância da carga 1 é: {Z1} [Ω]')
#print()
# Carga 2: ligação estrela aterrada
Z2 = 12 - 4 *1j
#print(f'A impedância da carga 2 é: {Z2} [Ω]')
#print()
# Carga 3: ligação delta
Z3 = 20 / 3 # transformado em estrela
#print(f'A impedância da carga 3 é: {Z3} [Ω]')
#print()