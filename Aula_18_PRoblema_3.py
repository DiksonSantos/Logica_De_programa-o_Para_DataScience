idade = int(input("Digite Sua Idade: "))
atividade = float(input("Tempo De Atividade Profissional: "))
#Deve ter idade MENOR que 70 e MAIS de 25 anos de Carteira.
#OU ainda até pode ser mais Velho (>70) porém Tem que ter MAIS Experiencia
#As condições estão entre parenteses formando sentenças {Novidade}
if (idade < 70) or (atividade >= 25) or (idade >= 70 and atividade >=30):
    print("Aprovado  -  Apto Para a Vaga")
else:
    print("Reprovado Não Apto")
