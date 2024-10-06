import os
from PIL import Image, ImageDraw, ImageFont

def add_text_with_outline(image_path, text, position, font_size, output_path):
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    
    # Prepare for drawing
    draw = ImageDraw.Draw(img)
    
    # Load the default font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        # Fallback to default Pillow font if arial.ttf is not available
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

    # Save the result
    img.save(output_path)

# Function to process all images in the current directory
def process_images_in_directory(text, position, font_size):
    current_directory = os.getcwd()  # Get current working directory

    # Loop through all files in the current directory
    for filename in os.listdir(current_directory):
        # Check if the file is an image by extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(current_directory, filename)
            output_path = image_path
            
            # Add text to the image
            add_text_with_outline(image_path, text, position, font_size, output_path)
            print(f"Processed: {filename} -> {output_path}")

# Example usage
text = input("Enter the text to overlay on all images \"\\n\" = Newline: ")  # Prompt for text to overlay
position = (100, 100)  # X, Y coordinates for the text
font_size = 40  # Font size

# Process all images in the current directory
process_images_in_directory(text, position, font_size)