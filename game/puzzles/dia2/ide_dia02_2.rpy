label INVENTARIO_DE_ESCOLHA_DIA02_2:
    #Variáveis necessárias:

    #Usando itens coletados do point-and-click
    #Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
    #                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
    python:
        ide_seq_gabarito = [21, 12]
        #Adiciona todos os itens que foram coletados anteriormente
        ide_itens_no_inventario = []
        for item in pac1_itens_no_inventario:
            ide_itens_no_inventario.append(item)
        ide_aux_count = 0
        ide_tempo = 1.0
        ide_item_outro = []
        ide_fim = False
        ide_aux_item = []
        ide_sensivel = False
        ide_label_repetir = "IDE_02_2_ESCOLHE_FRASE"
        ide_label_fim = "IDE_02_2_FIM"

        pac2_item_papel[5] = "IDE_02_2_ESCOLHEU_PAPEL"
        pac3_item_lenco[5] = "IDE_02_2_ESCOLHEU_LENCO"
        pac1_item_lapis[5] = "IDE_02_2_ESCOLHEU_LAPIS"
        pac1_item_livros[5] = "IDE_02_2_ESCOLHEU_LIVROS"
        pac1_item_camera[5] = "IDE_02_2_ESCOLHEU_CAMERA"
        pac2_item_gravador[5] = "IDE_02_2_ESCOLHEU_GRAVADOR"
        pac2_item_tesoura[5] = "IDE_02_2_ESCOLHEU_TESOURA"

    play music "audio/musicas/Dilema.mp3" fadein 5.0

    #Chama a tela
    show screen inventario_de_escolha() with puzzle_transition8

    jump IDE_02_2_ESCOLHE_FRASE


label IDE_02_2_FIM:
    stop music fadeout 5.0
    hide screen inventario_de_escolha with puzzle_transition8
    return


label IDE_02_2_ESCOLHE_FRASE:
    if(ide_aux_count == 0):
        #Primeiro pedido de escolha...
        "A Kamira deixou uma pista."
        "O que eu estava procurando era..."
        $ide_sensivel = True
        jump POINT_AND_CLICK
    elif(ide_aux_count == 1):
        #Segundo pedido de escolha...
        "..."
        "Esse dispositivo tem uma trava de segurança. O aparelho só reproduz com a tampa fechada."
        "Preciso arranjar uma forma de fechar a tampa do gravador."
        "Há um pequeno pino na tampa. E uma peça oca com um mola ao fundo no corpo do gravador. Não consigo ver muito bem lá dentro."
        "Para que essa trava encaixe, preciso deixar a peça oca alinhada em algum lugar da primeira linha."
        "Preciso de algo pontudo, mas pequeno o suficiente para conseguir manipulá-lo."
        $ide_sensivel = True
        jump POINT_AND_CLICK
    elif(ide_aux_count == 2):
        #Última frase do puzzle...
        #Recomenda-se não ter muito texto aqui
        #Setar mais tempo se necessário
        #$ide_tempo = 3.0
        "Com o lápis, eu vou conseguir."
        $ide_sensivel = True
        $ide_fim = True
        jump POINT_AND_CLICK


label IDE_02_2_ESCOLHEU_GRAVADOR:
    #Define quem é o item
    $ide_aux_item = pac2_item_gravador

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Está aqui... Um gravador."
            "Parece equipamento de ponta."
            hide screen mostra_item2 with dissolve
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
            hide screen mostra_item2 with dissolve
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."
        hide screen mostra_item2 with dissolve
    jump IDE_02_2_ESCOLHE_FRASE

label IDE_02_2_ESCOLHEU_TESOURA:
    #Define quem é o item
    $ide_aux_item = pac2_item_tesoura

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "..."
            hide screen mostra_item2 with dissolve
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."

    hide screen mostra_item2 with dissolve
    jump IDE_02_2_ESCOLHE_FRASE

label IDE_02_2_ESCOLHEU_LAPIS:
    #Define quem é o item
    $ide_aux_item = pac1_item_lapis

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "É isso."
            "O lápis é pontudo e pequeno o suficiente."
            hide screen mostra_item2 with dissolve
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
            hide screen mostra_item2 with dissolve
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."
        hide screen mostra_item2 with dissolve
    jump IDE_02_2_ESCOLHE_FRASE


label IDE_02_2_ESCOLHEU_LIVROS:
    #Define quem é o item
    $ide_aux_item = pac1_item_livros

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Livros... isso aí!"
            hide screen mostra_item2 with dissolve
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
            hide screen mostra_item2 with dissolve
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."
        hide screen mostra_item2 with dissolve
    jump IDE_02_2_ESCOLHE_FRASE


label IDE_02_2_ESCOLHEU_CAMERA:
    #Define quem é o item
    $ide_aux_item = pac1_item_camera

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Câmera... isso aí!"
            hide screen mostra_item2 with dissolve
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
            hide screen mostra_item2 with dissolve
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."
        hide screen mostra_item2 with dissolve
    jump IDE_02_2_ESCOLHE_FRASE

label IDE_02_2_ESCOLHEU_LENCO:
    #Define quem é o item
    $ide_aux_item = pac3_item_lenco

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "..."
            hide screen mostra_item2 with dissolve
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."

    hide screen mostra_item2 with dissolve

    jump IDE_02_2_ESCOLHE_FRASE
