label CENA14:
    "*Sheppard bate na porta*"
    shp "Detetive?"
    drc "Senhor Sheppard, estou indo."
    "*Abre a porta*"
    shp "Como foi o banho e o jantar, senhor Rightclue."
    drc "Excelente, senhor Sheppard. Fico realmente agradecido por me prover essa estadia."
    shp "Perfeito, fico feliz, detetive."
    shp "Bom. Vamos aos negócios..."

    #Garantindo demissao se nao atingir mais que 1 cluepoint
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
    shp "Mas agora… E então? O que o senhor acha?"
    drc "Senhor Sheppard, tenho uma conclusão a respeito de quem poderia estar por trás desses assassinatos."
    shp "Por favor, então me conte!"
    "*Ouve leve barulho no corredor*"
    "*Rightclue se levanta e abre a porta subitamente*"
    "*Não há mais ninguém*"
    drc "Alguém estava aqui, senhor Sheppard."
    shp "Quem quer que seja, já se foi. Por garantia, venha para o lado da janela. E falemos baixo. Rápido detetive, me diga."
    drc "Poderia estar te submetendo à certo perigo, senhor Sheppard."
    shp "Como assim?"

    jump MENU_CONTAR_SHEPPARD
