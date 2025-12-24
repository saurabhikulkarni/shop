from PIL import Image
import os

# Path to the new icon in the images folder
input_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\new_appicon.png"
output_base = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images"

# Load the new icon
img = Image.open(input_path)
print(f"Loaded image size: {img.size}")

# Ensure it's RGBA
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Create the main app icon (1024x1024)
main_icon = img.resize((1024, 1024), Image.Resampling.LANCZOS)
main_icon.save(os.path.join(output_base, "appicon.png"))
print(f"✓ Created: appicon.png (1024x1024)")

# Create foreground version with padding for adaptive icons
# For adaptive icons, use 70% safe zone for better visibility
target_size = 1024
safe_zone_size = int(target_size * 0.70)

foreground_img = img.copy()
foreground_img.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)

# Create transparent canvas
foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

# Center the icon
x = (target_size - foreground_img.size[0]) // 2
y = (target_size - foreground_img.size[1]) // 2
foreground.paste(foreground_img, (x, y), foreground_img)

foreground.save(os.path.join(output_base, "appicon_foreground.png"))
print(f"✓ Created: appicon_foreground.png (1024x1024 with padding)")

print("\n✓ Success! App icons created.")
print("Deleting temporary new_appicon.png...")
os.remove(input_path)
print("✓ Done!")
