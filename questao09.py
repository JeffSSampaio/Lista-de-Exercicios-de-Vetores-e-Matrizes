linha = 3
coluna = 3
soma_c = []

matriz = [int]* linha
for l in range(len(matriz)):
    matriz[l] = [int] * coluna
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = int(input(f"Digite {c+1}º valor: "))
        print(matriz[l])              

for c in range(len(matriz)):
    soma = 0
    for l in range(len(matriz)):
      soma += matriz[l][c]
    soma_c.append(soma)

for l in range(len(matriz)):
     print(matriz[l])

print(f"A soma das colunas é: {soma_c}")