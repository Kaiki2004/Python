def somatorio (n):
  s = 1
  for i in range(2,n+1,1):
    s = s + (i/(i*i))
  return s

n = int(input("escreva um número "))
result = somatorio(n)
print(result)