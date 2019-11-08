import time

numero1 = float(input("insira um numero: "))
numero2 = float(input("insira o segundo numero: "))
numero3 = float(input("insira o terceiro numero: "))

conjunto1 = [numero2, numero3]

conjunto2 = [numero1, numero3]

if numero1 > max(conjunto1):
    print(numero1)
elif numero2 > max(conjunto2):
    print(numero2)
else:
    print(numero3)

time.sleep(10)
