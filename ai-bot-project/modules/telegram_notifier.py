import requests
import json
import os

class TelegramNotifier:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '../configs/secrets.json')
        with open(config_path) as f:
            self.config = json.load(f)
    
    def send_alert(self, message, image_path=None):
        url = f"https://api.telegram.org/bot{self.config['TELEGRAM_TOKEN']}/sendMessage"
        params = {
            "chat_id": self.config['CHAT_ID'],
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, params=params)
        
        if image_path:
            self.send_photo(image_path, message)

    def send_photo(self, image_path, caption=""):
        url = f"https://api.telegram.org/bot{self.config['TELEGRAM_TOKEN']}/sendPhoto"
        files = {'photo': open(image_path, 'rb')}
        data = {'chat_id': self.config['CHAT_ID'], 'caption': caption}
        requests.post(url, files=files, data=data)