dias = int(input())

ano = dias // 365
diasAno = dias - (ano * 365)

mes = diasAno // 30
anoMes = diasAno - (mes * 30)

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(anoMes))

