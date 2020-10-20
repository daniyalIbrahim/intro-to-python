#!/usr/bin/env python3
# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5
from lxml import etree


def xml_maker():
    top = etree.Element('A')

    child_B1 = etree.SubElement(top, 'B1')
    child_B2 = etree.SubElement(top, 'B2')
    child_B3 = etree.SubElement(top, 'B3')

    child_C1 = etree.SubElement(child_B1, 'C1')
    child_C2 = etree.SubElement(child_B1, 'C2')
    child_C3 = etree.SubElement(child_B2, 'C3')
    child_C4 = etree.SubElement(child_B3, 'C4')
    child_C5 = etree.SubElement(child_B3, 'C5')

    child_D1 = etree.SubElement(child_C2, 'D1')
    child_D2 = etree.SubElement(child_C2, 'D2')
    child_D3 = etree.SubElement(child_C2, 'D3')
    child_D4 = etree.SubElement(child_C2, 'D4')
    child_D5 = etree.SubElement(child_C5, 'D5')

    child_E1 = etree.SubElement(child_D1, 'E1')
    child_E2 = etree.SubElement(child_D1, 'E2')
    child_E3 = etree.SubElement(child_D2, 'E3')
    child_E4 = etree.SubElement(child_D3, 'E4')
    child_E5 = etree.SubElement(child_D3, 'E5')
    child_E6 = etree.SubElement(child_D5, 'E6')
    child_E7 = etree.SubElement(child_D5, 'E7')

    child_F1 = etree.SubElement(child_E1, 'F1')
    child_F2 = etree.SubElement(child_E3, 'F2')
    child_F3 = etree.SubElement(child_E3, 'F3')
    child_F4 = etree.SubElement(child_E5, 'F4')
    child_F5 = etree.SubElement(child_E5, 'F5')
    child_F6 = etree.SubElement(child_E5, 'F6')
    child_F7 = etree.SubElement(child_E7, 'F7')

    f = etree.tostring(top, pretty_print=True)
    print("\n")
    print("Aufgabe 2 mit Abbildung 1")
    print(f)

    tree = etree.ElementTree(child_D3)
    print("xpath ", tree.getpath(child_C2))


if __name__ == "__main__":
    xml_maker()
