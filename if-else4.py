import time

letra = input("insira uma letra: ")

vogal = ["a", "e", "i", "o", "u"]

if letra in vogal:
    print("vogal")
else:
    print("consoante")

time.sleep(10)
