image pac3_img_abajur:
    "images/engler/itens_no_cenario/abajur_cen.png"

image pac3_img_gaveta1:
    "images/engler/itens_no_cenario/gaveta1.png"
    xzoom -1.0

image pac3_img_gaveta2:
    "images/engler/itens_no_cenario/gaveta2.png"
    xzoom -1.0

#ATENÇÃO: GARANTIR QUE OS ITENS POSSUEM ID'S DIFERENTES
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]

default pac3_item_chave = ["images/engler/itens/chave.png", "Uma chave. Estava muito bem escondida...", False, 31, False, "IDE_03_ESCOLHEU_CHAVE"]
default pac3_item_cofre = ["images/engler/itens/cofre.png", "Um cofre. O que será que ele guarda?", False, 32, False, "IDE_03_ESCOLHEU_COFRE"]

default pac3_item_telefone = ["images/engler/itens_no_cenario/telefone.png", "Um telefone. Por algum motivo, Joe deixa o aparelho no chão do quarto...", False, 33, False, "IDE_03_ESCOLHEU_TELEFONE"]
default pac3_item_vitrola = ["images/engler/itens_no_cenario/vitrola.png", "Uma vitrola. Joe deve gostar de escutar algumas músicas.", False, 34, False, "IDE_03_ESCOLHEU_VITROLA"]
default pac3_item_vela = ["images/engler/itens_no_cenario/vela.png", "Uma vela. Está pendurada na parede do quarto do Joe.", False, 35, False, "IDE_03_ESCOLHEU_VELA"]
default pac3_item_radio = ["images/engler/itens_no_cenario/radio.png", "Um rádio. Estava dentro da gaveta do Joe.", False, 36, False, "IDE_03_ESCOLHEU_RADIO"]

default pac3_fim = False

#Label responsável por inicializar variáveis e chamar a tela
label CHAMA_TELA_PAC_DIA3:
    #Inicializa as variáveis necessárias
    python:
        pac3_fim = False
        pac3_item_chave[2] = False
        pac3_item_cofre[2] = False
        pac3_item_telefone[2] = False
        pac3_item_vitrola[2] = False
        pac3_item_vela[2] = False
        #... outros itens "inuteis"
        #pac1_itens_no_inventario = []

    #Chama a tela de point and click
    play music "audio/musicas/Tensao.mp3" fadein 5.0
    show screen point_and_click_dia3() with dissolve
    jump POINT_AND_CLICK

label FIM_TELA_PAC_DIA3:
    stop music fadeout 5.0
    python:
        if(len(pac1_itens_no_inventario) == 3):
            #pegou apenas o lenco, o cofre e a chave
            persistent.pac3 = True
            renpy.notify("Conquista - Passado Guardado!")
            conferir_todas_conquistas()
    hide screen point_and_click_dia3 with dissolve
    return

screen point_and_click_dia3():

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
        background "images/engler/cenarios/quarto joe.png"
        xsize 1280
        ysize 720

        #Botão de saída do puzzle(APENAS QUANDO COLETOU, NO MÍNIMO, AS PISTAS DO SANGUE E DO RELÓGIO)
        if(pac3_fim):
            imagebutton:
                action Jump("FIM_TELA_PAC_DIA3")
                auto pac1_img_saida
                #idle pac1_img_saida
                at idc_botao_sair
                focus_mask True

        #Botão que inicia uma interação no abajur e coleta o item chave
        imagebutton:
            action Jump("PAC3_SELECIONA_ABAJUR")
            idle "pac3_img_abajur"
            focus_mask True
            xalign 0.15
            yalign -0.01

        #Botão de coleta para o item cofre
        imagebutton:
            action Jump("PAC3_SELECIONA_COFRE")
            idle "images/engler/itens_no_cenario/cofre_do_quarto2.png"
            focus_mask True
            xalign 0.22
            yalign 0.805

        #Botão de coleta para o item gaveta 1
        imagebutton:
            action Jump("PAC3_SELECIONA_GAVETA")
            idle "pac3_img_gaveta1"
            focus_mask True
            xalign 0.272
            yalign 0.910

        #Botão de coleta para o item gaveta 2
        imagebutton:
            action Jump("PAC3_SELECIONA_GAVETA")
            idle "pac3_img_gaveta2"
            focus_mask True
            xalign 0.150
            yalign 0.915

        #Botão de coleta para o item telefone
        imagebutton:
            action Jump("PAC3_SELECIONA_TELEFONE")
            idle "images/engler/itens_no_cenario/telefone_cen.png"
            focus_mask True
            xalign -0.005
            yalign 0.844

        #Botão de coleta para o item vitrola
        imagebutton:
            action Jump("PAC3_SELECIONA_VITROLA")
            idle "images/engler/itens_no_cenario/vitrola_cen.png"
            focus_mask True
            xalign 0.1275
            yalign 0.46

        #Botão de coleta para o item vela
        imagebutton:
            action Jump("PAC3_SELECIONA_VELA")
            idle "images/engler/itens_no_cenario/vela_cen.png"
            focus_mask True
            xalign 0.963
            yalign 0.115

        #Botão para abrir inventário de coleta
        imagebutton:
            action Show("inventario_de_coleta", itens_no_inventario=pac1_itens_no_inventario)
            auto "images/inventario/bg_seta_%s.png"
            activate_sound "audio/sonoplastia/AbrindoPasta.mp3"
            #idle pac1_img_inv_but
            at idc_botao_abrir



