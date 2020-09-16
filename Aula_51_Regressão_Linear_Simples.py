"""
ESTOU USANDO O PYCHARM, POIS A BIBLIOTECA 'SKLEARN' SÓ ESTAVA DISPONIVEL
NO AMBIENTE VIRTUAL 'sistemaAbc'
"""

import numpy as np
from sklearn.linear_model import LinearRegression

quant = int(input("Inform Quantidade De Var Do Model: "))
x_ = list(range(0, quant))
y_ = list(range(0, quant))

print("Informe as", quant, "Variaveis Dependentes")

for n in range(0, quant):
    print("Informe a Variavel", n+1)
    y_[n] = int(input())

print("Informe as", quant, "Var Independentes: ")
for n in range(0, quant):
    print("Informe o Valor ", n+1)
    x_[n] = int(input())

print("Informe o valro que quer prever")
prev = list(range(0, 1))
prev[0] = int(input())

x_ = np.asarray(x_)
x_ = x_.reshape(-1, 1)
y_ = np.asarray(y_)

modelo = LinearRegression()
modelo.fit(x_, y_)

prev = np.asarray(prev)
prev = prev.reshape(-1, 1)

resp = modelo.predict(prev.reshape(-1, 1))
An = int(resp)
print(f"Resultado da previsão:{round(An):.2f} ")
