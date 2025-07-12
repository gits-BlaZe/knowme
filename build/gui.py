from pathlib import Path
import json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

KNOWLEDGE_BASE_PATH = Path("D:/knowledge_base.json")

def load_knowledge_base(path):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_knowledge_base(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def add_person(name, info, knowledge_base):
    knowledge_base[name] = info
    save_knowledge_base(KNOWLEDGE_BASE_PATH, knowledge_base)
    messagebox.showinfo("Success", f"Information about {name} has been stored.")

def append_person(name, info, knowledge_base):
    if name in knowledge_base:
        knowledge_base[name] += " " + info
        save_knowledge_base(KNOWLEDGE_BASE_PATH, knowledge_base)
        messagebox.showinfo("Success", f"Information about {name} has been updated.")
    else:
        messagebox.showerror("Error", f"{name} does not exist in the knowledge base.")

def delete_person(name, knowledge_base):
    if name in knowledge_base:
        del knowledge_base[name]
        save_knowledge_base(KNOWLEDGE_BASE_PATH, knowledge_base)
        messagebox.showinfo("Success", f"{name} has been deleted from the database.")
    else:
        messagebox.showerror("Error", f"{name} does not exist in the database.")

def search_person(name, knowledge_base, text_widget):
    if name in knowledge_base:
        text_widget.delete(1.0, "end")  
        text_widget.insert("end", knowledge_base[name])
    else:
        messagebox.showerror("Error", f"No information found about {name}.")

knowledge_base = load_knowledge_base(KNOWLEDGE_BASE_PATH)

# GUI Setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\build\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("360x720")
window.configure(bg="#4D4D4D")
window.resizable(False, False)

canvas = Canvas(
    window,
    bg="#4D4D4D",
    height=720,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(180.0, 177.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(179.0, 514.306396484375, image=image_image_2)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(179.5, 514.5, image=entry_image_1)
entry_1 = Text(bd=0, bg="#BCBCBC", fg="#000716", highlightthickness=0,font="Courier")
entry_1.place(x=28.0, y=337.0, width=303.0, height=353.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(181.0, 87.5, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#4D4D4D", fg="#FFFFFF", highlightthickness=0,font="Palatino")
entry_2.place(x=62.5, y=64.0, width=237.0, height=45.0)

def on_append():
    name = entry_2.get().strip()
    info = entry_1.get(1.0, "end").strip()
    if name and info:
        append_person(name, info, knowledge_base)
    else:
        messagebox.showerror("Error", "Please enter a name and information.")

def on_delete():
    name = entry_2.get().strip()
    if name:
        delete_person(name, knowledge_base)
    else:
        messagebox.showerror("Error", "Please enter a name.")

def on_add():
    name = entry_2.get().strip()
    info = entry_1.get(1.0, "end").strip()
    if name and info:
        add_person(name, info, knowledge_base)
    else:
        messagebox.showerror("Error", "Please enter a name and information.")

def on_search():
    name = entry_2.get().strip()
    if name:
        search_person(name, knowledge_base, entry_1)
    else:
        messagebox.showerror("Error", "Please enter a name.")

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=on_append, relief="flat")
button_1.place(x=158.0, y=215.22988891601562, width=178.4541473388672, height=67.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=on_delete, relief="flat")
button_2.place(x=23.0, y=215.0, width=120.0, height=67.0)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=on_add, relief="flat")
button_3.place(x=216.0, y=132.0, width=120.0, height=67.0)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=on_search, relief="flat")
button_4.place(x=23.0, y=132.0, width=178.0, height=67.0)

canvas.create_text(100.0, 1.0, anchor="nw", text="Know   Me", fill="#FFFFFF", font=("Consolas", 32 * -1))

window.mainloop()