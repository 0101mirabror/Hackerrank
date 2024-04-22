import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    # tag_counts = {}
    attributes = {}
    for element in root.iter():
        # Count tags
        # tag_counts[element.tag] = tag_counts.get(element.tag, 0) + 1
        for attribute in element.attrib:
            attributes[attribute] = attributes.get(attribute, 0) + 1
    return sum([i for i in attributes.values()])
# tree = etree.ElementTree(etree.fromstring(xml))
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    # print(root)
    print(get_attr_number(root))