from PIL import Image
import os

# Check the current appicon colors
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
img = Image.open(appicon_path)

print(f"Analyzing appicon.png...")
print(f"Size: {img.size}, Mode: {img.mode}")

# Sample pixels to understand the color scheme
pixels = img.load()
width, height = img.size

# Sample center and edges
center_color = pixels[width//2, height//2]
corner_color = pixels[10, 10]
edge_color = pixels[width//2, 10]

print(f"\nColor samples:")
print(f"Corner (10,10): RGBA{corner_color}")
print(f"Edge (center-top): RGBA{edge_color}")
print(f"Center: RGBA{center_color}")

# Check if we need to invert
# Purple background should have low R, lower G, higher B
# White D should have high R, G, B
print("\n--- Color Analysis ---")
if corner_color[0] > 200 and corner_color[1] > 200 and corner_color[2] > 200:
    print("❌ PROBLEM: Background is WHITE (should be PURPLE)")
    print("❌ The icon colors are inverted!")
    needs_fix = True
elif corner_color[2] > corner_color[1]:
    print("✓ Background appears to be purple/blue")
    needs_fix = False
else:
    print("⚠ Unclear color scheme")
    needs_fix = True

if needs_fix:
    print("\n🔧 Need to invert the icon colors!")
else:
    print("\n✓ Icon colors look correct")

print("\nExpected:")
print("  - Background: Purple (RGB around 91, 63, 160)")
print("  - Logo (D): White (RGB 255, 255, 255)")
