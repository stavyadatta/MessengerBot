import random
import os
from flask import Flask, request
from pymessenger.bot import Bot
import casesDataSet
import pycountry
app = Flask(__name__)

VERIFY_TOKEN = 'COVID_CHATS'
os.environ['VERIFY_TOKEN'] = 'COVID_CHATS'
ACCESS_TOKEN = 'EAAMd3g3exIMBAH8QbDKRZBOg5cpDmuXdshjL5z357suPlENg47XG7dJnQTdsU94x3JeAzMPZBvwZCyjhyff0LsmTRYTZBIVe8QLrxNK8sw2JqNfAZC1oe3BG5bytve8kGPYMNVlzdJc9pJrYR8cd9vW8Y2vocWWaZCrYwdxo2ntAZDZD '
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
                        response_sent_text = get_message(message['message'].get('text'))
                        send_message(recipient_id, response_sent_text)
                        # in case of gif or text
                        if message['message'].get('attachments'):
                            response_non_text = get_message()
                            send_message(recipient_id, response_non_text)
        return "Message Processed"



def verify_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid argument"


def get_message(country):
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!",
                        "We're greatful to know you :)"]
    # return selected item to the user
    numberOfCases = ''
    deaths = ''
    if pycountry.countries.get(name=country):
        numberOfCases, deaths = casesDataSet.numberOfCasesInCountry(country)
    random_message = random.choice(sample_responses)
    random_message += ' cases {} and deaths {}'.format(numberOfCases, deaths)
    return random_message



def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    import os

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
