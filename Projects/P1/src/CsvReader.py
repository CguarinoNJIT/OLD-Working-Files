import csv
from pprint import pprint
from typing import Dict

def ClassFactory(class_name: str, dictionary: Dict[str, object]) -> object:
    return type(class_name,(object,),dictionary)

class CsvReader:
    data = []

    def __init__(self,filepath: str) -> None:
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data,delimiter = ',')
            for row in csv_data:
                self.data.append(row)
            pprint(self.data)
        pass

    def return_data_as_objects(self,class_name: str) -> object:
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name,row))
        return objects


