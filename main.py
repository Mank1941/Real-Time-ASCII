"""
    ASCII_Convert
    by Prosper Manyele
"""
import tkinter as tk
from video_capture import VideoCapture

def main():
    # Create main window
    window = tk.Tk()
    window.title("ASCII Converter")
    window.state('zoomed')  # Windowed fullscreen

    # Set up main grid
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=3)  # Video side larger
    window.grid_columnconfigure(1, weight=1)

    # Video Capture Panel
    video_capture_frame = tk.Frame(window, bg="black")
    video_capture_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Control Panel
    control_panel_frame = tk.Frame(window, bg="gray")
    control_panel_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    control_panel_frame.grid_rowconfigure(1, weight=1)
    control_panel_frame.grid_rowconfigure(2, weight=1)

    panel_title = tk.Label(control_panel_frame, text="Control Panel", bg="gray", font=("Arial", 18))
    panel_title.grid(row=0, column=0, pady=10)

    controls_frame_left = tk.Frame(control_panel_frame, bg="lightgray")
    controls_frame_left.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    controls_frame_right = tk.Frame(control_panel_frame, bg="lightgray")
    controls_frame_right.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    # Initialize VideoCapture
    VideoCapture(video_capture_frame, controls_frame_left, controls_frame_right)

    # Exit fullscreen with Escape
    window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

    window.mainloop()

if __name__ == '__main__':
    main()
