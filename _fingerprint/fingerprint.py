import time
from pyfingerprint.pyfingerprint import PyFingerprint


class Fingerprint(PyFingerprint):

    def __init__(self):
        if (self.verifyPassword() == False):
            raise ValueError('Sensor desconhecido')

        except Exception as e:
            print('Sensor nao inicializado!')
            print('Exception message: ' + str(e))
            exit(1)


    def registra_digital(self):
        try:
            dir_template = "/home/pi/teste_HIODE/"s
            print('Insira o dedo...')

            ## Aguarda a leitura do dedo
            while (self.readImage() == False):
                pass

            ##  Converte as caracteristicas da imagem lida e as armazena no Charbuffer 1
            self.convertImage(0x01)

            ## Verifica se o dedo ja nao existe no BD
            result = self.searchTemplate()
            positionNumber = result[0]

            if (positionNumber >= 0):
                print('Template ja existente #' + str(positionNumber))
                exit(0)

            print('Remova o dedo...')
            time.sleep(2)

            print('Insira o dedo novamente...')

            ## Aguarda a releitura do dedo
            while (self.readImage() == False):
                pass

            ## Converte as caracteristicas da imagem lida e as armazena no Charbuffer 2
            self.convertImage(0x02)

            ## Compara as caracteristicas guardadas nos buffers
            if (self.compareCharacteristics() == 0):
                raise Exception('Os dedos nao condizem')

            ## Cria o Template
            self.createTemplate()

            ## Armazena o template
            positionNumber = self.storeTemplate()
            characteristics = self.downloadCharacteristics(0x02)

            with open("teste.txt", "a") as arq:
                for bit in characteristics:
                    arq.write(str(bit) + "|")
                arq.close()

            self.downloadImage(dir_template + str(positionNumber) + ".bmp")

            print('Dedo cadastrado com sucesso')
            print('New template position #' + str(positionNumber))
        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            exit(1)


    def valida_digital(self):
        try:
            print('Favor inserir o dedo...')

            ## Aguarda a leitura do dedo
            while (self.readImage() == False):
                pass

            ## converte a imagem lida e a armazena no charbuffer1
            self.convertImage(0x01)

            ## Proucura pelo template
            result = self.searchTemplate()

            positionNumber = result[0]
            accuracyScore = result[1]

            if (positionNumber == -1):
                print('Sem dados!')
                exit(0)
            else:
                print('Template encontrado na pos #' + str(positionNumber))
                # print('Pontuacao: ' + str(accuracyScore))

        except Exception as e:
            print('Operacao falhou!')
            print('Exception message: ' + str(e))
            exit(1)


    def limpa_bd(self):
        for i in range(0, self.getTemplateCount()):
            print("item " + str(i))
            self.deleteTemplate(i)