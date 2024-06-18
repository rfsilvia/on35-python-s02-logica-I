def calcula_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

print(calcula_media(10, 12))
print(calcula_media(5, 7)) 


def retorna_informacoes_pessoais(nome, idade, genero, cidade_natal, cpf, saldo, dividas):
    tem_nome_sujo = dividas > saldo

    return f"A pessoa {nome}, de idade {idade}, gênero {genero}, natural de {cidade_natal}, de cpf {cpf}, tem o nome sujo? {tem_nome_sujo}"

print(retorna_informacoes_pessoais("Ana", 37, "travesti", "Fortaleza", "123456789", 1500, 178))
