label CENA23:

    play music "audio/musicas/Pistas.mp3" fadein 2.0

    $flag_kamira = 0
    $visCoz = False

    scene jardim
    with Fade(3, 2, 0.5)

    "Certo..."
    "Preciso agir rápido e começar a investigar quem já chegou do enterro."
    "Kamira T. Cashand está ali no jardim, [ind_a_info[1]] deu a volta pelos fundos e entrou na cozinha."
    "[ind_b_info[1]] veio junto com [ind_a_info[1]] e foi para o hall. Só Joe Cashand que ainda não chegou."
    "Uma rápida olhada em volta..."

    label ESCOLHA_CONV_DIA2C3:
    menu:
        "Vejamos..."

        "Conversar com [ind_a_info[0]]" if not visCoz:

            $visCoz = True

            "Bom... acho que melhor começar com [ind_a_info[1]]."
            "Vou tentar me aproximar na cozinha."
            "Talvez eu descubra algo..."

            play sound "audio/sonoplastia/AbrindoPorta.mp3"
            scene cozinha
            with Fade(2, 1, 0.5)
            play sound "audio/sonoplastia/FechandoPorta.mp3"
            $renpy.pause(2, hard=hardPause)

            call DIALOGO_ROLES_D2C3(ind_a) from _call_DIALOGO_ROLES_D2C3

            drc "Confie em mim, [ind_a_info[1]], acharei o culpado. Mas preciso de sua cooperação."
            drc "Me conte o que viu na noite em que seu [ind_a_info[2]] foi assassinado. Quem subiu ao quarto?"
            ind_a "..."
            ind_a "Pois bem. Naquela noite, me encontrei com todos na sala. Sheppard estava lá também."
            ind_a "Após várias garrafas de espumante, meu [ind_a_info[2]] subiu ao quarto. Não passava bem por suas complicações de saúde e ainda assim insistia em beber."
            drc "Estamos indo bem. O que mais, [ind_a_info[1]]?"
            ind_a "Após beber mais algumas taças, senti que precisava checar se ele estava bem."
            ind_a "Foi então que subi ao quarto. Vi Kamira passando com lágrimas nos olhos. A segui de volta para baixo, e perguntei o que havia acontecido."
            drc "E o que ela disse?"
            ind_a "Disse que havia brigado com meu [ind_a_info[2]]."
            "..."
            drc "Entendo."
            drc "Não tem mais nada que queira me contar?"
            ind_a "O senhor tem minha palavra. Desta hora, até o momento da morte, não notei mais nada de suspeito."
            drc "Entendo."
            drc "Mais uma coisa..."
            drc "Pode me contar como era o senhor Sheppard? Digo, no dia a dia da família."
            ind_a "Sheppard era da família. Sempre foi considerado assim por todos nós."
            ind_a "Sou nesse momento, uma pessoa horrorizada por tudo isso... Meu [ind_a_info[2]], meu [ind_a_info[3]] e agora Sheppard."
            drc "Compreendo."
            drc "Certo... Acho que já é suficiente por agora. Até mais, [ind_a_info[1]]."

            hide hugo
            hide catherine

            "..."
            "Certo, já tenho um destino."

            play sound "audio/sonoplastia/AbrindoPorta.mp3"

            scene fundo preto
            with Fade(0.4, 0.4, 0.5)

            play sound "audio/sonoplastia/FechandoPorta.mp3"
            $renpy.pause(2, hard=hardPause)

            play sound "audio/sonoplastia/Passos.mp3"
            scene jardim
            with Fade(1, 4, 0.5)

            jump ESCOLHA_CONV_DIA2C3

        "Conversar com [ind_b_info[0]]" if not visHall:
            $visHall = True
            "Tentarei com [ind_b_info[1]], no Hall. Talvez eu consiga ligar as coisas obtendo detalhes de cada um."

            play sound "audio/sonoplastia/AbrindoPorta.mp3"
            $renpy.pause(2, hard=hardPause)

            scene hall
            with Fade(2, 1, 0.5)

            play sound "audio/sonoplastia/FechandoPorta.mp3"
            $renpy.pause(2, hard=hardPause)

            call DIALOGO_ROLES_D2C3(ind_b) from _call_DIALOGO_ROLES_D2C3_1

            drc "Estou ciente, [ind_b_info[1]]. Mas peço colaboração."
            drc "Me diga o que você sabe, o que você viu na noite em que seu [ind_b_info[2]] foi assassinado."
            drc "Quem subiu ao quarto?"
            ind_b "Creio ter sido a primeira pessoa a subir ao quarto. Meu [ind_b_info[2]] estava acamado."
            "Certo... Preciso ficar atento a cada detalhe."
            ind_b "Ele tossia muito. Dei-lhe água."
            ind_b "Após isso, voltei ao salão."
            ind_b "Passado algum tempo, vi descerem Kamira e [ind_a_info[1]]."
            drc "O que faziam?"
            ind_b "Kamira estava chorando ao canto e [ind_a_info[1]] a consolava."
            if not visCoz:
                drc "Sabe me dizer o motivo?"
                ind_b "Parece que houve uma discussão entre ela e meu [ind_b_info[2]]."
                drc "Certo. Mais alguma coisa?"
                ind_b "É tudo o que eu sei..."
                "Verificarei com [ind_a_info[1]] depois..."
            else:
                "Parece que [ind_a_info[1]] falava a verdade."
            drc "Entendo."
            drc "Mais uma coisa..."
            drc "Pode me contar como era o senhor Sheppard? Digo, no dia a dia da família."
            ind_b "Sheppard era uma homem leal. Fazia parte da nossa família. Nos viu crescer, dentro desta casa."
            ind_b "..."
            ind_b "Ainda não acredito que isso esteja acontecendo..."
            ind_b "É horrível, senhor"
            drc "Compreendo."
            drc "Bom, era só isso que eu precisava escutar por agora. Descanse um pouco, [ind_b_info[1]]."

            hide hugo with dissolve

            play sound "audio/sonoplastia/AbrindoPorta.mp3"
            $renpy.pause(2, hard=hardPause)

            scene fundo preto
            with Fade(0.4, 0.4, 0.5)

            play sound "audio/sonoplastia/FechandoPorta.mp3"
            $renpy.pause(1, hard=hardPause)

            play sound "audio/sonoplastia/Passos.mp3"
            scene jardim
            with Fade(2, 1, 0.5)

            if ind_a_info[1] == "Catherine": #rigato: por que isso está longe do hide do hugo? Não é um bug?
                hide catherine neutra
            "..."
            "Certo, já tenho um destino."
            jump ESCOLHA_CONV_DIA2C3


        "Conversar com Kamira T. Cashand":


            if flag_kamira == 0:
                "Ela está aflita. E parece chorar."
                "Talvez eu deva me aproximar em breve, mas darei um tempo."
                "Talvez se eu investigasse outro herdeiro..."
                $flag_kamira = 1
                jump ESCOLHA_CONV_DIA2C3

            if flag_kamira == 1:
                "Já decidi não incomodá-la. Pelo menos por agora..."
                jump ESCOLHA_CONV_DIA2C3

            if flag_kamira == 2:
                "Descobri uma evidência forte. Mas preciso de mais detalhes de terceiros antes de verificar a versão dela da história."
                "Talvez eu devesse..."
                jump ESCOLHA_CONV_DIA2C3

            "Tenho o controle da situação."
            "Devo agir com sabedoria."
            "..."
            drc "Senhorita. Com licença"

            show kamira lagrimas at center with dissolve

            kmr "O que deseja, detetive?"
            "Com calma e astúcia..."
            drc "Meus pêsames por outra perda. Eu gostaria que soubesse que gastarei todo meu esforço para descobrir quem está por trás disso."
            drc "Vocês têm a minha palavra."
            kmr "Mesmo agora, o senhor permanece. Por quê?"
            "Muito supeito... Bom, serei franco."
            drc "Fui inspirado por um certo homem, que permaneceu leal a sua palavra, mesmo depois de quem a exigiu partir."
            drc "Encontrarei o culpado, pode ter certeza. Mas preciso da sua colaboração."
            kmr "E o que o senhor precisa de mim?"
            "Ela derruba lágrimas. Serão verdadeiras?"
            "Acho difícil. Dado o que todos disseram. Mas devo ter calma..."
            drc "Preciso que me diga o que aconteceu na noite em que seu tio morreu."
            drc "Viu algo estranho? Algo diferente? O que aconteceu naquela noite, senhorita Kamira?"
            kmr "..."
            "Ela acena em negação com a cabeça. A informação que ela guarda é decisiva."
            drc "Senhorita, por favor, ajude-me a resolver isso."
            drc "Preciso da sua palavra. Minha conclusões estão convergindo para uma pessoa."
            "Tenho o controle da situação. Estou te jogando contra a parede. O que me diz?"
            kmr "..."

            show kamira chorando at center with dissolve:
                xzoom 0.99 yzoom 0.99

            kmr "Eu não pude me desculpar. Não pude."
            kmr "Poderia ter sido diferente."
            drc "Do que a senhorita fala? Me conte de uma vez."
            kmr "Era só ele ter dito..."
            kmr "Dito o maldito nome..."
            kmr "..."
            "Do que ela está falando?"
            drc "Calma, senhorita."

            show kamira lagrimas at center with dissolve

            kmr "Com licença."
            drc "Senhorita?"

            hide kamira neutra with dissolve

            "Ela se foi..."
            "Chorando."
            "Não posso errar. Minha decisão é crucial."
            #menu:
            #    "Ligar para Carlo e entregar Kamira":
            #        call ENTREGAR(kamira_info)
            #
            #    "Continuar a investigar, e ter certeza":
            "Mas também não posso me apressar e condenar alguém inocente."
            "Talvez eu deva dar uma volta pela parte externa e ver se consigo notar algo na edificação, pode ser uma possibilidade para acesso e fuga."
            "Joe chegou."
            "Ele irá direto para dentro."
            drc "Joe. Podemos conversar um instante?"

            show joe neutro with dissolve:
                xalign 0.5 yalign 0.9999999

            joe "Por favor, senhor Rightclue. Me dê um tempo."
            joe "Preciso assimilar tudo isso."
            drc "Tudo bem. Entendo."
            drc "Mas por favor, podemos conversar mais tarde?"
            joe "..."
            joe "Talvez mais tarde, detetive."

            hide joe with dissolve

            "Bom, que seja, tentarei falar com ele novamente em breve."
            "Agora, ao estudo da edificação."


            stop music fadeout(5)

            scene jardim noite
            with Fade(3, 2, 0.5)

            "..."
            jump CENA24


