label CENA23:

    default kamira_desceu = 0

    scene cidade
    with Fade(3, 2, 0.5)

    "Certo..."
    "Preciso agir rapido e começar a investigar quem já chegou do enterro."
    "Kamira está ali no jardim, [ind_a_info[1]] deu a volta pelos fundos e entrou na cozinha"
    "[ind_b_info[0]] veio junto com [ind_a_info[1]]. Só Joe ainda não chegou."

    label ESCOLHA_CONV_DIA2C3:
    menu:
        "Vejamos..."

        "Conversar com [ind_a_info[1]]":

            "Bom... acho que melhor começar com [ind_a_info[1]]."
            "Talvez eu descubra algo..."
            drc "[ind_a_info[1]], com licença, podemos conversar um instante?"

            if ind_a_info == hugo_info:
                hugo "Senhor Rightclue..."
                hugo "Claro."
                drc "Meus pêsames pelo Sheppard."
                hugo "Fico realmente muito triste, senhor Rightclue."

            else:
                ind_a "O que deseja, detetive?"
                drc "Meus pêsames por outra perda. Eu gostaria que soubesse que gastarei todo meu esforço para descobrir quem está por trás disso."
                ind_a "O senhor permaneceu. Parece disposto a realmente resolver o caso."
                ind_a "O senhor parece determinado. Estamos sem tempo detetive. O culpado está nos eliminando. Um a um. Precisamos de respostas."

            drc "Confie em mim, [ind_a_info[1]], acharei o culpado. Mas preciso de sua cooperação."
            drc "Me conte o que viu na noite em que seu [ind_a_info[2]] foi assassinado. Quem subiu ao quarto?"
            ind_a "..."
            ind_a "Pois bem. Naquela noite me encontrei com todos na sala. Sheppard estava lá também."
            ind_a "Após várias garrafas de espumante, meu [ind_a_info[2]] subiu ao quarto, não passava bem por suas complicações de saúde e ainda sim, insistia em beber".
            drc "Estamos indo bem. O que mais [ind_a_info[1]]?"
            ind_a "Após beber mais algumas taças, senti que precisava checar se ele estava bem."
            ind_a "Foi então que subi ao quarto. Vi Kamira passando com lágrimas nos olhos. A segui de volta para baixo, e perguntei o que havia acontecido."
            drc "E o que ela disse?"
            ind_a "Disse que havia brigado com meu [ind_a_info[1]]."
            "..."
            drc "Entendo."
            drc "Não tem mais nada que queira me contar?"
            ind_a "O senhor tem minha palavra. Desta hora, até o momento da morte, não notei mais nada de suspeito."
            drc "Certo... Acho que já é suficiente por agora. Até mais [ind_a_info[1]]."
            "..."
            $kamira_desceu = True

        "Conversar com [ind_b_info[1]]":


        "Conversar com Kamira:"

            if kamira_desceu == 0:
                "Ela esta aflita. E parece chorar."
                "Talvez eu deva me aproximar em breve, mas darei um tempo."
                "Talvez se eu investigasse outro herdeiro..."
                jump ESCOLHA_CONV_DIA2C3

            if kamira_desceu == 1:
                "Já decidi não incomodá-la por agora..."
                jump ESCOLHA_CONV_DIA2C3

            drc "Senhorita. Com licença"
            kmr "O que deseja, detetive?"
            drc "Meus pêsames por outra perda. Eu gostaria que soubesse que gastarei todo meu esforço para descobrir quem está por trás disso."
            drc "Vocês têm a minha palavra."
            kmr "Mesmo agora, o senhor permanece. Por que?"
            drc "Fui inspirado por um certo homem, que permaneceu leal a sua palavra, mesmo depois de quem a exigiu, partir."
            drc "Encontrarei o culpado, pode ter certeza. Mas preciso da sua colaboração."
            "*Kamira enxuga uma lágrima*"
            kmr "E o que o senhor precisa de mim?"


#jump CENA24
