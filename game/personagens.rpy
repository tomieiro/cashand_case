#Definindo Nomes dos aleatorios
herdeiros = ["Joe Cashand", "Catherine Vladita Cashand", "Kamira Thereza Cashand", "Hugo Theodore Cashand"]
individuo_rand = renpy.random.randint(0, 2)

#Definindo Objeto Personagem
define drc = Character("Rightclue")
define shp = Character("Sheppard")
define ind_a = Character(herdeiros[individuo_rand%3])
define ind_b = Character(herdeiros[(individuo_rand+1)%3])
define ind_c = Character(herdeiros[(individuo_rand+2)%3])
define hugo = Character(herdeiros[3])
