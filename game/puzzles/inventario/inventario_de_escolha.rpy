#TELA DE INVENTARIO DE ESCOLHA: contém todos os itens coletados em um point-and-click
# e funciona como um puzzle onde alguns itens precisam ser coletados, na ordem, para resolvê-lo.

#Gabarito das sequências de itens que devem ser selecionados(identificados pelo ID)
default ide_seq_gabarito = [1, 0]

default ide_itens_no_inventario = []

default ide_aux_count = 0

default ide_aux_item = []

default ide_fim = False

default ide_tempo = 3.0

transform ide_bot_tr:
    maxsize (150, 150)
    xalign 0.5
    yalign 0.5

#Usando itens coletados do point-and-click
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
screen inventario_de_escolha():
    modal True

    if(ide_fim):
        timer ide_tempo action Jump("FIM_IDE_TESTE")
        #key "mousedown_1" action Jump("FIM_IDE_TESTE")

    frame:
        xalign 0.5
        yalign 0.2
        maximum (700, 250)
        background "#000"
        hbox:
            xsize 1.0
            ysize 1.0
            for item in ide_itens_no_inventario:
                frame:
                    background "#fff"
                    xsize 200
                    ysize 200
                    margin (15, 25)
                    imagebutton:
                        idle item[0]
                        action [Jump(item[5])]
                        at ide_bot_tr


init python:

    def ide_nao_escolhido(item):
        return (item[4] == False)

    def ide_proximo_correto(item):
        global ide_seq_gabarito
        return (len(ide_seq_gabarito) != 0 and item[3] == ide_seq_gabarito[0])

    def ide_escolheu_item(item):
        global ide_seq_gabarito
        global ide_aux_count
        item[4] = True
        ide_seq_gabarito.pop(0)
        ide_aux_count += 1
