cedula = int(input())
valor = cedula // 100
print('{} nota(s) de R$ 100,00'.format(valor))

cedula = cedula - (valor * 100)
valor = cedula // 50
print('{} nota(s) de R$ 50,00'.format(valor))

cedula = cedula - (valor * 50)
valor = cedula // 20
print('{} nota(s) de R$ 20,00'.format(valor))

cedula = cedula - (valor * 20)
valor = cedula // 10
print('{} nota(s) de R$ 10,00'.format(valor))

cedula = cedula - (valor * 10)
valor = cedula // 5
print('{} nota(s) de R$ 5,00'.format(valor))

cedula = cedula - (valor * 5)
valor = cedula // 2
print('{} nota(s) de R$ 2,00'.format(valor))

cedula = cedula - (valor * 2)
valor = cedula // 1
print('{} nota(s) de R$ 1,00'.format(valor))
