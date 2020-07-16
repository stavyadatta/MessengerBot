from twilio.twiml.messaging_response import MessagingResponse
from flask import request
from modifyingMessages import textDecider


def whastappFunction():
    print("Function called")
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    response_sent_text = textDecider(incoming_msg)
    print(type(response_sent_text))
    print(response_sent_text)

    if type(response_sent_text) == list:
        for i in response_sent_text:
            msg.body(i)
        return str(resp)
    msg.body(response_sent_text)
    return str(resp)