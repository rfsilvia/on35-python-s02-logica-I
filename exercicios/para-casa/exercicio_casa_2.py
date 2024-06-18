# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

tamanho_arquivo_mb = float(input("Qual é o tamanho do arquivo em megabytes?"))

velocidade_internet_mbps = float(input("Qual é a velocidade do seu link de internet?"))

conversao_mpbs_para_mb = float(velocidade_internet_mbps / 8)

print(conversao_mpbs_para_mb)

tempo_aprox_download = float(conversao_mpbs_para_mb / 60)

print(f"O tempo aproximado de downoload do seu arquivo é de {tempo_aprox_download} minutos")


