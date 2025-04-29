# ascii_converter.py
# Convet Image into Ascii Art

from converter import image_to_ascii, ascii_to_image
from PIL import Image

def gen_ascii_art(image, size=None, scale=1.0, brightness=1.0, sharpness=1.0):
    """
        Generates an ASCII art image from a given PIL image.
    """
    ascii_art = image_to_ascii(
        image,
        size=size,
        scale=scale,
        brightness=brightness,
        sharpness=sharpness
    )
    return ascii_to_image(ascii_art)

def main():
    """
        Test function for generating ASCII art from a sample image.
    """
    image_path = "Images/sample.jpg"
    image = Image.open(image_path)
    ascii_image = gen_ascii_art(image, size=(80, 60))
    ascii_image.show()
    ascii_image.save('Images/output.jpg')
    print("ASCII Art saved to Images/output.jpg")

if __name__ == "__main__":
    # Replace this with the path to your image
    main()