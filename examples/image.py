import cv2
import argparse
import gptstream


def main(image: str, prompt: str):
    connector = gptstream.OpanAIConnector()
    image_numpy = cv2.imread(image)
    if image is None:
        raise IOError(f"Cannot load image from {image_numpy}")

    description = connector.simple_prompt(image=image_numpy, prompt=prompt)
    print(description)

    cv2.imshow('Loaded Image', image_numpy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image display script with a prompt')
    parser.add_argument(
        '--image', type=str, required=True, help='Path to the image file')
    parser.add_argument(
        '--prompt', type=str, required=True, help='Prompt for the AI to describe the image')
    args = parser.parse_args()
    main(args.image, args.prompt)
