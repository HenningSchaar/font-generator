# Font Generator

## Overview
The Font Generator is a Python application that takes BMP images with black lines on a white background and converts them into a system-wide usable font. This project automates the process of image processing and font creation.

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

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.