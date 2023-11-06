import cv2
import base64
import numpy as np


def encode_image_to_base64(image: np.ndarray) -> str:
    """
    Encodes a given image represented as a NumPy array to a base64-encoded string.

    Parameters:
       image (np.ndarray): A NumPy array representing the image to be encoded.

    Returns:
       str: A base64-encoded string representing the input image in JPEG format.

    Raises:
       ValueError: If the image cannot be encoded to JPEG format.
   """

    success, buffer = cv2.imencode('.jpg', image)
    if not success:
        raise ValueError("Could not encode image to JPEG format.")

    encoded_image = base64.b64encode(buffer).decode('utf-8')
    return encoded_image


def compose_payload(image: np.ndarray, prompt: str) -> dict:
    """
    Composes a payload dictionary with a base64 encoded image and a text prompt for the GPT-4 Vision model.

    Args:
        image (np.ndarray): The image in the form of a NumPy array to encode and send.
        prompt (str): The prompt text to accompany the image in the payload.

    Returns:
        dict: A dictionary structured as a payload for the GPT-4 Vision model, including the model name,
              an array of messages each containing a role and content with text and the base64 encoded image,
              and the maximum number of tokens to generate.
    """
    base64_image = encode_image_to_base64(image)
    return {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
