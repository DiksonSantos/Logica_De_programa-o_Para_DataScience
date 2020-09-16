#Criando Duas Listas:
Lista1 = list(range(1,6))
Lista2 = list(range(1,6))


#Apenas Para Exibir Um Contador de vezes que foi rodado o Laço (Até 5x):
for n in range(0,5):
    print("Informe o número da osição ", n+1, "da primeira lista")
    Lista1[n] = int(input("Numero: ")) #Aqui as 5 Posições da Lista 1 Vão sendo preenchidas. (1,6 == 0,5)

for n in range(0,5):
    print("Informe o número da osição ", n+1, "da Segunda lista")
    Lista2[n] = int(input("Numero: "))

for n in range(0,5):
    if Lista1[n] == Lista2[n]:   #[n]  SImboliza o Objeto Percorrido da Lista.
        print("Valor Semelhante em", Lista1[n], "e", Lista2[n], "Diferentes da Posição", n+1)
