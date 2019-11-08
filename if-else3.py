import time

sexo = input("insira o sexo (M para Masculino ou F para Feminino)")

if sexo in ["M", "m"]:
    print("Masculino")
elif sexo in ["F", "f"]:
    print("Feminino")
else:
    print("Sexo Invalido")

time.sleep(10)
