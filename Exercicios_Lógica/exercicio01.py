vet = []
soma = 0
n = int(input('informe o tamanho o vetor '))
for i in range(n):
  vet.append(int(input('informe um número ')))
  soma = soma + vet[i]

print(f'a soma do vetor é: {soma}')