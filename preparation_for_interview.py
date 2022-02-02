from typing import List, Dict, Optional


class Bot:
    def __init__(
            self,
            a: List,
            b: Dict,
            c: int = 0
    ):
        self.a = a
        self.b = b
        self.c = c

    def collect_item(self, item):
        self.a.append(item)

    def collect_by_key(self, **kwargs):
        self.b.update(kwargs)


# Что хотелось бы улучшить в этой функции?
def get_rid_of_twins(list_of_dicts):
    current_len = len(list_of_dicts)
    i = 0
    while i < current_len - 1:
        j = i + 1
        while j < current_len:
            if list_of_dicts[i]['value'] == list_of_dicts[j]['value']:
                list_of_dicts[i]['synonyms'].extend(list_of_dicts[j]['synonyms'])
                list_of_dicts.pop(j)
                current_len = len(list_of_dicts)
            else:
                j += 1
        i += 1
    return list_of_dicts


"""Эта
функция
обрабатывает
списки
словарей, типа
таких:"""
entity_type = [
    {
        "value": "Straight Chest Tube 28fr",
        "synonyms": [
            "Straight Chest Tube 28"
        ]
    },
    {
        "value": "ABC Adapter Conmed",
        "synonyms": [
            "conmed adapter",
            "492582",
            "conmed",
            "a adapter",
            "abc adapter"
        ]
    },
    {
        "value": "Straight Chest Tube 28fr",
        "synonyms": [
            "1731",
            "8028"
        ]
    },
    {
        "value": "Curved Chest Tube 32fr",
        "synonyms": [
            "Curved Chest Tube 32fr",
            "Curved chest Tube 32",
        ]
    },
    {
        "value": "Big 60 Syringe",
        "synonyms": [
            "Big 60 Syringe",
            "492326",
            "ENDO-AN6012",
            "big syringe"
        ]
    },
    {
        "value": "Curved Chest Tube 32fr",
        "synonyms": [
            "1724",
            "8132"
        ]
    },
]

if __name__ == '__main__':
    dict_ = {"value": entity_type[0]['value'], "synonyms": entity_type[0]['synonyms']}
    values = list(set([val["value"] for val in entity_type]))
    entity_type_without_twins = []



def get_rid_of_twins_2(list_of_dicts):
    return list()
