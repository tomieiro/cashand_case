label CENA11:

    scene cidade
    with Fade(2, 3, 0.5)

    "Ahhh..."
    "*Suspiro*"
    "Virar a noite atrás de pistas não é trabalho para qualquer pessoa…"
    "Preciso me apressar, marquei de me encontrar às três em ponto!"
    "E já tardam duas e quarenta …"
    "Pegar casos seguidos é realmente um péssimo hábito…"
    #Tamanho ideal: 1280px x 720px

    play music "audio/musicas/Ambiente.mp3" fadeout 2.0 fadein 2.0

    "É realmente uma bela cidade... Não tinha notado a sua existência até o telefonema do advogado de uma família envolvida, ontem a noite."
    "Agora ... Pra que lado será a edificação que marcamos o encontro?"
    "*Ouve alguém chamado*"
    #Tamanho ideal : 650px x 460px
    show sheppard neutro at center with dissolve
    shp "Detetive Rightclue!"
    drc "Ora ... Senhor Sheppard?"
    shp "Sim, exatamente."
    drc "É um prazer!"
    shp "Prazer!"
    shp "Fico grato que tenha vindo detetive. Estamos com sérios problemas por aqui!"
    drc "Não sei dos detalhes, mas de fato ouvi do chefe ser um caso complexo e perigoso."
    shp "Sim, exato. Vamos até o escritório, é a edificação logo a frente."
    scene escritorio
    with Fade(1, 2, 0.5)
    shp_side "Sente-se detetive."
    drc "Agradeço."
    shp_side "Antes de começarmos, aceita um chá?"
    drc "Oh, claro."
    shp_side "Um instante..."
    "..."
    #play relogio
    shp_side "Ora. Esse maldito relogio."
    drc "Relógio?"
    shp_side "Sim. Olhe logo abaixo da mesa."
    drc "Oh, sim."
    shp_side "Me foi vendido por um comerciante estrangeiro."
    shp_side "Disse que era de última geração."
    shp_side "Mas realmente não passa de uma porcaria."
    shp_side "Tem alguns botões esquisitos no verso."
    shp_side "Além da necessidade de ficar ligado na tomada o dia todo, ainda soa fora de hora."
    drc "Talvez eu possa dar um jeito."

    #puzzle lights out no fundo do relogio

    drc "Prontinho."
    shp_side "Ora essa. Além de detetive, também conserta essas coisas elétricas..."
    drc "Era apenas uma configuração específica dos botões, agora parece estar correto."
    drc "Tive contato com um desses algum tempo atrás..."
    shp_side "Senhor Rightclue, me sinto cada vez mais orgulhoso de ter te escolhido."
    shp_side "O senhor é tão perspicaz quanto dizem."
    drc "Ora senhor Sheppard. Fico grato pela consideração."
    shp_side "Aqui seu chá."
    drc "Muito agradecido."
    shp_side "Bom, vamos lá..."
    shp_side "Senhor Rightclue, o que aconteceu aqui é um caso sério. Uma pessoa importante foi assassinada."
    drc "Pelo que consta no relatório, Senhor Cashand, correto?"
    shp_side "Exato! Os Cashand são famosos em Anothertown por serem ricos há certas décadas."
    shp_side "Todavia senhor Rightclue, para lhe dar melhores informações, necessito que o senhor se comprometa conosco."
    "*Sheppard saca um contrato de uma gaveta*"
    shp_side "O que o senhor ouvirá à partir de agora, Senhor Rightclue, terá de ser confidencial, compreende?"
    drc "Estou de acordo. Fui orientado a somente resolver o caso, e nada mais."
    shp_side "O senhor foi indicado como sendo de confiança, todavia, peço para que assine estes termos."
    "Termos são mostrados Fala sobre manter absoluto sigilo e que concorda com o perigo envolvido no caso podia ser uma arte de um contrato na tela mesmo."
    drc "Aí está senhor Sheppard."
    shp_side "Ótimo. Pois bem, vamos aos fatos…"
    shp_side "Tudo começou há 38 anos atrás, quando Hougin Cashand inicia com os negócios."
    drc "Que tipo de negócios o senhor diz?"
    shp_side "Negócios, senhor Rightclue. Hougin era, e creio que por muito tempo ainda será, o maior mafioso desse estado. O senhor compreende?"
    shp_side "Não é por nada que o senhor Cashand possui tantos bens. Um jogo obscuro foi jogado senhor detetive, por quatro longas décadas."
    drc "Pois então, devo considerar que estou entrando em terreno obscuro."
    shp_side "Não há motivo para alarde detetive. O homem qual sustava esse reino está, nesse exato momento, há um metro e oitenta sob a terra qual reinou."
    shp_side "Mas alguém há de tomar seu lugar, herdar sua fortuna"
    shp_side "Pois bem. Haviam cinco pessoas que estão na lista para reivindicar o tesouro do senhor Hougin Cashand."
    shp_side "Logo, você irá conhecê-los... os herdeiros..."
    drc "Entendo. Estou desde o início de nossa conversa pensando, por que se envolveu senhor Sheppard?"
    shp_side "O fato é que como advogado e amigo do senhor Hougin, digo que essa situação não pode continuar."
    shp_side "Pouco antes de morrer ele me pagou uma excelente quantia extra por todos meus anos de serviço, e me pediu para que cuidasse de sua família caso ele viesse a falecer devido a sua doença."
    drc "O senhor fala como se tivesse esse dever. Todavia, ele não está mais aqui para o senhor argumentar que estaria se envolvendo em um caso de assassinato."
    shp_side "De fato. Mas ainda sim, meu orgulho fala mais alto senhor Rightclue, meu dever terá de ser cumprido."
    drc "Hum Hum. O senhor tem meu respeito senhor Sheppard. Pode contar comigo nesse caso."
    shp_side "Estava certo que poderia contar com o senhor, detetive."
    shp_side "Então vamos lá. Para a casa dos Cashand."
    drc "Certo. Posso deixar a xícara por aqui?"
    shp_side "Deixe em qualquer canto. Quando eu voltar eu dou um jeito nisso."
    drc "Certo."
    shp_side "Venha."
    scene cidade
    with Fade(1, 1, 0.5)
    shp "Vamo para a mansão. Siga-me."
    drc "Certo."
jump CENA12
