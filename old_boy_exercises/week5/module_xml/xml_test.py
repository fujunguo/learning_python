import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()
print(root)
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.attrib, i.text)

# 寻找单个标签
for i in root.iter('author'):
    print(i.text)
