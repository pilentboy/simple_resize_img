from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from resize_img import ResizeImage

root = Tk()
root.title("Resize Image Tool")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#208090") 

current_img = None
current_img_path = None

resized_width = StringVar(root, "500")
resized_height = StringVar(root, "500")
current_path = StringVar(root,"")

image_instance=ResizeImage("./assets/default.jpg")
# ------------------ Top: Image Preview ------------------ #
preview_frame = Frame(root)
preview_frame.pack(pady=10)




top_image = Button(preview_frame, text="No Image", width=200,cursor="hand2", height=200, bg="#ddd", relief="sunken",command=lambda : image_instance.display_image(resized_width.get(),resized_height.get()))
top_image.pack()

def set_top_image(path):
    global current_img, current_img_path
    current_img_path = path
    pil_img = Image.open(path)
    resized = pil_img.resize((200, 200), Image.LANCZOS)
    current_img = ImageTk.PhotoImage(resized)
    top_image.config(image=current_img, text="")
    current_path.set(path.split("/")[-1])

set_top_image("./assets/default.jpg")

# ------------------ Middle: Controls ------------------ #
controls_frame = Frame(root)
controls_frame.pack(pady=20)

# Open Button
def open_file_dialog():
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select an image file",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if filepath:
        set_top_image(filepath)
        show_resize_controls()
        image_instance.src=filepath
        print("Selected file:", filepath)

browser_btn = Button(controls_frame, text="Browse Image", width=20, bg='gray', fg='white', font=('Arial', 10), command=open_file_dialog)
browser_btn.grid(row=0, column=0, columnspan=2,pady=4)

# Width & Height Inputs
width_label = Label(controls_frame, text="New Width:")
width_input = Entry(controls_frame, textvariable=resized_width, width=10)

height_label = Label(controls_frame, text="New Height:")
height_input = Entry(controls_frame, textvariable=resized_height, width=10)

width_label.grid(row=1, column=0, pady=5, sticky='e')
width_input.grid(row=1, column=1, pady=5, sticky='w')

height_label.grid(row=2, column=0, pady=5, sticky='e')
height_input.grid(row=2, column=1, pady=5, sticky='w')

# Save Button
def save_resized_image():
    try:
        width = int(resized_width.get())
        height = int(resized_height.get())
        image_instance.src=current_img_path
        image_instance.resize_image(width,height)
        print(f"Image saved at {width}x{height}")
    except Exception as e:
        print("Error resizing:", e)

save_btn = Button(controls_frame, text="Save Resized Image", width=20, bg='green', fg='white', font=('Arial', 10), command=save_resized_image)
save_btn.grid(row=3, column=0, columnspan=2, pady=15)

# ------------------ Optional: Hide inputs initially ------------------ #
def show_resize_controls():
    width_label.grid()
    width_input.grid()
    height_label.grid()
    height_input.grid()
    save_btn.grid()

# Start with controls hidden
width_label.grid_remove()
width_input.grid_remove()
height_label.grid_remove()
height_input.grid_remove()
save_btn.grid_remove()

root.mainloop()
