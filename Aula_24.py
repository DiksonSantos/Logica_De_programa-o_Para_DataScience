valido = False
while valido == False:
    int1 = int(input("Informe o Primeiro Valor: "))
    int2 = int(input("Segundo Valor: "))
    if int1>0 and int2>0 and int1<int2:
        valido = True
# 'x' percorre de int1 até int2 Que recebe +1 == Contagem  Progressiva.
for x in range(int1, int2+1):
    print(x)

#De int2 que é o valor máximo, Volta para int1, ao passo -1 Que significa Regredir a contagem.
for int2 in range(int2, int1-1, -1):
    print(int2)

"""Chega ao valor máximo, e do valor Maximo Volta para 1"""
