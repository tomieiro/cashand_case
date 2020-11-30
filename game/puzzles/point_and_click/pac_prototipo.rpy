#Tem que ter 1 tela para cada point-and-click

define pacp_img_puzzle = "images/prototipo/tranca_%s.png"
define pacp_img_estante = "images/prototipo/gaveta_%s.png"
define pacp_img_vela = "images/prototipo/vela_%s.png"
define pacp_img_inv_but = "images/inventario/bg_seta.png"

#ATENÇÃO: GARANTIR QUE OS ITENS POSSUEM ID'S DIFERENTES
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
default pacp_item_vela = ["images/prototipo/vela_idle.png", "Uma simples vela.", False, 0, False, "IDE_ESCOLHEU_VELA"]
default pacp_item_vela2 = ["images/prototipo/vela_idle.png", "Uma simples vela.", False, 0, False, "IDE_ESCOLHEU_VELA2"]
default pacp_item_vela3 = ["images/prototipo/vela_idle.png", "Uma simples vela.", False, 0, False, "IDE_ESCOLHEU_VELA3"]
default pacp_item_vela4 = ["images/prototipo/vela_idle.png", "Uma simples vela.", False, 0, False, "IDE_ESCOLHEU_VELA4"]
default pacp_item_vela5 = ["images/prototipo/vela_idle.png", "Uma simples vela.", False, 0, False, "IDE_ESCOLHEU_VELA5"]
default pacp_item_cookie = ["images/prototipo/cookie.png", "Um cookie aparentemente delicioso!", False, 1, False, "IDE_ESCOLHEU_COOKIE"]


default pacp_itens_no_inventario = []

#Label responsável por inicializar variáveis e chamar a tela
label CHAMA_TELA_PAC_PROTOTIPO:
    python:
        pacp_item_vela[2] = False
        pacp_item_cookie[2] = False
        pacp_itens_no_inventario = []
    play music "audio/musicas/Pistas.mp3" fadeout 1
    #Chama a tela de point and click
    show screen point_and_click_prototipo() with dissolve
    jump POINT_AND_CLICK

screen point_and_click_prototipo():

    #Sensível a cliques apenas quando não há diálogo acontecendo
    sensitive(  not renpy.get_screen("say") and
                not renpy.get_screen("inventario_de_coleta") and
                not renpy.get_screen("mostra_item") and
                not renpy.get_screen("mostra_item2")
                )

    frame:
        background "images/cenarios/escritorio.png"
        xsize 1280
        ysize 720

        #Exemplo de botão que chama um puzzle
        imagebutton:
            action Jump("SLIDER_TEST")
            auto pacp_img_puzzle
            focus_mask True
            xalign 0.432
            yalign 0.47

        #Exemplo de botão que inicia uma interação e coleta um item
        imagebutton:
            action Jump("PACP_SELECIONA_ESTANTE")
            auto pacp_img_estante
            focus_mask True
            xalign 0.462
            yalign 0.632

        #Exemplo de botão que coleta, explicitamente, um item da tela
        if(not pacp_item_vela[2]):
            imagebutton:
                action Jump("PACP_SELECIONA_VELA")
                auto pacp_img_vela
                focus_mask True
                xalign 0.4064
                yalign 0.835

        if(not pacp_item_vela2[2]):
            imagebutton:
                action Jump("PACP_SELECIONA_VELA2")
                auto pacp_img_vela
                focus_mask True
                xalign 0.752
                yalign 0.210

        if(not pacp_item_vela3[2]):
            imagebutton:
                action Jump("PACP_SELECIONA_VELA3")
                auto pacp_img_vela
                focus_mask True
                xalign 0.632
                yalign 0.112

        if(not pacp_item_vela4[2]):
            imagebutton:
                action Jump("PACP_SELECIONA_VELA4")
                auto pacp_img_vela
                focus_mask True
                xalign 0.932
                yalign 0.120

        if(not pacp_item_vela5[2]):
            imagebutton:
                action Jump("PACP_SELECIONA_VELA5")
                auto pacp_img_vela
                focus_mask True
                xalign 0.522
                yalign 0.365

        #Exemplo de botão para abrir inventário de coleta
        imagebutton:
            action Show("inventario_de_coleta", itens_no_inventario=pacp_itens_no_inventario)
            auto "images/inventario/bg_seta_%s.png"
            #idle pacp_img_inv_but
            at idc_botao_abrir


