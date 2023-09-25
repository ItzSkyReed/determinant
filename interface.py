import tkinter
import tkinter as tk
from tkinter import ttk
import determinant

root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Ебланки лол")
text_var = []
entries = []

window_height = 470
window_width = 320
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

frame_grid = tkinter.Frame(root)
frame_matrix = tkinter.Frame(root)
frame_matrix_size = tkinter.Frame(frame_grid)
frame_buttons = tkinter.Frame(frame_grid)
label1 = ttk.Label(root)
def answer_tracker(text):
        label1.config(text=text)
        label1.pack(anchor='sw')
def get_matrix(matrix_size):
    try:
        matrix = []
        for i in range(matrix_size):
            matrix.append([])
            for j in range(matrix_size):
                if text_var[i][j].get() != '':
                    matrix[i].append(float(text_var[i][j].get()))
                else:
                    matrix[i].append(float(0))
        return matrix
    except ValueError as ex:
        print()
    except Exception as ex:
        print(ex)


def matrix_generator(matrix_size):
    global text_var, entries
    if frame_matrix:
        for widget in frame_matrix.winfo_children():
            widget.destroy()
        entries = []
        text_var = []
    frame_matrix.pack(anchor='center', pady=50)
    for i in range(matrix_size):
        text_var.append([])
        entries.append([])
        for j in range(matrix_size):
            text_var[i].append(tkinter.StringVar())
            entries[i].append(ttk.Entry(frame_matrix, textvariable=text_var[i][j], width=10))
            entries[i][j].grid(column=j, row=i)


matrix_size = tk.IntVar()
matrix_size.set(0)
size_radiobutton_2x2 = ttk.Radiobutton(frame_grid, text="2x2", variable=matrix_size, value=2,
                                       command=lambda: matrix_generator(matrix_size.get()))
size_radiobutton_2x2.grid(column=1, row=1)
size_radiobutton_3x3 = ttk.Radiobutton(frame_grid, text="3x3", variable=matrix_size, value=3,
                                       command=lambda: matrix_generator(matrix_size.get()))
size_radiobutton_3x3.grid(column=1, row=2)
size_radiobutton_4x4 = ttk.Radiobutton(frame_grid, text="4x4", variable=matrix_size, value=4,
                                       command=lambda: matrix_generator(matrix_size.get()))
size_radiobutton_4x4.grid(column=1, row=3)
print_matrix_button = ttk.Button(frame_grid, text="Вывести матрицу",
                                 command=lambda: answer_tracker(determinant.determinant_order_4(get_matrix(matrix_size.get()))), width=20)
print_matrix_button.grid(column=2, row=1)
print_matrix_button1 = ttk.Button(frame_grid, text="Вывести матрицу",
                                  command=lambda: get_matrix(matrix_size.get()), width=20)
print_matrix_button1.grid(column=2, row=2)
print_matrix_button2 = ttk.Button(frame_grid, text="Вывести матрицу",
                                  command= lambda: get_matrix(matrix_size.get()), width=20)
print_matrix_button2.grid(column=2, row=3, padx=10)
frame_grid.pack(anchor='nw')
root.mainloop()
