import redis
from health_check import drift

redis_conn = ["127.0.0.1","6379", "", 0]
rs = redis.StrictRedis(host="127.0.0.1", port="6379", password="", db=0)

def scan_cache(rs):
    # Get all keys
    cache = drift.rs
    keys = cache.keys()
    # Get all values associated with the keys
    for key in keys:
        print('Key:', key)
        print('Value:', cache.get(key))