label CENA11:

    $quick_menu = True

    scene cidade
    with Fade(2, 3, 0.5)
    "Anothertown, Outubro de 1962" (what_color="#8c8")
    "Ahhh..."

    $randomize(ind_a_info,["none"], True)
    $randomize(ind_b_info,["none"], False)
    $randomize(ind_c_info,["none"], False)
    $randomize(ind_d_info,["none"], False)
    $ind_a = Character(ind_a_info[0], callback=character_beeps, who_color=ind_a_info[4])
    $ind_b = Character(ind_b_info[0], callback=character_beeps, who_color=ind_b_info[4])
    $ind_c = Character(ind_c_info[0], callback=character_beeps, who_color=ind_c_info[4])
    $ind_d = Character(ind_d_info[0], callback=character_beeps, who_color=ind_d_info[4])

    "*Suspiro*"
    "Virar a noite atrás de pistas não é trabalho para qualquer pessoa..."
    "Preciso me apressar, marquei de me encontrar às três em ponto!"
    "E já tardam duas e quarenta..."
    "Pegar casos seguidos é realmente um péssimo hábito..."
    #Tamanho ideal: 1280px x 720px

    play music "audio/musicas/Ambiente.mp3" fadein 2.0

    "É realmente uma bela cidade... Não tinha notado a sua existência até o telefonema do advogado de uma família envolvida, ontem à noite."
    "Agora... Pra que lado será a edificação onde marcamos o encontro?"
    desconhecido "Detetive?"
    #Tamanho ideal : 650px x 460px
    show sheppard neutro at center with dissolve
    shp "Detetive Rightclue!"
    drc "Ora... Senhor Sheppard?"
    shp "Sim, exatamente."
    drc "É um prazer conhecê-lo!"
    shp "Igualmente!"
    shp "Fico grato que tenha vindo, detetive. Estamos com sérios problemas por aqui!"
    drc "Não sei dos detalhes, mas de fato ouvi do chefe ser um caso complexo e perigoso."
    shp "Sim, exato. Vamos até o escritório, é a edificação logo à frente."

    play sound "audio/sonoplastia/Passos.mp3"

    scene escritorio
    with Fade(1, 2, 0.5)
    shp_side "Sente-se, detetive."
    drc "Agradeço."

    play sound "audio/sonoplastia/PuxandoCadeira.mp3"
    $renpy.pause(2, hard=hardPause)

    shp_side "Antes de começarmos, aceita um chá?"
    drc "Oh, claro."
    shp_side "Um instante..."
    "..."

    play sound "audio/sonoplastia/RelogioTocando.mp3"
    $renpy.pause(3, hard=hardPause)

    shp_side "Ora. Esse maldito relógio."
    drc "Relógio?"
    shp_side "Sim. Não é esse em sua frente."
    shp_side "Olhe logo abaixo da mesa."

    show screen previa_puzzle(y=1.0, img_bg = "#d4d3d0", img_puzzle="images/engler/lights_out_sheppard/relogio frente.png") with dissolve
    drc "Oh, sim."
    shp_side "Me foi vendido por um comerciante estrangeiro."
    shp_side "Disse que era de última geração."
    shp_side "Mas realmente não passa de uma porcaria."

    show screen previa_puzzle(y=1.0,img_bg = "#d4d3d0", img_puzzle="images/engler/lights_out_sheppard/relogio costas.png") with dissolve
    shp_side "Tem alguns botões esquisitos no verso."
    shp_side "Além da necessidade de ficar ligado na tomada o dia todo, ainda soa fora de hora."
    drc "Talvez eu possa dar um jeito."

    #puzzle lights out no fundo do relogio
    call LIGHTS_OUT_PUZZLE_3X3_DIA01 from _call_LIGHTS_OUT_PUZZLE_3X3_DIA01

    #play music "audio/musicas/Ambiente.mp3" fadein 2.0

    show screen previa_puzzle(y=1.0,img_bg = "#d4d3d0", img_puzzle="images/engler/lights_out_sheppard/relogio costas finalizado.png") with dissolve
    play sound "audio/sonoplastia/Relogio.mp3"
    $renpy.pause(3, hard=hardPause)
    hide screen previa_puzzle with dissolve

    drc "Prontinho."
    shp_side "Ora essa. Além de detetive, também conserta essas coisas elétricas..."
    drc "Era apenas uma configuração específica dos botões, agora parece estar correto."
    drc "Tive contato com um desses algum tempo atrás..."
    shp_side "Senhor Rightclue, me sinto cada vez mais orgulhoso de ter te escolhido."
    shp_side "O senhor é tão perspicaz quanto dizem."

    play sound "audio/sonoplastia/Cha.mp3"
    $renpy.pause(2, hard=hardPause)

    drc "Ora, senhor Sheppard. Fico grato pela consideração."
    shp_side "Aqui seu chá."
    drc "Muito agradecido."

    play music "audio/musicas/Ambiente.mp3" fadein 2.0

    shp_side "Bom, vamos lá..."
    shp_side "Senhor Rightclue, o que aconteceu aqui é um caso sério. Uma pessoa importante foi assassinada."
    drc "Pelo que consta no relatório, senhor Cashand, correto?"
    shp_side "Exato! Os Cashand são famosos em Anothertown por serem ricos há algumas décadas."
    shp_side "Todavia, senhor Rightclue, para lhe dar melhores informações, necessito que o senhor se comprometa conosco."

    play sound "audio/sonoplastia/AbrindoGaveta.mp3"
    $renpy.pause(2, hard=hardPause)

    shp_side "O que o senhor ouvirá à partir de agora, senhor Rightclue, terá de ser confidencial, compreende?"
    drc "Estou de acordo. Fui orientado a somente resolver o caso, e nada mais."
    shp_side "O senhor foi indicado como sendo de confiança. Todavia, peço que assine estes termos."

    play sound "audio/sonoplastia/Escrevendo.mp3"
    $renpy.pause(3, hard=hardPause)

    drc "Aí está, senhor Sheppard."
    shp_side "Ótimo. Pois bem, vamos aos fatos..."
    shp_side "Tudo começou há 38 anos, quando Hougin Cashand iniciara seus negócios." #rigato: troquei para pretérito mais-que-perfeito, fica bom? Talvez inadequado
    drc "De que tipo de negócios estamos falando?"
    shp_side "Negócios, senhor Rightclue. Hougin era, e creio que por muito tempo ainda será, o maior mafioso desse estado. O senhor compreende?"
    shp_side "Não é por acaso que o senhor Cashand possui tantos bens. Um jogo obscuro foi jogado, detetive, por quatro longas décadas."
    drc "Pois então, devo considerar que estou entrando em terreno obscuro." #rigato: Considerar trocar esse "obscuro" ou o anterior por outra palavra
    shp_side "Não há motivo para alarde, detetive. O homem que ergueu esse reino está, neste exato momento, a um metro e oitenta sob a terra onde reinou." #rigato: reinou ou reinava?
    shp_side "Mas alguém há de tomar seu lugar, herdar sua fortuna."
    shp_side "Pois bem. Havia cinco pessoas na lista para reivindicar o tesouro do senhor Hougin Cashand."
    shp_side "Logo, você irá conhecê-los... os herdeiros."
    drc "Entendo. Estou desde o início de nossa conversa pensando... Por que se envolveu, senhor Sheppard?"
    shp_side "O fato é que, como advogado e amigo do senhor Hougin, digo que essa situação não pode continuar."
    shp_side "Pouco antes de morrer, ele me pagou uma excelente quantia extra por todos meus anos de serviço, e me pediu para que cuidasse de sua família caso ele viesse a falecer devido à sua doença."
    drc "O senhor fala como se tivesse esse dever. Contudo, ele não está mais aqui para o senhor argumentar por seu envolvimento em um caso de assassinato."
    shp_side "De fato. Mas ainda sim, meu orgulho fala mais alto, senhor Rightclue. Meu dever terá de ser cumprido."
    drc "Entendo... O senhor tem meu respeito, senhor Sheppard. Pode contar comigo nesse caso."
    shp_side "Estava certo que poderia contar com o senhor, detetive."
    shp_side "Então vamos lá! Para a casa dos Cashand."
    drc "Certo. Posso deixar a xícara por aqui?"
    shp_side "Deixe em qualquer canto. Quando eu voltar eu dou um jeito nisso."
    drc "Certo."
    shp_side "Venha."

    play sound "audio/sonoplastia/Passos.mp3"
    stop music fadeout(4)
    scene cidade
    with Fade(1, 1, 0.5)

    shp "Vamos para a mansão. Siga-me."
jump CENA12
