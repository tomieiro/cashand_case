#aqui usa %s
define pac1_img_saida = "images/inventario/finalizar_%s.png"
define pac1_img_estante = "#f80"

image pac1_img_relogio:
    "images/engler/itens/relogio.png"
    zoom 0.5

define pac1_img_inv_but = "images/inventario/bg_seta.png"

#ATENÇÃO: GARANTIR QUE OS ITENS POSSUEM ID'S DIFERENTES
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
default pac1_item_relogio = ["images/engler/itens/relogio.png", "Um belo relógio. Parece funcional, apesar de estar 8 minutos atrasado.", False, 10, False, "IDE_01_ESCOLHEU_RELOGIO"]
default pac1_item_sangue = ["#f00", "Uma inscrição escrita em sangue, já seco. Me parece ser uma pista valiosa.", False, 11, False, "IDE_01_ESCOLHEU_SANGUE"]
#... outros itens "inuteis"

default pac1_itens_no_inventario = []

default pac1_fim = False

#Label responsável por inicializar variáveis e chamar a tela
label CHAMA_TELA_PAC_DIA1:
    #Inicializa as variáveis necessárias
    python:
        pac1_fim = False
        pac1_item_relogio[2] = False
        pac1_item_sangue[2] = False
        #... outros itens "inuteis"
        pac1_itens_no_inventario = []

    #QUAL MÚSICA TOCAR? VAI TER EFEITOS SONOROS DE COLETA? FALHA NO CLICK OU SUCESSO NO CLICK???
    #play music "audio/musicas/Pistas.mp3" fadeout 1

    #Chama a tela de point and click
    #$Show("point_and_click_dia1", transition="puzzle_transition1")()
    show screen point_and_click_dia1() with puzzle_transition8

    jump POINT_AND_CLICK

label FIM_TELA_PAC_DIA1:
    hide screen point_and_click_dia1 with puzzle_transition8
    return

screen point_and_click_dia1():

    #Sensível a cliques apenas quando não há diálogo acontecendo
    sensitive(  not renpy.get_screen("say") and
                not renpy.get_screen("inventario_de_coleta") and
                not renpy.get_screen("mostra_item") and
                not renpy.get_screen("mostra_item2")
                )

    frame:
        background "images/engler/cenarios/quarto hougin.png"
        xsize 1280
        ysize 720

        #Botão de saída do puzzle(APENAS QUANDO COLETOU, NO MÍNIMO, AS PISTAS DO SANGUE E DO RELÓGIO)
        if(pac1_fim):
            imagebutton:
                action Jump("FIM_TELA_PAC_DIA1")
                auto pac1_img_saida
                #idle pac1_img_saida
                at idc_botao_sair
                focus_mask True

        #Botão que inicia uma interação na estante e coleta o item da mancha de sangue
        imagebutton:
            action Jump("PAC1_SELECIONA_ESTANTE")
            #auto pac1_img_estante
            idle pac1_img_estante
            focus_mask True
            xalign 0.25
            yalign 0.63
            xsize 100
            ysize 100

        #Botão de coleta para o item relógio
        if(not pac1_item_relogio[2]):
            imagebutton:
                action Jump("PAC1_SELECIONA_RELOGIO")
                #auto pac1_img_relogio
                idle "pac1_img_relogio"
                focus_mask True
                xalign 0.85
                yalign 0.65
                xsize 100
                ysize 100

        #Botão para abrir inventário de coleta
        imagebutton:
            action Show("inventario_de_coleta", itens_no_inventario=pac1_itens_no_inventario)
            auto "images/inventario/bg_seta_%s.png"
            #idle pac1_img_inv_but
            at idc_botao_abrir


label PAC1_SELECIONA_ESTANTE:
    if(not pac1_item_sangue[2]):
        "O que é aquilo na cômoda? Uma mancha..."
        show screen mostra_item(pac1_item_sangue[0]) with dissolve
        pause 0.3
        "Uma mancha de sangue..."
        drc "Olhe, senhor Sheppard, uma inscrição."
        drc "Possui um tom rubro, parece ser sangue já seco."
        #show sheppard neutro onlayer screens at center with dissolve
        shp_side "Como não havíamos notado isso antes?"
        drc "Realmente, é uma pequena inscrição, mas parece ser uma valiosa pista."
        hide screen mostra_item with dissolve
        #hide sheppard onlayer screens with dissolve
        $renpy.notify("Coletou Pista - Mancha de Sangue!")
        python:
            pac1_item_sangue[2] = True
            pac1_itens_no_inventario.append(pac1_item_sangue)

        #Se selecionar a outra pista essencial também, pode sair
        if(pac1_item_relogio[2]):
            "Acho que já coletei todas as pistas que eu precisava..."
            drc "Acho que isto é suficiente, Sheppard!"
            show sheppard neutro onlayer screens at center with dissolve:
                xzoom 1.1 yzoom 1.1  xalign 0.5 yalign 0.99999
            shp "Já acabou, detetive?"
            drc "Espera, acho que vou dar uma última olhada."
            hide sheppard onlayer screens with dissolve
            $pac1_fim = True
    else:
        "Acho que não há mais nada para ver aqui..."
    jump POINT_AND_CLICK

label PAC1_SELECIONA_RELOGIO:
    show screen mostra_item(pac1_item_relogio[0]) with dissolve
    pause 0.3
    "Um relógio..."
    drc "É, certamente, um belo relógio."
    #show sheppard neutro onlayer screens at center with dissolve
    shp_side "Parece estar funcional, senhor Rightclue."
    drc "Correto. Todavia, encontra-se 8 minutos atrasado."
    shp_side "Talvez esteja com as engrenagens ruins."
    drc "Certamente."
    hide screen mostra_item with dissolve
    #hide sheppard onlayer screens with dissolve
    $renpy.notify("Coletou Pista - Relógio!")
    python:
        pac1_item_relogio[2] = True
        pac1_itens_no_inventario.append(pac1_item_relogio)
    #Se selecionar a outra pista essencial também, pode sair
    if(pac1_item_sangue[2]):
        "Acho que já coletei todas as pistas que eu precisava..."
        drc "Acho que isto é suficiente, Sheppard!"
        show sheppard neutro onlayer screens at center with dissolve:
            xzoom 1.1 yzoom 1.1  xalign 0.5 yalign 0.99999
        shp "Já acabou, detetive?"
        drc "Espera, acho que vou dar uma última olhada."
        hide sheppard onlayer screens with dissolve
        $pac1_fim = True
    jump POINT_AND_CLICK
