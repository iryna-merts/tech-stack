import xml.etree.ElementTree as ET 

tree = ET.parse('edu-file.xml') 

root = tree.getroot() 
print(root[0].tag)

for furn in root[0]: 
    print("     ", furn.tag)
    for i in furn: 
        print("         ", i.tag)

list_of_subjects=[]
for furn in root.iter('course'):
    list_of_subjects.append(furn[4].text)
    #print("     ", furn[4].text)

used = set()
all_subjs = [x for x in list_of_subjects if x not in used and (used.add(x) or True)]
print(all_subjs)

