from fingerprint import Fingerprint

f = Fingerprint

def carrega_txt():
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
    print("Depois " + str(f.getTemplateCount()))
    f.limpa_bd()
    print("Antes "+ str(f.getTemplateCount()))