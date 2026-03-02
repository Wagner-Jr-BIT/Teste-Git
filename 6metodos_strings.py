frase = "O PythOn É Mais LegaL"
#.capitalize - Deixa a primeira letra da string maiúscula e o restante minúscula
print(frase.capitalize())

# .title() - Deixa a primeira letra de cada palavra maiúscula e o restante minúscula
print(frase.title())

# .center(TAMANHO, CARACTERE) - Centraliza a string em um campo de largura especificada
print(frase.center(50, "-"))

# len (objeto) - Retorna o número de caracteres em uma string
print(len(frase))

# .upper() - Converte todos os caracteres da string para maiúscula
print(frase.upper())
# .lower() - Converte todos os caracteres da string para minúscula
print(frase.lower())
# .find("caractere") - Retorna o índice da primeira ocorrência do caractere ou substring especificada
print(frase.find("P"))
# .replace("caractere_antigo", "caractere_novo") - Substitui todas as ocorrências do caractere antigo pelo caractere novo
print(frase.replace("PythOn", "Wagner"))

arquivo = 'casdratro_clientes.txt'
#.startswith("caractere") - Verifica se a string começa com o caractere ou substring especificada
print(arquivo.startswith("casdratro"))
#.endswith("caractere") - Verifica se a string termina com o caractere ou substring especificada
print(arquivo.endswith(".txt"))

# .isalpha() - Verifica se todos os caracteres da string são letras (sem espaços ou números)
print("Python".isalpha())
# .isdigit() - Verifica se todos os caracteres da string são dígitos (números)
print("Python12345".isdigit())
# .isalnum() - Verifica se todos os caracteres da string são alfanuméricos (letras ou números, sem espaços)
print("Python12345".isalnum())

# .strip() - Remove os espaços em branco do início e do final da string
senha = '  123456     '
if senha.strip() == "123456":
    print("Senha correta")
else:
    print("Senha incorreta, tente novamente")
# se add um espaço apos a ação de strip, o codigo não reconhecerá a senha como correta. caindo assim no else, mesmo que a senha digitada seja "123456" (sem os espaços)