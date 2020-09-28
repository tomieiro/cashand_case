
init python:

    def seleciona_e_propaga(x, y, pecas, dim, propagando):
        if x>=0 and x<dim and y>=0 and y<dim:
            pecas[(x*dim)+y] = not pecas[(x*dim)+y]
            print(pecas)
            if propagando:
                propagando = False
                adjacentes = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
                for adj in adjacentes:
                    seleciona_e_propaga(adj[0], adj[1], pecas, dim, propagando)
                propagando = True

    def confere_fim_puzzle(pecas, fim, dim):
        retorno = True
        for i in range(dim*dim):
            retorno = retorno and pecas[i]
        fim[0] = retorno

style grid_daora:
    spacing 10

style margem_daora:
    padding (10, 10)
    background Solid("#ff9900")

style vazio:
    size(0,0)

default fim = [False]
default pecas = [False] * 100
default x = 0
default y = 0
default propagando = True

screen lights_out_puzzle(dim):
    window:
        style "tela_cheia"
        hbox:
            at truecenter
            xsize 1280
            frame:
                if fim[0]:
                    xalign 0.3
                    yalign 0.5
                else:
                    at truecenter
                style "margem_daora"
                grid dim dim:
                    style "grid_daora"
                    for i in range(dim*dim):
                        $x = int(i/dim)
                        $y = i%dim
                        window:
                            style "fundo_branco"
                            imagebutton:
                                action [Function(seleciona_e_propaga, x, y, pecas, dim, propagando), Function(confere_fim_puzzle, pecas, fim, dim), renpy.restart_interaction]
                                selected (pecas[i])
                                idle "imagem_tomieiro"
                                selected_idle "imagem_angra"
            if fim[0]:
                window:
                    at truecenter
                    style "fundo_branco"
                    textbutton "Finalinar":
                        action Return()
                        at truecenter
