from random import randint

def verificarValor(matriz,valor):
  result = 0
  for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c] == valor:
        result = 1
  return result

linha = 5
coluna = 5

matriz = [0] * linha
for l in range(len(matriz)):
  matriz[l] = [0] * coluna
  
for l in range(len(matriz)):
  for c in range(len(matriz[l])):
      valor = randint(0,99)
      if verificarValor(matriz,valor) == 0:
          matriz[l][c] = valor
      else:
       print("Valor ja inserido:", valor)
       valor = randint(0, 99)
       while verificarValor(matriz, valor) == 1:
        valor = randint(0, 99)
      matriz[l][c] = valor    

for l in range(len(matriz)):
    print(matriz[l])        