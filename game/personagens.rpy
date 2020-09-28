init offset = 0

#Definindo personagens fixos
define drc = Character("Rightclue")
define shp = Character("Sheppard")
define mrth = Character("Martha")

#Definindo Informações dos personagens aleatórios
define joe_info =  ["Joe Cashand","Joe","pai"]
define catherine_info = ["Catherine V. Cashand","Catherine","tio"]
define kamira_info = ["Kamira T. Cashand","Kamira","irmão"]
define hugo_info = ["Hugo T. Cashand","Hugo","pai"]

#Definindo informações de personagens aleatórios que podem ser inocentes e/ou culpados
define possiveis_inocentes = [joe_info, catherine_info, kamira_info]
define possiveis_culpados = [hugo_info]

#Definindo roles aleatorias

#Inocentes:
define ind_a_info = []
define ind_b_info = []
define ind_c_info = []

#Culpado...

#Sorteamento das roles
init offset = 1
init python:
    #Usa as variáveis declaradas anteriormente
    global ind_a_info
    global ind_b_info
    global ind_c_info
    global possiveis_inocentes
    #Sorteia as roles dos inocentes
    ind_a_info = renpy.random.choice(possiveis_inocentes)
    possiveis_inocentes.remove(ind_a_info)
    ind_b_info = renpy.random.choice(possiveis_inocentes)
    possiveis_inocentes.remove(ind_b_info)
    ind_c_info = renpy.random.choice(possiveis_inocentes)
    print(ind_a_info, ind_b_info, ind_c_info)


init offset = 2
define ind_a = Character(ind_a_info[0])
define ind_b = Character(ind_b_info[0])
define ind_c = Character(ind_c_info[0])

#Inicialmente, há apenas 1 possível culpado
define hugo = Character(possiveis_culpados[0][0])

init offset = 0
