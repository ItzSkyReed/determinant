import os
import sys
import customtkinter
from PIL import ImageTk
import re
import matrix_operations

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")
root = customtkinter.CTk()
font = customtkinter.CTkFont(family='Comfortaa', size=13, weight='bold')
root.title("Матричный калькулятор")
window_height = 400
window_width = 552
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


frame_grid = customtkinter.CTkFrame(root, corner_radius=0)
frame_matrix = customtkinter.CTkFrame(root, corner_radius=0)
frame_matrix_size = customtkinter.CTkFrame(frame_grid, corner_radius=0)
frame_buttons = customtkinter.CTkFrame(root, corner_radius=0)
frame_result = customtkinter.CTkFrame(root, corner_radius=0, height=160, fg_color="#C1C1C1")
frame_result.pack_propagate(False)
frame_matrix_ans = customtkinter.CTkFrame(frame_result, corner_radius=3, fg_color='transparent')

# В начале!
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


label = customtkinter.CTkLabel(frame_result, text='')
label.pack(anchor='nw', expand=True, fill='both')

def callback(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
root.bind('<Control-KeyRelease-a>', callback)

def matrix_check(matrix):
    pattern = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if ''.join(re.findall(pattern, str(matrix[i][j]))) != str(matrix[i][j]):
                print(matrix[i][j])
                return False
    return True

def one_line_answer(answer):
    global label
    frame_matrix_ans.destroy()
    try:
        label.destroy()
    except:
        pass
    label = customtkinter.CTkLabel(frame_result, text='')
    label.pack(anchor='nw', expand=True, fill='both')
    label.configure(frame_result, text=answer, font=('Comfortaa', 17, 'bold'), height=130, width=1000)

def matrix_answer(answer):
    global frame_matrix_ans
    matrix = answer[0]
    rows = answer[1]
    cols = answer[2]
    try:
        label.destroy()
    except:
        pass
    global entries_ans
    try:
        for widget in frame_matrix_ans.winfo_children():
            widget.destroy()
    except:
        frame_matrix_ans = customtkinter.CTkFrame(frame_result, corner_radius=3, fg_color='transparent')
    frame_matrix_ans.pack(anchor='c', expand=True)
    if len(answer) == 4:
        deter = (answer[3])
        if abs(deter) >= 999_999.999:
            deterf = "{:.3e}".format(abs(deter))
        else:
            deterf = round(abs(deter), 3)
            if (deterf % 1) == 0:
                deterf = int(deterf)
        deter_label = customtkinter.CTkLabel(frame_matrix_ans, text=f'{int(deter // abs(deter))}/{deterf} ×',
                                             font=('Comfortaa', 17, 'bold'))
        deter_label.grid(row=0, column=0, rowspan=rows+1)
    entries_ans = []
    for i in range(rows):
        entries_ans.append([])
        for j in range(cols):
            entries_ans[i].append(
                customtkinter.CTkLabel(frame_matrix_ans, text=matrix[i][j], font=font, width=97,
                                       justify=customtkinter.CENTER, corner_radius=0, fg_color='#D3D3D3'))
            entries_ans[i][j].grid(column=j + 1, row=i + 1, padx=1, pady=1)
            entries_ans[i][j].grid_propagate(0)


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
        return ['Ошибка']

def matrix_generator(rows, cols):
    global text_var, entries, previous_size_rows, previous_size_cols, frame_matrix
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
                    customtkinter.CTkEntry(frame_matrix, textvariable=text_var[i][j], width=110, font=font,
                                           justify=customtkinter.CENTER, corner_radius=3, fg_color='#D3D3D3',
                                           border_color="#AAAAAA",
                                           border_width=1))
                entries[i][j].grid(column=j, row=i)
        previous_size_cols = cols
        previous_size_rows = rows
        if rows != cols:
            inverse_button.configure(state='disabled')
            determinant_button.configure(state='disabled')
        else:
            determinant_button.configure(state='normal')
            inverse_button.configure(state='normal')


def rows_slider_callback(value):
    rows_slider_num.configure(text=f'  {int(value)}  ')


