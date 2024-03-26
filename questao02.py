vetor = []
y = 0
x = 0

for num in range(8):
     num = int(input("Digite um valor: "))
     vetor.append(num)
     
for interagerX in vetor:
     x += interagerX
for interagerY in vetor:
      y += interagerY

print(f"Sendo o Vetor : {vetor} ")
print(f"A soma de {x} + {y} = {x + y}")