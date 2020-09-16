prod = int(input("Quantidade de Produtos: "))
val_compra = float(input("Valor Da Compra: "))

tot = 0

if prod <= 2:
    tot = val_compra - (val_compra / 100 * 2)
    print(tot)
#Usei tudo IF funcionou da mesma forma também:
elif prod > 2 and prod <=5:
    tot = val_compra - (val_compra / 100 * 5)
    print(tot)

elif prod > 5 and prod <10:
    tot = val_compra - (val_compra / 100 * 10)
    print(tot)

elif prod > 10:
    tot = val_compra - (val_compra / 100 * 15)
    print(tot)
