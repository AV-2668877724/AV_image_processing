🖼️ Image Color Analysis & Conversion (RGB → CMY → HSI)

This project performs automated image color analysis by dividing an input image into 9 equal horizontal grids and computing essential color model information for each grid. It extracts average RGB values, converts them into Normalized RGB, CMY, and HSI, and also displays a color patch representing each grid’s dominant color.

This tool is useful for beginners learning digital image processing concepts and for those who want a simple demonstration of color model conversions using Python.

🚀 Features
✅ Image Grid Segmentation

The input image is divided into 9 horizontal sections.

Each part is analyzed independently.

🎨 RGB Extraction

Converts BGR → RGB using OpenCV.

Automatically samples dominant pixels from each grid.

Computes the average RGB value of the grid.

🔄 Color Model Conversions

For each grid’s average color, the project computes:

Normalized RGB

Scales each component into a 0–1 range.

CMY (Cyan–Magenta–Yellow)

Converts RGB into subtractive color model used in printing.

HSI (Hue–Saturation–Intensity)

Shows human-perception–oriented color components.

Handles angle calculation and division edge cases.

📌 Color Patch Display

Displays a small 400×200 rectangle showing the calculated grid color.

Ensures visibility by auto-adjusting dark colors.

🧮 Mathematical Foundations

The project includes clear formulas for:

Normalized RGB

CMY conversion

HSI: hue angle, saturation, intensity

🛠️ Technologies Used

Python

OpenCV (cv2) – image processing

NumPy – numerical operations

PIL (Pillow) – image display

Custom modules:

AV_image_conversion_RGB_CMY_HSI.py

AV_display_image_with_RGB.py

📂 How It Works

Load the image (picture.jpeg).

Detect image height & divide into 9 equal grids.

For each grid:

Extract pixel values.

Compute average RGB.

Convert to Normalized RGB, CMY, and HSI.

Print values.

Display color patch.

📸 Example Output (Console)
Average value of RGB in First Grid: (122, 98, 75)
Normalized RGB: (0.478, 0.384, 0.294)
CMY: (0.521, 0.615, 0.705)
HSI: (32.560°, 0.221, 98.333)
Displayed color patch for RGB (122, 98, 75)

🎯 Purpose of This Project

This project was created to help understand:

How images store pixel values

How to extract & average RGB components

How different color models (RGB, CMY, HSI) represent the same color

Practical implementation of formulas in Python

Working with OpenCV and PIL

It serves as a great mini-project for image processing, color theory, or digital media coursework.
