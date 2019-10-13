import os

from flask import Flask
from flask import request

from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import MessageEvent
 
# Set credentilas securely
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)

app = Flask(__name__)

# Instanciate LINEBot object 
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route('/callback', methods=['POST'])
def callback():
    print('>>> Calllbacked.')
    sig = request.headers['X-Line-Signature']
    req = request.get_data(as_text=True)
    print('>>> sig : \n{}'.format(sig))
    print('>>> req : \n{}'.format(req))
    handler.handle(req, sig)
    return 'OK'


if __name__ == "__main__":
    print('>>> Starting Flask apps as background process...')
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)