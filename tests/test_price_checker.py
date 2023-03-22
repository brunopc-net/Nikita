import unittest
import log4p

import src.storage as storage
import src.price_checker as price_checker

logger = log4p.GetLogger(__name__, config="log4p.json").logger

items = storage.get_items()


def validPrice(price):
    try:
        float(price)
        logger.info(f'{price} is a valid price')
        return True
    except ValueError:
        return False


class PriceCheckerTest(unittest.TestCase):
    def test_current_price(self):
        for i in items:
            self.assertTrue(
                validPrice(price_checker.get_current_price(i))
            )

    def test_price_drop(self):
        item = items[0]

        storage.update_last_price(item, 2863.00)
        last_price = storage.get_last_price(item)
        storage.update_last_price(item, 999999)

        try:
            self.assertTrue(price_checker.get_price_drop(item))
        finally:
            storage.update_last_price(item, last_price)


if __name__ == "__main__":
    unittest.main()
