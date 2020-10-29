init offset = 0

#Definindo personagens fixos
define drc = Character("Rightclue")
define shp = Character("Sheppard")
define mrth = Character("Martha")
define vnc = Character("Carlo Venchinni")
define hugo = Character("Hugo T. Cashand")
define carlo = Character("Carlo Venchinni")
define desconhecido = Character("???")

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
define ind_a = Character(ind_a_info[0])
define ind_b = Character(ind_b_info[0])
define ind_c = Character(ind_c_info[0])
define assassino = Character(assassino_info[0])

init offset = 0

## OBSERVACOES IMPORTANTES
#
# -> CENA12 O HUGO NAO PODE SER NEM O IND_B E NEM O IND_C
# -> CENA22 O JOE NAO PODE SER O IND_A
# -> CENA 23 A KAMIRA PODE SER NEM IND_A E NEM IND_B.
#
#
## FIM