label PAC3_SELECIONA_ABAJUR:
    if(not pac3_item_chave[2]):
        "Parece ter algo dentro do abajur..."
        show screen mostra_item(pac3_item_chave[0]) with dissolve
        pause 0.3
        "Uma chave..."
        "Estava muito bem escondida."
        "Mas por quê?"
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Chave!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            #renpy.pause(1, hard=hardPause)
            pac3_item_chave[2] = True
            pac1_itens_no_inventario.append(pac3_item_chave)
        #Se selecionar a outra pista essencial também, pode sair
        if(pac3_item_cofre[2]):
            "Acho que já coletei todas as pistas que eu precisava..."
            "Vamos lá, estou quase acabando com isso!"
            $pac3_fim = True
    else:
        "Não há mais nada escondido no abajur."
    jump POINT_AND_CLICK

label PAC3_SELECIONA_COFRE:
    if(not pac3_item_cofre[2]):
        show screen mostra_item(pac3_item_cofre[0]) with dissolve
        pause 0.3
        "Interessante..."
        "Então, o Joe tem um cofre..."
        "O que será que ele guarda nele?"
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Cofre!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            #renpy.pause(1, hard=hardPause)
            pac3_item_cofre[2] = True
            pac1_itens_no_inventario.append(pac3_item_cofre)
        #Se selecionar a outra pista essencial também, pode sair
        if(pac3_item_chave[2]):
            "Acho que já coletei todas as pistas que eu precisava..."
            "Vamos lá, estou quase acabando com isso!"
            $pac3_fim = True
    else:
        "Já vi o cofre. O que será que o Joe guarda nele?"
    jump POINT_AND_CLICK

label PAC3_SELECIONA_GAVETA:
    if(not pac3_item_radio[2]):
        show screen mostra_item(pac3_item_radio[0]) with dissolve
        pause 0.3
        "Um rádio."
        "Estava guardado na gaveta."
        "Talvez não esteja mais funcionando..."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Rádio!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            #renpy.pause(1, hard=hardPause)
            pac3_item_radio[2] = True
            pac1_itens_no_inventario.append(pac3_item_radio)
    else:
        "Já vi as gavetas. Não há mais nada nelas."
    jump POINT_AND_CLICK

label PAC3_SELECIONA_TELEFONE:
    if(not pac3_item_telefone[2]):
        show screen mostra_item(pac3_item_telefone[0]) with dissolve
        pause 0.3
        "Um telefone..."
        "Está num lugar um pouco... estranho..."
        "O Joe parece ser um rapaz meio desorganizado..."
        "Ou gosta muito de falar no telefone sentado."
        "Mas, enfim, de volta à investigação..."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Telefone!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            #renpy.pause(1, hard=hardPause)
            pac3_item_telefone[2] = True
            pac1_itens_no_inventario.append(pac3_item_telefone)
    else:
        "Não preciso mais ver o telefone..."
    jump POINT_AND_CLICK

label PAC3_SELECIONA_VITROLA:
    if(not pac3_item_vitrola[2]):
        show screen mostra_item(pac3_item_vitrola[0]) with dissolve
        pause 0.3
        "Uma vitrola."
        "Parece que o Joe gosta de escutar uma boa música na tranquilidade de seu quarto."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Vitrola!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            #renpy.pause(1, hard=hardPause)
            pac3_item_vitrola[2] = True
            pac1_itens_no_inventario.append(pac3_item_vitrola)
    else:
        "Não preciso mais ver a vitrola..."
    jump POINT_AND_CLICK

label PAC3_SELECIONA_VELA:
    if(not pac3_item_vela[2]):
        show screen mostra_item(pac3_item_vela[0]) with dissolve
        pause 0.3
        "Uma vela."
        "Está pendurada na parede do quarto."
        "Mas o que me incomoda é que está muito perto da cama..."
        "Pode causar um incêndio."
        "Joe não leva jeito para essas coisas mesmo..."
        hide screen mostra_item with dissolve
        $renpy.notify("Coletou Pista - Vela!")
        play sound "audio/sonoplastia/ColetandoPista.mp3"
        python:
            #renpy.pause(1, hard=hardPause)
            pac3_item_vela[2] = True
            pac1_itens_no_inventario.append(pac3_item_vela)
    else:
        "Já investiguei a vela."
    jump POINT_AND_CLICK
