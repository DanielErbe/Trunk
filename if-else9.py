import time

numero1 = float(input("insira o primeiro numero: "))
numero2 = float(input("insira o segundo numero: "))
numero3 = float(input("insira o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(numero1, ">")
elif numero2 > numero1 and numero2 > numero3:
    print(numero2, ">")
else:
    print(numero3, ">")


if numero2 <= numero1 <= numero3 or numero3 <= numero1 <= numero2:
    print(numero1, ">")
elif numero1 <= numero2 <= numero3 or numero3 <= numero2 <= numero1:
    print(numero2, ">")
else:
    print(numero3, ">")
    

if numero1 < numero2 and numero1 < numero3:
    print(numero1)
elif numero2 < numero1 and numero2 < numero3:
    print(numero2)
else:
    print(numero3)

time.sleep(10)
