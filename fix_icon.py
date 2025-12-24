from PIL import Image
import os

# Load the appicon to check its properties
appicon_path = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images\appicon.png"
img = Image.open(appicon_path)

print(f"Appicon size: {img.size}")
print(f"Appicon mode: {img.mode}")

# Get the dominant purple color from the image
pixels = img.load()
width, height = img.size

# Sample the background color (corners)
colors = []
for x, y in [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1), (width//2, 0), (0, height//2)]:
    pixel = pixels[x, y]
    if len(pixel) >= 3:
        colors.append(pixel[:3])

# Average the colors
avg_r = sum(c[0] for c in colors) // len(colors)
avg_g = sum(c[1] for c in colors) // len(colors)
avg_b = sum(c[2] for c in colors) // len(colors)

hex_color = f"#{avg_r:02X}{avg_g:02X}{avg_b:02X}"
print(f"\nDetected background color: {hex_color}")
print(f"RGB: ({avg_r}, {avg_g}, {avg_b})")

# Now create a better foreground version
# For Android adaptive icons, the safe zone should be about 66% of the canvas
# But we can make it slightly larger (75-80%) since the design is bold
output_base = r"d:\shop\E-commerce-Complete-Flutter-UI\assets\images"

target_size = 1024

# Try different safe zone sizes
for percentage in [0.80]:  # Use 80% for better visibility
    safe_zone_size = int(target_size * percentage)
    
    foreground_img = img.copy()
    foreground_img.thumbnail((safe_zone_size, safe_zone_size), Image.Resampling.LANCZOS)
    
    # Create transparent canvas
    foreground = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
    
    # Center the icon
    x = (target_size - foreground_img.size[0]) // 2
    y = (target_size - foreground_img.size[1]) // 2
    foreground.paste(foreground_img, (x, y), foreground_img)
    
    foreground.save(os.path.join(output_base, "appicon_foreground.png"))
    print(f"\n✓ Updated appicon_foreground.png (using {int(percentage*100)}% safe zone)")

print("\n✓ Done! Use this color in pubspec.yaml:")
print(f"  adaptive_icon_background: \"{hex_color}\"")
