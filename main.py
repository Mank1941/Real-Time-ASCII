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
    window.geometry("900x500")

    # Create a frame for video capture
    video_capture_frame = tk.Frame(window, width=640, height=480, bg="black")
    video_capture_frame.grid(row=0, column=0, padx=10, pady=10)
    video_capture_frame.grid_propagate(False)  # Lock frame size
    video_capture_frame.pack_propagate(False)

    # Add a label to the video capture frame
    video_label = tk.Label(video_capture_frame, text="Video Capture", fg="white", bg="black")
    video_label.place(relx=0.5, rely=0.5, anchor="center")

    # Create a frame for the video capture panel
    video_capture_panel = tk.Frame(window, width=220, height=480, bg="gray")
    video_capture_panel.grid(row=0, column=1, padx=10, pady=10, sticky="ns")
    video_capture_panel.grid_propagate(False)  # Lock panel size
    video_capture_panel.pack_propagate(False)

    # Add a title to the panel
    panel_title = tk.Label(video_capture_panel, text="Control Panel", bg="gray", font=("Arial", 14))
    panel_title.pack(pady=10)

    # Init the VideoCapture
    video_capture = VideoCapture(video_capture_frame, video_capture_panel)

    # Run the Tkinter event loop
    window.mainloop()

if __name__ == '__main__':
     main()


