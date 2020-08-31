from ExtratorArgumentosUrl import ExtratorArgumentosUrl


''' metodo sem a decoração staticmethod
url = "https://www.bytbank.com.br/cambio?moedaorigem=real"
argumento = ExtratorArgumentosUrl(url)
print(argumento)
'''

#metodo com a decoração staticmethod
url = "https://bytebank.com/cambio?moedaoRigem=real&moedadestino=dolar&valor=1500"


argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)
print(id(argumentosUrl))
print(id(argumentosUrl2))
print(argumentosUrl == argumentosUrl2)
'''
moedaOrigem, moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaDestino, moedaOrigem,valor)
print(argumentosUrl)

#string = "bytebankbytebyte"
#stringNova = string.replace("byte", "Marcos", 2)
#print(stringNova)

banco1 = "bytebank"
banco2 = "Bytebank".upper()


urlByteBank = "https://bytebank.com"
url1 = "https://buscasites.com/busca?q=https://bytebank.com"
url2 = "https://bitebank.com.br"
url3 = "https://bytebank.com/cambio/teste/teste"
#esse metodo starswith, retorna verdadeira se as duas string forem exatamente iguais
print(url3.startswith(urlByteBank))
'''