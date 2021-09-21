arquivo = open("teste.txt", "r")
saida = open("saida.txt", "w")

for linha in arquivo:
    strings = linha.split()
    if(len(strings) > 0 and strings[0] == 'old'):
        backup = linha[8:]
    elif(len(strings) > 0 and strings[0] == 'new'):
        linha = "\t" + "new " + backup
    saida.write(linha)

arquivo.close()
saida.close()
