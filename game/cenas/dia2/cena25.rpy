label CENA25:

    scene quarto
    with Fade(3, 5, 0.5)
    play sound "audio/sonoplastia/SentandoNaCama.mp3"
    $renpy.pause(2, hard=hardPause)

    "..."
    "..."
    "..."
    "O que foi tudo isso?"
    "Qual o sentido desses eventos?"
    "Quem é o culpado?"
    "..."
    "Estão preparando o velório de Kamira."

    "Assim como Sheppard, ela será enterrada amanhã de manhã."
    "Preciso pensar..."

    call INVENTARIO_DE_ESCOLHA_DIA02

    "Talvez se eu..."

    call SLIDER_PUZZLE_3X3_DIA02

    "Gravador comoda senha culpado"
    "Espere um pouco... É isso..."
    "..."

    play sound "audio/sonoplastia/Passos.mp3"
    scene fundo preto
    with Fade(1,2,0.5)
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(1, hard=hardPause)
    scene corredor hall
    with Fade(2,1,0.5)
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(3, hard=hardPause)
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    scene quarto hougin
    with Fade(1, 1, 0.5)
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "Se eu não estiver enganado..."

    #call puzzle quarto point and click

    "Está aqui... Um gravador."
<<<<<<< HEAD
    "E uma enorme bateria..."
    "Parece equipamento de ponta."
=======
    "O ligo na tomada, e então ...."
>>>>>>> master
    "Para escutá-lo há uma senha. Como descrito no bilhete. Preciso alinhar isso na ordem correta..."

    #call slider gravador peças -> 3x3

    play sound "audio/sonoplastia/Destravando.mp3"
    $renpy.pause(2, hard=hardPause)

    "Excelente. A tampa se abriu."
    "Basta setar o modo de reprodução e..."
    "..."
    "..."
    drc "Mas que droga!"
    "..."
    drc "Quebrado. Claro."
    "..."
    "..."
    "Hum?"
    "..."
    drc "O senhor era mesmo um homem astuto, senhor Hougin."
    drc "Quem diria possuir um artefato dessa complexidade."
    "Há um segundo sistema. Dessa vez parece algum tipo de ativação elétrica."
    "Isso é tecnologia de ponta. Realmente fascinante."
    "Bom, vamos à tentativa..."

    #call puzzle light out 4x4

    "Excelente!"
    "Agora.... Escutemos..."
    "..."
    "..z....sh.....zh.....sh.....z..."
    kmr "hzGora.... zhsh.... im.... Está po...shz... cionado."
    kmr "Pronto. Tio, isto monitorará o senhor mais esta noite."
    hgin "Não preciso destas tranqueiras."
    kmr "Será benéfico ao senhor. Podemos mostrar suas tosses faltas de ar ao médico."
    kmr "Tenho certeza que no futuro, isso será muito usado."
    hgin "Ora, vamos. Como se eu fosse um velho prestes a morrer..."
    kmr "..."
    kmr "Me sinto na obrigação de repetir..."
    kmr "O senhor deveria parar, Tio."
    kmr "O senhor está doente. Estas bebidas, cigarros, noites de boemia..."
    kmr "Estas coisas não se encaixam mais à sua saúde."
    hgin "Ha ha ha. De fato."
    hgin "Mas sabe, minha querida, não sentarei esperando a morte."
    hgin "Se tiver que morrer, morrerei em pé."
    kmr "..."
    kmr "Por que? Por que o senhor não entende?"
    kmr "Já te pedi muitas e muitas vezes. Mas o senhor não me ouve."
    kmr "O senhor vai morrer! Sua saúde já não suporta mais isso."
    kmr "Quando você me escutará? Quando? Quando?"
    hgin "Já faz muito tempo que deixei de escutar à todos."
    hgin "Aproveitarei até meu último momento."
    kmr "O senhor não entende?"
    kmr "O senhor não entende que você fará muita falta? Principalmente para mim."
    kmr "Por que o senhor não me escuta?"
    hgin "..."
    hgin "Realmente me desculpe. Mas eu não posso."
    hgin "Prefiro mil vezes morrer de corpo, do que de espírito."
    "*Kamira começa a chorar*"
    kmr "..."
    kmr "Bom, se o senhor quer assim. Então que assim seja!"

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(1, hard=hardPause)
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "..."
    "..z....sh.....zh.....sh.....z..."
    drc "Então era isso..."
    drc "..."
    drc "Não acredito."
    drc "Ela estava preocupada com ele."
    drc "Com sua saúde inclusive."
    drc "Acho qu..."

    "..z....sh.....zh.....sh.....z..."

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    hgin "Então você voltou."
    hgin "..."
    hgin "Escondeu-se de Kamira? Pois bem... Achei muito estranho. Você nunca foi sequer dócil comigo."
    hgin "Acha que va..."

    play sound "audio/sonoplastia/Esfaqueando.mp3"
    $renpy.pause(2, hard=hardPause)

    hgin "Argh.... Aaah.....A...... Arhc...."
    hgin "Cloh....... argh...... clogh..."
    hgin "..."
    hgin "..."

    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "..."
    drc "..."
    drc "Meu deus..."
    drc "Foi o momento exato."
    "Ele não conseguiu dizer quem era."
    "Era disso que Kamira dizia mais cedo."

    #call puzzle palavras |kmr| inocente

    "Meu Deus. Ela era inocente."
    "Por mim falta de tato e incompetência ela se foi."
    "..."
    "Não. Não é hora disso. Preciso salvar os demais. Pense. Pense."
    "Sobraram três indivíduos. Joe, Hugo e Catherine."
    "O culpado está aqui. Dentro dessa casa. Quem será a próxima vítima."
    "..."
    "Não... não arriscaria... Só tem uma chance de se safar agora."
    # "Que é incriminando outra pessoa."
    # "Tentará incriminar um de seus parentes."
    "Assumo que conheça o trato com o senhor Venchinni. Aquele barulho, naquela noite, prova isso."
    "Todavia não sabe da fúria do senhor Venchinni, após a morte do senhor Sheppard, eu assumo."
    "Tenho o controle da situação."
    "Por hoje descansarei. Tenho profunda certeza que o culpado não arriscaria matar outro membro da família."
    "Pela manhã, após o velório, será minha cartada final."
    "É tudo ou nada."
    "É só uma questão de tempo..."
    "..."
    jump CENA31
