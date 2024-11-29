import os

from PIL import ImageFont
from PIL import ImageDraw
from PIL.Image import Image

def add_centered_text_with_outline(image: Image, text: str, font: str=None, font_size=70):
    """
    Adds centered text with a black outline and white fill in the middle of an image.

    Args:
    image (PIL.Image.Image): The PIL image object.
    text (str): The text to be added to the image.
    font (str, optional): The path to the .ttf font file. Defaults to None, which uses a default font.
    font_size (int, optional): The size of the font. Defaults to 50.

    Returns:
    PIL.Image.Image: The modified image with the text in the middle.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if font:
        font = os.path.join(script_dir, "fonts", font)

    draw = ImageDraw.Draw(image)
    width, height = image.size

    if font:
        font = ImageFont.truetype(font, font_size)
    else:
        font = ImageFont.load_default(font_size)

    # Calculate text size and position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    # Draw text at different offsets around the center to fake an outline
    outline_range = 5
    for x_offset in range(-outline_range, outline_range + 1):
        for y_offset in range(-outline_range, outline_range + 1):
            if x_offset != 0 or y_offset != 0:
                draw.text((text_x + x_offset, text_y + y_offset), text, font=font, fill="black")

    # Draw the main text
    draw.text((text_x, text_y), text, font=font, fill="white")

    return image
