import curses

def main(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.addstr("Консольный редактор LUMA", curses.A_BOLD)
    while True:
        stdscr.clear()
        stdscr.addstr("Консольный редактор LUMA", curses.A_BOLD)
        stdscr.addstr("\nНажмите 'F1' для справки\n")
        stdscr.refresh()
        curses.curs_set(1)

        input_text = ""
        while True:
            key = stdscr.getch()  # Считываем нажатую клавишу

            if key == 17:
                return  # Выход из приложения, ctrl+q
            elif key == curses.KEY_F1:
                display_help(stdscr)
                break  # Возврат к запросу ввода после справки ctrl+h
            elif key == 10:  # Enter
                break
            elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:
                if input_text:
                    input_text = input_text[:-1]
                    y, x = stdscr.getyx()
                    stdscr.move(y, x - 1)
                    stdscr.delch()
            else:
                try:
                    input_text += chr(key)
                    stdscr.addch(key)
                except ValueError:
                    pass

        if key == (ord('h')):
            continue  # Повтор запроса ввода после справки


        # Парсинг ввода пользователя
        try:
            word, filename = input_text.split(maxsplit=1)
            stdscr.clear()
            display_text(stdscr, filename)
            stdscr.refresh()
        except ValueError:
            stdscr.clear()
            stdscr.addstr("Неверный формат ввода. Используйте формат '<luma> <название файла>'.\n")

        stdscr.addstr("\nНажмите любую клавишу для продолжения...")
        stdscr.refresh()
        stdscr.getch()  # Ожидание нажатия клавиши перед повтором запроса ввода


def display_text(stdscr, str_name_file):
    content = ''
    try:
        with open(str_name_file, "r", encoding="utf-8") as file:
            content = file.read()
            stdscr.addstr(content)

    except FileNotFoundError:
        stdscr.addstr("Файл не найден. Создать новый? yes/no")





def display_help(stdscr):
    help_message = "Инструкция:\n" \
                   "<luma> <название файла> - Начать редактирование файла\n" \
                   "F1 - Выйти из справки\n" \
                   "^Q - Выйти из приложения\n" \

    stdscr.clear()
    stdscr.addstr(help_message)
    stdscr.refresh()
    stdscr.getch()  # Ожидание нажатия клавиши для выхода из справки

curses.wrapper(main)