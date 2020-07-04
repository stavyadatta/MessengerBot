import random
import os
from flask import Flask, request
from pymessenger.bot import Bot
from modifyingMessages import textDecider

app = Flask(__name__)

VERIFY_TOKEN = 'COVID_CHATS'
ACCESS_TOKEN = 'EAAMd3g3exIMBADqWvOr89Yi4QUEne7QTZARU4qEQPRxp0a8MJHBNZCqtw4D5GrC1uJCV6PbPKU1X7OGb0jiOw3MQ435cKZCvNjqgByl1D7b6wvXvqlgXQjZC0ZAVZABQBv1ZAQV5biOZBtZCcbAq5T3eGTZBIEf9gIcuVr5cpTM1zy0gZDZD '
#ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
#VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
bot = Bot(ACCESS_TOKEN)


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
