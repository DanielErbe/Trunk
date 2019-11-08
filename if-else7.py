import time

numero1 = float(input("insira um numero: "))
numero2 = float(input("insira o segundo numero: "))
numero3 = float(input("insira o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("Maior:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Maior:", numero2)
else:
    print("Maior:", numero3)

if numero1 < numero2 and numero1 < numero3:
    print("Menor:", numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("Menor:", numero2)
else:
    print("Menor:", numero3)


time.sleep(10)
