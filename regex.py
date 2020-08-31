import re
email1 = "Meu numero é 122341234, 657489639, 3904167481"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "12341234 é o meu celular"

padrao = "[0-9]{4,8}[-]*[0-9]{4,8}"

retorno = re.findall(padrao, email1)
print(retorno)