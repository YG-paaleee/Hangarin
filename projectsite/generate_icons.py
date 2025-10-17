from PIL import Image, ImageDraw, ImageFont
import os

# Icon sizes
sizes = [72, 96, 128, 144, 152, 192, 384, 512]

# Create icons directory if it doesn't exist
icons_dir = 'static/img/icons'
os.makedirs(icons_dir, exist_ok=True)

# Define colors
green_dark = (45, 106, 79)  # #2d6a4f
green_light = (64, 145, 108)  # #40916c

for size in sizes:
    # Create new image with green gradient background
    img = Image.new('RGB', (size, size), green_dark)
    draw = ImageDraw.Draw(img)
    
    # Create gradient effect
    for y in range(size):
        ratio = y / size
        r = int(green_dark[0] + (green_light[0] - green_dark[0]) * ratio)
        g = int(green_dark[1] + (green_light[1] - green_dark[1]) * ratio)
        b = int(green_dark[2] + (green_light[2] - green_dark[2]) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    
    # Draw white "H" letter
    try:
        # Try to use a system font
        font_size = int(size * 0.6)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("Arial.ttf", font_size)
            except:
                try:
                    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
                except:
                    # Fallback to default font
                    font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # Get text size and center it
    text = "H"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) / 2
    y = (size - text_height) / 2 - bbox[1]
    
    # Draw the "H" in white
    draw.text((x, y), text, fill='white', font=font)
    
    # Save the icon
    filename = f'{icons_dir}/icon-{size}x{size}.png'
    img.save(filename)
    print(f'Created {filename}')

print('\nAll icons created successfully!')
print('Icons are in the static/img/icons/ folder')