label DIALOGO_ROLES_D2C3(whoIs):

    if whoIs == ind_a:
        drc "[ind_a_info[1]], com licença, podemos conversar um instante?"
    else:
        drc "[ind_b_info[1]], com licença, podemos conversar um instante?"

    #Se for o Hugo...

    if str(whoIs) == "Hugo T. Cashand":

        show hugo neutro at center with dissolve

        hugo "Senhor Rightclue..."
        hugo "Claro."
        hugo "Ainda estou um pouco chocado com tudo, mas acho que uma companhia viria bem, senhor Rightclue."
        hugo "Tanto para mim, quanto para o Thorn."
        hugo "Mas ele me consola bastante."
        hugo "Não é, garotão?"
        play sound "audio/sonoplastia/Thorn.mp3"
        $renpy.pause(3, hard=hardPause)
        drc "Entendo, você e sua familia estão passando por um momento dificil."
        hugo "Está sendo difícil para todos... e tenho medo do que pode acontecer nos proximos dias com o resto de nós."

    #Se for a Catherine...
    else:

        show catherine neutra at center with dissolve

        cth "O que deseja, detetive?"
        drc "Eu gostaria que soubesse que gastarei todo meu esforço para descobrir quem está por trás disso."
        cth "O senhor permaneceu. Parece disposto a realmente resolver o caso."
        cth "É realmente uma boa pessoa, detetive."
        cth "O senhor parece determinado."
        cth "Estamos sem tempo, detetive."
        cth "O culpado está nos eliminando. Um a um."
        cth "Precisamos de respostas."

    if flag_kamira <= 1:
        $flag_kamira = 2
        return

    if flag_kamira == 2:
        $flag_kamira = 3
        return

    return
