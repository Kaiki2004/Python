def somatorio(n):
  x = 1
  for i in range(2,(n+1),1):
    x = x + (i/(i*i))
  return x

n = int(input('digite um número '))

resp = somatorio(n)
print(resp)
