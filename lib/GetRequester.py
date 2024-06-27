import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        res = requests.get(self.url)
        return res.content

    def load_json(self):
        res_body = self.get_response_body()
        return json.loads(res_body)