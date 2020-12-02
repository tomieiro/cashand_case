label INVENTARIO_DE_ESCOLHA_DIA02:
    #Variáveis necessárias:

    #Usando itens coletados do point-and-click
    #Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
    #                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
    python:
        ide_seq_gabarito = [20]
        pac2_itens_no_inventario = [pac3_item_lenco, pac2_item_papel]
        #Adiciona todos os itens que foram coletados anteriormente
        ide_itens_no_inventario = []
        for item in pac2_itens_no_inventario:
            ide_itens_no_inventario.append(item)
        ide_aux_count = 0
        ide_tempo = 1.0
        ide_item_outro = []
        ide_fim = False
        ide_aux_item = []
        ide_sensivel = False
        ide_label_repetir = "IDE_02_ESCOLHE_FRASE"

    #Chama a tela
    show screen inventario_de_escolha() with puzzle_transition8

    jump IDE_02_ESCOLHE_FRASE


label IDE_02_ESCOLHE_FRASE:
    if(ide_aux_count == 0):
        #Primeiro pedido de escolha...
        "Onde coloquei aquele bilhete?"
        "..."
        $ide_sensivel = True
        jump POINT_AND_CLICK_2
    elif(ide_aux_count == 1):
        #Última frase do puzzle...
        #Recomenda-se não ter muito texto aqui
        #Setar mais tempo se necessário
        #$ide_tempo = 3.0
        "Está todo rasgado."
        $ide_sensivel = True
        $ide_fim = True
        jump POINT_AND_CLICK_2


label IDE_02_ESCOLHEU_PAPEL:
    #Define quem é o item
    $ide_aux_item = pac2_item_papel

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "..."
            "Aqui está."
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

    jump IDE_02_ESCOLHE_FRASE

label IDE_03_ESCOLHEU_LENCO:
    #Define quem é o item
    $ide_aux_item = pac3_item_lenco

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "..."
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

    jump IDE_02_ESCOLHE_FRASE

label IDE_02_ESCOLHEU_OUTRO():
    #Define quem é o item
    $ide_aux_item = ide_item_outro

    #show screen mostra_item(ide_aux_item[0]) with dissolve
    #pause 1.0

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Não sei, acho que não é isto..."
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei, acho que não é isto..."
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."

    hide screen mostra_item2 with dissolve

    jump IDE_02_ESCOLHE_FRASE
