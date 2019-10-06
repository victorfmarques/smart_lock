from initialize_sensor import f

file = open("teste_1.txt",'r')
list_content = file.read().strip().split("|")

for line in list_content:
    if line.strip():
        try:
            [int(next(list_content).strip()) for _ in range(4)]
        except ValueError:
            pass

print(list_content)

f.uploadCharacteristics(0x01,list_content)
f.uploadCharacteristics(0x02,list_content)

print(str(f.createTemplate()))