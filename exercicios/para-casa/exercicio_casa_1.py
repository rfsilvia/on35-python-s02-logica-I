# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato, o salário líquido. Calcule os descontos e o salário líquido. 

valor_hora = float(input("Quanto que você ganha por hora?"))

horas_trabalhadas_mes = float(input("Quantas horas você trabalha por mês?"))

salario_bruto_mensal = valor_hora * horas_trabalhadas_mes
print(f"O seu salário bruto mensal é no valor de R$ {salario_bruto_mensal}.")

valor_ir = float(salario_bruto_mensal * 0.11)
print(f"O valor que você paga de imposto de renda é R$ {valor_ir}.")

valor_inss = float(salario_bruto_mensal * 0.08)
print(f"O valor que você paga de INSS é R$ {valor_inss}.")

valor_sindicato = float(salario_bruto_mensal * 0.05)
print(f"O valor que você paga para o sindicato é R$ {valor_sindicato}.")


def calculo_salario(salario_bruto_mensal):
    salario_liquido_mensal = salario_bruto_mensal - valor_ir - valor_inss - valor_sindicato
    return salario_liquido_mensal

resultado = calculo_salario(salario_bruto_mensal)

print(f"O valor do seu salário líquido mensal é de R$ {resultado}.")      
