# ascii_converter.py
# Convet Image into Ascii Art

from image_to_ascii.converter import image_to_ascii, ascii_to_image
from PIL import Image

def gen_ascii_art(image, size=None, scale=1):
    ascii_art = image_to_ascii(image, size=size, scale=scale)
    return ascii_to_image(ascii_art)

def main():
    image_path = "Images/sample.jpg"
    image = Image.open(image_path)
    ascii_image = gen_ascii_art(image, size=(10, 10))
    ascii_image.show()
    # ascii_image.save('Images/output.jpg')
    print(f"ASCII Art saved to Images/output.jpg")

if __name__ == "__main__":
    # Replace this with the path to your image
    main()