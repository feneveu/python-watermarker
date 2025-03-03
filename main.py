import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        width, height = image.size
        image = image.resize((width//4,height//4))  # Resize image
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        draw(file_path)


def draw(file_path):
    # Load the image
    image = Image.open(file_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Choose a font and size
    font_path = "arial.ttf"  # Replace with the path to your font file, or None for default
    font_size = 30
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        font = ImageFont.load_default()

    # Text properties
    text = "Hello, Pillow!"
    text_color = (255, 255, 255)  # White
    text_position = (50, 50)  # Coordinates (x, y)

    # Add the text to the image
    draw.text(text_position, text, fill=text_color, font=font)

    # Save the modified image (optional)
    image.save("output_image.jpg")


    # Convert the PIL image to Tkinter PhotoImage
    tk_image = tk.PhotoImage(image)

    # Create a Canvas widget to display the image
    canvas = tk.Canvas(root, width=image.width, height=image.height)
    canvas.pack()

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor="nw", image=tk_image)



root = tk.Tk()
root.title("Image Uploader")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

image_label = tk.Label(root)
image_label.pack()

root.mainloop()