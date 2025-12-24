from PIL import Image
import os

# You need to manually save the attached image as "new_appicon.png" in d:\shop\
# This script will process it

input_path = r"d:\shop\new_appicon.png"
output_base = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images"

if not os.path.exists(input_path):
    print("ERROR: Please save the attached purple 'D' logo image as: d:\\shop\\new_appicon.png")
    print("Then run this script again.")
    exit(1)

# Load the new icon
img = Image.open(input_path)
print(f"Loaded image size: {img.size}")

# Ensure it's RGBA
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Create the main app icon (1024x1024)
main_icon = img.resize((1024, 1024), Image.Resampling.LANCZOS)
main_icon.save(os.path.join(output_base, "appicon.png"))
print(f"Created: appicon.png (1024x1024)")

# Create foreground version with padding for adaptive icons
# For adaptive icons, use 66% safe zone
target_size = 1024
safe_zone_size = int(target_size * 0.66)

# Resize to fit safe zone
foreground_img = img.copy()
foreground_img.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)

# Create transparent canvas
foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

# Center the icon
x = (target_size - foreground_img.size[0]) // 2
y = (target_size - foreground_img.size[1]) // 2
foreground.paste(foreground_img, (x, y), foreground_img)

foreground.save(os.path.join(output_base, "appicon_foreground.png"))
print(f"Created: appicon_foreground.png (1024x1024 with padding)")

print("\nSuccess! App icons created.")
print("Now run: flutter pub run flutter_launcher_icons")