def cols_slider_callback(value):
    cols_slider_num.configure(text=f'  {int(value)}  ')


def create_matrix_btn_event():
    matrix_generator(int(rows_slider.get()), int(cols_slider.get()))


def determinant_button_event():
    if previous_size_rows != 0 and previous_size_cols != 0:
        around = ''
        deter = matrix_operations.determinant(get_matrix(previous_size_rows, previous_size_cols))
        if deter.is_integer():
            deter = int(deter)
        elif round(deter, 5) == 0 and deter != 0:
            around = 'примерно'
        one_line_answer(f'Определитель {around} равен: {round(deter, 5)}')


def inverse_button_event():
    if previous_size_rows != 0 and previous_size_cols != 0:
        if matrix_check(get_matrix(previous_size_rows, previous_size_cols)):
            answer = matrix_operations.inverse_matrix(get_matrix(previous_size_rows, previous_size_cols))
            if answer != 0:
                matrix_answer(answer)
            else:
                one_line_answer('Невозможно определить обратную матрицу.\nОпределитель равен 0')
        else:
            one_line_answer('Матрица содержит недопустимые символы')

def transposition_button_event():
    if previous_size_rows != 0 and previous_size_cols != 0:
        answer = matrix_operations.transposition(get_matrix(previous_size_rows, previous_size_cols))
        rows = len(answer)
        cols = len(answer[0])
        matrix_answer([answer,rows,cols])


rows_slider_text = customtkinter.CTkLabel(frame_grid, text="Строки матрицы:", fg_color="transparent", width=140,
                                          anchor='w', padx=10)
rows_slider_num = customtkinter.CTkLabel(frame_grid, text="2", fg_color="transparent", width=20)
cols_slider_text = customtkinter.CTkLabel(frame_grid, text="Столбцы матрицы:", fg_color="transparent", width=140,
                                          anchor='w', padx=10)
cols_slider_num = customtkinter.CTkLabel(frame_grid, text="2", fg_color="transparent", width=20)
rows_slider = customtkinter.CTkSlider(frame_grid, number_of_steps=3, from_=1, to=4, command=rows_slider_callback,
                                      width=200)
rows_slider.set(2)
cols_slider = customtkinter.CTkSlider(frame_grid, number_of_steps=3, from_=1, to=4, command=cols_slider_callback,
                                      width=200)
cols_slider.set(2)
rows_slider_num.grid(column=3, row=1)
cols_slider_num.grid(column=3, row=2)
rows_slider_text.grid(column=1, row=1)
cols_slider_text.grid(column=1, row=2)
rows_slider.grid(column=2, row=1)
cols_slider.grid(column=2, row=2)

create_matrix_btn = customtkinter.CTkButton(frame_grid, text="Создать Матрицу", command=create_matrix_btn_event,
                                            font=font,width=175)
create_matrix_btn.grid(column=4, row=1, rowspan=2, sticky="ew", ipadx=5)

determinant_button = customtkinter.CTkButton(frame_buttons, text="Определитель", command=determinant_button_event,
                                             corner_radius=3, width=176, font=font)
inverse_button = customtkinter.CTkButton(frame_buttons, text="Обратная матрица", command=inverse_button_event,
                                         corner_radius=3, width=176, font=font)
transposition_button = customtkinter.CTkButton(frame_buttons, text="Транспонирование",
                                               command=transposition_button_event,
                                               corner_radius=3, width=176, font=font)
transposition_button.grid(column=3, row=1, padx=4)
determinant_button.grid(column=1, row=1, padx=4)
inverse_button.grid(column=2, row=1, padx=4)
frame_grid.pack(anchor='nw', fill=customtkinter.X)
frame_buttons.pack(anchor='c', fill=customtkinter.X)
frame_result.pack(side='bottom', fill=customtkinter.X)
root.wm_iconbitmap()
root.iconphoto(True, ImageTk.PhotoImage(file=get_file("data_files/icon.png"), master=root))
root.resizable(width=False, height=False)
root.configure(fg_color='#dbdbdb')
root.mainloop()
