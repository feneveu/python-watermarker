import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Function to add watermark and display the image
def add_watermark():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    image = Image.open(file_path).convert("RGBA")

    # Resize image proportionally
    max_size = (500, 500)
    image.thumbnail(max_size, Image.LANCZOS)

    watermark_text = text_entry.get().strip()
    if not watermark_text:
        watermark_text = 'Watermark'

    # Create watermark layer
    watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    # Choose font
    font = ImageFont.truetype("arial.ttf", 20)

    # Watermark text
    bbox = draw.textbbox((0, 0),watermark_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Position watermark at bottom-right
    x = image.width - text_width - 10
    y = image.height - text_height - 10
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Merge watermark with image
    watermarked_image = Image.alpha_composite(image, watermark).convert("RGB")

    # Display image in Tkinter
    tk_image = ImageTk.PhotoImage(watermarked_image)
    panel.config(image=tk_image)
    panel.image = tk_image

# Create the main Tkinter window
root = tk.Tk()
root.title("Watermark App")
root.geometry("600x600")
root.configure(bg="#23486A")  # Dark background color

# Title Label
title_label = tk.Label(root, text="Watermarker", font=("Arial", 20, "bold"), bg="#23486A", fg="white")
title_label.pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14), width=30, justify="center", bd=3)
text_entry.insert(0, "Enter watermark text")  # Default text
text_entry.pack(pady=5)

# Create a frame for the image display
frame = tk.Frame(root, width=520, height=520, bg="white", relief="ridge", bd=3)
frame.pack(pady=10)

# Label to show the image
panel = tk.Label(frame, bg="white")
panel.pack(expand=True)

# Custom Styled Button
def on_enter(e):
    btn.config(bg="#3B6790", fg="white")

def on_leave(e):
    btn.config(bg="#4C7B8B", fg="white")

btn = tk.Button(root, text="Open Image", command=add_watermark, font=("Arial", 14, "bold"), bg="#4C7B8B", fg="white",
                activebackground="#1ABC9C", activeforeground="white", relief="flat", padx=20, pady=10, bd=3)
btn.pack(pady=15)

btn.bind("<Enter>", on_enter)  # Button hover effect
btn.bind("<Leave>", on_leave)

# Run the Tkinter event loop
root.mainloop()
