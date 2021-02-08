import pytesseract as pyt

def img_to_text(cover):
    text = pyt.pytesseract.image_to_string(pyt.pytesseract.Image.open(cover))
    text = text.split('\n')
    final = " "
    text = final.join(text)
    return text
