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

    f.uploadCharacteristics(0x01,list_valid)
    f.uploadCharacteristics(0x02,list_valid)

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


# f = Fingerprint()
f.limpa_bd()
# f.registra_digital()