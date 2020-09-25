#Definindo Nomes dos aleatorios
define herdeiros = [["Joe Cashand","Joe","pai"], ["Catherine V. Cashand","Catherine","tio"], ["Kamira T. Cashand","Kamira","irmão"], ["Hugo T. Cashand","Hugo","pai"]]
define individuo_rand = renpy.random.randint(0, 2)

#Definindo Objeto Personagem
define drc = Character("Rightclue")
define shp = Character("Sheppard")
define mrth = Character("Martha")
define hugo = Character(herdeiros[3][0])

#Definindo roles aleatorias
define ind_a = [Character(herdeiros[individuo_rand%3][0]),herdeiros[individuo_rand%3]]
define ind_b = [Character(herdeiros[(individuo_rand+1)%3][0]),herdeiros[(individuo_rand+1)%3]]
define ind_c = [Character(herdeiros[(individuo_rand+2)%3][0]),herdeiros[(individuo_rand+2)%3]]
