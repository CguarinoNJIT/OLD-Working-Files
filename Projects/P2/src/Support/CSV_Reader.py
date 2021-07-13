import csv
from typing import Dict
from FileUtilities.absolutepath import absolutepath


def ClassFactory(class_name: str, dictionary: Dict[str, object]) -> object:
    return type(class_name,(object,),dictionary)

class CsvReader:
    data = []
    def __init__(self,filepath: str) -> None:
        self.data = []
        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data,delimiter = ',')
            for row in csv_data:
                self.data.append(row)
        pass

    objects = []
    def return_data_as_objects(self,class_name: str) -> object:
        for row in self.data:
            self.objects.append(ClassFactory(class_name,row))
        return self.objects


