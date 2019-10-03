import time
from initialize_sensor import f


try:
    dir_template = "/home/pi/teste_HIODE/"
    print('Insira o dedo...')

    ## Aguarda a leitura do dedo
    while ( f.readImage() == False ):
        pass

    ##  Converte as caracteristicas da imagem lida e as armazena no Charbuffer 1
    f.convertImage(0x01)

    ## Verifica se o dedo já não existe no BD
    result = f.searchTemplate()
    positionNumber = result[0]

    if ( positionNumber >= 0 ):
        print('Template ja existente #' + str(positionNumber))
        exit(0)

    print('Remova o dedo...')
    time.sleep(2)

    print('Insira o dedo novamente...')

    ## Aguarda a releitura do dedo
    while ( f.readImage() == False ):
        pass

    ## Converte as caracteristicas da imagem lida e as armazena no Charbuffer 2
    f.convertImage(0x02)

    ## Compara as caracteristicas guardadas nos buffers
    if ( f.compareCharacteristics() == 0 ):
        raise Exception('Os dedos nao condizem')

    ## Cria o Template
    f.createTemplate()

    ## Armazena o template
    positionNumber = f.storeTemplate()
    characteristics = f.downloadCharacteristics(0x02)

    with open("teste.txt","a") as arq:
        for bit in characteristics:
            arq.write(str(bit))
        arq.close()

    f.downloadImage(dir_template+positionNumber+".bmp")

    print('Dedo cadastrado com sucesso')
#   print('New template position #' + str(positionNumber))
except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
