default lop_fim = False
default lop_pecas = [False] * 9
default lop_x = 0
default lop_y = 0
default lop_tam_peca = 200

label lights_out_puzzle_3:
    #Variáveis necessárias:
    python:
        lop_fim = False
        lop_pecas = [False] * 9
        lop_x = 0
        lop_y = 0
    #Chama a tela
    call screen lights_out_puzzle(3)
    return

screen lights_out_puzzle(dim,
img_bg = "#000",
img_bot_idle="images/teste/dogbutton_idle.jpg",
img_bot_hover="images/teste/dogbutton_hover.jpg",
img_bot_selected_idle="images/teste/dogbutton_selected_idle.jpg",
img_bot_selected_hover="images/teste/dogbutton_selected_hover.jpg"):

    default bot_idle = im.Scale(img_bot_idle, lop_tam_peca, lop_tam_peca)
    default bot_hover = im.Scale(img_bot_hover, lop_tam_peca, lop_tam_peca)
    default bot_selected_idle = im.Scale(img_bot_selected_idle, lop_tam_peca, lop_tam_peca)
    default bot_selected_hover = im.Scale(img_bot_selected_hover, lop_tam_peca, lop_tam_peca)

    if lop_fim:
        timer 1.0 action Return()

    frame:
        style "lop_tela_cheia"
        background img_bg
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
                                idle bot_idle
                                hover bot_hover
                                selected_idle bot_selected_idle
                                selected_hover bot_selected_hover
            #if lop_fim:
                #frame:
                    #at truecenter
                    #style "lop_fundo_branco"
                    #textbutton "Finalizar":
                        #action Return()
                        #at surge_botao_final



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
