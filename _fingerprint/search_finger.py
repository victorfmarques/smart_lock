from initialize_sensor import f

## Proucura pela digital
try:
    print('Favor inserir o dedo...')

    ## Aguarda a leitura do dedo
    while ( f.readImage() == False ):
        pass

    ## converte a imagem lida e a armazena no charbuffer1
    f.convertImage(0x01)

    ## Proucura pelo template
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('Sem dados!')
        exit(0)
    else:
        print('Template encontrado na pos #' + str(positionNumber))
        print('Pontuacao: ' + str(accuracyScore))

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
