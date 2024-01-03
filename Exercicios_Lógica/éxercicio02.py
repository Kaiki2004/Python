vet = []
media = 0
par = 0
cont = 0

n = int(input('informe o tamanho do vetor '))

for i in range(n):
  vet.append(int(input('informe um número ')))
  if(vet[i] %2 == 0):
    par = par + vet[i]
    cont = cont + 1

media = par/cont
print(f'a média dos números pares é: {media}')