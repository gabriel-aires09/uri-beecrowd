valor = input().split(" ")
N1, N2, N3, N4 = valor
split = valor

N1 = float(split[0])
N2 = float(split[1])
N3 = float(split[2])
N4 = float(split[3])

MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4)) / 10
print("Media: {:.1f}".format(MEDIA))

if (MEDIA >= 7):
    print("Aluno aprovado.")
elif (MEDIA >= 5 and MEDIA <= 6.9):
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {}".format(exame))
    mediaExame = (MEDIA + exame) / 2
    if (mediaExame >= 5):
          print("Aluno aprovado.")
          print("Media final: {:.1f}".format(mediaExame))
    else:
          print("Aluno reprovado.")
          print("Media final: {:.1f}".format(mediaExame))
else:
    print("Aluno reprovado")
