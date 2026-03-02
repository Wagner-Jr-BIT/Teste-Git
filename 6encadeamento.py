frase_torta = "   Naruto é piOr que o One PIECE  "

frase_formatada = frase_torta.strip().capitalize().replace('pior', 'melhor')
print(frase_formatada)
# cuidado ao usar o .replace, com letras maiusculas após utlizar um metodo de formatção, pois o .replace é case-sensitive, ou seja, ele diferencia letras maiusculas de minusculas. Se a palavra "pior" for escrita com letra maiuscula após a formatação, o .replace não irá reconhecer e substituir a palavra corretamente.