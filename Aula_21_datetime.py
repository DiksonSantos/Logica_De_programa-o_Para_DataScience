from datetime import date

idade = int(input("Sua Idade: "))
ano = date.today().year

if ano - idade == 18:
    print(f"Sua Idade ={ano - idade} Apto ao Serviço")
else:
    print("Vai jogar Programar Computadores")

        


