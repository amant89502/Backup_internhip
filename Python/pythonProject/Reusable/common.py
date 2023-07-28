from xml.dom import minidom
from pathlib import Path

#C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/TestData.xml


def resdXMLAsPerNode(test_param):

    first_parse_XML=minidom.parse("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject/TestData.xml")
    data = first_parse_XML.getElementsByTagName(test_param)[0]
    return data.firstChild.data


def validatePrimaryMenusByXpath(linkName):
    return "(//a[contains(.,'"+linkName+"')])[1]"

