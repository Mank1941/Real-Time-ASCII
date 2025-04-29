# video_capture.py
# Video Capture and ASCII Conversion Panel

import os
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from ascii_converter import gen_ascii_art

class VideoCapture:
    def __init__(self, parent_frame, controls_frame_left, controls_frame_right):
        """
        Initialize the VideoCapture instance.
        """
        self.parent_frame = parent_frame
        self.cap = cv2.VideoCapture(0)  # Open webcam

        self.running = True
        self.bw_mode = False
        self.brightness = 1.0
        self.contrast = 1.0
        self.show_ascii = False

        # Display label for video or ASCII output
        self.video_display_label = tk.Label(parent_frame)
        self.video_display_label.pack(fill=tk.BOTH, expand=True)

        self.create_controls(controls_frame_left, controls_frame_right)
        self.update_frame()

        parent_frame.bind("<Destroy>", self.on_close)

    def create_controls(self, capture_frame, ascii_frame):
        """
        Creates control sliders and buttons.
        """
        # --- Capture Controls ---
        tk.Label(capture_frame, text="Capture Width").pack()
        self.capture_width_slider = tk.Scale(
            capture_frame, from_=100, to=640, orient=tk.HORIZONTAL, command=self.update_ascii_size_limits
        )
        self.capture_width_slider.set(640)
        self.capture_width_slider.pack()

        tk.Label(capture_frame, text="Capture Height").pack()
        self.capture_height_slider = tk.Scale(
            capture_frame, from_=100, to=480, orient=tk.HORIZONTAL, command=self.update_ascii_size_limits
        )
        self.capture_height_slider.set(480)
        self.capture_height_slider.pack()

        tk.Button(capture_frame, text="Snap Frame", command=self.snap_frame).pack(pady=5)
        self.bw_button = tk.Button(capture_frame, text="BW: OFF", command=self.toggle_bw)
        self.bw_button.pack(pady=5)

        tk.Label(capture_frame, text="Brightness").pack()
        self.brightness_slider = tk.Scale(capture_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack()

        tk.Label(capture_frame, text="Contrast").pack()
        self.contrast_slider = tk.Scale(capture_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack()

        self.swap_button = tk.Button(capture_frame, text="Swap View", command=self.swap_view)
        self.swap_button.pack(pady=5)

        # --- ASCII Controls ---
        tk.Button(ascii_frame, text="Snap Frame to ASCII", command=self.snap_frame_to_ascii).pack(pady=5)

        tk.Label(ascii_frame, text="ASCII Size X (width)").pack()
        self.size_x_slider = tk.Scale(ascii_frame, from_=10, to=640, orient=tk.HORIZONTAL)
        self.size_x_slider.set(80)
        self.size_x_slider.pack()

        tk.Label(ascii_frame, text="ASCII Brightness").pack()
        self.ascii_brightness_slider = tk.Scale(ascii_frame, from_=0.5, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.ascii_brightness_slider.set(1.0)
        self.ascii_brightness_slider.pack()

        tk.Label(ascii_frame, text="ASCII Sharpness").pack()
        self.ascii_sharpness_slider = tk.Scale(ascii_frame, from_=0.5, to=3.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.ascii_sharpness_slider.set(1.0)
        self.ascii_sharpness_slider.pack()

        tk.Label(ascii_frame, text="ASCII Scale").pack()
        self.scale_slider = tk.Scale(ascii_frame, from_=0.25, to=2.0, resolution=0.25, orient=tk.HORIZONTAL)
        self.scale_slider.set(1.0)
        self.scale_slider.pack()

    def update_frame(self):
        """
        Updates the displayed frame, switching between raw camera and ASCII.
        """
        if not self.running:
            return

        ret, frame = self.cap.read()
        if ret:
            width = self.capture_width_slider.get()
            height = self.capture_height_slider.get()
            frame = cv2.resize(frame, (width, height))

            frame = cv2.convertScaleAbs(
                frame,
                alpha=self.contrast_slider.get(),
                beta=50 * (self.brightness_slider.get() - 1)
            )

            if self.bw_mode:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(frame_rgb)

            if self.show_ascii:
                # Create ASCII image
                size_x = self.size_x_slider.get()
                aspect_ratio = height / width
                size_y = int(size_x * aspect_ratio)

                ascii_img = gen_ascii_art(
                    pil_img,
                    size=(size_x, size_y),
                    scale=self.scale_slider.get(),
                    brightness=self.ascii_brightness_slider.get(),
                    sharpness=self.ascii_sharpness_slider.get()
                )

                # Resize ASCII image to fit
                display_width = self.video_display_label.winfo_width()
                display_height = self.video_display_label.winfo_height()

                if display_width > 0 and display_height > 0:
                    ascii_img = ascii_img.copy()
                    ascii_img.thumbnail((display_width, display_height), Image.Resampling.LANCZOS)

                imgtk = ImageTk.PhotoImage(image=ascii_img)
            else:
                imgtk = ImageTk.PhotoImage(image=pil_img)

            self.video_display_label.imgtk = imgtk
            self.video_display_label.configure(image=imgtk)

        self.parent_frame.after(200, self.update_frame)

    def snap_frame(self):
        """
        Saves the current raw frame as an image.
        """
        frame = self.take_frame()
        if frame is not None:
            file_name = os.path.join("./Images", "sample.jpg")
            cv2.imwrite(file_name, frame)
            print(f"Frame saved to {file_name}")

    def snap_frame_to_ascii(self):
        """
        Saves the current frame as ASCII art.
        """
        frame = self.take_frame()
        if frame is not None:
            pil_img = Image.fromarray(frame)
            size_x = self.size_x_slider.get()
            capture_width = self.capture_width_slider.get()
            capture_height = self.capture_height_slider.get()
            aspect_ratio = capture_height / capture_width
            size_y = int(size_x * aspect_ratio)

            ascii_img = gen_ascii_art(
                pil_img,
                size=(size_x, size_y),
                scale=self.scale_slider.get()
            )

            ascii_img_path = os.path.join("./Images", "output.jpg")
            ascii_img.save(ascii_img_path)
            print(f"ASCII Art saved to {ascii_img_path}")

    def take_frame(self):
        """
        Captures a frame with camera adjustments.
        """
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.convertScaleAbs(
                frame,
                alpha=self.contrast_slider.get(),
                beta=50 * (self.brightness_slider.get() - 1)
            )
            if self.bw_mode:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            return frame
        return None

    def toggle_bw(self):
        """
        Toggles black and white mode on/off.
        """
        self.bw_mode = not self.bw_mode
        self.bw_button.config(text="BW: ON" if self.bw_mode else "BW: OFF")

    def swap_view(self):
        """
        Switches between normal and ASCII display.
        """
        self.show_ascii = not self.show_ascii
        self.swap_button.config(text="View: ASCII" if self.show_ascii else "View: Normal")

    def update_ascii_size_limits(self, event=None):
        """
        Update the ASCII size slider limit based on capture width.
        """
        capture_width = self.capture_width_slider.get()
        self.size_x_slider.config(to=capture_width)
        if self.size_x_slider.get() > capture_width:
            self.size_x_slider.set(capture_width)

    def on_close(self):
        """
        Safely releases resources on close.
        """
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()

