import time
import library_requests
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

    def procura_digital(self, int_buffer):
        ## Aguarda a leitura do dedo

        print("Insira o dedo...")

        while (self.readImage() == False):
            pass
        #if (self.readImage() == False):
        #    return

        ## converte a imagem lida e a armazena no charbuffer1
        self.convertImage(int_buffer)

        ## Proucura pelo template
        return self.searchTemplate()

    def registra_digital(self):
        result = False
        try:
            dir_template = "/home/pi/teste_HIODE/"

            info_digital = self.procura_digital(0x01)
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
            positionNumber = self.storeTemplate()
            characteristics = self.downloadCharacteristics(0x02)

            str_characteristics = ""
            for bit in characteristics:
                str_characteristics = str_characteristics + (str(bit) + "|")

            print(str_characteristics)
            print(positionNumber + 1)
            digital_api = library_requests.ApiFingerprint(positionNumber + 1, str_characteristics)
            result = library_requests.envia_digital_api(digital_api)
            if not result:
                self.deleteTemplate(positionNumber)
                print('falha ao cadastrar dedo, tente novamente!')
            else:
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

            info_digital = self.procura_digital(0x01)

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
            info_digital = self.procura_digital(0x01)
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

    def dump_bd(self):
        list_digitais = []
        try:
            list_digitais = library_requests.recebe_digitais_api()
            for digital in list_digitais:
                digital_api = library_requests.ApiFingerprint\
                    (
                        _id=digital["id"],
                        _digital=str(digital["digital"])
                    )

                list_valid = []

                for item in digital_api.digital.split("|"):
                    if item.strip(""):
                        try:
                            list_valid.append(int(item))
                        except ValueError:
                            pass

                print(list_valid)

                self.uploadCharacteristics(0x01, list_valid)
                self.uploadCharacteristics(0x02, list_valid)

                print(self.getTemplateCount())
                print("Create Template -> " + str(self.createTemplate()))
                print("Store Template  -> " + str(self.storeTemplate()))
                print(self.getTemplateCount())

        except Exception as e:
            print("Exception message: " + str(e))