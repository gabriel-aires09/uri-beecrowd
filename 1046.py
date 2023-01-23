a, b = map(int, input().split())

if a > b:
    horas = (24 - a) + b
elif b > a:
    horas = b - a
elif a == b:
    horas = 24

print(f"O JOGO DUROU %.0f HORA(S)" % horas)
