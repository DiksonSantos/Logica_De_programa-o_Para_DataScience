tab = int(input("Quantas notas Serão Calculadas"))
soma = 0
for tab in range(1, tab+1):
    texto = "Informe o " + str(tab) + " Numero: "
    soma += int(input(texto))

print("A Media é Igual a : ", soma / tab)
