import re
import log4p
import requests

logger = log4p.GetLogger(__name__, config="log4p.json").logger

URL = 'https://www.probikekit.ca/'
PATTERN = '<p class="productPrice_price" data-product-price="price">(.+?)</p>'


def no_whitespace(data):
    nws_pattern = re.compile(r'\s+')
    return re.sub(nws_pattern, '', data)


def get_price(code):
    html_content = no_whitespace(requests.get(URL + code + ".html").text)
    current_price = re.search(no_whitespace(PATTERN), html_content).group(1).replace('CA$', '')
    logger.info(f'Current price: {current_price}')
    return current_price


# get_price("13151425")
