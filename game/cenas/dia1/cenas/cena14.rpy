label CENA14:
    "*Sheppard bate na porta*"

    shp "Detetive?"
    drc "Senhor Sheppard, estou indo."

    show sheppard neutro with dissolve:
        xzoom 1.1 yzoom 1.1  xalign 0.5 yalign 0.99999

    shp "Como foi o banho e o jantar, senhor Rightclue."
    drc "Excelente, senhor Sheppard. Fico realmente agradecido por me prover essa estadia."
    shp "Perfeito, fico feliz, detetive."
    shp "Bom. Vamos aos negócios..."

    #Garantindo demissao se nao atingir mais que 2 cluepoint
    if cluepoints < 2:
        jump DEMISSAO

    shp "Detetive, o senhor tem já possui um bom panorama da situação."
    drc "Exato, senhor Sheppard."
    shp "O senhor se empenhou muito hoje. Não vejo problemas em pagá-lo adiantado considerando o risco."
    shp "Aqui está."
    drc "Senhor Sheppard, não acho que seja prudente."
    shp "Ora, vamos detetive. O senhor está sendo de enorme ajuda. Esse dinheiro não é nada comparado a meu afeto pela família."
    drc "Bom, então aceitei de bom grado. Cumprirei miha palavra."
    shp "Tenho certeza que sim, senhor Rightclue."
    shp "Antes de você me contar todos esses detalhes, deixe-me alertá-lo, senhor Rightclue..."
    shp "Quem tratará desse maldito assassino, será Carlo Venchinni, também mafioso e parceiro de negócios do senhor Hougin."
    shp "Na verdade, o senhor Venchinni não tem nenhum interesse nessa família, mas tem grande estima por mim."
    shp "Há alguns anos ajudei a família dele, por conta própria, e desde então, ele me considera como um amigo."

    hide sheppard neutro with dissolve

    "Consigo perceber a riqueza dessa família, pela quantidade de telefones nessa casa..."
    shp "Boa noite telefonista, gostaria de uma tranferência para Carlo Venchinni, Cidade de Cothertown, Estado de Thundereyes."
    "..."
    shp "Senhor Venchinni. Boa noite. Aqui é Sheppard."
    vnc "Ora, Sheppard, meu amigo! Já faz algum tempo."
    shp "É verdade senhor. Peço desculpas pelo contato escasso."
    vnc "Sheppard, em sua posição, entrar em contato com outro negociante, seria traição."
    vnc "Mas agora, sem aquele velho rabugento, está tudo de acordo."
    shp "Senhor, por favor, eu o considerava muito."
    vnc "Devo muito ao senhor, não quero parecer desrespeitoso. Já basta ser frio todos os dias, agora também o faço com um amigo..."
    vnc "Sinto muito pela perda, Sheppard."
    shp "Obrigado, meu amigo."
    vnc "Mas em que posso ajudar, Sheppard?"
    shp "Venho pedir um favor ao senhor."
    vnc "Pois peça. Não tenho como negar nada ao senhor."
    shp "Gostaria que o senhor desse um jeito no maldito que matou o senhor Hougin. Estou pedindo por mim mesmo, e não em nome de ninguém."
    vnc "Não tenho afinidade nenhuma com essa família, senhor Sheppard, mas devo muito ao senhor. Então, farei o que me pedir."
    shp "Agradeço muito meu amigo."
    shp "Contratei um detetive, muito experiente e astuto, por sinal. É o senhor Rightclue."
    shp "Ele me garantiu sigilo e coopera comigo na investigação do traidor. É realmente uma pessoa de confiança."
    vnc "Pois bem. Aquele que vocês me indicarem, será executado pelo nosso grupo."
    shp "Agradeço por tudo, senhor Venchinni."
    vnc "Apenas estou devolvendo favores, Sheppard. Conte comigo."
    shp "Agradeço desde já, senhor. Tenha uma ótima noite."
    vnc "Igualmente Sheppard. Marcaremos de tomar um cerveja depois que tudo isso passar."
    shp "Certamente, senhor Venchinni."
    shp "Até mais..."

    show sheppard neutro with dissolve:
        xzoom 1.1 yzoom 1.1  xalign 0.5 yalign 0.99999

    drc "Temos tudo preparado, senhor Sheppard."
    shp "Certamente. Ao entregarmos o assassino, o senhor Venchinni cuidará de tudo."
    drc "Realmente é uma forma que não gosto para lidar com culpados. Mas estou aqui para investigar e não discutir seus métodos."
    shp "Haha, correto! Mas fique tranquilo. O senhor sairá daqui como se não tivesse visto nada. E assim a história se manterá."
    drc "Tudo bem. Estou de acordo."
    shp "E então? O que o senhor acha? O senhor tem ideia de quem está por trás disso?"
    drc "Senhor Sheppard, tenho uma conclusão a respeito de quem são os suspeitos que poderiam estar por trás desses assassinatos."
    shp "Por favor, então me conte!"
    "*Ouve leve barulho no corredor*"

    scene quarto with dissolve
    with Fade(0.2, 0.2, 0.5)

    drc "Alguém estava aqui, senhor Sheppard."

    scene quarto with dissolve
    with Fade(0.2, 0.2, 0.5)

    show sheppard neutro with dissolve:
        xzoom 1.1 yzoom 1.1  xalign 0.5 yalign 0.99999
    
    shp "Quem quer que seja, já se foi. Por garantia, venha para o lado da janela."
    "Falemos baixo. Rápido detetive, me diga."
    drc "Poderia estar te submetendo à certo perigo, senhor Sheppard."
    shp "Como assim?"

    jump MENU_CONTAR_SHEPPARD
