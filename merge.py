from PIL import Image, ImageDraw, ImageFont
import textwrap

# Define column headers
column_headers = ["Prompt", "Copilot", "DALL·E", "Emu", "Imagen"]

# Define prompts
prompts = [
    "Create an image of a street sign with a specific set of directions.'",
    "Generate image of a movie screen with the phrase 'limitless possibilities'",
    "A crowded busy street with the words 'Futuristic ways pave and illuminate 2025!'",
    "Generate a menu card of a London Cafe!",
    "Generate an Image of a laptop screen with the slogan 'Forging Tomorrow's Frontiers'"
]

# Define image paths for each model (Replace with actual paths)
image_paths = [
    ["GenAI_Dataset/Copilot(Microsoft)/Street_Sign.png", "GenAI_Dataset/Dall-E3(ChatGpt)/DALL·E 2025-02-15 00.29.37 - A realistic street sign at an intersection, featuring three directional arrows with text. The top sign points forward and says 'Future Ahead'. The lef.webp", "GenAI_Dataset/Emu(MetaAI)/a_street_sign_with_a_specific_set.jpeg", "GenAI_Dataset/Imagen(Gemini)/Gemini_Generated_Image_anvcplanvcplanvc.jpg"],
    ["GenAI_Dataset/Copilot(Microsoft)/Limitless.png", "GenAI_Dataset/Dall-E3(ChatGpt)/DALL·E 2025-02-15 00.29.29 - A large movie screen in a dark cinema, displaying the phrase 'Limitless Possibilities' in bold, glowing white letters. The screen emits a soft light, .webp", "GenAI_Dataset/Emu(MetaAI)/a_movie_screen_with_the_phrase_limitless.jpeg", "GenAI_Dataset/Imagen(Gemini)/Gemini_Generated_Image_1mqqb41mqqb41mqq.jpg"],
    ["GenAI_Dataset/Copilot(Microsoft)/futuristic.png", "GenAI_Dataset/Dall-E3(ChatGpt)/DALL·E 2025-02-15 00.37.57 - A bustling, crowded city street at night, filled with neon billboards and digital screens. The billboards display the words 'Futuristic ways pave and .webp", "GenAI_Dataset/Emu(MetaAI)/a_crowded_busy_street_with_the_words.jpeg", "GenAI_Dataset/Imagen(Gemini)/Gemini_Generated_Image_18opge18opge18op.jpg"],
    ["GenAI_Dataset/Copilot(Microsoft)/Menu.png", "GenAI_Dataset/Dall-E3(ChatGpt)/DALL·E 2025-02-15 00.33.50 - A stylish London cafe menu card with a vintage yet modern aesthetic. The menu is elegantly designed with a chalkboard-style background and white handw.webp", "GenAI_Dataset/Emu(MetaAI)/a_menu_card_of_a_london_cafe.jpeg", "GenAI_Dataset/Imagen(Gemini)/Gemini_Generated_Image_xkanelxkanelxkan.jpg"],
    ["GenAI_Dataset/Copilot(Microsoft)/laptop.png", "GenAI_Dataset/Dall-E3(ChatGpt)/DALL·E 2025-02-15 10.07.59 - A modern laptop with a sleek design placed on a desk. The screen displays the slogan 'Forging Tomorrow's Frontiers' in a futuristic, bold font with a .webp", "GenAI_Dataset/Emu(MetaAI)/a_laptop_screen_with_the_slogan_forging.jpeg", "GenAI_Dataset/Imagen(Gemini)/Gemini_Generated_Image_q3gizcq3gizcq3gi.jpg"]
]

# Set image size
# image_size = (256, 256)  # Resize all images to a fixed size
image_size = (220, 220)

# Load images and resize
images = [[Image.open(img_path).resize(image_size) for img_path in row] for row in image_paths]

arial_font_path = "/Library/Fonts/Arial.ttf"
impact_font_path = "/Library/Fonts/Impact.ttf"

# Load fonts (adjust path if needed)
try:
    print("ok")
    font = ImageFont.truetype(arial_font_path, 20)  # Normal text font
    header_font = ImageFont.truetype(impact_font_path, 21)  # Bold & bigger header font
except:
    print("except")
    font = ImageFont.load_default()
    header_font = font  # Fallback if bold font is unavailable

# Define sizes for grid layout
header_height = 33  # Increased header space for bigger text
prompt_width = 175  # Space for the prompt text
grid_width = prompt_width + (image_size[0] * 4)  # 4 model columns
grid_height = header_height + (image_size[1] * 5)  # 5 rows + header

# Create a blank image with white background
final_image = Image.new("RGB", (grid_width, grid_height), "white")
draw = ImageDraw.Draw(final_image)

# Function to wrap text and center it
def draw_wrapped_text(draw, text, x, y, width, font, line_spacing=10, fill="black"):
    max_chars_per_line = width // (font.size // 2)  # Rough estimate for wrapping
    wrapped_text = textwrap.fill(text, width=max_chars_per_line)  # Wrap text

    # Split into lines and draw each one
    lines = wrapped_text.split("\n")
    total_text_height = len(lines) * (font.size + line_spacing)
    y_offset = y + (image_size[1] - total_text_height) // 2  # Center vertically

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x_position = x + (width - text_width) // 2  # Centering the text horizontally
        draw.text((x_position, y_offset), line, fill=fill, font=font)
        y_offset += font.size + line_spacing  # Move to next line

# Function to draw bold column headers
def draw_column_headers(draw, headers, x_start, y_start, column_widths, font, fill="black"):
    for i, header in enumerate(headers):
        x_position = x_start + sum(column_widths[:i]) + (column_widths[i] // 2)  # Center in column
        bbox = draw.textbbox((0, 0), header, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw.text((x_position - text_width // 2, y_start + (header_height - text_height) // 2), header, fill=fill, font=font)

# Define column widths
column_widths = [prompt_width] + [image_size[0]] * 4  # Prompt + 4 model columns

# Draw bold & large column headers
draw_column_headers(draw, column_headers, 0, 0, column_widths, header_font, fill="black")

# Paste images into the final grid and add prompts
for row_idx, (prompt, row_images) in enumerate(zip(prompts, images)):
    y_offset = header_height + row_idx * image_size[1]  # Adjusting text position

    # Wrap and center-align the prompt in its allocated width
    draw_wrapped_text(draw, prompt, 0, y_offset, prompt_width, font)

    # Paste model-generated images in the next columns
    for col_idx, img in enumerate(row_images):
        x_offset = prompt_width + col_idx * image_size[0]
        final_image.paste(img, (x_offset, y_offset))

# Save the final merged image
final_image.save("test_merged_output.png")
print("Merged image saved as merged_output_with_large_bold_headers.png")
