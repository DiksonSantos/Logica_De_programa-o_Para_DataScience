from statistics import mean

#Uma Lista Contendo 10 Posições:
lista = list(range(1,11))   #lista = [0:10]

#Inserimos As Notas nestas 10 Posições:
for n in range(0,10):
    print("Informa Numero Na Posição: ", n+1)
    lista[n] = int(input('Nota: '))
    
    #Caso digite Um Numero Menor que ZERO:
    while lista[n] <=0:
        print("Entrada Inválida, por favor Digite Um Numero Positivo")
        lista[n] = int(input('Nota Num Positivo: '))

soma = 0
for n in range(0,10):
    soma += lista[n]

#Metodo tradicional de calcular Medias:
print("Media Calculada \ Manualmente\" igual a : ", soma / 10)

#Aplicou a função á Lista:
print("Media Calculada \ por função\"Igual a : ", mean(lista))
