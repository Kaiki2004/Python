def compara(v1,v2):
  if v1 < v2:
    x = v1
    return x
  elif v1 > v2:
    x = v2
    return x
  else:
    return "os dois valores são iguais"

x1 = int(input('informe um valor '))
x2 = int(input('informe outro valor '))
res = compara(x1,x2)
print(res)

