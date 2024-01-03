from contextlib import nullcontext
def cont(i,v):
  cont = 0
  for c in v:
    if i == c:
      cont += 1
  return cont

def moda(v):
  maior = 0
  block = False
  elemento = 0
  for i in v:
    x = cont(i,v)
    if x == maior and elemento != i:
      block = True
    elif x > maior:
      block = False
      maior = x
      elemento = i
    print(block,maior,elemento)
  if block == True:
      return "não existe moda"
  else:
    return elemento
n = int(input('escreva o tamanho do vetor '))
v = []
for i in range(n):
  v.append(int(input('escreva um número para o vetor ')))


result = moda(v)
print(v)
print(f'a moda é:', result)