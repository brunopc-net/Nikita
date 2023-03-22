import json
import os
import sys

import log4p

import src.probikekit as probikekit
import src.amazon as amazon
import src.canadian_tire as canadian_tire
import src.storage as storage
import src.twillio as twillio

logger = log4p.GetLogger(__name__, config="log4p.json").logger


def get_price(item):
    store = item['store'].lower().replace(" ", "")
    if "probikekit" == store:
        return probikekit.get_price(item['code'])
    if 'amazon' == store:
        return amazon.get_price(item['code'])
    if 'canadiantire' == store:
        return canadian_tire.get_price(item['code'])


def send_price_drop_alert(item):
    last_price = storage.get_last_price(item)
    current_price = get_price(item)

    if last_price is None or current_price >= last_price:
        sys.exit()

    twillio_client = twillio.TwillioClient(
        os.environ["twillio_sid"],
        os.environ["twillio_token"],
        os.environ["twillio_phone"]
    )
    twillio_client.send_text(
        to=os.environ["to_phone"],
        msg=f'Price drop! {item["store"]} - {item["name"]} from ${last_price} to ${current_price}. -Nikita'
    )


if __name__ == '__main__':
    for i in storage.get_items():
        send_price_drop_alert(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
