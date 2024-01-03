vet = []
for i in range(100):
  vet.append(int(input('informe um número ')))
  if(vet[i] %2 == 0):
    vet[i] = 1
  else:
    vet[i] = 0

print(vet)
