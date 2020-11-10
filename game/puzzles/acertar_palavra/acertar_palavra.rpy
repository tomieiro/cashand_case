default app_img_bot = "images/teste/app_botao.png"

default app_fim = False

default app_a = "A"

transform app_tr:
    parallel:
        linear 2.0 xalign 0.0
        linear 2.0 xalign 1.0
        repeat
    parallel:
        linear 2.3 yalign 0.0
        linear 2.3 yalign 1.0
        repeat



screen acertar_palavra_puzzle():
    modal True

    #Sensível apenas quando o puzzle ainda não acabou
    sensitive (not app_fim)

    frame:
        style "app_tela_cheia"
        vbox:
            frame:
                style "app_tela_resposta"
            frame:
                style "app_tela_puzzle"
                frame:
                    at app_tr
                    style "app_estilo_botao"
                    textbutton "[app_a]":
                        idle_background Frame("images/teste/app_botao.png")
                        hover_background Frame("images/teste/app_botao2.png")
                        padding (30, 20)
                        focus_mask True
                        action SetVariable("app_a", "B")
                        style "app_estilo_botao"
                        text_style "app_estilo_texto"



style app_tela_cheia:
    background Solid("#000000")
    xsize 1280
    ysize 720

style app_tela_resposta:
    background Solid("#00f")
    xsize 1280
    ysize 200

style app_tela_puzzle:
    background Solid("#00e")
    xsize 1280
    ysize 520

style app_estilo_botao:
    size (100, 100)
    xalign 0.0
    yalign 0.0

style app_estilo_texto:
    color "#000"
    size 50
