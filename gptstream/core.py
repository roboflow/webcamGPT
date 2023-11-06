import os

import numpy as np
import requests

from gptstream.utils import compose_payload


API_KEY = os.getenv('OPENAI_API_KEY')


class OpanAIConnector:

    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key

    def simple_prompt(self, image: np.ndarray, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = compose_payload(image=image, prompt=prompt)
        response = requests.post("https://api.openai.com/v1/chat/completions",
                                 headers=headers, json=payload).json()
        return response['choices'][0]['message']['content']
