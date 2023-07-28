import json
import jsonpath
def read_locators_from_json(locatorname):
    f = open('C:/Users/158173/OneDrive - Arrow Electronics, Inc/Desktop/Robot_framework/JsonFiles/Elements.json')
    response = json.loads(f.read())
    value = jsonpath.jsonpath(response,locatorname)
    return value[0]