label PACP_SELECIONA_ESTANTE:
    if(not pacp_item_cookie[2]):
        shp_side "Quer investigar essa gaveta?"
        drc "Será que há algum item nela?"
        drc "Olha só!"
        $renpy.notify("Coletou cookie!")
        show screen mostra_item(pacp_item_cookie[0]) with dissolve
        pause 0.3
        "Minha barriga estava roncando agora a pouco. Este cookie pode ser útil..."
        python:
            pacp_item_cookie[2] = True
            pacp_itens_no_inventario.append(pacp_item_cookie)
        hide screen mostra_item with dissolve
        shp_side "Mas eu tava deixando pra mais tar..."
        drc "Delicioso!"
        drc "O que? o senhor disse algo?"
        shp_side "Ah, deixa pra lá..."
    else:
        "Acho que não há mais nada que eu possa pegar por aqui..."
        shp_side "Ufa, ainda bem que ele não viu o burrito..."
        drc "Disse alguma coisa?"
        shp_side "Não, nada..."
        drc "Ok..."
    jump POINT_AND_CLICK

label PACP_SELECIONA_VELA:
    $renpy.notify("Coletou uma pista - Vela!")
    show screen mostra_item(pacp_item_vela[0]) with dissolve
    pause 0.3
    "É apenas uma vela comum, mas vou me lembrar dela!"
    python:
        pacp_item_vela[2] = True
        pacp_itens_no_inventario.append(pacp_item_vela)
    hide screen mostra_item with dissolve
    jump POINT_AND_CLICK


label PACP_SELECIONA_VELA2:
    $renpy.notify("Coletou uma pista - Vela!")
    show screen mostra_item(pacp_item_vela2[0]) with dissolve
    pause 0.3
    "É apenas uma vela comum, mas vou me lembrar dela!"
    python:
        pacp_item_vela2[2] = True
        pacp_itens_no_inventario.append(pacp_item_vela2)
    hide screen mostra_item with dissolve
    jump POINT_AND_CLICK

label PACP_SELECIONA_VELA3:
    $renpy.notify("Coletou uma pista - Vela!")
    show screen mostra_item(pacp_item_vela3[0]) with dissolve
    pause 0.3
    "É apenas uma vela comum, mas vou me lembrar dela!"
    python:
        pacp_item_vela3[2] = True
        pacp_itens_no_inventario.append(pacp_item_vela3)
    hide screen mostra_item with dissolve
    jump POINT_AND_CLICK

label PACP_SELECIONA_VELA4:
    $renpy.notify("Coletou uma pista - Vela!")
    show screen mostra_item(pacp_item_vela4[0]) with dissolve
    pause 0.3
    "É apenas uma vela comum, mas vou me lembrar dela!"
    python:
        pacp_item_vela4[2] = True
        pacp_itens_no_inventario.append(pacp_item_vela4)
    hide screen mostra_item with dissolve
    jump POINT_AND_CLICK

label PACP_SELECIONA_VELA5:
    $renpy.notify("Coletou uma pista - Vela!")
    show screen mostra_item(pacp_item_vela5[0]) with dissolve
    pause 0.3
    "É apenas uma vela comum, mas vou me lembrar dela!"
    python:
        pacp_item_vela5[2] = True
        pacp_itens_no_inventario.append(pacp_item_vela5)
    hide screen mostra_item with dissolve
    jump POINT_AND_CLICK
