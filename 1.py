import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

def read_data(filename):
    voltage = []
    current = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=' ') 
            for row in reader:
                if len(row) >= 2:
                    voltage.append(float(row[0]))
                    current.append(float(row[1])) 
    except Exception as e:
        print("Помилка при читанні файлу:", e)
    return voltage, current

def plot_graph(voltage, current, figure):
    figure.clear() 
    ax = figure.add_subplot(111)
    ax.plot(voltage, current, marker='o', color='b', linestyle='-')
    ax.set_xlabel("Напруга (V)", fontsize=8)
    ax.set_ylabel("Сила струму (A)", fontsize=8)
    ax.set_title("Залежність", fontsize=10)
    ax.tick_params(axis='both', which='major', labelsize=6)
    figure.tight_layout() 

def update_canvas(event):
    plot_graph(voltage, current, fig) 
    canvas.draw()

root = tk.Tk()
root.geometry("200x150")
root.configure(bg="beige")
root.title("Графік")

filename = "data.txt" 
voltage, current = read_data(filename)

fig = Figure(dpi=100)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True) 

plot_graph(voltage, current, fig)
canvas.draw()

root.bind("<Configure>", update_canvas)

root.mainloop()


