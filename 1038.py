valor = input().split(" ")
codigo, quantidade = valor

if (codigo == '1'):
    total = int(quantidade) * 4
    print("Total: R$ {:.2f}".format(total))

elif (codigo == '2'):
    total = int(quantidade) * 4.50
    print("Total: R$ {:.2f}".format(total))

elif (codigo == '3'):
    total  = int(quantidade) * 5
    print("Total: R$ {:.2f}".format(total))

elif (codigo == '4'):
    total  = int(quantidade) * 2
    print("Total: R$ {:.2f}".format(total))

elif (codigo == '5'):
    total  = int(quantidade) * 1.50
    print("Total: R$ {:.2f}".format(total))
