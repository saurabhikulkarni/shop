from PIL import Image
import os

# Load and analyze the icon
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
img = Image.open(appicon_path)

print(f"Analyzing icon: {img.size}, mode: {img.mode}")

# Convert to RGB to get actual colors (removing transparency)
rgb_img = img.convert('RGB')
pixels = rgb_img.load()
width, height = img.size

# Find the purple background color by sampling non-white areas
purple_samples = []
for x in range(0, width, 10):
    for y in range(0, height, 10):
        r, g, b = pixels[x, y]
        # Skip white areas (the "D" logo) - looking for the purple background
        if not (r > 200 and g > 200 and b > 200):
            if r < g:  # Purple has more blue/red than green
                purple_samples.append((r, g, b))

if purple_samples:
    # Get the most common purple shade
    avg_r = sum(c[0] for c in purple_samples) // len(purple_samples)
    avg_g = sum(c[1] for c in purple_samples) // len(purple_samples)
    avg_b = sum(c[2] for c in purple_samples) // len(purple_samples)
    
    hex_color = f"#{avg_r:02X}{avg_g:02X}{avg_b:02X}"
    print(f"Detected purple background: {hex_color}")
    print(f"RGB: ({avg_r}, {avg_g}, {avg_b})")
else:
    # Default to the purple from the image
    hex_color = "#5B3FA0"  # The purple from your logo
    print(f"Using default purple: {hex_color}")

# Create optimized foreground icon (80% for better visibility on adaptive icons)
output_base = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images"
target_size = 1024
safe_zone_size = int(target_size * 0.80)

foreground_img = img.copy()
foreground_img.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)

# Create transparent canvas
foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))

# Center the icon
x = (target_size - foreground_img.size[0]) // 2
y = (target_size - foreground_img.size[1]) // 2
foreground.paste(foreground_img, (x, y), foreground_img)

foreground.save(os.path.join(output_base, "appicon_foreground.png"))
print(f"✓ Created appicon_foreground.png (80% safe zone)")

print(f"\n✓ Update pubspec.yaml with:")
print(f"  adaptive_icon_background: \"{hex_color}\"")
