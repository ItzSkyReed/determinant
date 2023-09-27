import os
import sys

import customtkinter
from PIL import ImageTk

import matrix_operations

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()
font = customtkinter.CTkFont(family='Comfortaa', size=13, weight='bold')
root.title("Матричный калькулятор")
window_height = 370
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
frame_result = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent", height=1)
frame_matrix_ans = customtkinter.CTkFrame(frame_result, corner_radius=0, fg_color='yellow',width=20,height=50)
previous_size_cols = 0
previous_size_rows = 0
previous_size_rows_ans = 0
previous_size_cols_ans = 0


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_file(file_path):
    file_path = resource_path(file_path)
    return file_path


label = customtkinter.CTkLabel(frame_result, text='', height=130)
label.pack(anchor='nw', expand=True)


def one_line_answer(answer):
    answer_status = answer[0]
    if answer_status:
        answer_return = f'Ответ: {answer[1]}'
    else:
        answer_return = f'Ошибка! {answer[1]}'
    label.configure(frame_result, text=answer_return, fg_color="transparent", font=('Comfortaa', 17, 'bold'),
                    height=130, anchor='nw')
    label.pack(anchor='nw')


def matrix_answer(answer):
    matrix = answer[0]
    rows = answer[1]
    cols = answer[2]
    print(rows, cols)
    global entries_ans, previous_size_rows_ans, previous_size_cols_ans
    if previous_size_rows_ans != rows or previous_size_cols_ans != cols:
        for widget in frame_matrix_ans.winfo_children():
            widget.destroy()
        entries_ans = []
        frame_matrix_ans.place(relx=.5, rely=.5, anchor="c")
        for i in range(rows):
            entries_ans.append([])
            for j in range(cols):
                entries_ans[i].append(
                    customtkinter.CTkLabel(frame_matrix_ans, text=matrix[i][j], width=75, font=font,
                                           justify=customtkinter.CENTER, corner_radius=0, fg_color='#D3D3D3'))
                entries_ans[i][j].grid(column=j, row=i)
        previous_size_rows_ans = cols
        previous_size_cols_ans = rows


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
    except:
        pass


def matrix_generator(rows, cols):
    global text_var, entries, previous_size_rows, previous_size_cols
    if previous_size_rows != rows or previous_size_cols != cols:
        for widget in frame_matrix.winfo_children():
            widget.destroy()
        entries = []
        text_var = []
        frame_matrix.pack(anchor='c', side='top', pady=20)
        for i in range(rows):
            text_var.append([])
            entries.append([])
            for j in range(cols):
                text_var[i].append(customtkinter.StringVar())
                entries[i].append(
                    customtkinter.CTkEntry(frame_matrix, textvariable=text_var[i][j], width=75, font=font,
                                           justify=customtkinter.CENTER, corner_radius=3,
                                           placeholder_text='Введите число', fg_color='#D3D3D3', border_color="#AAAAAA",
                                           border_width=1))
                entries[i][j].grid(column=j, row=i)
        previous_size_cols = cols
        previous_size_rows = rows
        if rows != cols:
            determinant_button.configure(state='disabled')
        else:
            determinant_button.configure(state='normal')


def rows_slider_callback(value):
    rows_slider_num.configure(text=f'  {int(value)}  ')


def cols_slider_callback(value):
    cols_slider_num.configure(text=f'  {int(value)}  ')


def create_matrix_btn_event():
    matrix_generator(int(rows_slider.get()), int(cols_slider.get()))


def determinant_button_event():
    if previous_size_rows != 0 and previous_size_cols != 0:
        one_line_answer(matrix_operations.determinant(get_matrix(previous_size_rows, previous_size_cols)))


def inverse_button_event():
    if previous_size_rows != 0 and previous_size_cols != 0:
        matrix_answer(matrix_operations.inverse_matrix(get_matrix(previous_size_rows, previous_size_cols)))


def transposition_button_event():
    print("button pressed")


rows_slider_text = customtkinter.CTkLabel(frame_grid, text="Строки матрицы:", fg_color="transparent", width=135,
                                          anchor='w', padx=10)
rows_slider_num = customtkinter.CTkLabel(frame_grid, text="2", fg_color="transparent", width=20)
cols_slider_text = customtkinter.CTkLabel(frame_grid, text="Столбцы матрицы:", fg_color="transparent", width=135,
                                          anchor='w', padx=10)
cols_slider_num = customtkinter.CTkLabel(frame_grid, text="2", fg_color="transparent", width=20)
rows_slider = customtkinter.CTkSlider(frame_grid, number_of_steps=3, from_=1, to=4, command=rows_slider_callback,
                                      width=180)
rows_slider.set(2)
cols_slider = customtkinter.CTkSlider(frame_grid, number_of_steps=3, from_=1, to=4, command=cols_slider_callback,
                                      width=180)
cols_slider.set(2)
rows_slider_num.grid(column=3, row=1)
cols_slider_num.grid(column=3, row=2)
rows_slider_text.grid(column=1, row=1)
cols_slider_text.grid(column=1, row=2)
rows_slider.grid(column=2, row=1)
cols_slider.grid(column=2, row=2)

create_matrix_btn = customtkinter.CTkButton(frame_grid, text="Создать Матрицу", command=create_matrix_btn_event,
                                            font=font)
create_matrix_btn.grid(column=4, row=1, rowspan=2, sticky="ew", ipadx=5)

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
frame_result.pack(anchor='nw', side='bottom', fill=customtkinter.X)
root.wm_iconbitmap()
root.iconphoto(True, ImageTk.PhotoImage(file=get_file("data_files/icon.png"), master=root))
root.resizable(width=False, height=False)
root.configure(fg_color='#dbdbdb')
root.mainloop()
