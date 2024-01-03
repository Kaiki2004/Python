from random import randint
vet = []
vpar = []
vimpar = []
n = 20
for i in range(n):
  vet.append(randint(1,100))
for i in range(n):
  if vet[i] %2 == 0:
    vpar.append(vet[i])
  else:
    vimpar.append(vet[i])
print(vet)
print(vpar)
print(vimpar)