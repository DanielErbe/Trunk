import time

nota_1 = float(input("insira a primeira nota: "))

nota_2 = float(input("insira a segunda nota: "))

media = (nota_1+nota_2)/2

if media > 6.9 and media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com Distinção")

time.sleep(10)
