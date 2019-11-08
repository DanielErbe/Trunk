import time

produto1 = float(input("insira o valor do primeiro produto: "))
produto2 = float(input("insira o valor do segundo produto: "))
produto3 = float(input("insira o valor do terceiro produto:"))

if produto1 < produto2 and produto1 < produto2:
    print(produto1)
elif produto2 < produto1 and produto2 < produto3:
    print(produto2)
else:
    print(produto3)


time.sleep(10)
