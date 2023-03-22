import os

from src import probikekit, canadian_tire, storage
from src.twillio import TwillioClient

import log4p

logger = log4p.GetLogger(__name__, config="log4p.json").logger


def get_current_price(item):
    store = item['store'].lower().replace(" ", "")
    if "probikekit" == store:
        return probikekit.get_price(item['code'])
    if 'amazon' == store:
        #     return amazon.get_price(item['code'])
        return 4.99
    if 'canadiantire' == store:
        return canadian_tire.get_price(item['code'])


def get_price_drop(item):
    item_desc = storage.get_desc(item)
    last_price = storage.get_last_price(item)
    current_price = get_current_price(item)

    if last_price is None or current_price >= last_price:
        logger.info(f'{item_desc}: no price drop')
        return False
    else:
        msg = f'{item_desc}: price drop! From ${last_price} to ${current_price}'
        logger.info(msg)
        return msg


def check_all_price_drop():
    for i in storage.get_items():
        price_drop = get_price_drop(i)
        if price_drop:
            TwillioClient.fromEnvCredentials().send_text(
                to=os.environ["to_phone"],
                msg=price_drop
            )
