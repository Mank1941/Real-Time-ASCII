import cv2
import tkinter as tk
from tkinter import Frame
import cv2
from PIL import Image, ImageTk, ImageOps, ImageEnhance
from tkinter import messagebox

class VideoCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Capture")

        # Create a frame for video display
        self.video_frame = Frame(self.root, width=640, height=480, bg="black")
        self.video_frame.grid(row=0, column=0, padx=0, pady=0)

        # Create a frame for the empty panel on the right
        self.control_panel  = Frame(self.root, width=200, height=480, bg="gray")
        self.control_panel .grid(row=0, column=1, padx=0, pady=0)

        # Create range input fields for width and height
        self.capture_width = tk.Scale(self.control_panel , from_=100, to_=640, orient="horizontal", label="Capture Width")
        self.capture_width.set(320)  # Set default width
        self.capture_width.grid(row=0, column=0, padx=10, pady=10)

        self.capture_height = tk.Scale(self.control_panel , from_=100, to_=480, orient="horizontal", label="Capture Height")
        self.capture_height.set(240)  # Set default height
        self.capture_height.grid(row=1, column=0, padx=10, pady=10)

        # Create a button to take a picture
        self.take_picture_button = tk.Button(self.control_panel , text="Take Picture", command=self.take_picture)
        self.take_picture_button.grid(row=2, column=0, padx=10, pady=20)

        # Create a toggle button for BW mode
        self.bw_mode = tk.BooleanVar(value=False)
        self.bw_toggle = tk.Checkbutton(self.control_panel , text="BW", variable=self.bw_mode,  command=self.toggle_bw_mode)
        self.bw_toggle.grid(row=2, column=1, padx=10, pady=20)

        # Create sliders for Brightness, Saturation, and Contrast
        self.brightness_slider = tk.Scale(self.control_panel, from_=0.5, to_=2.0, resolution=0.1, orient="horizontal",
                                          label="Brightness")
        self.brightness_slider.set(1.0)  # Default brightness
        self.brightness_slider.grid(row=3, column=0, padx=10, pady=10)

        self.contrast_slider = tk.Scale(self.control_panel, from_=0.5, to_=2.0, resolution=0.1, orient="horizontal",
                                        label="Contrast")
        self.contrast_slider.set(1.0)  # Default contrast
        self.contrast_slider.grid(row=3, column=2, padx=10, pady=10)

        # Open the video capture
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not access the webcam.")
            self.root.quit()

        self.update_frame()

    def capture_frame(self):
        """
        Captures a single frame from the webcam.
        :return: A frame (nump array) if successful, otherwise None
        """
        # Capture frame-by-frame
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Could not read a frame from the webcam.")
            return None

        # Resize the frame to half the resolution
        _width = self.capture_width.get()
        _height = self.capture_height.get()
        frame = self.resize_frame(frame, _width, _height)
        return frame

    def resize_frame(self, frame, width, height):
        """
        Resize a frame
        :param frame: The frame to resize
        :param width:
        :param height:
        :return:
        """
        resize_frame = cv2.resize(frame, (width, height))
        return resize_frame

    def display_frame(self, frame):
        # Convert frame (OpenCV format) to PIL Image format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)

        # Check BW mode and convert the PIL Image if necessary
        if self.bw_mode.get():  # If the BW toggle is ON
            image = ImageOps.grayscale(image)  # Convert the PIL Image to grayscale

        # Apply Brightness adjustment
        brightness = self.brightness_slider.get()
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness)

        # Apply Contrast adjustment
        contrast = self.contrast_slider.get()
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)

        # Convert to ImageTk for display
        image_tk = ImageTk.PhotoImage(image)

        # Create or update the label with the frame
        if not hasattr(self, 'image_label'):
            self.image_label = tk.Label(self.video_frame, image=image_tk)
            self.image_label.image = image_tk  # Store the reference to avoid garbage collection
            self.image_label.place(x=0, y=0, width=640, height=480)
        else:
            self.image_label.config(image=image_tk)
            self.image_label.image = image_tk

    def update_frame(self):
        # Capture and display the frame every 30ms (approx. 30 FPS)
        frame = self.capture_frame()
        if frame is not None:
            # Add text to the frame
            # height, width, _ = frame.shape
            # text = f"{width}x{height}"
            # cv2.putText(frame, text, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            # Display the frame
            self.display_frame(frame)

        # Call update_frame again after 200ms (5 FPS)
        self.root.after(200, self.update_frame)

    def take_picture(self):
        # Capture the current frame
        frame = self.capture_frame()
        if frame is not None:
            # Get the current date and time for the filename
            filename = "Images\captured_image.png"

            # Save the frame as an image file
            cv2.imwrite(filename, frame)

            # Display a success message
            messagebox.showinfo("Success", f"Image saved as {filename}")
        else:
            messagebox.showerror("Error", "No frame captured. Try again.")

    def toggle_bw_mode(self):
        mode = "ON" if self.bw_mode.get() else "OFF"
        print(f"BW Mode is now {mode}")

    def on_close(self):
        # Release the capture and close the window
        self.cap.release()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoCaptureApp(root)

    # Handle closing the window
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()