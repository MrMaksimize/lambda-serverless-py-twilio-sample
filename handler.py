import sys, os, json

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import logging

from twilio import twiml

resp = twiml.Response()
with resp.message("Hello, Mobile Monkey") as m:
    m.media("https://demo.twilio.com/owl.png")

log = logging.getLogger()
log.setLevel(logging.DEBUG)

def receive_sms(event, context):
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/xml"
        },
        "body": str(resp)
    }

    return response
