import os
import cv2
import argparse
import requests
import gptstream


API_KEY = os.getenv('OPENAI_API_KEY')

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def main(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise IOError(f"Cannot load image from {image_path}")

    payload = gptstream.compose_payload(image=image, prompt="What is this?")

    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers=HEADERS, json=payload).json()

    print(response['choices'][0]['message']['content'])

    cv2.imshow('Loaded Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image display script')
    parser.add_argument('--image_path', type=str, help='Path to the image file')
    args = parser.parse_args()
    main(args.image_path)
