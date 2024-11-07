import tkinter as tk
import string

def process_text():
    input_text = entry.get() 
    processed_text = ''.join(char for char in input_text if char not in string.punctuation)
    
    with open("string.txt", "w") as file:
        file.write(processed_text)
   
    result_label.config(text="Текст збережено у файл string.txt")

root = tk.Tk()
root.title("Видалення розділових знаків")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Введіть текст:")
label.grid(row=0, column=0, sticky="w")

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Обробити", command=process_text)
button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
