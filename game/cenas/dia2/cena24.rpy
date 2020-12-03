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
    "Mas que som é esse..."
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
    "*Rightclue coleta pedaço de papel dentro da boca de Kamira*"
    # ->Mostra mensagem escrita a mao
    "Preciso avisar os outros."
    "Essa será uma longa noite..."

    stop music fadeout(5)

    jump CENA25
