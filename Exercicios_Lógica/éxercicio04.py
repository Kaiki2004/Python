vet = []
mult = []
for i in range(10):
  vet.append(int(input('informe um número ')))

for i in range(10):
  mult.append(vet[i]*3)

for i in range (10):
  print(f'a multiplicação de cada posição é {mult[i]}')
