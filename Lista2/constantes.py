import numpy as np
import math

# ============= Definicao do número complexo α =============
α = complex(np.cos(2*np.pi/3), np.sin(2*np.pi/3))
#print(f'O número complexo α é: {α:.3f}')

# ============= Definicao das sequências positivas e negativas ============= 
np.set_printoptions(precision=3)
SEQ_POS = np.array([[1], 
                    [α ** 2], 
                    [α]])

SEQ_NEG = np.array([[1], 
                    [α], 
                    [α ** 2]])

# ============= Valores Constantes =============
# Fonte
# Fonte 1: sequencia positiva, em estrela e V_an = 6350 ∠ 10
V1 = complex(6350 * np.cos(np.deg2rad(10)), 6350 * np.sin(np.deg2rad(10)))
FONTE1 = V1 * SEQ_POS

# Fonte 2: sequencia negativa, em delta e V_ab = 13800 ∠ 50
V2 = complex((13800 / math.sqrt(3)) * np.cos(np.deg2rad(50 - 30)), (13800 / math.sqrt(3)) * np.sin(np.deg2rad(50 - 30))) # já transformada em estrela
FONTE2 = V2 * SEQ_NEG
FONTE2_DELTA = complex((13800) * np.cos(np.deg2rad(50)), (13800) * np.sin(np.deg2rad(50))) * SEQ_NEG

# Fonte 3: sequencia positiva, em estrela e V_an = 6600 ∠ 15
V3 = complex(6600 * np.cos(np.deg2rad(15)), 6600 * np.sin(np.deg2rad(15))) 
FONTE3 = V3 * SEQ_POS

# Linhas 
# Linha 1: sem mútuas
L1 = 2.5 #[Km]
Z_P1 = (0.15 + 1j*0.2) * L1 # Impedância própria da linha 1 [Ω]

# Linha 2: mútuas iguais entre fases
L2 = 4.0 #[Km]
Z_P2 = (0.2 + 1j*0.35) * L2 # Impedância própria da linha 2 [Ω]
Z_M2 = (0.09 * 1j) * L2 # Impedância mútua da linha 2 [Ω]

# Impedância por Fase
# Carga 1: ligação estrela isolada
Z1 = 18 + 6 *1j #[Ω]
# Carga 2: ligação estrela aterrada
Z2 = 12 - 4 *1j #[Ω]
# Carga 3: ligação delta
Z3 = 20 / 3 # transformado em estrela