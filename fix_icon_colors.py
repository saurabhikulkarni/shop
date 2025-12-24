from PIL import Image, ImageDraw, ImageChops
import os

# Load the current icon
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
output_base = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images"

img = Image.open(appicon_path).convert('RGBA')
print(f"Original icon: {img.size}")

# Extract the white "D" logo by inverting colors
# The current icon has purple content on transparent background
# We need to extract just the white parts (which appear as the "D" shape)

# Method: Invert the icon to get white "D" on colored background
# Then extract the white parts as our foreground

# Create inverted version
inverted = ImageChops.invert(img.convert('RGB'))
inverted = inverted.convert('RGBA')

# Now we need to extract the white "D" shape
# The "D" is the negative space in the purple area
pixels = img.load()
new_img = Image.new('RGBA', img.size, (0, 0, 0, 0))
new_pixels = new_img.load()
width, height = img.size

# Extract white "D" by finding areas that are NOT purple
for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        # If pixel has low opacity OR is not purple-ish, it's part of the "D"
        if a < 128 or (r > 200 and g > 200 and b > 200):
            # This is the "D" shape - make it white
            new_pixels[x, y] = (255, 255, 255, 255)
        elif a > 0:
            # This is purple content - check if it's actually the inverse
            # Purple areas in the original might be the actual logo
            if r < 150 and b > 50:  # Purple-ish
                # Keep as transparent (background will show through)
                new_pixels[x, y] = (0, 0, 0, 0)
            else:
                # Make it white (it's the logo)
                new_pixels[x, y] = (255, 255, 255, 255)

# Now create the properly sized foreground icon
target_size = 1024
safe_zone_percentage = 0.72

safe_zone_size = int(target_size * safe_zone_percentage)
foreground_img = new_img.copy()
foreground_img.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)

# Create transparent canvas
foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

# Center the icon
x = (target_size - foreground_img.size[0]) // 2
y = (target_size - foreground_img.size[1]) // 2

# Create rounded corners mask
mask = Image.new('L', foreground_img.size, 0)
mask_draw = ImageDraw.Draw(mask)
radius = int(foreground_img.size[0] * 0.08)
mask_draw.rounded_rectangle([(0, 0), foreground_img.size], radius=radius, fill=255)

# Apply mask
foreground_img.putalpha(mask)

# Paste onto canvas
foreground.paste(foreground_img, (x, y), foreground_img)

# Save
output_path = os.path.join(output_base, "appicon_foreground.png")
foreground.save(output_path)
print(f"✓ Created corrected foreground icon (white D on transparent)")

# Also let's verify what color the background should be
print(f"\n✓ Make sure pubspec.yaml has:")
print(f"  adaptive_icon_background: \"#5B3FA0\"  # Purple background")
