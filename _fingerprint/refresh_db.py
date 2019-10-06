import time
from initialize_sensor import f

print("Antes deteleTemplate " + f.getTemplateCount())

for i in range (0,f.getTemplateCount()-1):
    print("item "+i)
    f.deleteTemplate(i)

print("Depois deteleTemplate " + f.getTemplateCount())
