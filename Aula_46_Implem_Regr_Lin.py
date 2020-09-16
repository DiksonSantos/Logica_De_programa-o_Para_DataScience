from regressao import *

quant = int(input("Informe Quantidade de Variaveis: "))

x_ = list(range(0, quant))
y_ = list(range(0, quant))

print("Informe as", quant, "Variaveis DEPendentes")
for n in range(0,quant):
    print("Informe o valor ",n+1)
    y_[n] = int(input("Insere: "))

print("informe as", quant, "Variaveis INDependentes")
for i in range(0,quant):
      print('Informe o valor',n+1)
      x_[n] = int(input())

print("Informe o valor que quer prever: ")
prev = float(input("Informe"))

#Variavel 'cor' guarda a função 'correlacao' do arquivo 'regressao.py'
cor = correlacao(x_, y_)
inc = inclinacao(x_, y_, cor)
inter = interceptacao(x_, y_, inc)
result = previsao(inter, inc, prev)


print("Modelo: ")
print("Correlação", cor)
print("Inclinação: ", inc)
print("Interceptação", inter)
print("Valor Para prever: ", prev)
print("Resultado da Previsão ", result)
