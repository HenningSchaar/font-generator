# Font Generator

## Overview
The Font Generator is a Python application that takes BMP images with black lines on a white background and converts them into a system-wide usable font. This project automates the process of image processing and font creation.

It is entirely vibe coded, both out of laziness and as an experiment. Please don't take the code to seriously. "Claude 3.7 Thinking" was used for most of it. 

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd font-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Prepare your BMP files:
   - Place your BMP files in the `input` directory. Ensure that the files are named appropriately (e.g., "A.bmp", "B.bmp", etc.).

## Usage
To generate the font, run the main script:
```
python src/font_generator.py
```

This will process the images in the `input` directory and create the font files in the `output` directory.

## Output
The generated font files will be located in the `output` directory. Follow the instructions in `output/README.md` to install the font system-wide.