import os.path

import cv2
import tkinter as tk
from tkinter import Frame
import cv2
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import tkinter as tk
from tkinter import messagebox, filedialog

from ascii_converter import gen_ascii_art

class VideoCapture:
    def __init__(self, parent_frame, controls_frame_left, controls_frame_right):
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
        self.show_ascii = False

        self.video_display_label = tk.Label(parent_frame)
        self.video_display_label.pack(fill=tk.BOTH, expand=True)

        self.create_controls(controls_frame_left, controls_frame_right)
        self.update_frame()

        # Bind the destroy event to clean up resources
        parent_frame.bind("<Destroy>", self.on_close)

    def create_controls(self, capture_frame, ascii_frame):
        """
        Creates control elements in the controls frame
        :param frame:
        :return:
        """
        # Capture Width Slider
        tk.Label(capture_frame, text="Capture Width").pack()
        self.capture_width_slider = tk.Scale(
            capture_frame, from_=100, to=640, orient=tk.HORIZONTAL, command=self.update_ascii_size_limits
        )
        self.capture_width_slider.set(640)
        self.capture_width_slider.pack()

        # Capture Height Slider
        tk.Label(capture_frame, text="Capture Height").pack()
        self.capture_height_slider = tk.Scale(
            capture_frame, from_=100, to=480, orient=tk.HORIZONTAL, command=self.update_ascii_size_limits
        )
        self.capture_height_slider.set(480)
        self.capture_height_slider.pack()

        # Snap Frame Button
        tk.Button(capture_frame, text="Snap Frame", command=self.snap_frame).pack(pady=5)

        # BW Toggle Button
        self.bw_button = tk.Button(capture_frame, text="BW: OFF", command=self.toggle_bw)
        self.bw_button.pack(pady=5)

        # Brightness Slider
        tk.Label(capture_frame, text="Brightness").pack()
        self.brightness_slider = tk.Scale(capture_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack()

        # Contrast Slider
        tk.Label(capture_frame, text="Contrast").pack()
        self.contrast_slider = tk.Scale(capture_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack()

        # Swap View Button
        self.swap_button = tk.Button(capture_frame, text="Swap View", command=self.swap_view)
        self.swap_button.pack(pady=5)

        # ASCII Controls
        # Snap Frame and Convert to ASCII
        tk.Button(ascii_frame, text="Snap Frame to ASCII", command=self.snap_frame_to_ascii).pack(pady=5)

        # Size X (Width)
        tk.Label(ascii_frame, text="ASCII Size X (width)").pack()
        self.size_x_slider = tk.Scale(ascii_frame, from_=10, to=640, orient=tk.HORIZONTAL)
        self.size_x_slider.set(640)  # Default
        self.size_x_slider.pack()

        # ASCII Brightness Slider
        tk.Label(ascii_frame, text="ASCII Brightness").pack()
        self.ascii_brightness_slider = tk.Scale(ascii_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.ascii_brightness_slider.set(1.0)
        self.ascii_brightness_slider.pack()

        # ASCII Sharpness Slider
        tk.Label(ascii_frame, text="ASCII Sharpness").pack()
        self.ascii_sharpness_slider = tk.Scale(ascii_frame, from_=0.5, to=3.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.ascii_sharpness_slider.set(1.0)
        self.ascii_sharpness_slider.pack()

        # Scale
        tk.Label(ascii_frame, text="ASCII Scale").pack()
        self.scale_slider = tk.Scale(ascii_frame, from_=0.25, to=2.0, resolution=0.25, orient=tk.HORIZONTAL)
        self.scale_slider.set(1.0)  # Default
        self.scale_slider.pack()

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
            pil_img = Image.fromarray(frame)

            if self.show_ascii:
                size_x = self.size_x_slider.get()

                capture_width = self.capture_width_slider.get()
                capture_height = self.capture_height_slider.get()
                aspect_ratio = capture_height / capture_width
                size_y = int(size_x * aspect_ratio)
                scale = self.scale_slider.get()

                # Get brightness and sharpness settings
                ascii_brightness = self.ascii_brightness_slider.get()
                ascii_sharpness = self.ascii_sharpness_slider.get()

                ascii_img = gen_ascii_art(pil_img, size=(size_x, size_y), scale=scale, brightness=ascii_brightness, sharpness=ascii_sharpness)

                imgtk = ImageTk.PhotoImage(image=ascii_img)
            else:
                # Normal Image
                imgtk = ImageTk.PhotoImage(image=pil_img)

            # Display
            self.video_display_label.imgtk = imgtk
            self.video_display_label.configure(image=imgtk)

        # Call update_frame again after 200ms (5 fps)
        self.parent_frame.after(200, self.update_frame)

    def take_frame(self):
        """
        Takes the current frame as an Image
        :return: Frame
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

            return frame
        return None

    def snap_frame(self):
        """
        Saves the current frame as an image.
        :return:
        """
        frame = self.take_frame()
        self.save_frame(frame)

    def save_frame(self, frame):
        file_name = os.path.join("./Images", f"sample.jpg")
        cv2.imwrite(file_name, frame)
        print(f"Frame saved to {file_name}")

    def snap_frame_to_ascii(self):
        """
        Snaps the current frame, saves it, and converts it to ASCII art image.
        """
        frame = self.take_frame()

        if (frame is not None):
            # self.save_frame(frame)
            pil_image = Image.fromarray(frame)

            # --- Get ASCII settings ---
            size_x = self.size_x_slider.get()

            capture_width = self.capture_width_slider.get()
            capture_height = self.capture_height_slider.get()
            aspect_ratio = capture_height / capture_width
            size_y = int(size_x * aspect_ratio)

            scale = self.scale_slider.get()

            # Convert saved frame to ASCII art
            # from ascii_converter import gen_ascii_art  # <-- import here to avoid circular imports
            ascii_img = gen_ascii_art(pil_image, size=(size_x, size_y), scale=scale)

            # Save the ASCII image
            ascii_img_path = os.path.join("./Images", f"output.jpg")
            ascii_img.save(ascii_img_path)

            print(f"ASCII Art saved to {ascii_img_path}")

    def toggle_bw(self):
        """
        Toggles black and white mode
        :return:
        """
        self.bw_mode = not self.bw_mode
        self.bw_button.config(text="BW: ON" if self.bw_mode else "BW: OFF")

    def update_ascii_size_limits(self, event=None):
        """
        Update the max values of ASCII Size X and Size Y sliders
        based on the current Capture Width and Capture Height values.
        """
        capture_width = self.capture_width_slider.get()
        capture_height = self.capture_height_slider.get()

        self.size_x_slider.config(to=capture_width)
        self.size_y_slider.config(to=capture_height)

        # Optional: Adjust current slider value if it's greater than the new max
        if self.size_x_slider.get() > capture_width:
            self.size_x_slider.set(capture_width)

        if self.size_y_slider.get() > capture_height:
            self.size_y_slider.set(capture_height)

    def swap_view(self):
        """
        Toggle between showing normal video and ASCII video.
        """
        self.show_ascii = not self.show_ascii
        self.swap_button.config(text="View: ASCII" if self.show_ascii else "View: Normal")

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