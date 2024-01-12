import qrcode
from tkinter import *
from PIL import Image

def generate_qr_code():
                                                       # Get values from entry widgets
    link = qr_link_value.get()
    outline_color = out_line_colour_value.get()
    background_color = bk_colour_value.get()

                                                         # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color=background_color, back_color=outline_color)

    # Save the image
    img.save("generated_qr_code.png")

    # Optionally, you can display the generated image in a new window
    img.show()

# GUI making
root = Tk()
root.geometry("400x200")
root.title("QR ABHISHEK CODE TECH")

Label(root, text="QR GENERATOR", fg="blue", font="comicsansms 19 bold",pady=15).grid(row=0, column=1)

Label(root, text="ENTER URL", font="comicsansms  7 bold",pady=7).grid(row=1, column=0)
Label(root, text="OUTLINE COLOR", font="comicsansms  7 bold",pady=7).grid(row=2, column=0)
Label(root, text="BACKGROUND COLOR", font="comicsansms  7 bold",pady=7).grid(row=3, column=0)

qr_link_value = StringVar()
out_line_colour_value = StringVar()
bk_colour_value = StringVar()

qr_link_entry = Entry(root, textvariable=qr_link_value)
out_line_colour_entry = Entry(root, textvariable=out_line_colour_value)
bk_colour_entry = Entry(root, textvariable=bk_colour_value)

qr_link_entry.grid(row=1, column=1)
out_line_colour_entry.grid(row=2, column=1)
bk_colour_entry.grid(row=3, column=1)

generate_button = Button(root, text="Generate QR Code",bg="yellow",fg="red",font="comicsansms  7 bold",command=generate_qr_code)
generate_button.grid(row=4,column=1,pady=10)

root.mainloop()
