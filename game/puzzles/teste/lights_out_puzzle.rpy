default lop_fim = False
default lop_pecas = [False] * 9
default lop_x = 0
default lop_y = 0

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

screen lights_out_puzzle(dim):

    window:
        style "lop_tela_cheia"
        vbox:
            at truecenter
            frame:
                at truecenter
                style "lop_margem"
                grid dim dim:
                    style "lop_grid"
                    for i in range(dim*dim):
                        $lop_x, lop_y = converte_para_duas_dimensoes(i, dim)
                        window:
                            style "lop_fundo_branco"
                            imagebutton:
                                action [Function(seleciona_e_propaga, dim, lop_x, lop_y), Function(confere_fim_puzzle, dim), renpy.restart_interaction]
                                selected (lop_pecas[i])
                                auto "images/teste/dogbutton_%s.jpg"
            if lop_fim:
                window:
                    at truecenter
                    style "lop_fundo_branco"
                    textbutton "Finalizar":
                        action Return()
                        at surge_botao_final



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
