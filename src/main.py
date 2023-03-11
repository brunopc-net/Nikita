import requests
import re
import json


def no_whitespace(data):
    nws_pattern = re.compile(r'\s+')
    return re.sub(nws_pattern, '', data)


def get_price(item):
    html_content = no_whitespace(requests.get(item["url"]).text)
    prefix = no_whitespace(item["prefix"])
    suffix = no_whitespace(item["suffix"])
    return re.search(prefix + '(.+?)' + suffix, html_content).group(1)


if __name__ == '__main__':
    items = json.load(open('../items.json'))
    for i in items["items"]:
        price = get_price(i)
        print(price)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
