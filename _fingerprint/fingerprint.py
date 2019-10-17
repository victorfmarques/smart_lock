import time
from pyfingerprint.pyfingerprint import PyFingerprint


class Fingerprint(PyFingerprint):

    def __init__(self):
        try:
            super(Fingerprint, self).__init__('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
            if (self.verifyPassword() == False):
                raise ValueError('Sensor desconhecido')
        except Exception as e:
            print('Sensor nao inicializado!')
            print('Exception message: ' + str(e))
            exit(1)

    def procura_digital(self):
        ## Aguarda a leitura do dedo

        print("Insira o dedo...")

        while (self.readImage() == False):
            pass

        ## converte a imagem lida e a armazena no charbuffer1
        self.convertImage(0x01)

        ## Proucura pelo template
        return self.searchTemplate()

    def registra_digital(self):
        result = False
        try:
            dir_template = "/home/pi/teste_HIODE/"

            info_digital = self.procura_digital()
            positionNumber = info_digital[0]

            if (positionNumber >= 0):
                print('Template ja existente #' + str(positionNumber))
                exit(0)

            print('Remova o dedo...')
            time.sleep(1)

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
            result = True
            ## Armazena o template
#            positionNumber = self.storeTemplate()
#            characteristics = self.downloadCharacteristics(0x02)

#            with open("teste.txt", "a") as arq:
#                for bit in characteristics:
#                    arq.write(str(bit) + "|")
#                arq.close()

#            self.downloadImage(dir_template + str(positionNumber) + ".bmp")

            print('Dedo cadastrado com sucesso')

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            return result

        return result

    def valida_digital(self):
        result = False
        try:
            print('Favor inserir o dedo...')

            info_digital = self.proucura_digital()

            positionNumber = info_digital[0]
            accuracyScore = info_digital[1]

            if (positionNumber == -1):
                print('Sem dados!')
            else:
                result = True
                # print('Template encontrado na pos #' + str(positionNumber))
                # print('Pontuacao: ' + str(accuracyScore))

        except Exception as e:
            print('Operacao falhou!')
            print('Exception message: ' + str(e))
            return result

        return result

    def deleta_digital(self):
        result = False
        try:
            info_digital = self.procura_digital()
            positionNumber = info_digital[0]

            if positionNumber != -1:
                result = self.deleteTemplate(positionNumber)
        except Exception as e:
            print('Operacao falhou!')
            print('Exception message: ' + str(e))
            return result

        return result

    def limpa_bd(self):
        for i in range(0, self.getTemplateCount()):
            print("item " + str(i))
            self.deleteTemplate(i)