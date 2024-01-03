from random import randint

def maior(v):
  maior = v[0]
  for i in range(n):
    if maior < v[i]:
     maior = v[i]
  return maior

n = int(input("escreva um número "))
v = []

for i in range(n):
  v.append(randint(1,10))

resut = maior(v)
print(v)
print(resut)