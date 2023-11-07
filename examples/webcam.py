import threading

import cv2

import webcamgpt

FRAME = None
FRAME_CAPTURE_EVENT = threading.Event()
STOP = False


def capture_frame(camera_id):
    global FRAME
    global STOP
    global FRAME_CAPTURE_EVENT
    cap = cv2.VideoCapture(camera_id)

    while cap.isOpened() and not STOP:
        ret, frame = cap.read()
        if not ret:
            break
        FRAME = frame
        FRAME_CAPTURE_EVENT.set()


def main():
    global STOP
    global FRAME
    global FRAME_CAPTURE_EVENT
    connector = webcamgpt.OpanAIConnector()

    frame_thread = threading.Thread(target=capture_frame, args=(1,))
    frame_thread.start()
    FRAME_CAPTURE_EVENT.wait()
    while True:
        print("Please enter your prompt or type 'quit' to exit:")
        prompt = input()
        if prompt.lower() == 'quit':
            break

        image_numpy = FRAME.copy()
        description = connector.simple_prompt(image=image_numpy, prompt=prompt)
        print(description)


if __name__ == '__main__':
    main()
