aH, aM, bH, bM = map(int, input().split())

if aH > bH:
    horas = (24 - aH) + bH
    if aM > bM:
        minutos = (60 - aM) + bM
if bH > aH:
    #horas = bH - aH
    if bM > aM:
        horas -= 1
        minutos = (60 - aM) + bM
elif aH == bH:
    horas = 24
    if aM == aM:
        minutos = 0

print("O JOGO DUROU {} HORAS(S) e {} MINUTO(S)".format(horas, minutos))



