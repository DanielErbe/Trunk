import time

salario_atual = float(input("insira o salário atual: "))


if salario_atual <= 280:
    salario_novo = salario_atual * 0.20 + salario_atual
elif salario_atual > 280 and salario_atual <= 700:
    salario_novo = salario_atual * 0.15 + salario_atual
elif salario_atual > 700 and salario_atual < 1500:
    salario_novo = salario_atual * 0.10 + salario_atual
else:
    salario_novo = salario_atual * 0.05 + salario_atual

print("Salario antes do ajuste:", salario_atual)

if salario_atual <= 280:
    print("Percentual do aumento aplicado:", "20%")
elif salario_atual > 280 and salario_atual <= 700:
    print("Percentual do aumento aplicado:", "15%")
elif salario_atual > 700 and salario_atual < 1500:
    print("Percentual do aumento aplicado:", "10%")
else:
    print("Percentual do aumento aplicado:", "5%")

if salario_atual <= 280:
    print("Reajuste:", salario_atual * 0.20)
elif salario_atual > 280 and salario_atual <= 700:
    print("Reajuste:", salario_atual * 0.15)
elif salario_atual > 700 and salario_atual < 1500:
    print("Reajuste:", salario_atual * 0.10)
else:
    print("Reajuste:", salario_atual * 0.05)

print("Salario após o reajuste:", salario_novo)

time.sleep(10)
