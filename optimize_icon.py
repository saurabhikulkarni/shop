from PIL import Image, ImageDraw
import os

# Load the appicon
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
output_base = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images"

img = Image.open(appicon_path)
print(f"Original icon: {img.size}, mode: {img.mode}")

# Ensure RGBA mode
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# For Android adaptive icons, we need to be more aggressive with sizing
# The safe zone for adaptive icons is actually closer to 66% to avoid clipping
# But we want the icon to be visible, so we'll use 72% as a sweet spot
target_size = 1024
safe_zone_percentage = 0.72  # 72% - good balance between safety and visibility

# Calculate dimensions
safe_zone_size = int(target_size * safe_zone_percentage)

# Resize the icon to fit within safe zone while maintaining aspect ratio
img_resized = img.copy()
img_resized.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)

# Create a transparent canvas
foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

# Center the resized icon
x = (target_size - img_resized.size[0]) // 2
y = (target_size - img_resized.size[1]) // 2

# Create a mask for smooth edges with rounded corners
mask = Image.new('L', img_resized.size, 0)
mask_draw = ImageDraw.Draw(mask)

# Draw rounded rectangle mask (slight rounding for smooth edges)
radius = int(img_resized.size[0] * 0.08)  # 8% corner radius for subtle curves
mask_draw.rounded_rectangle(
    [(0, 0), img_resized.size],
    radius=radius,
    fill=255
)

# Apply the mask to create smooth edges
img_with_rounded = Image.new('RGBA', img_resized.size, (0, 0, 0, 0))
img_with_rounded.paste(img_resized, (0, 0))
img_with_rounded.putalpha(mask)

# Paste onto the canvas
foreground.paste(img_with_rounded, (x, y), img_with_rounded)

# Save the foreground icon
output_path = os.path.join(output_base, "appicon_foreground.png")
foreground.save(output_path)
print(f"✓ Created optimized appicon_foreground.png")
print(f"  - Size: {target_size}x{target_size}")
print(f"  - Safe zone: {safe_zone_percentage*100}% ({safe_zone_size}x{safe_zone_size})")
print(f"  - Rounded corners: {radius}px radius")
print(f"  - Position: Centered at ({x}, {y})")
print("\n✓ Icon optimized for Android adaptive icons with proper curves!")
