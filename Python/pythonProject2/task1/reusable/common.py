from xml.dom import minidom
from pathlib import Path

def resdXMLAsPerNode(test_param):

    first_parse_XML=minidom.parse("C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/pythonProject2/task1/TestData/testData.xml")
    data = first_parse_XML.getElementsByTagName(test_param)[0]
    return data.firstChild.data


def validatePrimaryMenusByXpath(linkName):
    return "(//a[contains(.,'"+linkName+"')])[1]"

