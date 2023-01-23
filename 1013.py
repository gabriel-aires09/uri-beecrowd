VALOR = input().split(" ")
a, b, c = VALOR

split = VALOR
a = int(split[0])
b = int(split[1])
c = int(split[2])

MAIORAB = (a + b + abs(a - b))/ 2
MAIORAC = (a + c + abs(a - c)) / 2
MAIOR = (MAIORAB + MAIORAC + abs(MAIORAB - MAIORAC)) / 2
MAIOR = int(MAIOR)
print(f"{MAIOR} eh o maior")


