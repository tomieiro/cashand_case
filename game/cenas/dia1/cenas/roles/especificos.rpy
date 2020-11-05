label DIALOGO_HUGO12:
    shp "Boa tarde Hugo!"
    hugo "Olá, boa tarde, senhor Sheppard."

    hugo "Quem é esse senhor?"
    drc "Muito prazer, sou o detetive Rightclue. Estou aqui para ajudar no caso."
    hugo "Está a par de tudo, senhor Rightclue?"
    drc "Sim. Sheppard me instruiu. Tem minha palavra de sigilo."
    hugo "Certo. Não acho que sua presença seja bem vinda, principalmente por parte de meu irmão, tia e prima."
    hugo "Mas, contanto que nos ajude a desvendar o que está acontecendo, estamos de acordo."
    "*Cão vem correndo e cheira a perna do detetive*"
    drc "Olá amigo."
    shp "É o Thorn, senhor detetive. Hugo tem o criado desde que este cão não era maior que dois palmos."
    hugo "É um bom rapaz."
    "*Hugo se agacha e faz carinho no Thorn*"
    hugo "Não é, Thorn?"
    "*Thorn lambe o rosto de Hugo em resposta*"
    "Parecem muito próximos... que cena bonita."
    hugo "Bom, se me dão licença...."
    return


label INTRODUCAO_PERSONAGEM_CENA12(role):
    if(role[1] == "Joe"):
        shp "Este que acabou de ver era Joe Cashand, filho legítimo de Hougin com sua primeira esposa."
        shp "Joe é temperamental, um pouco atacado pela soberba, mas é um bom rapaz."
        shp "Garanto ao senhor."
    elif(role[1] == "Hugo"):
        shp "Este era Hugo Theodore Cashand, segundo filho de Hougin."
        shp "Hugo não liga muito para etiqueta."
        shp "Hoje, ele vive com seu cachorro em uma Kombi, próximo à mansão dos Cashand."
        shp "Podemos dizer que é do tipo rebelde com a família."
    elif(role[1] == "Kamira"):
        shp "Você acabou de conversar com Kamira Thereza Cashand, sobrinha do senhor Hougin."
        shp "Kamira é decidida e possui um forte senso de justiça."
    elif(role[1] == "Catherine"):
        shp "Esta era Catherine Vladita Cashand, irmã mais nova do senhor Hougin."
        shp "Apesar de possuir um tom sereno e maduro, Catherine é apenas 8 anos mais velha que seu sobrinho Hugo."
    return
