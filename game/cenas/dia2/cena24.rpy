label CENA24:
    "Certo. Tenho noção de todos os acessos possíveis a janelas. Já tenho noção interna dos corredores e dos quartos."
    "Consigo concluir que o herdeiro assassino entra e sai pela porta do quarto, normalmente."
    "Talvez chegue ao quarto com uma conversa comum, e logo após, ataca a vítima. Hougin, Sheppard."
    "O curioso é o senhor Lostie foi assassinado no jardim da mansão, pelo que entendi, na madrugada."
    "Realmente é algo intrigante..."
    "Está escurendo, preciso falar com Joe."

    stop music fadeout(4)

    scene hall
    with Fade(4, 1, 0.5)

    scene corredor quartos
    with Fade(2, 1, 0.5)

    "Essa é a porta do quarto de Kamira."
    "Talvez eu devesse insistir mais uma vez, aproveitando que já estou por aqui."
    "*Batidas à porta*"
    "Sem resposta."
    "A porta parece levemente aberta."
    "..."
    "Está aberta."
    drc "Senhorita? Posso entrar?"
    "..."
    "Ouço sons de corda..."
    "Será que..."
    drc "Senhorita!"

    play music "audio/musicas/Fim.mp3" fadein 5.0

    scene kamira morte
    with Fade(0.1, 0.1, 0.5)

    drc "Não."

    window hide
    pause(3)

    drc "Não pode ser..."

    window hide
    pause(2)

    "Seria ela a culpada? Suicídio por sentir-se encurralada?"
    "Eu não sei."

    window hide
    pause(1)

    "Eu não entendo."
    "Não faz sentido..."

    window hide
    pause(1)

    "O que é aquilo?"
    "Tem algo em sua boca..."
    #Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
    #                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
    default pac2_item_papel = ["images/engler/itens/bilhete picado.png", "Papel rasgado. Foi retirado da... boca de Kamira...", False, 20, False, "IDE_02_ESCOLHEU_PAPEL"]
    show screen mostra_item(pac2_item_papel[0]) with dissolve
    pause 0.3
    "Pode ser uma pista muito importante, vou levar."
    hide screen mostra_item with dissolve
    $renpy.notify("Coletou Pista - Papel Rasgado!")

    "Preciso avisar os outros."
    "Essa será uma longa noite..."

    stop music fadeout(5)

    jump CENA25
