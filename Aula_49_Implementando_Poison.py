from math import pow, factorial

def poisson(x,lam):
    return (pow(2.71828, -lam) * pow(lam,x) / factorial(x))*100

#J = poisson(3,2)
#print(f"{J:.2f}","%")

S = "Quais as chances de acontecerem: "
A = "Acidentes"

B = "Quando Acontecem em Média"

UM = int(input(S))
DOIS = int(input("Quando Já Ocorrem -> Acidentes: "))

P = poisson(UM, DOIS)
print(f"{P:.2f}%")
