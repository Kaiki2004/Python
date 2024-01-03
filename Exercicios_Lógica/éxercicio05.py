vet1 = []
vet2 = []
soma = []

for i in range(50):
  vet1.append(int(input('informe um número para o vetor 1 ')))
  vet2.append(int(input('informe um número para o vetor 2 ')))

for i in range(50):
    soma.append(vet1[i] + vet2[i])

print(f' A soma {soma}')