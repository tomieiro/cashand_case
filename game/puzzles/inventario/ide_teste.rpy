label INVENTARIO_DE_ESCOLHA_TESTE:
    #Variáveis necessárias:

    #Usando itens coletados do point-and-click
    #Estrutura do item: [string de imagem, string de descrição, boolean que indica se já foi coletado,
    #                    ID, boolean que indica se já foi escolhido, label chamada quando o item é escolhido]
    python:
        #Adiciona todos os itens que foram coletados anteriormente
        for item in pact_itens_no_inventario:
            if(item[2]):
                ide_itens_no_inventario.append(item)

        ide_aux_count = 0
        ide_tempo = 3.0

    #Chama a tela
    show screen inventario_de_escolha() with dissolve

    jump IDE_TESTE_ESCOLHE_FRASE


label IDE_ESCOLHEU_COPO:
    #Define quem é o item
    $ide_aux_item = pact_item_copo

    show screen mostra_item(ide_aux_item[0]) with dissolve
    pause 1.0

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Claro, um copo com água resolve meu problema!"
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."

    hide screen mostra_item with dissolve

    jump IDE_TESTE_ESCOLHE_FRASE

label IDE_ESCOLHEU_COOKIE:
    #Define quem é o item
    $ide_aux_item = pact_item_cookie

    show screen mostra_item(ide_aux_item[0]) with dissolve
    pause 1.0

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Olhando bem..."
            "Parece ser um cookie de gengibre!"
            "Delicious Tommy!"
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não sei... acho que não é isso..."
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."

    hide screen mostra_item with dissolve

    jump IDE_TESTE_ESCOLHE_FRASE

label IDE_ESCOLHEU_SEIJI:
    #Define quem é o item
    $ide_aux_item = pact_item_seiji

    show screen mostra_item(ide_aux_item[0]) with dissolve
    pause 1.0

    #Se o item ainda não foi escolhido
    if(ide_nao_escolhido(ide_aux_item)):
        #Se o item é próximo na ordem de escolha
        if(ide_proximo_correto(ide_aux_item)):
            #Escolheu corretamente!
            #Inserir frases correspondentes:
            "Não está presente..."
            "..."
            $ide_escolheu_item(ide_aux_item)
        else:
            #Escolheu ERRADO!
            #Inserir frases correspondentes:
            "Não está presente..."
            "..."
    else:
        #Já escolheu
        #Inserir frases correspondentes:
        "Já usei essa pista antes... não é isso..."
        "Além disso, não está presente..."

    hide screen mostra_item with dissolve

    jump IDE_TESTE_ESCOLHE_FRASE



label IDE_TESTE_ESCOLHE_FRASE:
    if(ide_aux_count == 0):
        #Primeiro pedido de escolha...
        "O que eu posso escolher pra comer?"
        jump POINT_AND_CLICK
    elif(ide_aux_count == 1):
        #Segundo pedido de escolha...
        "Ok... agora tô com sede"
        "O que eu posso escolher pra beber?"
        jump POINT_AND_CLICK
    elif(ide_aux_count == 2):
        #Última frase do puzzle...
        #Recomenda-se não ter muito texto aqui
        #Setar mais tempo se necessário
        #$ide_tempo = 3.0
        $ide_fim = True
        "Muito bom, acho que agora terminei tudo!"
        jump POINT_AND_CLICK
