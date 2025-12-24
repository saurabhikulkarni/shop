from PIL import Image, ImageDraw
import os

# First, check if the new black & white D logo was saved
new_logo_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
output_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"

# Load the black & white logo
img = Image.open(new_logo_path).convert('RGBA')
print(f"Loaded icon: {img.size}")

# Create purple gradient background
size = 1024
gradient = Image.new('RGB', (size, size))
draw = ImageDraw.Draw(gradient)

# Purple gradient colors (from darker purple to lighter purple)
color_top = (72, 37, 118)      # Dark purple #482576
color_bottom = (107, 76, 154)  # Lighter purple #6B4C9A

# Draw gradient
for y in range(size):
    # Calculate color for this line
    r = int(color_top[0] + (color_bottom[0] - color_top[0]) * y / size)
    g = int(color_top[1] + (color_bottom[1] - color_top[1]) * y / size)
    b = int(color_top[2] + (color_bottom[2] - color_top[2]) * y / size)
    draw.line([(0, y), (size, y)], fill=(r, g, b))

# Convert to RGBA
gradient = gradient.convert('RGBA')

# Now extract the white "D" from the logo
# The logo is black background with white D, so we need to extract the white parts
pixels = img.load()
logo_mask = Image.new('L', img.size, 0)
mask_pixels = logo_mask.load()

# Create mask from white parts
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixel = pixels[x, y]
        # If pixel is white-ish, add it to mask
        if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
            mask_pixels[x, y] = 255

# Resize logo to fit nicely (about 75% of canvas)
logo_white = Image.new('RGBA', img.size, (255, 255, 255, 0))
logo_white.putalpha(logo_mask)

# Resize if needed
if img.size[0] != size:
    logo_white = logo_white.resize((size, size), Image.Resampling.LANCZOS)

# Composite the white logo over the purple gradient
final = gradient.copy()
final.paste(logo_white, (0, 0), logo_white)

# Convert to RGB (remove alpha) for iOS compatibility
final_rgb = Image.new('RGB', (size, size), (255, 255, 255))
final_rgb.paste(final, (0, 0))

# Save
final_rgb.save(output_path)
print(f"✓ Created appicon.png with purple gradient background and white D logo")
print(f"✓ Size: {size}x{size}")
print(f"✓ No transparency - compatible with iOS and Android")
