# Real Time ASCII Conversation

### 🎥📜 Convert Live Video into ASCII Art!

Created by **Prosper Manyele**.

---

## 🖋️ Project Description

**ASCII_Convert** is a Python application that captures live webcam video and dynamically converts it into real-time ASCII art.  
Users can switch between the normal camera feed and a live ASCII feed, tweak image settings, and save frames as either normal images or ASCII images.

This project is built using **OpenCV**, **Pillow**, and **Tkinter** for GUI handling, camera capture, and ASCII conversion.

---

## 🛠 How It Works

- Captures live video frames from your webcam.
- Applies real-time brightness, contrast, and grayscale (black-and-white) adjustments.
- Converts each frame into ASCII characters based on brightness mapping.
- Displays the ASCII art live inside the GUI alongside the normal video feed.
- Allows you to:
  - Snap and save a raw camera frame
  - Snap and save an ASCII art frame
  - Toggle between camera view and ASCII view
  - Adjust frame size, brightness, sharpness, and scaling
- Live GUI updating at approximately **5 FPS** for smooth ASCII playback.

---

## 📋 Features

- Live webcam feed
- Live ASCII art feed
- Swap between Normal and ASCII View
- Brightness, Contrast, and Sharpness sliders
- Snap and Save frames (normal or ASCII)
- Fullscreen windowed mode for immersive experience
- Automatically resizes ASCII to match window size without distortion
- Aspect Ratio lock for clean ASCII shapes
- Fine-grain control over output appearance

---

## 💻 How to Use

### 1. Install Requirements

Make sure you have Python 3.9+ installed.  
Then install the required libraries:

```bash
pip install opencv-python pillow numpy
```

---

### 2. Run the Application

Simply run:

```bash
python main.py
```

✅ The application window will open in maximized (windowed fullscreen) mode.

---

### 3. Controls

| Section | Control | Action |
|:---|:---|:---|
| Video Controls | Capture Width / Height | Resize the raw camera feed |
| Video Controls | Brightness / Contrast | Adjust live camera feed |
| Video Controls | BW Toggle | Switch black-and-white mode on/off |
| Video Controls | Snap Frame | Save a raw camera frame |
| Video Controls | Swap View | Switch between Camera and ASCII display |
| ASCII Controls | ASCII Size X | Width (in characters) of ASCII output |
| ASCII Controls | ASCII Brightness | Adjust brightness in ASCII conversion |
| ASCII Controls | ASCII Sharpness | Sharpen the ASCII shapes |
| ASCII Controls | ASCII Scale | Overall scale factor for ASCII output |
| ASCII Controls | Snap Frame to ASCII | Save current view as an ASCII art image |

---

### 4. Keyboard Shortcuts

- **Escape** ➔ Exit fullscreen mode

---

### 5. Saving Outputs

- Raw snapshots are saved under `Images/sample.jpg`
- ASCII art snapshots are saved under `Images/output.jpg`
- You can customize the save paths inside `video_capture.py` if needed.

---

## 📂 Project Structure

```
ASCII_Convert/
│
├── main.py                # Main window setup
├── video_capture.py        # Video capture and control panel
├── ascii_converter.py      # ASCII generation logic
├── image_to_ascii/         # External ASCII conversion module (cited below)
├── Images/                 # Saved frames (raw and ASCII)
├── README.md               # Project documentation (this file)
```

---

## 🧠 Technical Details

- Uses OpenCV (`cv2.VideoCapture`) to access webcam frames.
- Uses Pillow to manipulate frames into ASCII characters.
- GUI is entirely built using **Tkinter**, lightweight and portable.
- Window automatically adapts to screen size, keeping aspect ratio correct.
- ASCII rendering uses brightness-to-character mapping.

---

## 🙏 Credits

- **ASCII conversion logic** was adapted and extended from:  
  🔗 [ajratnam/image-to-ascii](https://github.com/ajratnam/image-to-ascii)  
  Huge thanks to the original project for providing the core ASCII conversion functionality!

---

## 📜 License

This project is open-source and free to use.  
Feel free to customize, modify, and share it as needed!

---

# 🚀 Enjoy converting your live world into ASCII art!

---

# ✅ Quick Final Summary of What Changed:
- Added a full **Credits** section at the bottom.
- Properly cited [ajratnam/image-to-ascii](https://github.com/ajratnam/image-to-ascii).
- Kept your structure clean and professional.

---

Would you like me to also prepare a `requirements.txt` now, so you have a complete release-ready package? 🚀  
(One simple file: just `pip install -r requirements.txt` and you’re set!)  
Want me to generate it?