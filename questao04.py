matriz = [ 
    [8,0,7],
    [4,5,6],
    [3,10,2]      
          ]

def verificarQuadradoMagico(matriz):
    n = len(matriz) 
    somaQuadrado = (n * (n**2 + 1)) // 2 
    verificado = False 
# explicando
        # for l in range(len(matriz))
            # for c in range(len(matriz))   
        # interage em cada linha das colunas 
        #    C(0)(0)(0)
        # l(0)[8][0][7] => 8 + 0 + 7 = 15  
        #   C (1)(1)(1)
        # l(1)[4][5][6] => 4 + 5 + 6 = 15
        # # C (2) (2) (2) 
        # l(2)[3][10][2] = > 2 + 3 + 10 = 15
# explicando
        # for c in range(len(matriz))
            # for l in range(len(matriz) )   
        # interage em cada linha das colunas 
        #    C(0)(1)(2)
        # l(0)[8][0][7]        
        # l(1)[4][5][6] 
        # l(2)[3][10][2]
        #  C(0)l(0) + C(0)L(1) +c(0)(2) = 8 + 4 + 3 = 15
        #  C(1)l(0) + C(1)L(1) +c(1)(2) = 4 + 5 + 3 = 15
         # C(2)l(0) + C(2)L(1) +c(2)(2) = 2 + 3 + 10 = 15
   
    for l in range(n): 
        soma = 0 
        for c in range(n):
           soma += matriz[l][c] 
        if soma != somaQuadrado:
            verificado = False 
            break
        else:
            verificado = True
            
    if verificado:
        for c in range(n):
            soma = 0
            for l in range(n):
                soma += matriz[l][c]
            if soma != somaQuadrado:
                    verificado = False
                    break 
            else:
                    verificado = True                     
    if verificado: 
        SomaDiagonal = 0
        for d in range(n):
            SomaDiagonal += matriz[d][d]
        if SomaDiagonal != somaQuadrado:
              verificado = False
      
        else:
              verificado = True
                
    if verificado:
        SomaDiagonalSecundaria = 0
        for d in range(n):
            SomaDiagonalSecundaria += matriz[d][n-1-d]
        if SomaDiagonalSecundaria != somaQuadrado:
              verificado = False
                
        else:
              verificado = True
              
                
    if verificado:
        print("A matriz é um quadrado mágico.")
    else:
        print("A matriz não é um quadrado mágico.")
                    
            
                               
            
              
                  
verificarQuadradoMagico(matriz)                  
for i in range(len(matriz)):
    print(matriz[i])               
                
    