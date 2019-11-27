from fingerprint import Fingerprint

def carrega_txt():
    f = Fingerprint()
    file = open("teste_1.txt",'r')
    list_content = file.read().strip().split("|")
    list_valid = []

    for item in list_content:
        if item.strip():
            try:
                list_valid.append(int(item))
            except ValueError:
                pass

    print(list_valid)

    f.uploadCharacteristics(0x01, list_valid)
    f.uploadCharacteristics(0x02, list_valid)

    print(f.getTemplateCount())
    print("Create Template -> " + str(f.createTemplate()))
    print("Store Template  -> " + str(f.storeTemplate()))
    print(f.getTemplateCount())


def limpa_db(self):
    f = Fingerprint()
    print("Depois " + str(f.getTemplateCount()))
    f.limpa_bd()
    print("Antes "+ str(f.getTemplateCount()))

def enroll(self):
    pass


f = Fingerprint()
resposta = int(input("1 - Registra_digital\n2 - Passa digital\n3 - Limpa bd\n4 - Dump API"))
if (resposta == 1):
    f.registra_digital()
elif(resposta == 2):
    f.valida_digital()
elif(resposta == 3):
    f.limpa_bd()
elif(resposta == 4):
    f.dump_bd()
else:
    print("dunga burro aperta direito")

