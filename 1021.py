#ENTRADA
valor = float(input())

#NOTA de 100
nota100 = valor // 100
n100 = valor - (nota100 * 100)

#NOTA de 50
nota50 = n100 // 50
n50 = n100 - (nota50 * 50)

#NOTA de 20
nota20 = n50 // 20
n20 = n50 - (nota20 * 20)

#NOTA de 10
nota10 = n20 // 10
n10 = n20 - (nota10 * 10)

#NOTA de 5
nota5 = n10 // 5
n5 = n10 - (nota5 * 5)

#NOTA de 2
nota2 = n5 // 2
n2 = n5 - (nota2 * 2)

#MOEDAS
#MOEDA de 1
moeda1 = n2 // 1
m1 = n2 - (moeda1 * 1)

#MOEDA de 0.50
moeda50 = m1 // 0.50
m_50 = m1 - (moeda50 * 0.50)

#MOEDA de 0.25
moeda25 = m_50 // 0.25
m_025 = m_50- (moeda25 * 0.25)

#MOEDA de 0.10
moeda10 = m_025 // 0.10
m_010 = m_025 - (moeda10 * 0.10)

#MOEDA de 0.05
moeda05 = m_010 // 0.05
m_05 = m_010 - (moeda05 * 0.05)

#MOEDA de 0.01
moeda01 = m_05 // 0.01
m_001 = m_05 - (moeda01 * 0.01)

#OUTPUT NOTAS
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(nota100)))
print("{} nota(s) de R$ 50.00".format(int(nota50)))
print("{} nota(s) de R$ 20.00".format(int(nota20)))
print("{} nota(s) de R$ 10.00".format(int(nota10)))
print("{} nota(s) de R$ 5.00".format(int(nota5)))
print("{} nota(s) de R$ 2.00".format(int(nota2)))

#OUTPUT MOEDAS
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(moeda1)))
print("{} moeda(s) de R$ 0.50".format(int(moeda50)))
print("{} moeda(s) de R$ 0.25".format(int(moeda25)))
print("{} moeda(s) de R$ 0.10".format(int(moeda10)))
print("{} moeda(s) de R$ 0.05".format(int(moeda05)))
print("{} moeda(s) de R$ 0.01".format(int(moeda01)))
