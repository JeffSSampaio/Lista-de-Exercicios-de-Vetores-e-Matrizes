linha = 3
coluna =10
soma = 0
matriz = ['X'] * linha
nota = [float] * linha
gabarito =['B','C','D','A','E']
matricula = [] 
for l in range(len(matriz)):
    matriz[l] = ['X'] * coluna
    
for l in range(len(matriz)):
    print(f"Quadro de Respostas do {l+1}ºAluno {matriz[l]}")
for l in range(len(matriz)):
    alunoId = int(input(f"digite o numero de matricula do {l+1}ºAluno: "))
    matricula.append(alunoId)
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
    print(f"Nota do {l+1}ºAluno: {nota[l]} Matricula: {matricula[l]}") 
print(" ") 
print("RELAÇÂO GERAL DOS ALUNOS")         
for l in range(len(matriz)):
     if nota[l] >= 7.0:
        print(f"Nota do {l+1}ºAluno: {nota[l]} Matricula: {matricula[l]}\nStatus:Aprovação") 
     else:
        print(f"Nota do {l+1}ºAluno: {nota[l]} Matricula: {matricula[l]}\nStatus:Reprovação") 
        
   
    
        
