def impressao(int1, int2):
    for x in range(int1, int2+1):
        print(x)
    for int2 in range(int2, int1-1,-1):
        print(int2, end="-")

int1 = int(input("Primeiro Valro: "))
int2 = int(input("Informe Segundo Valor: "))

x = impressao(int1, int2)

