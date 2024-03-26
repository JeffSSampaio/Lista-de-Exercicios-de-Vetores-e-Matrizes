from random import randint
linha = 3
coluna = 3
jogoDaVelha = [0] * linha
jogadorX = 1 
coordenadas = []
jogadorY = -1
pontuacao = []
for l in range(len(jogoDaVelha)):
    jogoDaVelha[l] = [0] * coluna
  
def imprimirTabuleiro():
    for l in range(len(jogoDaVelha)):
        print(jogoDaVelha[l]) 
        
def verificarGanhador():
     n = len(jogoDaVelha)
     verificado = False 
     
     for l in range(n): 
        for c in range(n):   
         if jogoDaVelha[l] == 1:
            print(f"\nJogador Y ganhou!!!! ")
            imprimirTabuleiro()
            verificado = True
            break
         elif jogoDaVelha[l] == -1:
            print(f"\nJogador X ganhou!!!! ")
            imprimirTabuleiro()
            verificado = True
            break    
         else:
            verificado = False
            break
            
     if verificado:
        for c in range(n):
            soma = 0
        for l in range(n):
         if jogoDaVelha[l] == 1:
            print(f"\nJogador Y ganhou!!!! ")
            imprimirTabuleiro()
            verificado = True
            break
         elif jogoDaVelha[l] == -1:
            print(f"\nJogador X ganhou!!!! ")
            imprimirTabuleiro()
            verificado = True
            break    
         else:
            verificado = False
            break
                         
     if verificado: 
        for d in range(n):
            if jogoDaVelha[l][l] == 1:
               print(f"\nJogador Y ganhou!!!! ")
               imprimirTabuleiro()
               verificado = True
               break
            elif jogoDaVelha[l][l] == -1:
               print(f"\nJogador X ganhou!!!! ")
               imprimirTabuleiro()
               verificado = True
               break    
            else:
               verificado = False
               break
                
     if verificado:
        for d in range(n):     
          if jogoDaVelha[l][n-1-l] == 1:
            print(f"\nJogador Y ganhou!!!! ")
            imprimirTabuleiro()
            verificado = True
            break
          elif jogoDaVelha[l][n-1-l] == -1:
            print(f"\nJogador X ganhou!!!! ")
            imprimirTabuleiro()
            verificado = True
            break    
          else:
            verificado = False
            break  

def inserirPosicao(vez): 
    for i in range(1):
     linha = int(input("Digite a linha da coordenada que deseje inserir : "))
     coluna = int(input("Digite a coluna da coordenada que deseje inserir: "))
     coordenadas.append((linha, coluna)) 
    for coord in coordenadas:
     linha, coluna = coord 
    
     if 0 <= linha < len(jogoDaVelha) and 0 <= coluna < len(jogoDaVelha[0]):
        if vez == 1:
         jogoDaVelha[linha][coluna] = 1
         valor = jogoDaVelha[linha][coluna]
         print(f"Coordenada ({linha}, {coluna}): {valor}")
         imprimirTabuleiro()
         vez = randint(-1,1)
         return vez
        elif vez == -1:
         jogoDaVelha[linha][coluna] = -1
         valor = jogoDaVelha[linha][coluna]
         print(f"Coordenada ({linha}, {coluna}): {valor}")
         imprimirTabuleiro()
         vez = randint(-1,1)
         return vez
         
     else:
       print(f"Não é possivel encontrar coordenadas ({linha,coluna}) no Tabuleiro") 
def jogar():
   imprimirTabuleiro()
   while True:
    vez = randint(-1,1)
    if vez == 1:
        print("Jogador X, sua vez")
        inserirPosicao(1)
        verificarGanhador()
    elif vez == -1:
            print("Jogador Y, sua vez:\n")
            inserirPosicao(-1)
            verificarGanhador()
    else:
         break
                     
   
       
jogar()    
    
          