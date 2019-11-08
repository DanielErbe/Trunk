import time

turno = input("Em que turno você estuda? (M-matutino ou V-Vespertino ou N- Noturno): ")

if turno == "M" or turno == "m":
    print("Bom Dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde!")
elif turno == "N" or turno == "n":
    print("Boa Noite!")
else:
    print("Valor Invalido!")

time.sleep(10)
