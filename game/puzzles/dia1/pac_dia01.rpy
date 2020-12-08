#aqui usa %s
define pac1_img_saida = "images/inventario/finalizar_%s.png"

image pac1_img_estante:
    "images/engler/itens_no_cenario/mancha sangue.png"
    #rotate 10.0

image pac1_img_relogio:
    "images/engler/itens_no_cenario/relogio_parede2.png"

define pac1_img_inv_but = "images/inventario/bg_seta.png"

define pac1_img_gaveta1 = "images/engler/itens_no_cenario/gaveta1.png"

define pac1_img_gaveta2 = "images/engler/itens_no_cenario/gaveta2.png"

define pac1_img_lapis = "images/engler/itens_no_cenario/lapis_cen.png"

define pac1_img_livros = "images/engler/itens_no_cenario/livros_cen.png"

define pac1_img_camera = "images/engler/itens_no_cenario/camera_cen.png"

#ATENÇÃO: GARANTIR QUE OS ITENS POSSUEM ID'S DIFERENTES
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
default pac1_item_relogio = ["images/engler/itens/relogio.png", "Um belo relógio. Parece funcional, apesar de estar 8 minutos atrasado.", False, 10, False, "IDE_01_ESCOLHEU_RELOGIO"]
default pac1_item_sangue = ["images/engler/itens/sangue.png", "Uma inscrição escrita em sangue, já seco. Me parece ser uma pista valiosa.", False, 11, False, "IDE_01_ESCOLHEU_SANGUE"]

default pac1_item_lapis = ["images/engler/itens/lapis.png", "Um simples lápis. Provavelmente, pertencia ao senhor Hougin.", False, 12, False, "IDE_01_ESCOLHEU_LAPIS"]

default pac1_item_livros = ["images/engler/itens_no_cenario/livros.png", "Alguns livros. Parecem interessantes, mas não tenho tempo de lê-los. Uma pena...", False, 13, False, "IDE_01_ESCOLHEU_LIVROS"]

default pac1_item_camera = ["images/engler/itens_no_cenario/camera.png", "Uma câmera. Gostaria de ter uma dessas...", False, 14, False, "IDE_01_ESCOLHEU_LIVROS"]

default pac1_itens_no_inventario = []

default pac1_fim = False

#Label responsável por inicializar variáveis e chamar a tela
label CHAMA_TELA_PAC_DIA1:
    #Inicializa as variáveis necessárias
    python:
        pac1_fim = False
        pac1_item_relogio[2] = False
        pac1_item_sangue[2] = False
        pac1_item_lapis[2] = False
        pac1_item_livros[2] = False
        pac1_item_camera[2] = False
        #... outros itens "inuteis"
        pac1_itens_no_inventario = []

    #QUAL MÚSICA TOCAR? VAI TER EFEITOS SONOROS DE COLETA? FALHA NO CLICK OU SUCESSO NO CLICK???
    #play music "audio/musicas/Pistas.mp3" fadeout 1

    #Chama a tela de point and click
    #$Show("point_and_click_dia1", transition="puzzle_transition1")()
    play music "audio/musicas/Pistas.mp3" fadein 5.0
    show screen point_and_click_dia1() with puzzle_transition8
    #$renpy.show_screen("point_and_click_dia1", _layer="master")
    #$renpy.transition(puzzle_transition8)
    jump POINT_AND_CLICK

label FIM_TELA_PAC_DIA1:
    stop music fadeout 5.0
    #$renpy.transition(puzzle_transition8)
    #$renpy.hide_screen("point_and_click_dia1", layer="master")
    hide screen point_and_click_dia1 with puzzle_transition8
    return

