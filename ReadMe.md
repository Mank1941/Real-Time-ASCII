Perfect — now that your project is officially hosted at:  
🔗 **[Real-Time-ASCII](https://github.com/Mank1941/Real-Time-ASCII)**

and you want the `README.md` to properly:

- Mention that `config.py` and `converter.py` come from the cited external repo
- Credit the original creator clearly
- Integrate it into your professional documentation

✅ Let's update your `README.md` accordingly.

---

# 📜 Updated `README.md` for Real-Time-ASCII

# Real-Time-ASCII

🎥📜 Convert Live Video into ASCII Art — in Real Time!

Created by **Prosper Manyele**.

---

## 🖋️ Project Description

**Real-Time-ASCII** is a Python application that captures live webcam video and dynamically converts it into real-time ASCII art.  
Users can easily switch between the normal camera feed and a live ASCII feed, tweak image settings, and save frames as either normal images or ASCII art.

This project is built using **OpenCV**, **Pillow**, and **Tkinter** for GUI handling, camera capture, and ASCII conversion.

---

## 🛠 How It Works

- Captures live video frames from your webcam.
- Applies real-time brightness, contrast, and grayscale (black-and-white) adjustments.
- Converts each frame into ASCII characters based on brightness mapping.
- Displays the ASCII art live inside the GUI.
- Allows you to:
  - Snap and save a raw camera frame
  - Snap and save an ASCII art frame
  - Toggle between normal camera view and ASCII view
  - Adjust frame size, brightness, sharpness, and scaling
- Live GUI updating at approximately **5 FPS** for smooth ASCII playback.

---

## 📋 Features

- 🎥 Live webcam feed
- 🅰️ Live ASCII art feed
- 🔄 Swap between Normal and ASCII View
- ✨ Real-time Brightness, Contrast, and Sharpness sliders
- 🖼 Snap and Save frames (normal or ASCII)
- ⚡ Fullscreen windowed mode for immersive experience
- 📐 Automatically resizes ASCII to match window size without distortion
- 🧠 Aspect Ratio lock for clean ASCII shapes
- 🎛 Fine-grain control over output appearance

---

## 💻 How to Use

### 1. Install Requirements

First, install the necessary Python libraries:

```bash
pip install -r requirements.txt
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

You can customize the save paths in `video_capture.py` if needed.

---

## 📂 Project Structure

```
Real-Time-ASCII/
│
├── main.py                  # Main window and app entry
├── video_capture.py          # Webcam control and ASCII toggling
├── ascii_converter.py        # Logic to connect images to ASCII generation
├── config.py             # Character mapping configuration
├── converter.py          # Main ASCII generation algorithm
├── Images/                   # Saved frames (raw and ASCII)
├── README.md                 # Project documentation (this file)
├── requirements.txt          # Dependency list
```

---

## 🙏 Credits

- **ASCII Conversion Core**:
  - The `config.py` and `converter.py` files inside `image_to_ascii/` are adapted from the repository:  
    🔗 [ajratnam/image-to-ascii](https://github.com/ajratnam/image-to-ascii)  
  - Big thanks to the original creator for providing an excellent foundation for ASCII art generation!
  
- **Original application logic**, live video control, GUI design, and real-time system were designed and built by Prosper Manyele.

---

## 📜 License

This project is open-source and free to use.  
Feel free to customize, modify, and share it with attribution where appropriate!

---
