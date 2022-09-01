import math

with open("/storage/emulated/0/qpython/desvio p/numeros.txt", "r+") as c:
    raw = c.read()
    linhas = raw.split('\n')
    desvioPadrao = 0
    variancia = 0
    media = 0
    erroa = 0
    for linha in linhas:
        media = media + float(linha)
    media = media/len(linhas)
    for linha in linhas:
        variancia = variancia + (float(linha) - media) ** 2
    variancia = variancia/(len(linhas) - 1)
    erroa = (math.sqrt(variancia)/(math.sqrt(len(linhas))))
    desvioPadrao = math.sqrt(variancia)
with open("/storage/emulated/0/qpython/desvio p/resultado.txt", "w+") as r:
    r.write("Media: " + str(media) + "\n")
    r.write("Variancia: " + str(variancia) + "\n")
    r.write("Desvio Padrao: " + str(desvioPadrao) + "\n")
    r.write("Erro provavel aleatorio: " + str(erroa) + "\n")