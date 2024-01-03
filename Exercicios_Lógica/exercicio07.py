vet = [1,1]
n = int(input('informe a quantidade '))
for i in range(n):
  vet.append(vet[i] + vet[i + 1])
print(vet)