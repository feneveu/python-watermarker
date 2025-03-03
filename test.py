import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk


def watermark():
    """loads the image and watermarks it"""

    # need to be able to access the watermarker from the function call
    global text_entry

    # the filepath of the image is gained from the filedialog opening/user choosing
    file_path = filedialog.askopenfilename()
    # if there is no file path exit
    if not file_path:
        return

    # allows us to do futher combinations of image on top images later
    image = Image.open(file_path).convert("RGBA")

    # make the image smaller at a ratio
    max_size = (500, 500)
    image.thumbnail(max_size, Image.LANCZOS)

    # Get user input text(if it's nothing watermark = watermark)
    watermark_text = text_entry.get().strip() if text_entry else "Watermark"

    # Remove text entry after user selects an image
    text_entry.pack_forget()

    # Create watermark layer
    watermark = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    # Choose font
    font = ImageFont.truetype("arial.ttf", 20)

    # Get text size using textbbox
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Position watermark at bottom-right
    x = image.width - text_width - 10
    y = image.height - text_height - 10
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # Semi-transparent white

    # Merge watermark with image
    watermarked_image = Image.alpha_composite(image, watermark).convert("RGB")

    # Display image in Tkinter
    tk_image = ImageTk.PhotoImage(watermarked_image)
    panel.config(image=tk_image)
    panel.image = tk_image


# Create the main Tkinter window
root = tk.Tk()
root.title("Watermark App")
root.geometry("600x650")
root.configure(bg="#23486A")  # Dark background color

# Title Label
title_label = tk.Label(root, text="Image Watermarker", font=("Arial", 20, "bold"), bg="#23486A", fg="white")
title_label.pack(pady=10)

# Textbox for entering watermark text
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
    btn.config(bg="#1ABC9C", fg="white")


def on_leave(e):
    btn.config(bg="#16A085", fg="white")


# instantiates button
btn = tk.Button(root, text="Open Image", command=watermark, font=("Arial", 14, "bold"), bg="#16A085", fg="white",
                activebackground="#1ABC9C", activeforeground="white", relief="flat", padx=20, pady=10, bd=3)
btn.pack(pady=15)

# hover over button and color change effect
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Run the Tkinter event loop
root.mainloop()
