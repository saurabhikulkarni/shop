from PIL import Image
import os

# Check appicon.png
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
img = Image.open(appicon_path)

print("=== Current appicon.png Analysis ===")
print(f"Size: {img.size}")
print(f"Mode: {img.mode}")

# Check if it has transparency
has_transparency = img.mode == 'RGBA' and any(pixel[3] < 255 for pixel in img.getdata())
print(f"Has transparency: {has_transparency}")

# Sample some pixels to understand the design
pixels = img.load()
width, height = img.size

# Check corners and center
corner = pixels[10, 10]
center = pixels[width//2, height//2]
print(f"\nCorner pixel RGBA: {corner}")
print(f"Center pixel RGBA: {center}")

# Count transparent vs opaque pixels
transparent_count = 0
opaque_count = 0
for x in range(0, width, 10):
    for y in range(0, height, 10):
        if img.mode == 'RGBA':
            if pixels[x, y][3] < 128:
                transparent_count += 1
            else:
                opaque_count += 1

print(f"\nPixel distribution (sampled):")
print(f"Transparent pixels: {transparent_count}")
print(f"Opaque pixels: {opaque_count}")

print("\n=== Compatibility Analysis ===")
if has_transparency:
    print("⚠ WARNING: Image has transparency")
    print("  - iOS: May show white/black background where transparent")
    print("  - Android: May not display correctly on all devices")
else:
    print("✓ Image has solid background")

if img.size[0] == img.size[1] and img.size[0] >= 1024:
    print("✓ Size is square and adequate (1024x1024+)")
else:
    print("⚠ Size may not be optimal")

print("\n=== Recommendation ===")
print("For BEST results on both platforms:")
print("1. Image should have a SOLID background (no transparency)")
print("2. Size should be 1024x1024")
print("3. Logo should have padding from edges (safe zone)")
print("\nCurrent image may need adjustment for optimal display.")
