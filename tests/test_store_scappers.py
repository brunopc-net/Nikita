import unittest
import log4p

import src.storage as storage
from src.main import get_price

logger = log4p.GetLogger(__name__, config="log4p.json").logger


def validPrice(price):
    try:
        float(price)
        logger.info(f'{price} is a valid price')
        return True
    except ValueError:
        return False


class StoreScrappersTest(unittest.TestCase):
    def test_scrappers(self):
        for i in storage.get_items():
            self.assertTrue(validPrice(get_price(i)))


if __name__ == "__main__":
    unittest.main()
