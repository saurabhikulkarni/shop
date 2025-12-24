from PIL import Image
import os

# Paths
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
output_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon_foreground.png"

# Load the original appicon
img = Image.open(appicon_path)
print(f"Original appicon.png size: {img.size}")

# For Android adaptive icons, the foreground should be scaled down
# The safe zone is approximately 66% of the total icon size
# We'll create a 1024x1024 canvas (standard icon size) and place the icon centered with padding

# Create target size (1024x1024 is standard for app icons)
target_size = 1024

# Calculate the safe zone (66% of target size for proper display)
safe_zone_size = int(target_size * 0.66)

# Resize the appicon to fit within the safe zone
img.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)

# Create a transparent canvas
foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

# Calculate position to center the resized icon
x = (target_size - img.size[0]) // 2
y = (target_size - img.size[1]) // 2

# Paste the resized icon onto the canvas
foreground.paste(img, (x, y), img if img.mode == 'RGBA' else None)

# Save the foreground icon
foreground.save(output_path)
print(f"Created foreground icon: {output_path}")
print(f"Foreground icon size: {foreground.size}")
print(f"Icon is centered with proper padding for adaptive icons")
