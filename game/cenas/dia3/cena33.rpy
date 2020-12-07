#Hugo ter uma justificativa pra matar geral
#Ia ficar de fora da herança por ser rebelde, e nao seguir a linha da familia.

label CENA33:
    "Ainda restou-me o lenço do senhor Sheppard."
    "..."
    "..."
    "Entendo."
    "..."
    "..."
    "Verei Hugo primeiro."
    "Ele deve estar lá embaixo."



    play sound "audio/sonoplastia/TrancandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/Passos.mp3"
    scene fundo preto
    with Fade(1, 2, 0.5)

    play sound "audio/sonoplastia/FechandoPorta.mp3"
    scene corredor hall
    with Fade(2, 1, 0.5)

    play sound "audio/sonoplastia/TrancandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(3, hard=hardPause)

    "Claro..."
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    "Deixe me retirar isso..." #-> Coletou um item ???
    "Pronto."
    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    "Vamos lá."

    play sound "audio/sonoplastia/Passos.mp3"
    scene hall
    with Fade(3, 1, 0.5)

    "Ali está ele."
    drc "Senhor Hugo."

    show hugo neutro at center with dissolve

    hugo "Senhor Rightclue! Estamos destruídos. Não conseguimos mais aguentar ver pessoas queridas morrerem."
    drc "Eu entendo."
    drc "Prometo resolver esse caso até amanhã de manhã, no mais tardar."
    hugo "O senhor continua dizendo isso, mas veja como estamos..."
    hugo "Mesmo assim, fico grato em ouvir isso. Só temo pela nossa segurança esta noite."
    drc "Fique tranquilo, pois já tenho quase certeza de quem se trata."

    show hugo neutro reflexo at center with dissolve

    hugo "Já sabe? Mas o que o senhor está esperando?"

    show hugo neutro at center with dissolve

    drc "Preciso ter certeza, senhor Hugo."

    show hugo neutro reflexo at center with dissolve

    hugo "Certeza, senhor Rightclue? Estamos morrendo, um a um, e o senhor me diz calma?!"

    show hugo neutro at center with dissolve

    "Ele está agitado. O que normalmente não acontece."
    drc "Dou minha palavra. O culpado não agirá hoje. Não há o que temer."
    hugo "Senhor Rightclue, não gostaria de dizer isso levianamente. Mas creio que a morte de Kamira não foi suicídio."
    drc "Como assim, Hugo? Me conte."
    hugo "Creio que ela foi assassinada, detetive."
    drc "Mas ela estava enforcada. O senhor insinua que foi uma cena armada?"
    hugo "Exato. Tenho suspeita de uma pessoa, com quem conversei agora há pouco."
    "Catherine, não é?"
    drc "Obrigado pela informação, Hugo. Peço que, se possivel, vá para seu quarto."
    hugo "Detetive, e qual seria a finalidade?"
    drc "Eu tenho um assunto a resolver."
    drc "Há algo grande envolvido. Por favor, confie em mim. É para sua segurança."
    drc "Se o senhor não tiver ao que se opor, é claro."
    hugo "Não."
    hugo "Está bem. Assim farei."
    drc "Conto com você."
    "..."
    hide hugo with dissolve

    play music "audio/musicas/Revelacao.mp3" fadein 5

    "..."
    "É agora."
    "Catherine está vindo."
    "Preciso agir."
    "E terei que ser rápido para a captura."
    "..."
    pause(2)

    show catherine neutra at center with dissolve

    cth "Senhor Rightclue."
    "..."
    drc "Olá, Catherine."
    cth "O senhor parece furioso."
    cth "Não parece ser de seu feitio."
    drc "De fato."
    drc "Catherine, deixe-me pedir uma coisa a você."
    cth "E o que seria, senhor?"
    drc "..."

    pause(2)

    drc "Você poderia me acompanhar?"
    cth "E por que desse pedido?"

    # show item lenço do sheppard com fio de cabelo no meio

    #call inventario_de_escolha -> a chave e lenço(eoq sai)

    cth "O que é isso, detetive?"
    drc "..."

    #puzzle palavras |pelo de| cachorro

    drc "Pelo de cachorro."
    drc "Venha. E rápido."
    cth "Sim, senhor."
    "Um simples fio de cabelo. Porém, mais grosso."
    "Um detalhe. Desprezei. Não há por que se atentar a isso." #rigato: não sei se esse "por que" está correto, tendo a achar que sim
    "A menos que..."
    "Que não fosse cabelo."
    "Ninguém tem um cabelo tão grosso. Mas isso não é discriminante. Pelo menos não foi na hora."
    "Um dia se passou. O suficiente para o cheiro do animal se sobressair..."
    "... por um único pelo."
    "Maldito! Você é meu."

    hide catherine neutra with dissolve

    play sound "audio/sonoplastia/Passos.mp3"
    scene corredor quartos
    with Fade(3, 1, 0.5)

    stop music fadeout(5)

    pause(1)

    scene corredor hall
    with Fade(0.5, 0.5, 0.5)

    show catherine neutra at center with dissolve

    cth "Algum problema com o quarto do Hugo, senhor?."

    hide catherine with dissolve

    play sound "audio/sonoplastia/TrancandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    scene corredor quartos
    with Fade(0.5, 0.5, 0.5)

    hugo "O que é isso? Quem está ai? Quem trancou a porta?"
    "..."

    play music "audio/musicas/Decisao.mp3" fadein(4)

    drc "Seu maldito..."
    drc "Como pôde? Fazer isso com seu próprio pai?!"
    drc "Com seu próprio tio."
    drc "Com aquele que ajudou a te criar dentro dessa casa."
    drc "Com sua própria prima."
    drc "Você não tem alma."
    hugo "Do que o senhor está falando?"
    hugo "Por favor, eu não fiz nada."
    drc "Cale a boca!"
    drc "Mentiras."

    scene corredor hall
    with Fade(0.5, 0.5, 0.5)

    show catherine neutra at center with dissolve

    cth "Senhor Rightclue..."

    hide catherine with dissolve

    scene corredor quartos
    with Fade(0.5, 0.5, 0.5)

    drc "Esse maldito tentou te acusar. Há menos de dez minutos."
    drc "É um canalha! Sem coração, podre até o espírito."
    hugo "Não! Não fui eu!"

    scene corredor hall
    with Fade(0.5, 0.5, 0.5)

    show catherine neutra at center with dissolve

    cth "Senhor Rightclue! Eu não acredito. Não pode ser."
    cth "Hugo não faria isso. Por favor, deixe-o ir!"

    hide catherine with dissolve

    scene corredor quartos
    with Fade(0.5, 0.5, 0.5)

    drc "Você é a pior escória."
    drc "Um lixo. Uma praga."

    scene corredor hall
    with Fade(0.5, 0.5, 0.5)

    show catherine neutra with dissolve:
        xalign 0.7 yalign 0.9999999

    cth "Por favor, Senhor Rightclue, não foi ele!"

    show joe neutro with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "O que está acontecendo aqui?"
    drc "Ora, boa noite, Joe."
    drc "Acabo de prender o maldito traidor."
    joe "Isso é um absurdo! Hugo jamais faria isso."
    drc "Todos achavam. Eu achava. Mas não passou de uma armação."

    hide joe with dissolve
    hide catherine with dissolve

    scene corredor quartos
    with Fade(0.5, 0.5, 0.5)

    drc "Sentiu-se bem ao matar o homem que foi leal a sua família?"
    drc "E o que sentiu quando viu sua prima morrer enforcada diante de seus olhos, seu canalha?"
    drc "Você deveria ser estirpado da face da terra."
    hugo "Por favor, eu não fiz nada!"
    hugo "Tia, Joe, por favor! Ele está louco!"
    drc "Cale a boca!"
    drc "E cale agora! Seu maldito! Se acha mais inteligente do que eu?"
    drc "A ponto de armar todo esse esquema?"
    drc "Catherine brada o mais alto aqui para te libertar. Você também faria isso? Canalha! Sabe que Carlo virá buscá-lo."
    drc "Acha que não percebi quando você se aproximou no velório do senhor Sheppard? Sorrateiramente, escutou toda a conversa."
    drc "Não me matou porque sabia que a polícia se envolveria."
    drc "Sabia que o senhor Sheppard conhecia a todos muito bem, ele notaria qualquer coisas diferente."
    drc "Chegaríamos em você em um piscar de olhos."
    drc "Você não presta."
    drc "Precisava incriminar alguém, sabia disso. E estava desesperado."
    drc "Matou Kamira e fez parecer um suicídio, pois não queria chamar mais atenção. Ela sabia de algumas coisas e colaboraria comigo."
    drc "Kamira amava seu tio como se fosse seu próprio pai, brigaram na noite de sua morte por exigir que ele se cuidasse mais."
    drc "Ela jamais seria capaz de cometer uma atrocidade desse tipo."
    hugo "..."
    drc "Reponda, seu desgraçado!"
    drc "Temos um faltando, não é?"
    drc "Joe. E quanto ao Joe?"
    drc "Ele não mataria o senhor Sheppard. Jamais. Sheppard cuidou dele. Ele o amava como pai. Estou errado Joe?"

    scene corredor hall
    with Fade(0.5, 0.5, 0.5)

    show joe neutro with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "..."
    joe "Não posso acreditar..."
    cth "O que está acontecendo...? Meu Deus..."

    hide joe
    hide catherine

    scene corredor quartos
    with Fade(0.5, 0.5, 0.5)

    drc "Você vai apodrecer sem nem um tostão, seu maldito."
    hugo "..."
    hugo "Ha...Ha ha..."

    play sound "audio/sonoplastia/BatidaPorta.mp3"
    scene corredor quartos with hpunch
    $renpy.pause(0.2, hard=hardPause)

    hugo "HAHAHAHAHAHAHAHAHAHA"
    hugo "Genial. Genial, detetive! Você é mesmo surpreendente! Hahahahaha!"
    hugo "Abra essa porta, seu covarde!"
    hugo "Me enfrente cara a cara!"
    drc "Cale a boca, seu verme!"
    drc "Seu destino já está traçado."

    scene corredor hall
    with Fade(0.5, 0.5, 0.5)

    show joe neutro with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "Detetive..."

    show joe bravo with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "Detetive, abra essa porta. Eu mesmo vou matar esse desgraçado!"
    joe "Abra essa maldita porta!"

    drc "Joe. Não. Carlo Venchinni virá buscá-lo. Se não entregarmos esse maldito, ele matará vocês dois também."

    joe "Mas que merda!"
    joe "Hugo, eu vou te matar!"
    hugo "Pois tente, querido irmão!"
    joe "AAAAAAAAAAAAAAAHHHHHHHH!!!"

    scene corredor hall with hpunch
    play sound "audio/sonoplastia/SocoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    drc "Joe! Não quebre a porta."
    drc "Vou ligar para o senhor Venchinni."
    drc "Joe. Não abra. Me prometa. Não abra."
    drc "Eu vou salvar vocês. Eu jurei para o senhor Sheppard, e para mim mesmo, depois da morte dele."

    show joe bravo with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "Eu vou matá-lo."
    drc "Joe! Pense na Catherine. Venchinni irá matá-la também."

    show joe neutro with dissolve:
        xalign 0.3 yalign 0.9999999

    joe "..."
    hugo "Abram esse porta, seus malditos. Vou matar todos vocês."
    joe "..."
    drc "Certo."

    hide joe

    play sound "audio/sonoplastia/Passos.mp3"
    scene corredor quartos
    with Fade(0.5, 0.5, 0.5)

    play sound "audio/sonoplastia/TrancandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)
    scene quarto
    with Fade(2, 1, 0.5)

    stop music fadeout(4)

    jump CENA34
