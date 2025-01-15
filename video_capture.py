import os.path

import cv2
import tkinter as tk
from tkinter import Frame
import cv2
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import tkinter as tk
from tkinter import messagebox, filedialog


class VideoCapture:
    def __init__(self, parent_frame, controls_frame):
        """
        Initializes the VideoCapture Instance
        :param root: The Tkinter frame where the video feed will be displayed
        """

        self.parent_frame = parent_frame
        self.cap = cv2.VideoCapture(0)  # Open the video capture

        self.running = True
        self.bw_mode = False
        self.brightness = 1.0
        self.contrast = 1.0

        self.video_label = tk.Label(parent_frame)
        self.video_label.pack(fill=tk.BOTH, expand=True)

        # Create control elements
        self.create_controls(controls_frame)

        # Start Updating frames
        self.update_frame()

        # Bind the destroy event to clean up resources
        parent_frame.bind("<Destroy>", self.on_close)

    def create_controls(self, frame):
        """
        Creates control elements in the controls frame
        :param frame:
        :return:
        """
        # Capture Width Slider
        tk.Label(frame, text="Capture Width").pack()
        self.capture_width_slider = tk.Scale(frame, from_=100, to=640, orient=tk.HORIZONTAL)
        self.capture_width_slider.set(640)
        self.capture_width_slider.pack()

        # Capture Height Slider
        tk.Label(frame, text="Capture Height").pack()
        self.capture_height_slider = tk.Scale(frame, from_=100, to=480, orient=tk.HORIZONTAL)
        self.capture_height_slider.set(480)
        self.capture_height_slider.pack()

        # Snap Frame Button
        tk.Button(frame, text="Snap Frame", command=self.snap_frame).pack(pady=5)

        # BW Toggle Button
        self.bw_button = tk.Button(frame, text="BW: OFF", command=self.toggle_bw)
        self.bw_button.pack(pady=5)

        # Brightness Slider
        tk.Label(frame, text="Brightness").pack()
        self.brightness_slider = tk.Scale(frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack()

        # Contrast Slider
        tk.Label(frame, text="Contrast").pack()
        self.contrast_slider = tk.Scale(frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack()
    def update_frame(self):
        """
        Fetches and updates the video frame in the label.
        :return:
        """

        if not self.running:
            return

        ret, frame = self.cap.read()

        if ret:
            # Apply width/height adjustments
            width = self.capture_width_slider.get()
            height = self.capture_height_slider.get()
            frame = cv2.resize(frame, (width, height))

            # Apply brightness and contrast
            self.brightness = self.brightness_slider.get()
            self.contrast = self.contrast_slider.get()
            frame = cv2.convertScaleAbs(frame, alpha=self.contrast, beta=50 * (self.brightness - 1))

            # Apply BW mode if enabled
            if self.bw_mode:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

            # Convert frame to ImageTk format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        # Call update_frame again after 200ms (5 fps)
        self.parent_frame.after(200, self.update_frame)

    def snap_frame(self):
        """
        Saves the current frame as an image.
        :return:
        """
        ret, frame = self.cap.read()
        if ret:
            # Apply brightness and contrast adjustments
            brightness = self.brightness_slider.get()
            contrast = self.contrast_slider.get()
            frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=50 * (brightness - 1))

            # Apply BW mode if enabled
            if self.bw_mode:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

            # Generate file name with timestamp for uniqueness
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = os.path.join("./Images", f"snapshot_{timestamp}.jpg")
            cv2.imwrite(file_name, frame)
            print(f"Frame saved to {file_name}")

    def toggle_bw(self):
        """
        Toggles black and white mode
        :return:
        """
        self.bw_mode = not self.bw_mode
        self.bw_button.config(text="BW: ON" if self.bw_mode else "BW: OFF")

    def on_close(self):
        # Release the capture and close the window
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    pass
    # root = tk.Tk()
    # app = VideoCaptureApp(root)
    #
    # # Handle closing the window
    # root.protocol("WM_DELETE_WINDOW", app.on_close)
    # root.mainloop()