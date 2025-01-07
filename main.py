"""
    ASCII_Convert
    by Prosper Manyele
"""
import cv2
from video_capture import*


def display_frame(frame):
    """
    Displays a frame
    :param frame: The frame to display
    """

    height, width, _ = frame.shape

    # Text Properties
    text = f"{width}x{height}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (0, 255, 0)  # Green color in BGR
    thickness = 2
    position = (10, height - 10)  # 10 pixels from the bottom-left corner

    # Overlay the text on the frame
    cv2.putText(frame, text, position, font, font_scale, color, thickness, lineType=cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('ASCII_Convert', frame)

def main():
    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Press 'q' to exit the video capture or click the close button (X).")

    while True:
        # Capture a frame
        frame = capture_frame(cap)
        if frame is None:
            break

        # Display the frame with text
        display_frame(frame)

        # Check if 'q' is pressed or the window is closed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
     main()


