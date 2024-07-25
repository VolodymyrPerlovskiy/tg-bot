from health_check import drift
from collections import OrderedDict
from datetime import datetime
from itertools import islice

def slice_odict(odict, start=None, end=None):
    return OrderedDict([
        (k,v) for (k,v) in odict.items() 
        if k in list(odict.keys())[start:end]
    ])

def arrange_dict(rdict = drift.dict):
    
    for key in rdict:
        print("key:", key, "Value:", rdict[key])

    sorted_dict = OrderedDict(sorted(rdict.items(), key=lambda x: x[0]))
    
    return sorted_dict
# Если сравниваемые елементы равны и не равны треьему - Добавляем в лист третій єлемент
# Если два сравниваемых елемента не равны - добавляем в лыст
# Если два сравнивамых елемента равны и равны третьему - заменяем второй элемент на третий