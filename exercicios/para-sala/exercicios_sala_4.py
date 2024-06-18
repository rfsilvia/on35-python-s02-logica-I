#Faça um programa que peça as 4 notas bimestrais e mostre a média
nota1 = float(input("insira a primeira nota:"))
print(nota1)

nota2 = float(input("insira a segunda nota:"))
print(nota2)

nota3 = float(input("insira a terceira nota:"))
print(nota3)

nota4 = float(input("insira a quarta nota:"))
print(nota4)

media = ((nota1 + nota2 + nota3 + nota4) / 4)
print(f"A média bimestral é: {media}")