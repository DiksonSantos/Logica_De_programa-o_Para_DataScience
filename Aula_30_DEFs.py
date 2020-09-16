#EXERCICIOS AULA 30:
def media(a,b):
    """Calculadora de Medias"""
    A = a
    B = b
    Res = (A + B) / 2
    if Res >= 6.0:
        print(f"Sua Nota é {Res} Aprovado")
    elif Res < 6:
        print(f"Sua Nota {Res} Esta A Baixo de 6 = Reprovado :/")
    else:
        return "Fim"

UM = 0
DOIS = 0

while True:
    Quest = str(input("Calcular Média S ou N? : ")).upper()
    if Quest == "N".upper(): #nEM PRECISA DO uPPER aQUI
        break
    elif Quest == "S".upper():
        UM = float(input("Digite Um Numero: "))
        DOIS = float(input("Digite Outro Numero: "))
        MED = media(UM,DOIS)
        print(MED)


