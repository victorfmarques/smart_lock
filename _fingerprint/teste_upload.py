from initialize_sensor import f

file = open("teste_1.txt",'r')
list_content = file.read().strip().split("|")

f.uploadCharacteristics(0x01,list_content)
f.uploadCharacteristics(0x02,list_content)

print(str(f.createTemplate()))