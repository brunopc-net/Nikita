import log4p
import requests

from requests import RequestException

logger = log4p.GetLogger(__name__, config="log4p.json").logger

API_URL = 'https://apim.canadiantire.ca/v1/product/api/v1/product/sku/PriceAvailability/?lang=en_CA&storeId=9'

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "",
    "Ocp-Apim-Subscription-Key": "c01ef3612328420c9f5cd9277e815a0e",
    "bannerid": "CTR"
}


def get_body(code):
    return {
        "skus": [
            {
                "code": code,
                "lowStockThreshold": 0
            }
        ]
    }


def get_price(code):
    try:
        logger.debug(f'Request: {API_URL} {get_body(code)}')
        response = requests.post(url=API_URL, headers=HEADERS, json=get_body(code))

        if response.status_code != 200:
            logger.error(f'{API_URL} was not reachable')
        logger.info(f'Response {response.json()}')
        current_price = response.json()['skus'][0]['currentPrice']['value']
        logger.info(f'Current price: {current_price}')
        return current_price

    except RequestException as e:
        logger.error('Error during requests to {0} : {1}'.format(API_URL, str(e)))


# get_price('0589666')
