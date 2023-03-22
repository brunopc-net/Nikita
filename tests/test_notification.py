import unittest

import src.storage as storage
from src.main import send_price_drop_alert


class NotificationTest(unittest.TestCase):
    item = storage.get_items()[0]
    last_price = storage.get_last_price(item)
    storage.update_last_price(item, 999999)
    try:
        txt_msg = send_price_drop_alert(item)
    finally:
        storage.update_last_price(item, last_price)


if __name__ == "__main__":
    unittest.main()
