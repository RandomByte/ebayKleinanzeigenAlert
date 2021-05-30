import requests
import os

try:
    from ebAlert.credential import TOKEN, CHAT_ID
except ImportError:
    TOKEN = os.environ["EB_ALERT_TOKEN"]
    CHAT_ID = os.environ["EB_ALERT_CHAT_ID"]


def send_message(message):
    send_text = """https://api.telegram.org/bot{}/sendMessage?chat_id={}
    &parse_mode=Markdown&text={}""".format(TOKEN,
                                           CHAT_ID,
                                           message)
    response = requests.get(send_text)
    return response.json()['ok']
