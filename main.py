"""
    ASCII_Convert
    by Prosper Manyele
"""
import tkinter as tk
from video_capture import VideoCapture

def main():
    # Create the main window
    window = tk.Tk()
    window.title("ASCII Converter")
    window.geometry("1000x600")
    # window.attributes('-fullscreen', True)

    # Create a frame for video capture
    video_capture_frame = tk.Frame(window, width=640, height=480, bg="black")
    video_capture_frame.grid(row=0, column=0, padx=10, pady=10)
    video_capture_frame.grid_propagate(False)  # Lock frame size
    video_capture_frame.pack_propagate(False)

    # Create a master frame for control panel
    control_panel_frame = tk.Frame(window, width=300, height=480, bg="gray")
    control_panel_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")
    control_panel_frame.grid_propagate(False)

    # Add a title to the control panel
    panel_title = tk.Label(control_panel_frame, text="Control Panel", bg="gray", font=("Arial", 14))
    panel_title.pack(pady=10)

    # --- Split the Control Panel into two inner frames ---
    controls_frame_left = tk.Frame(control_panel_frame, bg="lightgray")
    controls_frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    controls_frame_right = tk.Frame(control_panel_frame, bg="lightgray")
    controls_frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Init the VideoCapture
    video_capture = VideoCapture(video_capture_frame, controls_frame_left, controls_frame_right)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
     main()


