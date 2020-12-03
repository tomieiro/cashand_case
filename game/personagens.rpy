init offset = 0

#Sons dos diálogos dos personagens:
init python:
    def rightclue_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Rightclue.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def sheppard_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Sheppard.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def joe_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Joe.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def kamira_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Kamira.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def catherine_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Catherine.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def hugo_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Hugo.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def martha_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Martha.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def carlo_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Carlo.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

    def hougin_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/Hougin.mp3", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")


#Definindo personagens fixos
define drc = Character("Rightclue", who_color="#c8c8ff", callback=rightclue_beeps)
define shp = Character("Sheppard", who_color="#c8ffc8", callback=sheppard_beeps)
define hgin = Character("Hougin Cashand", callback=hougin_beeps)
define mrth = Character("Martha", callback=martha_beeps)
define vnc = Character("Carlo Venchinni", callback=carlo_beeps)
define hugo = Character("Hugo T. Cashand", callback=hugo_beeps)
define kmr = Character("Kamira T. Cashand", who_color="#1cff91", callback=kamira_beeps)
define cth = Character("Catherine V. Cashand", callback=catherine_beeps)
define joe = Character("Joe Cashand", callback=joe_beeps)
define desconhecido = Character("???", callback=carlo_beeps)

#Imagem Side do Sheppard
define shp_side = Character("Sheppard", image="shepp", who_color="#c8ffc8", callback=sheppard_beeps)
image side shepp = "images/engler/personagens/sheppard/side sheppard neutro 1.png"

#Definindo Informações dos personagens aleatórios
define joe_info =  ["Joe Cashand","Joe","pai","irmão"]
define catherine_info = ["Catherine V. Cashand","Catherine","irmão","sobrinho"]
define kamira_info = ["Kamira T. Cashand","Kamira","tio","primo"]
define hugo_info = ["Hugo T. Cashand","Hugo","pai","irmão"]

#Definindo informações de personagens aleatórios que podem ser inocentes e/ou culpados
define possiveis_inocentes = [joe_info, catherine_info, kamira_info, hugo_info]
define inocentes_gen = []
define possiveis_culpados = [hugo_info]

#Inocentes:
define ind_a_info = []
define ind_b_info = []
define ind_c_info = []
define ind_d_info = []

#Culpado...
define assassino_info = []

init offset = 1
init python:
    def randomize(role, excecoes, clean):
        if(clean):
            inocentes_gen.clear()
            for i in possiveis_inocentes:
                if i[1] not in excecoes:
                    inocentes_gen.append(i)
        if role != []:
            role.clear()
        #Sorteia as roles dos inocentes
        role.extend(renpy.random.choice(inocentes_gen))
        inocentes_gen.remove(role)

    def apply_voices(role):
        if role[1] == "Kamira":
            return kamira_beeps
        elif role[1] == "Joe":
            return joe_beeps
        elif role[1] == "Hugo":
            return hugo_beeps
        elif role[1] == "Catherine":
            return catherine_beeps

#Sorteamento das roles
init offset = 2
init python:
    #Usa as variáveis declaradas anteriormente
    global ind_a_info
    global ind_b_info
    global ind_c_info
    global ind_d_info
    global assassino_info
    global possiveis_inocentes
    global inocentes_gen
    randomize(ind_a_info,["none"], True)
    randomize(ind_b_info,["none"], False)
    randomize(ind_c_info,["none"], False)
    randomize(ind_d_info,["none"], False)
    assassino_info = renpy.random.choice(possiveis_culpados)

init offset = 3
define ind_a = Character(ind_a_info[0], callback=apply_voices(ind_a_info))
define ind_b = Character(ind_b_info[0], callback=apply_voices(ind_b_info))
define ind_c = Character(ind_c_info[0], callback=apply_voices(ind_c_info))
define ind_d = Character(ind_d_info[0], callback=apply_voices(ind_d_info))
define assassino = Character(assassino_info[0], callback=hugo_beeps)

init offset = 0
