def soma(vet):
  s =0
  for i in range(5):
    s += vet[i]
  return s



vet = []
for i in range(5):
  vet.append(int(input('digite um número: ')))
resp = soma(vet)
print(f'a soma é: {resp}')