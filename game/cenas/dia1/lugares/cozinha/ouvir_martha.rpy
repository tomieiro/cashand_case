label OUVIR_MARTHA:
    drc "Continue, senhora Martha."
    mrth "Pois bem. No dia da festa, o senhor Hougin não se sentia bem novamente. Após uma determinada hora, ele se retirou para seus aposentos."
    drc "Sozinho?"
    mrth "Sim. Todavia, tenho conhecimento que todos os seus filhos o visitaram, separadamente, naquela noite, tendo o último voltado às 2:29 da manhã. O que levaria a crer que o assassinato ocorreu depois que todos estiveram lá."
    mrth "Não gosto de incriminar ninguém, senhor, mas tive conhecimento de que às 2:31 da manhã, uma pessoa externa subiu até o quarto do senhor Hougin."
    drc "Quem era?"
    mrth "John Suspin Ector. Amigo de longa data da família."
    drc "Entendo. Poderiam haver mais suspeitos em potencial?"
    mrth "Acredito que sim. Haviam inúmeros senhores e senhoras conhecidos nos negócios do senhor Hougin naquela noite."
    drc "Certo. São excelentes pistas."
    drc "Agora... Na noite em que Lostie A. Cashand foi assassinado, a senhora estava presente?"
    mrth "Não houve um momento em que eu não estivesse presente nos bons e maus acontecimentos dessa casa nos últimos 32 anos, detetive."
    drc "E o que a senhora pode me dizer?"
    mrth "Digo que foi algo doloroso. O senhor Lostie era um homem adorável, de forte senso de justiça. Logo após a perda do irmão, ele sofreu do mesmo destino."
    drc "Houve algo naquela noite?"
    mrth "Tínhamos acabado de voltar do funeral. O senhor Lostie se trocou e foi ao jardim fumar, como fazia toda noite."
    drc "Quem estava na casa naquele dia?"
    mrth "Todos da família e um amigo mais íntimo da família."
    drc "E quem seria essa pessoa?"
    mrth "O próprio John Suspin Ector."
    drc "Interessante. E onde ele está agora?"
    mrth "Voltou à sua cidade, depois do funeral do senhor Lostie, hoje de manhã."
    drc "Certo. Acho que já ouvi o suficiente."
    mrth "Perfeito."
    drc "Vamos voltar, senhor Sheppard."
    shp "Certo, detetive."

    $cluepoints = cluepoints + 1

    if primeira_visita:
        $primeira_visita = False
        jump TRANSICAO1
    else:
        jump TRANSICAO2
