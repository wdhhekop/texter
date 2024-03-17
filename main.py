from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QFileDialog, QPlainTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Текстовый редактор")

        # Создаем текстовое поле
        self.text_edit = QPlainTextEdit()
        self.setCentralWidget(self.text_edit)

        # Создаем меню
        self.menu_bar = QMenu("Меню")
        self.menu_bar.addAction("Открыть", self.open_file)
        self.menu_bar.addAction("Сохранить", self.save_file)
        self.menu_bar.addSeparator()
        self.menu_bar.addAction("Выход", self.close)

        # Добавляем меню в главное окно
        self.menuBar().addMenu(self.menu_bar)

    def open_file(self):
        # Открываем диалоговое окно для выбора файла
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt)")

        if filename:
            # Открываем файл и читаем его содержимое
            with open(filename, "r") as f:
                text = f.read()

            # Задаем текст в текстовом поле
            self.text_edit.setPlainText(text)

    def save_file(self):
        # Открываем диалоговое окно для сохранения файла
        filename, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt)")

        if filename:
            # Получаем текст из текстового поля
            text = self.text_edit.toPlainText()

            # Сохраняем текст в файл
            with open(filename, "w") as f:
                f.write(text)

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()


