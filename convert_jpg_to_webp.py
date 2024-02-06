from PIL import Image
import os

# Define the input and output directories
input_directory = 'input_images/'
output_directory = 'output_images/'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define the quality level for .webp conversion (JPEG Q=75)
webp_quality = 75

# Recursively traverse the input directory and its subdirectories
for root, _, files in os.walk(input_directory):
    for filename in files:
        if filename.endswith('.jpg'):
            # Construct the input and output file paths
            input_path = os.path.join(root, filename)
            relative_path = os.path.relpath(input_path, input_directory)
            output_path = os.path.join(output_directory, relative_path)
            output_path = os.path.splitext(output_path)[0] + '.webp'

            # Create the output directory structure if it doesn't exist
            output_folder = os.path.dirname(output_path)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Open the .jpg image using Pillow
            with Image.open(input_path) as img:
                # Convert and save the image as .webp format with specified quality
                img.save(output_path, 'webp', quality=webp_quality)

            print(f'Converted {input_path} to {output_path} with quality Q={webp_quality}')

print('Conversion completed!')