screen point_and_click_dia1():

    key "h" action NullAction()
    key 'mouseup_2' action NullAction()
    key 'noshift_K_h' action NullAction()

    #Sensível a cliques apenas quando não há diálogo acontecendo
    sensitive(  not renpy.get_screen("say") and
                not renpy.get_screen("inventario_de_coleta") and
                not renpy.get_screen("mostra_item") and
                not renpy.get_screen("mostra_item2")
                )

    frame:
        background "images/engler/cenarios/quarto hougin2.png"
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
            idle "pac1_img_estante"
            focus_mask True
            xalign 0.655
            yalign 0.730
            #xsize 100
            #ysize 100

        #Botão de coleta para o item relógio
        imagebutton:
            action Jump("PAC1_SELECIONA_RELOGIO")
            #auto pac1_img_relogio
            idle "pac1_img_relogio"
            focus_mask True
            xalign 0.025
            yalign -0.008


        #Botão de coleta para o item gaveta 1 (não coletavel no 1 dia)
        imagebutton:
            action Jump("PAC1_SELECIONA_GAVETA")
            idle pac1_img_gaveta1
            focus_mask True
            xalign 0.725
            yalign 0.905

        #Botão de coleta para o item gaveta 2 (não coletavel no 1 dia)
        imagebutton:
            action Jump("PAC1_SELECIONA_GAVETA")
            idle pac1_img_gaveta2
            focus_mask True
            xalign 0.855
            yalign 0.915

        if(not pac1_item_lapis[2]):
            #Botão de coleta para o item lapis (não obrigatorio no 1 dia)
            imagebutton:
                action Jump("PAC1_SELECIONA_LAPIS")
                idle pac1_img_lapis
                focus_mask True
                xalign 0.572
                yalign 0.850

        #Botão de coleta para o item  (não obrigatorio no 1 dia)
        imagebutton:
            action Jump("PAC1_SELECIONA_LIVROS")
            idle pac1_img_livros
            focus_mask True
            xalign 0.750
            yalign 0.831


        #Botão de coleta para o item  (não obrigatorio no 1 dia)
        imagebutton:
            action Jump("PAC1_SELECIONA_CAMERA")
            idle pac1_img_camera
            focus_mask True
            xalign 0.825
            yalign 0.532

        #Botão para abrir inventário de coleta
        imagebutton:
            action Show("inventario_de_coleta", itens_no_inventario=pac1_itens_no_inventario)
            auto "images/inventario/bg_seta_%s.png"
            #idle pac1_img_inv_but
            activate_sound "audio/sonoplastia/AbrindoPasta.mp3"
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
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            renpy.pause(1, hard=hardPause)
            pac1_item_sangue[2] = True
            pac1_itens_no_inventario.append(pac1_item_sangue)
            renpy.pause(1, hard=hardPause)
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
        "Não preciso mais ver a mancha. Já guardei a imagem em minha mente."
    jump POINT_AND_CLICK

label PAC1_SELECIONA_RELOGIO:
    if(not pac1_item_relogio[2]):
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
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            renpy.pause(1, hard=hardPause)
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
    else:
        "Não há mais nada para se ver no relógio..."
    jump POINT_AND_CLICK

label PAC1_SELECIONA_GAVETA:
    "Não consigo abrir a gaveta. Está trancada."
    jump POINT_AND_CLICK

label PAC1_SELECIONA_LAPIS:
    show screen mostra_item(pac1_item_lapis[0]) with dissolve
    pause 0.3
    "Um lápis."
    "Estava caído no chão."
    "Vou levar, talvez me seja útil futuramente..."
    hide screen mostra_item with dissolve
    $renpy.notify("Coletou Pista - Lápis!")
    play sound "audio/sonoplastia/ColetandoPista.mp3"
    python:
        renpy.pause(1, hard=hardPause)
        pac1_item_lapis[2] = True
        pac1_itens_no_inventario.append(pac1_item_lapis)

    #Se selecionar a outra pista essencial também, pode sair
    if(pac2_item_gravador[2]):
        "Acho que já coletei todas as pistas que eu precisava..."
        drc "Acho que isto é suficiente, She..."
        "É verdade..."
        "Ele não está mais aqui..."
        "Mas tudo bem. Vou fazer isso por ele. Pela Kamira também!"
        "Vou descobrir quem está por trás desses assassinatos!"
        "Só para garantir, acho que vou dar uma última olhada."
        $pac2_fim = True

    jump POINT_AND_CLICK

label PAC1_SELECIONA_LIVROS:
    if(not pac1_item_livros[2]):
        show screen mostra_item(pac1_item_livros[0]) with dissolve
        pause 0.3
        "Alguns livros..."
        "O senhor Hougin estava-os lendo, provavelmente."
        "O conteúdo deles parece interessante..."
        "..."
        "Não! Não posso me distrair!"
        "Voltando à investigação..."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Livros!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            renpy.pause(1, hard=hardPause)
            pac1_item_livros[2] = True
            pac1_itens_no_inventario.append(pac1_item_livros)
    else:
        "Não preciso mais ver os livros, mas..."
        "Mais uma olhadinha não mata ninguém..."
        "Quer dizer... NÃO!"
        "Tenho que manter o foco na investigação!"
    jump POINT_AND_CLICK


label PAC1_SELECIONA_CAMERA:
    if(not pac1_item_camera[2]):
        show screen mostra_item(pac1_item_camera[0]) with dissolve
        pause 0.3
        "Uma câmera..."
        "Para possuírem um aparelho assim..."
        "Devem ser bem ricos mesmo."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Câmera!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            renpy.pause(1, hard=hardPause)
            pac1_item_camera[2] = True
            pac1_itens_no_inventario.append(pac1_item_camera)
    else:
        "Já olhei a câmera."
        "Estou com um pouco de inveja..."
        "Gostaria de ter uma dessas."
    jump POINT_AND_CLICK
