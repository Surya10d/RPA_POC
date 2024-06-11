from PIL import Image
import pytesseract
import os


def solve_captcha(captcha_path):
    # Path to the Tesseract executable (required if it's not in your PATH)
    # Example for Windows:
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    if os.name == 'nt':
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load an image from file
    image = Image.open(captcha_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    # Print and Return the extracted text
    captcha = text.split("captcha")[0].split("Register Online ")[-1].split(" &")[0].replace(" ", "")
    captcha = captcha[:6]
    print("Captcha text", captcha)

    ff = open("captcha.txt", "a")
    ff.write("\n")
    ff.writelines(captcha)
    ff.close()

    return captcha


if __name__ == "__main__":
    captcha_path = ""
    solve_captcha(captcha_path)
