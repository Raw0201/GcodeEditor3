import os
import pyperclip  # pip install pyperclip
import webbrowser  # pip install webbrowser
import tkinter as tk
import customtkinter  # pip install customtkinter

from pathlib import Path
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class Condenser:
    def __init__(self):
        """Constructor ventana principal"""

        # Ventana principal
        self.main_window = customtkinter.CTk()
        self.main_window.minsize(500,500)
        self.main_window.geometry("300x300+50+50")
        self.main_window.after(0, lambda: self.main_window.state("zoomed"))

        title_font = customtkinter.CTkFont(family='Stencil', size=50)
        button_font = customtkinter.CTkFont(family='Times New Roman', weight="bold", size=20)
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("green")

        title_label = customtkinter.CTkLabel(self.main_window, text="PyCNC TAPE CONDENSER", font=title_font)
        title_label.pack(pady=30)

        # Marco de botones
        buttons_frame = customtkinter.CTkFrame(self.main_window)
        buttons_frame.pack()

        # Botones de acción
        btn_clear = customtkinter.CTkButton(
            buttons_frame, text="Limpiar ventanas", command=self.load_default_data, font=button_font, height=40, width=180)
        btn_clear.grid(row=0, column=0, padx=5, pady=5)

        btn_search = customtkinter.CTkButton(
            buttons_frame, text="Abrir tape", command=self.select_tape_file, font=button_font, height=40, width=180)
        btn_search.grid(row=0, column=1, padx=5, pady=5)

        btn_openweb = customtkinter.CTkButton(
            buttons_frame, text="Abrir simulador", command=self.open_web_browser, font=button_font, height=40, width=180)
        btn_openweb.grid(row=0, column=2, padx=5, pady=5)

        # Marco de ventana de datos
        main_frame = customtkinter.CTkFrame(self.main_window)
        main_frame.pack()

        # Ventana de datos - Tape completo
        complete_window_frame = customtkinter.CTkFrame(main_frame)
        complete_window_frame.grid(row=0, column=0, padx=5, pady=5)
        complete_window_button = customtkinter.CTkButton(complete_window_frame, text="Líneas completas", command=self.copy_complete, font=button_font, height=40, width=200)
        complete_window_button.pack(pady=5)

        self.complete_textbox = customtkinter.CTkTextbox(complete_window_frame, height=750, width=750)
        self.complete_textbox.pack(side=customtkinter.RIGHT)

        # Ventana de datos - Sólo líneas desbloqueadas
        unblocked_window_frame = customtkinter.CTkFrame(main_frame)
        unblocked_window_frame.grid(row=0, column=1, padx=5, pady=5)
        unblocked_window_button = customtkinter.CTkButton(unblocked_window_frame, text="Líneas desbloqueadas", command=self.copy_unblocked, font=button_font, height=40, width=200)
        unblocked_window_button.pack(pady=5)

        self.unblocked_textbox = customtkinter.CTkTextbox(unblocked_window_frame, height=750, width=750)
        self.unblocked_textbox.pack(side=customtkinter.LEFT)

        self.load_default_data()   

    def load_default_data(self):
        """Datos por defecto"""

        self.main_window.title("PyCNC TAPE CONDENSER")
        self.loops = 1
        self.loops_code = "L"
        self.tapes_code = "P"
        self.omit_lines = ["\n", "%", "", "M99"]
        self.omit_chars = ["("]
        self.omit_subrt = ["1.", "8999.cnc", "8999.CNC"]
        self.subrutine_codes = ["M98P", "/M98"]
        self.complete_textbox.delete("1.0", tk.END)
        self.unblocked_textbox.delete("1.0", tk.END)
        self.plot_lines = []
        self.file_linesL0 = []
        self.file_linesL1 = []
        self.file_linesL2 = []
        self.subrutine_paths = {}

    def open_web_browser(self):
        webbrowser.open("https://ncviewer.com/")

    def select_tape_file(self):
        """Selección de tape"""

        tape_name = fd.askopenfilename()
        if tape_name:
            self.load_default_data()
            self.main_window.title(f"PyCNC - {tape_name}")

            file_path = Path(tape_name)
            self.file_directory = file_path.parent

            file = file_path.name.split(".")
            self.file_name = file[0]
            try:
                self.file_extension = file[1]
            except:
                self.file_extension = ""
            self.condenser_L0(tape_name)

    def find_blocked_symbol(self, line):
        """Buscar línea bloqueada

        Args:
            line (str): Línea de tape

        Returns:
            char: Caracter de bloqueo de línea
        """

        return "/" if line[0] == "/" else ""

    def find_subrutine_number(self, line):
        """Buscar subrutina CNC

        Args:
            line (str): Línea de tape

        Returns:
            str: Número de subrutina con extensión
        """

        sub_index = line.find(self.tapes_code)
        return f"{line[sub_index + 1 : sub_index + 5]}.{self.file_extension}"

    def find_loops_quantity(self, line):
        """Buscar repeticiones de subrutina

        Args:
            line (str): Línea de tape

        Returns:
            int: Cantidad de repeticiones
        """

        loop_index = line.find(self.loops_code)
        loop = line[loop_index + 1 :].isdigit()
        
        if loop:
            return 1 if loop_index < 0 else int(line[loop_index + 1 :])

        return 1

    def file_not_found_error_message(self, tape_name, directory):
        """Mensaje de error por archivo no encontrado

        Args:
            tape_name (str): Número de tape
            directory (str): Directorio de ubicación del tape

        Raises:
            StopIteration: Detener iteración
        """

        answer = mb.askokcancel(
            title="Error",
            message=f"""El archivo {tape_name} no se encuentra en \n\n {directory}\n
            ¿Desea buscarlo en otro directorio?""",
        )
        return answer

    def general_error_message(self, error):
        """Mensaje genérico de error

        Args:
            error (error): Tipo de error

        Raises:
            StopIteration: Detener iteración
        """

        mb.showerror(message=f"Ocurrió un error: {error}")
        raise StopIteration

    def plot_lines_to_window(self, lines, window, block_symbol):
        """Mostrar líneas de ploteo en pantalla

        Args:
            lines (array): Líneas a plotear
            window (tk.Text): Ventana de texto
            block_symbol (str): Símbolo de bloqueo de línea
        """

        line_number = 1
        for line in lines:
            if line[0] != block_symbol:
                window.insert(tk.END, f"N{line_number} {line}")
                window.insert(tk.END, "\n")
                line_number += 1

    def copy_complete(self):
        text = self.complete_textbox.get("1.0", tk.END)
        pyperclip.copy(text)

    def copy_unblocked(self):
        text = self.unblocked_textbox.get("1.0", tk.END)
        pyperclip.copy(text)

    def condenser_L0(self, tape_L0):
        """Procesador de tape principal"""

        try:
            with open(tape_L0, "r") as file1:
                for line in file1:
                    self.file_linesL0.append(line.strip())
        except FileNotFoundError:
            self.file_not_found_error_message(self.file_name, self.file_directory)

        except Exception as e:
            self.general_error_message(e)

        for line0L0 in self.file_linesL0:
            if line0L0 in self.omit_lines or line0L0[0] in self.omit_chars:
                pass
            elif line0L0[:4] in self.subrutine_codes:
                blockL1 = "/" if line0L0[0] == "/" else ""
                tapeL1 = self.find_subrutine_number(line0L0)
                loopsL1 = self.find_loops_quantity(line0L0)

                if tapeL1 not in self.omit_subrt:
                    for _ in range(loopsL1):
                        self.condenser_L1(blockL1, tapeL1)
            else:
                loopsL1 = self.find_loops_quantity(line0L0)
                for _ in range (loopsL1):
                    self.plot_lines.append(line0L0)

        self.plot_lines_to_window(self.plot_lines, self.complete_textbox, "")
        self.plot_lines_to_window(self.plot_lines, self.unblocked_textbox, "/")

    def condenser_L1(self, blockL1, subrutineL1):
        """Procesador de subrutinas en nivel 1

        Args:
            blockL1 (str): Símbolo de bloqueo de líneas
            subrutineL1 (str): Número de subrutina
        """

        fileL1 = ""
        subLinesL1 = []
        file_linesL1 = []
        self.omit_chars.append("O")

        if subrutineL1 in self.subrutine_paths:
            subrutine_pathL1 = self.subrutine_paths[subrutineL1]
        else:
            subrutine_pathL1 = os.path.join(self.file_directory, subrutineL1)

        try:
            with open(subrutine_pathL1) as fileL1:
                for lineL1 in fileL1:
                    file_linesL1.append(lineL1.strip())
        except FileNotFoundError:
            answer = self.file_not_found_error_message(subrutineL1, self.file_directory)
            if answer == True:
                subrutine_pathL1 = fd.askopenfilename()
                self.subrutine_paths[subrutineL1] = subrutine_pathL1
                with open(subrutine_pathL1) as fileL1:
                    for lineL1 in fileL1:
                        file_linesL1.append(lineL1.strip())
            else:
                raise StopIteration
        except Exception as e:
            self.general_error_message(e)

        for line1L1 in file_linesL1:
            if line1L1 in self.omit_lines or line1L1[0] in self.omit_chars:
                pass
            elif line1L1[:4] in self.subrutine_codes:
                for subLineL1 in subLinesL1:
                    self.plot_lines.append(subLineL1)
                subLineL1 = []

                if blockL1 != "/":
                    blockL1 = "/" if line1L1[0] == "/" else ""

                tapeL2 = self.find_subrutine_number(line1L1)
                loopsL2 = self.find_loops_quantity(line1L1)
                self.condenser_L2(blockL1, tapeL2, loopsL2)
            else:
                loopsL2 = self.find_loops_quantity(line1L1)
                for _ in range (loopsL2):
                    self.plot_lines.append(f"{blockL1}{line1L1}")

    def condenser_L2(self, blockL2, subrutineL2, loopsL2):
        """Procesador de subrutinas en nivel 2

        Args:
            blockL2 (str): Símbolo de bloqueo de líneas
            subrutineL2 (str): Número de subrutina
            loopsL2 (int): Cantidad de repeticiones
        """

        fileL2 = ""
        subLinesL2 = []
        file_linesL2 = []

        if subrutineL2 in self.subrutine_paths:
            subrutine_pathL2 = self.subrutine_paths[subrutineL2]
        else:
            subrutine_pathL2 = os.path.join(self.file_directory, subrutineL2)

        try:
            with open(subrutine_pathL2) as fileL2:
                for lineL2 in fileL2:
                    file_linesL2.append(lineL2.strip())
        except FileNotFoundError:
            answer = self.file_not_found_error_message(subrutineL2, self.file_directory)
            if answer == True:
                subrutine_pathL2 = fd.askopenfilename()
                self.subrutine_paths[subrutineL2] = subrutine_pathL2
                with open(subrutine_pathL2) as fileL2:
                    for lineL2 in fileL2:
                        file_linesL2.append(lineL2.strip())
            else:
                raise StopIteration
        except Exception as e:
            self.general_error_message(e)

        for line2L2 in file_linesL2:
            if line2L2 in self.omit_lines or line2L2[0] in self.omit_chars:
                pass
            else:
                subLinesL2.append(f"{blockL2}{line2L2}")

        for _ in range(loopsL2):
            for subLineL2 in subLinesL2:
                self.plot_lines.append(subLineL2)


if __name__ == "__main__":
    app = Condenser()
    app.main_window.mainloop()
