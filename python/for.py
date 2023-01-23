entrada = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in notas:
    qtde_notas = int(entrada // i)
    entrada -= qtde_notas *  i
    print('{} nota(s) de R$ {:.2f}'.format(qtde_notas, i))

print("MOEDAS:")
for j in moedas:
    entrada = round(entrada, 2)
    qtde_moedas = int(entrada / j)
    entrada -= qtde_moedas * j
    print('{} moeda(s) de R$ {:.2f}'.format(qtde_moedas, j))
