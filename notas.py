'''
argumento = "https://www.bytbank.com.br/cambio?moedaorigem=real"
#............012345678910
subString = argumento[5:11]
print(subString)

----------------------------------------

argumento = "moedaorigem=real"
listaArgumentos = argumento.split("=")
print(listaArgumentos)

----------------------------------------------

argumento = "moedaorigem=real"
index = argumento.find("=")
subString = argumento[index + 1:]
print(subString)


string = ""
if string:
    print("Tem algo aqui")
else:
    print("Não tem nada aqui!!")
'''