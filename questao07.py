
linha = 5
coluna = 10
soma = 0
matriz = ['X'] * linha
nota = [float] * linha
gabarito =['B','C','D','A','E']

for l in range(len(matriz)):
    matriz[l] = ['X'] * coluna

for l in range(len(matriz)):
    print(f"Gabarito do {l+1}ºAluno {matriz[l]}")
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = input(F"{c+1}ºQUESTÃO\nMARCAR (A) (B) (C) (D) (E)\n").upper()

for l in range(len(matriz)):
    print(f"Gabarito do {l+1}ºAluno {matriz[l]}")
    
print("")    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == gabarito[c]:
            soma += 1
        nota[l] = soma
            
for l in range(len(matriz)):
    print(f"Nota do {l+1}ºAluno: {nota[l]}")   

    