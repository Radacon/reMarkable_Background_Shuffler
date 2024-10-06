#!/usr/bin/env python3
import os
from PIL import Image, ImageDraw, ImageFont

def add_text_with_outline(image_path, text, position, font_size, output_path):
    try:
        # Open the image
        img = Image.open(image_path).convert("RGBA")
        
        # Prepare for drawing
        draw = ImageDraw.Draw(img)
        
        # Load the default font
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", font_size)
        except OSError:
            # Fallback to default Pillow font if DejaVuSans.ttf is not available
            font = ImageFont.load_default()

        # Define text color (black) and outline color (white)
        text_color = (255, 255, 255)  # White fill
        outline_color = (0, 0, 0)  # Black outline

        # Position of the text
        x, y = position

        # Draw black outline by drawing text multiple times with slight offsets
        draw.text((x-2, y-2), text, font=font, fill=outline_color)
        draw.text((x+2, y-2), text, font=font, fill=outline_color)
        draw.text((x-2, y+2), text, font=font, fill=outline_color)
        draw.text((x+2, y+2), text, font=font, fill=outline_color)

        # Draw the main white text on top
        draw.text((x, y), text, font=font, fill=text_color)

        # Convert back to RGB if saving as JPEG
        if output_path.lower().endswith(('.jpg', '.jpeg')):
            img = img.convert("RGB")

        # Save the result
        img.save(output_path)
    except Exception as e:
        print(f"Skipping {image_path} due to an error: {e}")

# Function to calculate font size based on image dimensions
def calculate_font_size(image_path, text, text_percentage=0.3):
    with Image.open(image_path) as img:
        width, height = img.size
        # Estimate the size of the font to cover the desired percentage of the image
        draw = ImageDraw.Draw(img)
        font_size = 1
        while True:
            try:
                font = ImageFont.truetype("DejaVuSans.ttf", font_size)
            except OSError:
                font = ImageFont.load_default()
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            if text_width >= width * text_percentage or text_height >= height * text_percentage:
                break
            font_size += 1
        return font_size

# Function to process all images in the current directory
def process_images_in_directory(text):
    current_directory = os.getcwd()  # Get current working directory

    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file is an image by extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(current_directory, filename)
            output_path = image_path
            
            # Calculate font size based on image dimensions
            font_size = calculate_font_size(image_path, text)
            position = (100, 100)  # X, Y coordinates for the text
            
            # Add text to the image
            add_text_with_outline(image_path, text, position, font_size, output_path)
            print(f"Processed: {filename} -> {output_path}")

# Example usage
while True:
    text = input("Enter the text to overlay on all images (use \\n for a new line if desired): ")  # Prompt for text to overlay
    text = text.replace("\\n", "\n")
    print("You entered:\n")
    print(text)
    print()
    confirmation = input("Is this text correct? This is a permanent alteration to the files. (yes/no): ").strip().lower()
    if confirmation == 'yes':
        process_images_in_directory(text)
        break
    elif confirmation == 'no':
        print("Please re-enter the text.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")