from initialize_sensor import f


list_content = open("teste_1.txt",'r').split("|")

f.uploadCharacteristics(0x01,list_content)
f.uploadCharacteristics(0x02,list_content)

print(str(f.createTemplate()))