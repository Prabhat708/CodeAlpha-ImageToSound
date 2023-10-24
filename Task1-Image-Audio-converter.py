import pyttsx3
import pytesseract
from PIL import Image as PILImage
from tkinter import *
from tkinter import filedialog
import os
import time

window = Tk()
window.title('Image to Audio')
window.geometry("600x800")
window.config(background="#f0f0f0")

label_file_explorer = Label(window, text="Image to Audio Converter", font=("Arial", 16), bg="#f0f0f0", fg="black")
label_success = Label(window, text="", font=("Arial", 12), fg="green")
text_box = Text(window, height=10, width=60)
text_box.grid(column=1, row=3, pady=10, padx=10, columnspan=2)
text_box.grid_remove()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("images", "*.png *.jpg *.jpeg *.gif"), ("all files", "*.*")))

    label_file_explorer.configure(text="YOUR IMAGE IS SUCCESSFULLY UPLOADED \n CLICK SUBMIT FOR PROCESS")
    text_box.delete(1.0, END)
    label_success.configure(text="")

def convert():
    img = PILImage.open(filename)
    text = pytesseract.image_to_string(img)
    with open('img-txt.txt', 'w') as f:
        f.write(text)
    with open('img-txt.txt', 'r') as f:
        data = f.read()
        text_box.delete(1.0, END)
        text_box.insert(END, data)
    global audio_file_name
	
    timestamp = time.strftime('%Y%m%d%H%M%S')
    audio_file_name = f"output_{timestamp}.mp3"

    engine = pyttsx3.init()
    engine.save_to_file(data, audio_file_name)
    # engine.say(data)
    engine.runAndWait()
    label_success.configure(text="Conversion Successfully Completed \n Click play audio file button to play \nor display text file button to show the text")

def play_audio():
    
    os.system(f'start {audio_file_name}')

def display_text_file():
    with open('img-txt.txt', 'r') as f:
        data = f.read()
        text_box.delete(1.0, END)
        text_box.insert(END, data)
    text_box.grid()

button_explore = Button(window, text="Browse Files", font=("Arial", 12), bg="#4CAF50", fg="white", command=browseFiles)
button_Submit = Button(window, text="Submit", font=("Arial", 12), bg="#f0651a", fg="white", command=convert)
button_play = Button(window, text="Play Audio", font=("Arial", 12), bg="#008CBA", fg="white", command=play_audio)
button_display = Button(window, text="Display Text File", font=("Arial", 12), bg="#607D8B", fg="white", command=display_text_file)
button_exit = Button(window, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", command=exit)

label_file_explorer.grid(column=1, row=1, pady=20, padx=10, columnspan=2, sticky="n")
label_success.grid(column=1, row=2, pady=10, padx=10, columnspan=2, sticky="n")
button_explore.grid(column=1, row=4, padx=10, pady=10, sticky="ew")
button_Submit.grid(column=1, row=5, pady=10, padx=10, sticky="ew")
button_play.grid(column=1, row=6, pady=10, padx=10, sticky="ew")
button_display.grid(column=1, row=7, pady=10, padx=10, sticky="ew")
button_exit.grid(column=1, row=8, pady=10, padx=10, sticky="ew")

window.mainloop()
