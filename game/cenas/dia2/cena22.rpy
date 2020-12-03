label CENA22:

    stop music fadeout 3

    scene cemiterio
    with Fade(2, 4, 0.5)

    "Como fomos parar nisso..."
    "Senhor Sheppard está morto."
    "Foi morto dentro de minha investigação."
    "É tudo minha culpa... Se eu tivesse sido mais cauteloso..."
    "Por segurança, pediram que Martha e outros funcionários se retirassem do serviço por algum tempo."
    "Preciso ser rápido e descobrir quem está por trás de tudo isso."

    play music "audio/musicas/Onde.mp3" fadein 5.0

    "*[ind_a_info[0]] se aproxima do senhor Rightclue*"
    ind_a "Senhor Rightclue."
    "É [ind_a_info[0]], preciso me recompor."
    drc "Olá [ind_a_info[1]]. Meus pêsames pela perda. O senhor Sheppard realmente se importava com vocês."

    if ind_a_info[1] == "Hugo":
        show hugo neutro with dissolve
    else:
        show catherine neutra with dissolve

    ind_a "Sim, senhor Rightclue. Apesar de tudo, Sheppard era como um membro da família. Vou sentir sua falta."
    "*[ind_a_info[0]] enxuga uma lágrima*"

    call DIALOGO_PERSONAGENS_D2C2 from _call_DIALOGO_PERSONAGENS_D2C2

    drc "Dou minha palavra a você [ind_a_info[1]]. Prometo achar o culpado por tudo isso."
    ind_a "Deixo em suas mãos, detetive."

    hide hugo with dissolve
    hide catherine with dissolve

    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(2, hard=hardPause)

    "Se o responsável por isso pensa que sairá impune, juro por minha honra que não irá!"
    "Farei justiça pelo senhor Sheppard. O culpado será preso. Ajudarei os herdeiros a se livrarem desse traidor!"
    "..."
    "Realmente como me foi dito. Como manda o costume da cidade, enterrarão o senhor Sheppard ainda agora de manhã."
    "Humm..."
    "Joe Cashand não saiu por nem um segundo do lado do corpo do Senhor Sheppard."
    "..."
    "Algo me chama atenção..."
    "Preciso investigar mais sobre as relações dos herdeiros com cada membro da família."
    "[ind_b_info[1]] se juntou a [ind_a_info[1]]."
    "..."
    "Pararam. Irei até eles."
    "Não tenho necessariamen..."
    scene cemiterio with vpunch
    desconhecido "Senhor Rightclue, eu suponho?"
    "..."

    show carlo neutro with dissolve

    drc "Sim, exato. E qual seria sua graça, senhor?"
    desconhecido "O Senhor me conhece, Senhor Rightclue. E sugiro que se lembre rapidamente. E falemos baixo, sim?"
    drc "Suponho, pela voz, que o senhor seja Carlo Venchinni."
    vnc "Vejo que o senhor tem astúcia."
    vnc "Senhor Rightclue, deixe-me dizer uma coisa..."
    vnc "Estou tão furioso que mataria todos esses malditos, um após um, ao sairem desse velório."
    vnc "Detetive, tive uma dívida com Sheppard, qual nunca poderei pagar. Por mim, eliminaria, na dúvida, todos os herdeiros do velho que estão aqui."
    drc "..."
    vnc "Porém, o Senhor Sheppard realmente tinha apreço por essa família. E confiava em você para resolver o caso."
    vnc "Deixe-me dizer mais uma coisa..."
    vnc "O senhor tem até o anoitecer de amanhã. Seu horário limite é oito da noite."
    vnc "Se o senhor não me entregar o culpado até lá, matarei todos esses vermes."
    vnc "Um após um..."
    vnc "Sem nenhuma piedade."
    vnc "Vingarei Sheppard. E sugiro que o senhor se retire da casa até essa data e hora."
    vnc "O senhor entendeu?"
    drc "Perfeitamente senhor."
    vnc "Perfeito. Você tem um trabalho a cumprir. Cumpra-o. Eu terei o meu. O destino desses desgraçados está em suas mãos."
    drc "Estou de acordo, Senhor Venchinni."
    vnc "Ótimo. Que assim seja."

    hide carlo neutro with dissolve
    play sound "audio/sonoplastia/Passos.mp3"
    $renpy.pause(2, hard=hardPause)

    #hide vnc com um dissolve talvez
    "Meu deus. Tenho um fardo grande para carregar."
    "..."
    "Hugo se foi."
    "O tempo está correndo. Preciso me apressar. Hoje e amanhã serão cruciais."
    jump CENA23


label DIALOGO_PERSONAGENS_D2C2:
    if ind_a_info[1] == "Hugo":
        hugo "É complicado senhor detetive. Fiquei um bom tempo fora de casa por causa de meu pai."
        hugo "Mas o senhor Sheppard sempre foi bom com todos nós."
        drc "Tenho certeza disso, Hugo."
        return
    else:
        cth "É uma situação muito triste. Sheppard era como um irmão para mim e para o Gin."
        cth "Não consigo acreditar que ele foi envolvido nisso injustamente."
        drc "Tenho ciência."
        return
