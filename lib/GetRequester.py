import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status() # This will raise an error if the request was unsuccessful
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body is not None:
            try:
                data = json.loads(response_body)
                return data
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
        else:
            return None
