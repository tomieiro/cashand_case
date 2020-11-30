#Desbloquear conquista -> "Bom detetive!"
#DAORA DEMAIS
label TRANSICAO1:

    scene hall
    with Fade(2, 1, 0.5)

    show sheppard neutro with dissolve:
        xzoom 0.9 yzoom 0.9 xalign 0.5 yalign 0.99999

    if cluepoints < 1:
        shp "O senhor acha que conseguimos algo, senhor Rightclue?"
        drc "Precisamente. Consegui pensar em várias situações se encaixando, várias pistas que podem levar à uma ideia inicial."
        shp "Ótimo, vamos continuar."

    else:
        shp "O senhor acha que conseguimos algo, senhor Rightclue?"
        drc "Precisamente, consegui pensar em várias situações se encaixando, várias pistas que podem levar à uma ideia inicial."
        shp "Agradeço com todas as forças sua presença, detetive."
        drc "O senhor parece ser muito apegado a essa família, senhor Sheppard."
        "*Sheppard suspira*"
        shp "Correto. Esta família me acolheu, quando eu já não tinha mais nada. O senhor Hougin era como um irmão pra mim. Seus filhos, são como meus filhos. Esta casa, é minha casa."
        drc "O senhor não teve filhos senhor Sheppard?"
        shp "..."
        pause(2)
        shp "Eu já tive família senhor detetive. Esposa, um filho e uma filha."
        drc "E o que aconteceu."
        shp "Antes de conhecer o senhor Hougin, eu era maquinista."
        shp "Saía todos os dias do trabalho e corria para casa com toda minha força que me restava. Minha família sempre foi a coisa mais importante pra mim."
        shp "O amor, senhor detetive, é o que nos dá forças todos os dias, para se levantar da cama, aguentar tudo que nos acontece, pois sabemos que, no final desses dias, aqueles sorrisos estarão lá, te esperando, te confortando."
        shp "Mas nada dura para sempre senhor Rightclue. Seres humanos são falhos."
        shp "Naquele dia, naquele maldito dia, decidi que deveria fazer outro turno. Não avisei minha esposa e filhos, e preocupados com minha ausência, saíram para me procurar."
        "*Sheppard enxuga uma lágrima*"
        shp "Cinco minutos."
        shp "Apenas cinco minutos foram necessários para destruir minha vida, minha felicidade, e tirar dela minhas maiores preciosidades."
        shp "Assim que saíram, houve um acidente. Um caminhão desgovernado, bateu contra minha família."
        drc "Sinto muito, senhor Sheppard."
        shp "Já fazem 13 longos anos. Descobri da pior forma, que não existem remédios, senhor Rightclue, que possam curar essa sofrida saudade."
        "*Rightclue consola Sheppard com dois toques nas costas*"
        shp "Mas temos um caso aqui senhor detetive. Precisamos nos concentrar no presente."
        drc "Certamente, meu amigo."
        shp "Vamos, temos muito a procurar..."

    jump MENU_ESCOLHAS_DIA1
