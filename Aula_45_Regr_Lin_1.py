from numpy import *

# 'cov' vem de Numpy (É uma função):
    #'bias' é um parametro:
    #[0] e [1] São as posições dos resultados obtidos:
def correlacao(x, y):
    
    covariacao = cov(x,y, bias=True)[0][1]
    #'var' é outra função do pacote Numpy
    variancia_x = var(x)#Variancia de X
    variancia_y = var(y)#Variancia de y
    return covariacao / sqr(variancia_x * variancia_y )


def inclinacao(x,y,correlacao):
    stdx = std(x)
    stdy = std(y)
    return correlacao * (stdy / stdx)

def interceptacao(x,y , inclinacao):
    mediax = mean(x)
    mediay = mean(y)
    return mediay - mediax * inclinacao

def previsao(interceptacao, inclinacao, valor):
    return interceptacao + (inclincacao * valor)
