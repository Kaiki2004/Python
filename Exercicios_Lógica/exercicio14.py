from random import randint

def media(vet):
  soma = 0
  cont = 0
  for i in range(n):
    if i %2 != 0:
      soma = soma + vet[i]
      cont = cont + 1
  return soma/cont
vet = []
n = int(input("escreva um número "))

for i in range(n):
  vet.append(randint(1,10))


result = media(vet)

print(vet)
print(result)