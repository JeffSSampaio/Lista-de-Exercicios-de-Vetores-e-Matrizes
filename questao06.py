matriz = [[0,15,30,5,12],
          [15,0,10,17,28],
          [30,10,0,3,11],
          [5,17,3,0,80],
          [12,28,11,80,0]
          ]



soma = 0
coordenadas = [] 
for i in range(6):
    linha = int(input("Digite a linha da coordenada: "))
    coluna = int(input("Digite a coluna da coordenada: "))
    coordenadas.append((linha, coluna)) 


print("Valores correspondentes na matriz:")
for coord in coordenadas:
    linha, coluna = coord 
    
    if 0 <= linha < len(matriz) and 0 <= coluna < len(matriz[0]):
      valor = matriz[linha][coluna]
      soma += valor
      print(f"Coordenada ({linha}, {coluna}): {valor}")
    else:
       print(f"Não é possivel encontrar coordenadas ({linha,coluna}) na matriz")

print(f"Total = {soma}")
   

   

       
     
         
            
             