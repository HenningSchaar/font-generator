import os
from image_processor import ImageProcessor
from font_builder import FontBuilder

# Define mapping for special character files to their actual characters
SPECIAL_CHARS = {
    'comma.png': ',',
    'dot.png': '.',
    'question.png': '?',
    'exclamation.png': '!',
    'underscore.png': '_',
    'hyphen.png': '-',
    'colon.png': ':'
}

def main():
    # Initialize processors with custom size if needed
    image_processor = ImageProcessor(max_size=200)  # or any other size
    font_builder = FontBuilder()
    
    # Directory containing image files
    input_dir = "../input"
    
    # Process each PNG or BMP file
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        char = None
        
        # Check if it's a special character
        if filename in SPECIAL_CHARS:
            char = SPECIAL_CHARS[filename]
        # Check if it's a letter file
        elif filename.lower().endswith(('.png', '.bmp')) and len(filename) > 4:
            char = filename[0]  # Get character from filename (e.g., "A" from "A.png")
            
        if char:
            # Process image
            bitmap = image_processor.process_image(file_path)
            # Add to font
            font_builder.add_character(char, bitmap)
    
    # Save the font
    font_builder.save_font("../output/custom_font")

if __name__ == "__main__":
    main()