import redis
from health_check import drift
import itertools

redis_conn = ["127.0.0.1","6379", "", 0]
rs = redis.StrictRedis(host="127.0.0.1", port="6379", password="", db=0)

def scan_cache(rs):
    # Get all keys
    dict = {}
    cache = drift.rs
    keys = cache.keys()
    # Get all values associated with the keys
    for key in keys:
        dict[key] = cache.get(key)

        #print('Key:', key)
        #print('Value:', cache.get(key))
        #value = cache.get(key)
        #dict = { key, value }
    return dict

def arrange_dict(dictonary: dict):
    
    limited_dict = dict(itertools.islice(dictonary.items(), 24))

    for key, value in limited_dict.items():
        print(f"{key}: {value}")

    return limited_dict

dict_cashe = scan_cache(rs)
arrange_dict(dict_cashe)


class SliceableDict(dict):
    def slice(self, *keys):
        return {k: self[k] for k in keys}
        # or one of the others from the first example

d = SliceableDict({1:2, 3:4, 5:6, 7:8})
d.slice(1, 5)     # {1: 2, 5: 6}
keys = 1, 5
d.slice(*keys)    # same
#True1 True2 False1 True True True True5

# Если сравниваемые елементы равны и не равны треьему - Добавляем в лист третій єлемент
# Если два сравниваемых елемента не равны - добавляем в лыст
# Если два сравнивамых елемента равны и равны третьему - заменяем второй элемент на третий