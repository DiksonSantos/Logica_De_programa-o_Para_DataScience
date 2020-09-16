
Entrada = str(input("Digite Seu Nome: "))
Nomes = ['Dikson', 'Olivia', 'Newton', 'One']

#Fiz rodar certinho com este codigo a baixo:  (Sem erros).
for n in Nomes:
    if n == Entrada:
        print('Encontrado')
else:
    print("Não Encontrado")


#Lista Luna Só é mais complicado, mas o efeito é o mesmo:
"""
for n in range(len(Nomes)):  # Ou (0, len(Nomes))   Tambem funcionaria.
    if Entrada in Nomes[n]:
        print(f"{Entrada} Você Esta na Lista")
    else:
        print("Sorry")
"""

"""
#USANDO UMA FLAG:     -> Exemplo do professor.
found = False

for n in range(0, len(Nomes)):
     print(Nomes[n])
     if Nomes[n].lower() == Entrada.lower():
         found = True

if found == False:
    print("Nome Não Encontrado")
else:
    print("Nome Encontrado")
#Porém Neste Algoritmo ele mostra Todos os Nomes. No meu Isso não é necessário  ;)
"""
