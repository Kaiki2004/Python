from random import randint
def soma(vet):
  soma = 0
  for i in range(n):
    soma = vet[i] + soma
  return soma

def media(res):
  med = res/n
  return med

vet = []
n = int(input('informe um tamanho '))

for i in range(n):
  vet.append(randint(1,100))

res = soma(vet)
result = media(res)

print(vet)
print(res)
print(result)