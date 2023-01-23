VENDEDOR = input()
SALARY = float(input())
VENDAS = float(input())
COMISSION = VENDAS * 15 / 100
TOTAL = SALARY + COMISSION

print("TOTAL = R$ %0.2f" % TOTAL)
