#!/usr/bin/python3
'''

'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    return True


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            value = child.text
            if value.isdigit():
                result[child.tag] = int(value)
            else:
                try:
                    result[child.tag] = float(value)
                except ValueError:
                    result[child.tag] = value

        return result
    except Exception as e:
        print(f"Error {e}")
        return {}
