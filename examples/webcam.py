import cv2
import argparse


def main(camera_id):
    cap = cv2.VideoCapture(camera_id)

    if not cap.isOpened():
        raise IOError(f"Cannot open webcam with ID {camera_id}")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Webcam Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Webcam display script')
    parser.add_argument('--id', type=int, default=0, help='ID of the webcam device')
    args = parser.parse_args()
    main(args.id)
