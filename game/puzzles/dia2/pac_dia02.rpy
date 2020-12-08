#ATENÇÃO: GARANTIR QUE OS ITENS POSSUEM ID'S DIFERENTES
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
default pac2_item_gravador = ["images/engler/itens/gravador desligado aberto.png", "Um gravador. A tampa está aberta. Preciso arranjar uma forma de fechá-la.", False, 21, False, "IDE_02_2_ESCOLHEU_GRAVADOR"]
default pac2_item_tesoura = ["images/engler/itens/tesoura.png", "Uma tesoura. Também estava nas gavetas escondidas.", False, 22, False, "IDE_02_2_ESCOLHEU_TESOURA"]

default pac2_fim = False

#Label responsável por inicializar variáveis e chamar a tela
label CHAMA_TELA_PAC_DIA2:
    #Inicializa as variáveis necessárias
    python:
        pac2_fim = False
        pac2_item_gravador[2] = False
        #... outros itens "inuteis"
        #pac1_itens_no_inventario = []

    #Chama a tela de point and click
    play music "audio/musicas/Pistas.mp3" fadein 5.0
    show screen point_and_click_dia2() with puzzle_transition8
    jump POINT_AND_CLICK

label FIM_TELA_PAC_DIA2:
    stop music fadeout 5.0
    hide screen point_and_click_dia2 with puzzle_transition8
    return

screen point_and_click_dia2():

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
        if(pac2_fim):
            imagebutton:
                action Jump("FIM_TELA_PAC_DIA2")
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


        #Botão de coleta para o item gaveta 1 (coletavel no 2 dia)
        imagebutton:
            action Jump("PAC2_SELECIONA_GAVETA")
            idle pac1_img_gaveta1
            focus_mask True
            xalign 0.725
            yalign 0.905

        #Botão de coleta para o item gaveta 2 (coletavel no 2 dia)
        imagebutton:
            action Jump("PAC2_SELECIONA_GAVETA")
            idle pac1_img_gaveta2
            focus_mask True
            xalign 0.855
            yalign 0.915

        if(not pac1_item_lapis[2]):
            #Botão de coleta para o item lapis (obrigatorio no 2 dia)
            imagebutton:
                action Jump("PAC1_SELECIONA_LAPIS")
                idle pac1_img_lapis
                focus_mask True
                xalign 0.572
                yalign 0.850

        #Botão de coleta para o item  (não obrigatorio no 12 dia)
        imagebutton:
            action Jump("PAC1_SELECIONA_LIVROS")
            idle pac1_img_livros
            focus_mask True
            xalign 0.750
            yalign 0.831


        #Botão de coleta para o item  (não obrigatorio no 2 dia)
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




label PAC2_SELECIONA_GAVETA:
    if(not pac2_item_gravador[2]):
        "Espera, deve ter algo a mais atrás da cômoda."
        "Talvez se eu empurrar..."
        "Isso, tem duas gavetas escondidas!"
        "Vamos ver o que há dentro delas..."
        show screen mostra_item(pac2_item_gravador[0]) with dissolve
        pause 0.3
        "Um gravador. Está com a tampa aberta."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Gravador!")
        python:
            pac2_item_gravador[2] = True
            pac1_itens_no_inventario.append(pac2_item_gravador)

        "Também tem mais uma coisa..."
        show screen mostra_item(pac2_item_tesoura[0]) with dissolve
        pause 0.3
        "Uma tesoura. Vou levar, talvez me seja útil..."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Tesoura!")
        python:
            pac2_item_tesoura[2] = True
            pac1_itens_no_inventario.append(pac2_item_tesoura)

        #Se selecionar a outra pista essencial também, pode sair
        if(pac1_item_lapis[2]):
            "Acho que já coletei todas as pistas que eu precisava..."
            drc "Acho que isto é suficiente, She..."
            "É verdade..."
            "Ele não está mais aqui..."
            "Mas tudo bem. Vou fazer isso por ele. Pela Kamira também!"
            "Vou descobrir quem está por trás desses assassinatos!"
            "Só para garantir, acho que vou dar uma última olhada."
            $pac2_fim = True
    else:
        "Já retirei tudo que estava escondido da cômoda. Não preciso mais olhá-la."
    jump POINT_AND_CLICK
