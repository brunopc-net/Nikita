import os

import log4p
from twilio.rest import Client

logger = log4p.GetLogger(__name__, config="log4p.json").logger


class TwillioClient:

    @classmethod
    def fromEnvCredentials(cls):
        return cls(
            sid=os.environ["twillio_sid"],
            token=os.environ["twillio_token"],
            from_phone=os.environ["twillio_phone"]
        )

    def __init__(self, sid, token, from_phone):
        self.client = Client(sid, token)
        self.phone = from_phone

    def send_text(self, to, msg):
        txt_msg = self.client.messages.create(
            from_=self.phone,
            to=to,
            body=f'{msg}. -Nikita'
        )
        logger.info("Text msg sent, sid: " + txt_msg.sid + ", status: " + str(txt_msg.status))
        logger.info("Text msg price: " + str(txt_msg.price))
        return txt_msg
