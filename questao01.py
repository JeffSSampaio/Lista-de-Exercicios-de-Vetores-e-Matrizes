inteiros = []
par = []
impares =  []

for cont in range(20):
    leia = int(input("Digite um numero:"))
    inteiros.append(leia)
    
for num in inteiros :
     if num % 2 == 0:
        par.append(num)
     else:
        impares.append(num)

print(f"Numeros Inteiros {inteiros}")        
print(f"Numeros PARES {par}")
print(f"Numero IMPARES {impares}")  
          