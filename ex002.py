celular = "(41)96574-1728"

x = celular.find("(") + 1
y = celular.find(")")

indiceInicialCodigoArea = x
indiceFinalCodigoArea = y

print(celular[indiceInicialCodigoArea:indiceFinalCodigoArea])