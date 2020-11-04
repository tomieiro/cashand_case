#Tem que ter 1 tela para cada point-and-click

define pact_img_puzzle = "images/teste/puzzle_%s.png"
define pact_img_estante = "images/teste/estante_%s.png"
define pact_img_copo = "images/teste/water_%s.png"
define pact_img_inv_but = "images/teste/inv_but_idle.png"

#ATENÇÃO: GARANTIR QUE OS ITENS POSSUEM ID'S DIFERENTES
#Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
#                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
default pact_item_copo = ["images/teste/water_idle.png", "Um copo com água.", False, 0, False, "IDE_ESCOLHEU_COPO"]
default pact_item_cookie = ["images/teste/cookie.png", "Um cookie aparentemente 'Delicious'!", False, 1, False, "IDE_ESCOLHEU_COOKIE"]
default pact_item_seiji = ["#fff", "Não está presente...", True, 2, False, "IDE_ESCOLHEU_SEIJI"]

default pact_itens_no_inventario = [pact_item_seiji]

#Label responsável por inicializar variáveis e chamar a tela
label CHAMA_TELA_PAC_TESTE:
    python:
        pact_item_copo[2] = False
        pact_item_cookie[2] = False
        pact_itens_no_inventario = [pact_item_seiji]
    #Chama a tela de point and click
    show screen point_and_click_teste() with dissolve
    jump POINT_AND_CLICK


screen point_and_click_teste():

    #Sensível a cliques apenas quando não há diálogo acontecendo
    sensitive(not renpy.get_screen("say"))

    frame:
        background "images/teste/bg_test.png"
        xsize 1280
        ysize 720

        #Exemplo de botão que chama um puzzle
        imagebutton:
            #action Jump("LIGHTS_OUT_TEST")
            action Jump("FIM_PAC_TESTE")
            auto pact_img_puzzle
            focus_mask True
            xalign 0.8
            yalign 0.3

        #Exemplo de botão que inicia uma interação e coleta um item
        imagebutton:
            action Jump("SELECIONA_ESTANTE")
            auto pact_img_estante
            focus_mask True
            xalign 0.30
            yalign 0.50

        #Exemplo de botão que coleta, explicitamente, um item da tela
        if(not pact_item_copo[2]):
            imagebutton:
                action Jump("SELECIONA_COPO")
                auto pact_img_copo
                focus_mask True
                xalign 0.33
                yalign 0.24

        #Exemplo de botão para abrir inventário de coleta
        imagebutton:
            action Show("inventario_de_coleta", itens_no_inventario=pact_itens_no_inventario)
            idle pact_img_inv_but
            at idc_botao_abrir


label SELECIONA_ESTANTE:
    if(not pact_item_cookie[2]):
        show sheppard neutro onlayer screens at center with dissolve
        shp "Quer investigar esse criado mudo?"
        drc "Será que há algum item nele?"
        drc "Olha só!"
        $renpy.notify("Coletou cookie!")
        show screen mostra_item(pact_item_cookie[0]) with dissolve
        pause 0.3
        "Minha barriga estava roncando agora a pouco. Este cookie pode ser útil..."
        python:
            pact_item_cookie[2] = True
            pact_itens_no_inventario.append(pact_item_cookie)
        hide screen mostra_item with dissolve
        shp "Mas eu tava deixando pra mais tar..."
        drc "Delicioso!"
        drc "O que? o senhor disse algo?"
        shp "Ah, deixa pra lá..."
        hide sheppard onlayer screens with dissolve
    else:
        "Acho que não há mais nada que eu possa pegar por aqui..."
        show sheppard neutro onlayer screens at center with dissolve
        shp "Ufa, ainda bem que ele não viu o burrito..."
        drc "Disse alguma coisa?"
        shp "Não, nada..."
        drc "Ok..."
        hide sheppard onlayer screens with dissolve
    jump POINT_AND_CLICK

label SELECIONA_COPO:
    $renpy.notify("Coletou copo com água!")
    show screen mostra_item(pact_item_copo[0]) with dissolve
    pause 0.3
    "Estou com sede, acho que este copo pode ser útil!"
    python:
        pact_item_copo[2] = True
        pact_itens_no_inventario.append(pact_item_copo)
    hide screen mostra_item with dissolve
    jump POINT_AND_CLICK
