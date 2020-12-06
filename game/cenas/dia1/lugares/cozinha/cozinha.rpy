label COZINHA:
    shp "Ok. Favor me seguir, detetive."
    drc "Certo."

    play sound "audio/sonoplastia/Passos.mp3"
    scene cozinha
    with Fade(2, 1, 0.5)

    show sheppard neutro:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    shp "Esta é a cozinha. Aquela que o senhor vê ali é Martha, a empregada da família."

    play sound "audio/sonoplastia/Pratos.mp3"
    $renpy.pause(3, hard=hardPause)

    shp "Como vai, Martha?"

    show sheppard neutro with moveinright:
        xzoom 0.9 yzoom 0.9 xalign 0.7 yalign 0.99999

    show martha neutra:
        xzoom 0.85 yzoom 0.85 xalign 0.3 yalign 0.99999

    mrth "Senhor Sheppard, boa tarde para o senhor."
    drc "Prazer, senhora, detetive Rightclue."
    mrth "Encantada, detetive."
    drc "Senhora Martha, espero que a senhora não se importe que eu te faça algumas perguntas?"
    mrth "Por favor, faça à vontade. O que eu puder contribuir para a investigação, assim farei."
    drc "A senhora teve muito contato com o senhor Hougin?"
    mrth "Claro que sim, estou trabalhando aqui há 30 anos."
    drc "A senhora tinha boa relação com seu empregador, o senhor Hougin?"
    mrth "O senhor Hougin sempre foi como um parente. Estimo muito esse trabalho e essa família."
    drc "A senhora tinha conhecimento das movimentações da casa?"
    mrth "Precisamente. Ao andar por esses corredores por tantos anos, acabamos reconhecendo padrões."
    drc "A senhora estava presente no dia do assassinato do senhor Hougin?"
    mrth "Claro que sim. Havia uma grande festa de aniversário para o senhor Lostie."
    drc "Espere um pouco. Estão me dizendo que o senhor Hougin Cashand foi assassinado durante uma comemoração?"
    shp "Precisamente, senhor Rightclue. Não me achei na posição de contar algo desse tipo ao senhor, visto que o senhor descobriria por si mesmo, e talvez, eu o influenciasse de alguma forma inicial."
    drc "Tudo bem, Sheppard. Compreendo."

    menu:
        "E só me contam agora... O que eu deveria fazer?"

        "Voltar para a sala e decidir":
            drc "Creio que já ouvi o bastante por aqui, vamos voltar, senhor Sheppard."
            shp "Certo, detetive."
            if primeira_visita:
                $primeira_visita = False
                jump TRANSICAO1
            else:
                jump TRANSICAO2

        "Pedir mais informações à Martha":
            jump OUVIR_MARTHA
