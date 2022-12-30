import os
import tkinter as tk
import webp
import tkinter.filedialog as filedialog
from PIL import Image

# Define the input_file variable as a global variable
input_file = ""

def convert_webp_to_png(input_file, output_file):
    # Open the WebP image
    image = Image.open(input_file)

    # Save the image as a PNG
    image.save(output_file, "PNG")

# Create the main window
window = tk.Tk()
window.title("Webp to PNG Converter")

# Create a label and file selector button
label = tk.Label(text="Please select a .webp file:")
label.pack()

def select_file():
    global input_file
    input_file = tk.filedialog.askopenfilename(filetypes=[("WebP files", "*.webp")])

file_button = tk.Button(text="Select File", command=select_file)
file_button.pack()

# Create a convert button
def convert():
    # Set the output file path to the user's downloads folder
    output_folder = os.path.expanduser("~/Downloads")
    output_file = os.path.join(output_folder, os.path.basename(input_file).replace(".webp", ".png"))

    # Convert the .webp file to a .png file
    convert_webp_to_png(input_file, output_file)

    # Display a message indicating that the conversion is complete
    tk.messagebox.showinfo("Conversion Complete", f"Successfully converted {input_file} to {output_file}")

convert_button = tk.Button(text="Convert", command=convert)
convert_button.pack()

# Run the main loop
window.mainloop()
