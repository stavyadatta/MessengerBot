import random
import os
from flask import Flask, request
from pymessenger.bot import Bot
from modifyingMessages import textDecider
from flask import request
from whatsapp_webhook import whastappFunction
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

VERIFY_TOKEN = 'COVID_CHATS'
ACCESS_TOKEN = 'EAAMd3g3exIMBAD4cejiCObrARbzSwpq79ZCeGWtZAmW2nSj4bk8rYZCDZCWJctU0aMygZA2VQu7sqJMGn6vq4DyUbXIzFIHXgRlvQMGzEbDRylKevM2MfBRvd9yN7T5fSsSijyxWdTcIGWRLOPmva0PhS9GOZCjec3XMe2v6AbbQZDZD '
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
# VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)


@app.route('/whatsapp', methods=['POST'])
def whatsApp_bot():
    return whastappFunction()


@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_token(token_sent)
    else:
        output = request.get_json()
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = textDecider(message['message'].get('text'))
                        # response_sent_text = length_of_text_consideration(response_sent_text)
                        send_message(recipient_id, response_sent_text)
                        # in case of gif or text
                        if message['message'].get('attachments'):
                            response_non_text = textDecider()
                            send_message(recipient_id, response_non_text)
        return "Message Processed"


def verify_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid argument"


def length_of_text_consideration(response_sent_text):
    list_of_text = []
    if type(response_sent_text) == list:
        for info in response_sent_text:
            if len(info) > 1230:
                list_sub_text = info.split('\n\n')
                list_of_text += list_sub_text
            else:
                list_of_text.append(info)
        return list_of_text
    else:
        if len(response_sent_text) > 1270:
            list_of_text = response_sent_text.split('\n\n')
            return list_of_text
        else:
            return response_sent_text


def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    if type(response) == list:
        for list_entity in response:
            bot.send_text_message(recipient_id, list_entity)
    else:
        bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5557'))
    except ValueError:
        PORT = 5557
    app.run(HOST, PORT)
