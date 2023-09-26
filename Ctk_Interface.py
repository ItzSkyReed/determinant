import os
import sys

import customtkinter
from PIL import ImageTk

import determinant
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()
font=customtkinter.CTkFont(family='Comfortaa', size=13, weight='bold')
root.title("Матричный калькулятор")
window_height = 670
window_width = 501
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
frame_grid = customtkinter.CTkFrame(root, corner_radius=0)
frame_matrix = customtkinter.CTkFrame(root, corner_radius=0, fg_color='red')
frame_matrix_size = customtkinter.CTkFrame(frame_grid, corner_radius=0)
frame_buttons = customtkinter.CTkFrame(root, corner_radius=0)
frame_result = customtkinter.CTkFrame(root, corner_radius=0, fg_color='red')
previous_size_cols = 0
previous_size_rows = 0


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_file(file_path):
    file_path = resource_path(file_path)
    return file_path


def get_matrix(rows, cols):
    try:
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(cols):
                if text_var[i][j].get() != '':
                    matrix[i].append(float(text_var[i][j].get()))
                else:
                    matrix[i].append(float(0))
        return matrix
    except ValueError as ex:
        print(ex)
    except Exception as ex:
        print(ex)


def matrix_generator(rows, cols):
    global text_var, entries, previous_size_rows, previous_size_cols
    if previous_size_rows != rows or previous_size_cols != cols:
        for widget in frame_matrix.winfo_children():
            widget.destroy()
        entries = []
        text_var = []
        frame_matrix.pack(anchor='c', side='bottom',ipady=20)
        for i in range(rows):
            text_var.append([])
            entries.append([])
            for j in range(cols):
                text_var[i].append(customtkinter.StringVar())
                entries[i].append(
                    customtkinter.CTkEntry(frame_matrix, textvariable=text_var[i][j], width=75, font=font,
                                           justify=customtkinter.CENTER, corner_radius=2,
                                           placeholder_text='Введите число', fg_color='#D8D8D8', border_color="#AAAAAA",
                                           border_width=1))
                entries[i][j].grid(column=j, row=i)
        previous_size_cols = cols
        previous_size_rows = rows


def rows_slider_callback(value):
    rows_slider_num.configure(text=f'  {int(value)}  ')


def cols_slider_callback(value):
    cols_slider_num.configure(text=f'  {int(value)}  ')


def create_matrix_btn_event():
    matrix_generator(int(rows_slider.get()), int(cols_slider.get()))


def determinant_button_event():
    if previous_size_rows != 0 and previous_size_cols != 0:
        print(determinant.determinant(get_matrix(previous_size_rows, previous_size_cols)))


def inverse_button_event():
    print("button pressed")


def transposition_button_event():
    print("button pressed")


rows_slider_text = customtkinter.CTkLabel(frame_grid, text="Строки матрицы:", fg_color="transparent", width=135,
                                          anchor='w', padx=10)
rows_slider_num = customtkinter.CTkLabel(frame_grid, text="2", fg_color="transparent", width=20)
cols_slider_text = customtkinter.CTkLabel(frame_grid, text="Столбцы матрицы:", fg_color="transparent", width=135,
                                          anchor='w', padx=10)
cols_slider_num = customtkinter.CTkLabel(frame_grid, text="2", fg_color="transparent", width=20)
rows_slider = customtkinter.CTkSlider(frame_grid, number_of_steps=3, from_=1, to=4, command=rows_slider_callback,width=180)
rows_slider.set(2)
cols_slider = customtkinter.CTkSlider(frame_grid, number_of_steps=3, from_=1, to=4, command=cols_slider_callback,width=180)
cols_slider.set(2)
rows_slider_num.grid(column=3, row=1)
cols_slider_num.grid(column=3, row=2)
rows_slider_text.grid(column=1, row=1)
cols_slider_text.grid(column=1, row=2)
rows_slider.grid(column=2, row=1)
cols_slider.grid(column=2, row=2)

create_matrix_btn = customtkinter.CTkButton(frame_grid, text="Создать Матрицу", command=create_matrix_btn_event, font=font)
create_matrix_btn.grid(column=4, row=1, rowspan=2, sticky="ew",ipadx=5)

determinant_button = customtkinter.CTkButton(frame_buttons, text="Определитель", command=determinant_button_event,
                                             corner_radius=3, width=159, font=font)
inverse_button = customtkinter.CTkButton(frame_buttons, text="Обратная матрица", command=inverse_button_event,
                                         corner_radius=3, width=159, font=font)
transposition_button = customtkinter.CTkButton(frame_buttons, text="Транспонирование",
                                               command=transposition_button_event,
                                               corner_radius=3, width=159, font=font)
transposition_button.grid(column=3, row=1, padx=4)
determinant_button.grid(column=1, row=1, padx=4)
inverse_button.grid(column=2, row=1, padx=4)
frame_grid.pack(anchor='nw', fill=customtkinter.X)
frame_buttons.pack(anchor='c', fill=customtkinter.X)
frame_result.pack(side='bottom', ipady=110, fill=customtkinter.X)
root.wm_iconbitmap()
root.iconphoto(True, ImageTk.PhotoImage(file=get_file("data_files/icon.png"), master=root))
root.resizable(width=False, height=False)
root.configure(fg_color='#dbdbdb')
root.mainloop()
