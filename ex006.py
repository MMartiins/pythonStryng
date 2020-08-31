filme = "Vingadores - Era de Ulton"
filme = "Os quase Vingadores - End Game"
filme = "Detonadores - Os Vingadores"

#Uma forma de saber se os filmes listados são dos “Vingadores” ou não é verificando se o nome do filme começa com a
# palavra “Vingadores”, analise as sugestões de códigos para resolver esse problema e marque a alternativa que
# retornaria a resposta incorreta para os itens listados acima

#Código correto

filmeEhVingadores = filme.find("Vingadores")
if filmeEhVingadores:
    print("Esse filme é dos vingadores")
else:
    print("Esse filme não é dos vingadores")