init python:

    def timer_puzzle(st, at,
                        tempo_total = 10.0,
                        label_fim_tempo = 'FIM_LOP_3x3',
                        screen = 'lights_out_puzzle',
                        style_ok = 'lop_text_timer_ok',
                        style_acabando = 'lop_text_timer_acabando',
                        tempo_troca = 5.0,
                        formato_texto = "{minutes:02d}:{seconds:02d}" ,
                        fim = False):

        global lop_proximo_do_fim

        restante = tempo_total - st

        print(restante)

        parts_dict = {
            'minutes' : int( restante // 60 ),
            'seconds' : int( restante % 60 ),
            'micro_seconds' : str(int( (restante % 1) * 10000 )), # we use str() so we can define precision
        }

        if restante <= tempo_troca and not lop_proximo_do_fim:
            lop_proximo_do_fim = True
            renpy.music.play(filenames="audio/musicas/Dilema.mp3", channel="music", loop=True)

        if restante <= 0.0 and not fim:
            renpy.hide_screen(screen)
            renpy.jump(label_fim_tempo)

        return Text( formato_texto.format(**parts_dict),
                     style = style_ok if restante > tempo_troca else style_acabando), .1


default lop_fim = False
default lop_pecas = [False] * 9
default lop_x = 0
default lop_y = 0
default lop_tam_peca = 200

default lop_img_pecas = ["images/teste/puzzle/9.png", "images/teste/puzzle/8.png", "images/teste/puzzle/7.png",
                         "images/teste/puzzle/6.png", "images/teste/puzzle/5.png", "images/teste/puzzle/4.png",
                         "images/teste/puzzle/3.png", "images/teste/puzzle/2.png", "images/teste/puzzle/1.png"]

default lop_configuracoes = [[]]

default lop_game_over_label = "FIM_LOP_3x3"

default lop_proximo_do_fim = False

transform lop_img_tr(tam=200):
    size (tam, tam)
    xalign 0.5
    yalign 0.5


screen lights_out_puzzle(dim, img_bg = "#fff"):

    modal True

    #Sensível apenas quando não há diálogo ocorrendo
    sensitive (not lop_fim)

    frame:
        style "lop_tela_cheia"
        background img_bg
        if(not lop_fim):
            add DynamicDisplayable( timer_puzzle,
                                    tempo_total=120.0,
                                    tempo_troca=30.0,
                                    label_fim_tempo = lop_game_over_label,
                                    screen = 'lights_out_puzzle',
                                    style_ok = 'lop_text_timer_ok',
                                    style_acabando = 'lop_text_timer_acabando',
                                    fim = lop_fim
                                    ) at topright

        vbox:
            at truecenter
            frame:
                at truecenter
                style "lop_margem"
                grid dim dim:
                    style "lop_grid"
                    for i in range(dim*dim):
                        $lop_x, lop_y = converte_para_duas_dimensoes(i, dim)
                        frame:
                            style "lop_fundo_branco"
                            imagebutton:
                                action [Function(seleciona_e_propaga, dim, lop_x, lop_y), Function(confere_fim_puzzle, dim), renpy.restart_interaction]
                                selected (lop_pecas[i])
                                idle "#000"
                                selected_idle lop_img_pecas[i]
                                selected_hover lop_img_pecas[i]
                                at lop_img_tr(lop_tam_peca)

    if lop_fim:

        add "images/teste/puzzle/cc.png" maxsize (630, 630) at truecenter
        timer 3.0 action Return()


init python:

    def seleciona_e_propaga(dim, x, y):
        global lop_pecas
        if seleciona_sem_propagar(dim, x, y):
            adjacentes = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
            for adj in adjacentes:
                seleciona_sem_propagar(dim, adj[0], adj[1])


    def seleciona_sem_propagar(dim, x, y):
        global lop_pecas
        if x>=0 and x<dim and y>=0 and y<dim:
            i = converte_para_uma_dimensao(x, y, dim)
            lop_pecas[i] = not lop_pecas[i]
            return True
        return False

    def converte_para_duas_dimensoes(i, dim):
        x = int(i/dim)
        y = i%dim
        return x, y

    def converte_para_uma_dimensao(x, y, dim):
        return (x*dim)+y

    def confere_fim_puzzle(dim):
        global lop_pecas
        global lop_fim
        retorno = True
        for i in range(dim*dim):
            retorno = retorno and lop_pecas[i]
        lop_fim = retorno


style lop_grid:
    spacing 10

style lop_margem:
    padding (10, 10)
    background Solid("#ff9900")

style lop_tela_cheia:
    background Solid("#000000")
    xsize 1280
    ysize 720

style lop_fundo_branco:
    background Solid("#ffffff")

transform surge_botao_final:
    xalign 0.5
    yalign 0.5


style lop_text_timer_ok:
    size 60
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style lop_text_timer_acabando:
    size 60
    color "#F22"
    outlines [(2, "#000", 0, 0)]

style lop_text_timer_fim:
    size 60
    color "#2F2"
    outlines [(2, "#000", 0, 0)]
