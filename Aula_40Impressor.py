#Aula 40:
"""Importarei o arquivo 'impressor' pra ca"""

from impressor import*

valido = False


while valido== False:
    int1 = int(input("Informe O Valor: "))
    int2 =  int(input("Informe o Segundo Valor: "))
    if int2 <= int1:
        print("Valido invalidos! Tente Novamente")
    else:
        valido = True


imprime(int1, int2)
