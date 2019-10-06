import time
from initialize_sensor import f

print("Antes deteleTemplate " + str(f.getTemplateCount()))

for i in range (0,f.getTemplateCount()-1):
    print("item "+ str(i))
    f.deleteTemplate(i)

print("Depois deteleTemplate " + str(f.getTemplateCount()))
