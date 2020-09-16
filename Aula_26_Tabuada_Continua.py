
Flag = True #Esta Flag é opcional

while Flag == True: #Usando Apensa 'while True' também funcionaria.
    tab = float(input("Tabuada Do: "))
    for n in range(1,11):
        print(n, "X", int(tab), "=", int(n*tab))
    if tab == 0:
        #break   #Assim Também Funcionaria.
        Flag = False
    
