default app_fonte = "fonts/Xanh_Mono/XanhMono-Regular.ttf"

default app_img_bot = "images/teste/app_botao.png"

default app_fim = False

default app_qtd_letras = 5

default app_aux = ""

default app_pre_resposta = "Angra gosta muito de..."

default app_resposta = ["_", "_", "_", "_", "_", "_", "_", "_"]

default app_rod = 0

default app_gabarito = ["G", "E", "N", "G", "I", "B", "R", "E"]

default app_letras = [
                    ["E", "G", "M", "D", "W"],
                    ["A", "T", "U", "E", "S"],
                    ["N", "F", "A", "R", "M"],
                    ["G", "Q", "Z", "I", "O"],
                    ["R", "C", "I", "D", "A"],
                    ["B", "D", "N", "G", "L"],
                    ["E", "O", "V", "L", "R"],
                    ["A", "R", "I", "E", "U"],
                    ]

default app_rodadas = 8

default app_vidas = 3

default app_erros = 0

default app_vidas_restantes = 3

transform rotation:
    rotate 11

screen acertar_palavra_puzzle():
    modal True

    #Sensível apenas quando o puzzle ainda não acabou
    sensitive (not app_fim)

    if(app_vidas <= app_erros):
        timer 0.1 action Jump("APP_TESTE_GAME_OVER")

    if(app_fim):
        timer 3.0 action Return()

    frame:
        style "app_tela_cheia"

    frame:
        at rotation
        style "app_tela_resposta"
        vbox:
            xsize 1.0
            ysize 1.0
            text "[app_pre_resposta]":
                style "app_estilo_previa"
            hbox:
                at truecenter
                for j in range(app_rodadas):
                    text app_resposta[j]:
                        style "app_estilo_resposta"
                        at truecenter
            frame:
                style "app_estilo_vidas"
                hbox:
                    xsize 1.0
                    ysize 1.0
                    for i in range(app_erros):
                        add "images/puzzle_palavras/morte.png" maxsize (80, 80)
                    for i in range(app_vidas_restantes):
                        add "images/puzzle_palavras/vida.png" maxsize (80, 80)

    frame:
        style "app_tela_puzzle"
        if(not app_fim):
            for i in range(app_qtd_letras):
                frame:
                    if(i == 0):
                        at app_tr0
                    elif(i == 1):
                        at app_tr1
                    elif(i == 2):
                        at app_tr2
                    elif(i == 3):
                        at app_tr3
                    elif(i == 4):
                        at app_tr4
                    at truecenter
                    style "app_frame_botao"
                    $app_aux = app_letras[app_rod][i]
                    textbutton "[app_aux]":
                        focus_mask True
                        action [Function(app_seleciona_letra, app_aux)]
                        style "app_estilo_botao"
                        text_style "app_estilo_texto"



init python:

    def app_seleciona_letra(letra):
        global app_rod
        global app_resposta
        global app_gabarito
        global app_fim
        global app_erros
        global app_vidas
        global app_vidas_restantes
        if(letra == app_gabarito[app_rod]):
            #Escolheu corretamente
            app_resposta[app_rod] = letra
            app_rod = app_rod + 1
            if(app_rod == app_rodadas):
                #Acabou
                app_fim = True
        else:
            app_erros = app_erros + 1
            app_vidas_restantes = app_vidas - app_erros



transform app_tr0():
    xalign 0.500
    yalign 0.500
    parallel:
        linear 3.330 xalign 0.0
        linear 3.330 xalign 1.0
        repeat
    parallel:
        linear 2.105 yalign 0.0
        linear 2.105 yalign 1.0
        repeat

transform app_tr1():
    xalign 0.333
    yalign 0.256
    parallel:
        linear 4.423 xalign 1.0
        linear 4.423 xalign 0.0
        repeat
    parallel:
        linear 1.522 yalign 0.0
        linear 1.522 yalign 1.0
        repeat

transform app_tr2():
    xalign 0.634
    yalign 0.286
    parallel:
        linear 5.015 xalign 0.0
        linear 5.015 xalign 1.0
        repeat
    parallel:
        linear 3.321 yalign 1.0
        linear 3.321 yalign 0.0
        repeat

transform app_tr3():
    xalign 0.634
    yalign 0.789
    parallel:
        linear 2.225 xalign 0.0
        linear 2.225 xalign 1.0
        repeat
    parallel:
        linear 3.799 yalign 1.0
        linear 3.799 yalign 0.0
        repeat

transform app_tr4():
    xalign 0.333
    yalign 0.789
    parallel:
        linear 3.776 xalign 1.0
        linear 3.776 xalign 0.0
        repeat
    parallel:
        linear 5.912 yalign 0.0
        linear 5.912 yalign 1.0
        repeat

style app_tela_cheia:
    background "images/puzzle_palavras/palavras.png"
    xsize 1280
    ysize 720

#(780, 127, 360, 464)
style app_tela_resposta:
    xanchor 0.0
    yanchor 0.0
    xpos 0.509375
    xsize 360
    ypos 0.17921875
    ysize 464
    background "#1110"

style app_estilo_previa:
    xalign 0.5
    yalign 0.5
    size 40
    font "fonts/Xanh_Mono/XanhMono-Regular.ttf"
    color "#000"
    text_align 0.5

style app_estilo_resposta:
    xalign 0.5
    yalign 0.5
    size 60
    font "fonts/Xanh_Mono/XanhMono-Regular.ttf"
    color "#000"
    text_align 0.5

#[27, 517, 64, 599]
style app_tela_puzzle:
    xanchor 0.0
    yanchor 0.0
    xpos 0.02109375
    xsize 517
    ypos 0.088888889
    ysize 599
    background "#0000"

style app_estilo_vidas:
    background "#0000"
    ymargin 0.30
    xsize 0.78
    xalign 0.5

style app_frame_botao:
    size (100, 100)

style app_estilo_botao is button:
    idle_background "images/teste/app_botao.png"
    hover_background "images/teste/app_botao2.png"
    size (1.0, 1.0)
    xpadding 29
    ypadding 4
    xalign 0.5
    yalign 0.5

style app_estilo_texto:
    color "#000"
    size 80
    adjust_spacing True
    font "fonts/Xanh_Mono/XanhMono-Regular.ttf"
    xalign 0.5
    yalign 0.5
