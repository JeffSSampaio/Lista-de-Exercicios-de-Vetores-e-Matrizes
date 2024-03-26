from random import randint
linha = 3
coluna = 3
jogoDaVelha = [0] * linha
for l in range(len(jogoDaVelha)):
    jogoDaVelha[l] = [0] * coluna
  
def imprimirTabuleiro():
    for l in range(len(jogoDaVelha)):
        print(jogoDaVelha[l]) 
        
def verificarGanhador():
    for i in range(3):
        if jogoDaVelha[i][0] == jogoDaVelha[i][1] == jogoDaVelha[i][2] != 0 or \
           jogoDaVelha[0][i] == jogoDaVelha[1][i] == jogoDaVelha[2][i] != 0:
            return True


    if jogoDaVelha[0][0] == jogoDaVelha[1][1] == jogoDaVelha[2][2] != 0 or \
       jogoDaVelha[0][2] == jogoDaVelha[1][1] == jogoDaVelha[2][0] != 0:
        return True

    return False

def inserirPosicao(linha,coluna,valor): 
       if 0 <= linha < len(jogoDaVelha) and 0 <= coluna < len(jogoDaVelha[0]):
          jogoDaVelha[linha][coluna] = valor
          return True
       return False    
       
def jogar():
   vez = randint(0,1)
   jogador_atual = 1 if vez == 0 else 1
   while True:
     imprimirTabuleiro()
     print(f"Jogador {jogador_atual} sua vez:")
     linha = int(input("Digite a linha da coordenada que deseje inserir : "))
     coluna = int(input("Digite a coluna da coordenada que deseje inserir: "))
     if inserirPosicao(linha,coluna,jogador_atual):
        ganhador = verificarGanhador()
        if ganhador != False:
          imprimirTabuleiro()
          print(f"Jogador {jogador_atual} ganhou!")
          break
        jogador_atual = -jogador_atual  
     else:
          print("Posição invalida")

                     
   
       
jogar()    
    
          
