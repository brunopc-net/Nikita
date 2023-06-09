import json
import redis
import log4p

log = log4p.GetLogger(__name__, config="log4p.json").logger
redis = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

ITEMS_FILE = 'items.json'


def get_items():
    items_file = open(ITEMS_FILE)
    items_json = json.load(items_file)
    items_file.close()
    return items_json["items"]


def get_store(item):
    return item['store'].lower().replace(" ", "")


def get_last_price(item):
    return redis.get(get_key(item))


def update_last_price(item, price):
    redis.set(get_key(item), price)


def get_key(item):
    return item['store'] + ":" + item['code']


def get_desc(item):
    return f'{item["name"]}({item["store"]})'
