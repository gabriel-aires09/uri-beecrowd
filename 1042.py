# ler os três valores
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

nova = [a, b, c]
sortNova = sorted(nova)

# ordenar os valores em ordem crescente
print(sortNova[0])
print(sortNova[1])
print(sortNova[2])
print()
print(a)
print(b)
print(c)
