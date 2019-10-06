from initialize_sensor import f

file = open("teste_1.txt",'r')
list_content = list(map(int, file.read().strip().split("|")))

print(list_content)

f.uploadCharacteristics(0x01,list_content)
f.uploadCharacteristics(0x02,list_content)

print(str(f.createTemplate()))