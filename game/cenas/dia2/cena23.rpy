label CENA23:
    scene cidade
    with Fade(3, 2, 0.5)
    "Certo..."
    "Preciso agir rapido e começar a investigar quem já chegou do enterro."
    "Kamira está ali no jardim, [ind_a_info[1]] deu a volta pelos fundos e entrou na cozinha"
    "[ind_b_info[0]] veio junto com [ind_a_info[1]]. Só Joe ainda não chegou."
    menu:
        "Vejamos..."

        "Conversar com [ind_a_info[1]]":
            "Bom... acho que melhor começar com [ind_a_info[1]]."
            "Talvez eu descubra algo..."
            drc "[ind_a_info[1]], com licença, podemos conversar um instante?"
            if ind_a_info == hugo_info:
                ind_a "Senhor Rightclue..."
                ind_a "Claro."
                drc "Meus pêsames pelo Sheppard."

            else:
            ind_a "O que deseja, detetive?"
            drc "Meus pêsames por outra perda. Eu gostaria que soubesse que gastarei todo meu esforço para descobrir quem está por trás disso."
            ind_a "Não é nada fácil."
            ind_a "O senhor parece determinado. Estamos sem tempo detetive. O culpado está nos eliminando. Um a um. Precisamos de respostas."
            drc "Confie em mim, [ind_a_info[1]]. Mas preciso de sua cooperação."
            drc "Me conte o que viu na noite em que seu [ind_a_info[2]] foi assassinado. Quem subiu ao quarto?"
            ind_a "..."
            ind_a "Pois bem. Naquela noite me encontrei com Hugo e Kamira no saguão. Sheppard estava lá também."
            ind_a "Após várias garrafas de espumante, meu [ind_a_info[2]] subiu ao quarto, não passava bem por suas complicações de saúde e ainda sim, insistia em beber".
            drc "Estamos indo bem. O que mais [ind_a_info[1]]?"
            ind_a "Após beber mais algumas taças, senti que precisava checar se ele estava bem."
            ind_a "Foi então que subi ao quarto."

        "Conversar com [ind_b_info[1]]":

        "Conversar com a Kamira:"
            kmr "O que deseja, detetive?"
            drc "Meus pêsames por outra perda. Eu gostaria que soubesse que gastarei todo meu esforço para descobrir quem está por trás disso."
            kmr "Mesmo agora, o senhor permanece. Por que?"
            drc "Fui inspirado por um certo homem, que permaneceu leal a sua palavra, mesmo depois de quem exigiu, partir."
            drc "Encontrei o culpado, pode ter certeza. Mas preciso da sua colaboração."


#jump CENA24
