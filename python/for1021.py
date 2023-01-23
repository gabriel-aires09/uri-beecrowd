valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS")
for i in notas:
    calculo = int(valor // i)
    valor -= calculo * i
    print('{} nota(s) de R$ {:.2f}'.format(calculo, i))

print("MOEDAS")
for j in moedas:
    valor = round(valor, 2)
    moeda = int(valor / j)
    valor -= moeda * j
    print('{} moeda(s) de R$ {:.2f}'.format(moeda, j))


