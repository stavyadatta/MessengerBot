import os
from flask import Flask
from whatsapp_webhook import whastappFunction
from messenger_webhook import messenger_function

app = Flask(__name__)


@app.route('/whatsapp', methods=['POST'])
def whatsApp_bot():
    return whastappFunction()


@app.route('/messenger', methods=['GET', 'POST'])
def receive_message():
    return messenger_function()


if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5557'))
    except ValueError:
        PORT = 5557
    app.run(HOST, PORT)
