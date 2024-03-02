b = int(input("Kaç İşlemli bir işlem yapmak istiyorsunuz?"))
x = str(input("Hangi işlemi yapmak istiyorsun?"))

if b == 2:
    sayi_1 = int(input("Sayi 1i girin"))
    sayi_2 = int(input("Sayi 2yi girin"))
    if x == "+":
        print(sayi_1 + sayi_2)
    elif x == "-":
        print(sayi_1 - sayi_2)
    elif x == "*":
        print(sayi_1 * sayi_2)
    elif x == "/":
        print(sayi_1 / sayi_2)
if b == 3:
    sayi_1 = int(input("Sayi 1i girin"))
    sayi_2 = int(input("Sayi 2yi girin"))
    sayi_3 = int(input("Sayi 3yi girin"))
    if x == "+":
        print(sayi_1 + sayi_2 + sayi_3)
    elif x == "-":
        print(sayi_1 - sayi_2 - sayi_3)
    elif x == "*":
        print(sayi_1 * sayi_2 * sayi_3)
    elif x == "/":
        print(sayi_1 / sayi_2 / sayi_3)