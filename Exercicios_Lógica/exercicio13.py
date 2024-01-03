from random import randint

def menor(v):
  menor = v[0]
  for i in range(n):
    if menor > v[i]:
     menor = v[i]
  return menor

n = int(input("escreva um número "))
v = []

for i in range(n):
  v.append(randint(1,10))

resut = menor(v)
print(v)
print(resut)