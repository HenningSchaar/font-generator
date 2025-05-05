from PIL import Image
import numpy as np

class ImageProcessor:
    def __init__(self, max_size=64):
        self.max_size = max_size

    def trim_whitespace(self, bitmap):
        """Remove whitespace from both sides of the image"""
        # Find the leftmost black pixel
        left_border = bitmap.shape[1]
        for x in range(bitmap.shape[1]):
            if np.any(bitmap[:, x]):
                left_border = x
                break
                
        # Find the rightmost black pixel
        right_border = 0
        for x in range(bitmap.shape[1]-1, -1, -1):
            if np.any(bitmap[:, x]):
                right_border = x + 1
                break
        
        # Return trimmed bitmap
        return bitmap[:, left_border:right_border]

    def scale_image(self, image):
        """Scale the image down while maintaining aspect ratio"""
        width, height = image.size
        if width > self.max_size or height > self.max_size:
            scale = min(self.max_size / width, self.max_size / height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            return image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return image

    def process_image(self, file_path):
        # Open image with transparency support
        image = Image.open(file_path).convert('RGBA')
        
        # Create a white background
        background = Image.new('RGBA', image.size, (255, 255, 255, 255))
        
        # Composite the image onto the white background
        image = Image.alpha_composite(background, image)
        
        # Scale image
        image = self.scale_image(image)
        
        # Convert to black and white
        image = image.convert('1')
        
        # Convert to numpy array and invert (True for black, False for white)
        bitmap = ~np.array(image)
        
        # Trim whitespace from both sides
        bitmap = self.trim_whitespace(bitmap)
        
        return bitmap