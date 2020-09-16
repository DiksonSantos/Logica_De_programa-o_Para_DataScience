from scipy.stats import poisson
quant = float(input("Quantidade Normal de Acidentes: "))
prob = float(input(f"Probabilidade de Acidentes em {int(quant)} Para: "))


#Probabilidade de 3 acidentes Quando o Comum são 2 Acidentes:
print(f"{poisson.pmf(prob, quant):.2f}%")

