cot = 5.38
print("Digite o Valor em Dolares para Saber quantos R$ \n vai gastar Para Comprar Esta quantia em Dolares")
valor = int(input("Informe O Valor: "))
valor = float(valor) #Convertendo
conv = valor * cot
print(f"{conv:.2f}")
