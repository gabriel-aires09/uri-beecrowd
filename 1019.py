segundos = int(input())

# HORAS
conversaoHoras = segundos // 3600
segundosNovo = segundos - (3600 * conversaoHoras )

# MINUTOS
horasMinutos = segundosNovo // 60
minutosSegundos = segundosNovo - (60 * horasMinutos)

print("{}:{}:{}".format(conversaoHoras, horasMinutos, minutosSegundos))
