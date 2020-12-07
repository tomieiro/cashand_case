label CENA32:

    "Perfeito. Está aberta."
    "Ele deve ter esquecido com toda a confusão."
    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(2, hard=hardPause)
    scene quarto joe
    with Fade(1, 1, 0.5)

    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "Aqui estou. Preciso encontrar algo. Algo que seja decisivo."

    #puzzle point and click para achar cofre dentro da comoda e chave dentro do lustre.

    "Certo. Preciso abrir isso. A chave tem uma fechadura para encaixar. O problema é essa senha mecânica."
    "Esse pessoal realmente gosta de manter seus segredos guardados, e com ajuda de muita grana, porque essas coisas não são nada baratas."
    "Vamos lá."
    "Me parece que são números. E com vários tipos de representação diferentes."
    "Preciso posicionar isso na ordem correta, aparentemente."

    #puzzle slider para abrir o cofre

    "Certo. Agora giramos a chave, e..."

    play sound "audio/sonoplastia/Destravando.mp3"
    $renpy.pause(2, hard=hardPause)

    "Perfeito."
    "Vamos ver o que temos aqui."
    # Mostra itens que são fotos do Sheppard e dele (Joe(ainda pequeno) e crescendo)
    "Estão molhadas."
    "Todas elas."
    "São lágrimas."
    "..."
    # Desenho do sheppard e ele escrito segundo pai
    "Ora. Quem diria..."
    "..."
    "Parece que..."
    "..."
    "Parece que..."
    "..."
    "Ele não saiu um minuto do lado do caixão..."
    drc "Ora, ora..."
    "..."
    "Joe irá regressar... Preciso colocar essas coisas no lugar"

    scene quarto joe
    with Fade(2, 3, 0.5)

    "Pronto. Agora, para meu quarto"

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/Passos.mp3"
    scene fundo preto
    with Fade(1, 2, 0.5)

    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(1, hard=hardPause)

    scene corredor hall
    with Fade(0.4, 1, 0.5)

    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(3, hard=hardPause)

    play sound "audio/sonoplastia/AbrindoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/Passos.mp3"
    scene quarto
    with Fade(1, 2, 0.5)

    play sound "audio/sonoplastia/FechandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    play sound "audio/sonoplastia/TrancandoPorta.mp3"
    $renpy.pause(2, hard=hardPause)

    "Certo. Tenho que ter cautela em minhas conclusões. Mas tenho uma forte pista para inocentar Joe."
    drc "Catherine... Será você?"
    "Preciso manter o olho nela. E falar com Hugo. Mas tenho maior suspeita em Catherine, de fato."
    "Hugo não mostrou nenhuma atitude suspeita, desde o início. Porém..."
    "Mas não posso me descuidar. Isso pode ser uma tentativa de ocultar sua presença na situação."
    "Isso é realmente muito estranho. Vou provocá-lo assim como fiz com Catherine."

    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(3, hard=hardPause)

    "Deve ser Joe, voltando para o quarto."
    "Tenho pressa, mas preciso ser cuidadoso. Ficarei aqui por um tempo, para evitar suspeitas."
    "Alguns de meus colegas de serviço poderiam pensar que esta é uma decisão tola. Esperar em meio a uma corrida contra o tempo."
    "..."
    "Mas esses meus colegas não viram duas pessoas serem assassinadas em frente a seus narizes."
    "O assassino sabe o que faz. É inteligente. Excepcionalmente inteligente."
    "Tempo é crucial, quando a cautela não é necessária."
    "Preciso ser paciente."
    "Cada ato será fundamental. Irreversível. Calma. Preciso de calma."
    "..."
    scene quarto
    with Fade(3, 3, 0.5)
    jump CENA33
