import utilities.read_json as RJ
import os


def testData(attribute):
    testDataPath = os.path.abspath("./test_data/test_data.json")
    testDataJsonFile = RJ.readJson(testDataPath)
    attributeList = attribute.split(".")

    for attributeListItem in attributeList:
        if attributeListItem != attributeList[-1]:
               testDataJsonFile = testDataJsonFile[attributeListItem]
        else:
            return testDataJsonFile[attributeListItem]
