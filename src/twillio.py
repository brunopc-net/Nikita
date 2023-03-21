import log4p
from twilio.rest import Client

logger = log4p.GetLogger(__name__, config="log4p.json").logger


class TwillioClient:

    def __init__(self, sid, token, from_phone):
        self.client = Client(sid, token)
        self.phone = from_phone

    def send_text(self, to, msg):
        txt_msg = self.client.messages.create(
            from_=self.phone,
            to=to,
            body=msg
        )
        logger.info("Text msg sent, sid: " + txt_msg.sid + ", status: " + str(txt_msg.status))
        logger.info("Text msg price: " + str(txt_msg.price))
