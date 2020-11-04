init offset = 0

#Sons dos diálogos dos personagens:
init python:
    def character_beeps(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voices/voice_test.wav", loop="True", channel="sound")
        #elif event == "slow_done" or event == "end":
        elif event == "slow_done":
            renpy.sound.stop(channel="sound")

#EXEMPLO: define shp = Character("Sheppard", who_color="#c8ffc8", callback=character_beeps)

#Definindo personagens fixos
define drc = Character("Rightclue", callback=character_beeps)
define shp = Character("Sheppard", callback=character_beeps)
define hgin = Character("Hougin Cashand", callback=character_beeps)
define mrth = Character("Martha", callback=character_beeps)
define vnc = Character("Carlo Venchinni", callback=character_beeps)
define hugo = Character("Hugo T. Cashand", callback=character_beeps)
define kmr = Character("Kamira Cashand", callback=character_beeps)
define cth = Character("Catherine V. Cashand", callback=character_beeps)
define desconhecido = Character("???", callback=character_beeps)

#Definindo Informações dos personagens aleatórios
define joe_info =  ["Joe Cashand","Joe","pai","irmão"]
define catherine_info = ["Catherine V. Cashand","Catherine","irmão","sobrinho"]
define kamira_info = ["Kamira T. Cashand","Kamira","tio","primo"]
define hugo_info = ["Hugo T. Cashand","Hugo","pai","irmão"]

#Definindo informações de personagens aleatórios que podem ser inocentes e/ou culpados
define possiveis_inocentes = [joe_info, catherine_info, kamira_info]
define possiveis_culpados = [hugo_info]

#Definindo roles aleatorias

#Inocentes:
define ind_a_info = []
define ind_b_info = []
define ind_c_info = []
define assassino_info = []

#Culpado...

#Sorteamento das roles
init offset = 1
init python:
    #Usa as variáveis declaradas anteriormente
    global ind_a_info
    global ind_b_info
    global ind_c_info
    global assassino_info
    global possiveis_inocentes
    #Sorteia as roles dos inocentes
    ind_a_info = renpy.random.choice(possiveis_inocentes)
    possiveis_inocentes.remove(ind_a_info)
    ind_b_info = renpy.random.choice(possiveis_inocentes)
    possiveis_inocentes.remove(ind_b_info)
    ind_c_info = renpy.random.choice(possiveis_inocentes)
    assassino_info = renpy.random.choice(possiveis_culpados)
    #Trocar o assassino para tratar casos

init offset = 2
define ind_a = Character(ind_a_info[0], callback=character_beeps)
define ind_b = Character(ind_b_info[0], callback=character_beeps)
define ind_c = Character(ind_c_info[0], callback=character_beeps)
define assassino = Character(assassino_info[0], callback=character_beeps)

init offset = 0

## OBSERVACOES IMPORTANTES
#
# -> CENA12 O HUGO NAO PODE SER NEM O IND_B E NEM O IND_C
# -> CENA22 O JOE NAO PODE SER O IND_A
# -> CENA 23 A KAMIRA PODE SER NEM IND_A E NEM IND_B.
#
#
## FIM
