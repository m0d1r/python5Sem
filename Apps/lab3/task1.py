import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ftask1 import Ui_Form


class Task1(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stats = None
        self.btnLoad.clicked.connect(self.load_file)
        self.btnSave.clicked.connect(self.save_file)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Text (*.txt)")
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                tokens = f.read().split()
            if not tokens:
                raise ValueError("файл пуст")
            numbers = [int(t) for t in tokens]
        except (ValueError, OSError) as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось прочитать числа: {e}")
            return
        mx, mn = max(numbers), min(numbers)
        avg = sum(numbers) / len(numbers)
        self.stats = (mx, mn, avg)
        self.lblMax.setText(f"Максимум: {mx}")
        self.lblMin.setText(f"Минимум: {mn}")
        self.lblAvg.setText(f"Среднее: {avg:.4f}")

    def save_file(self):
        if self.stats is None:
            QMessageBox.warning(self, "Нет данных", "Сначала загрузите файл")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить", "", "Text (*.txt)")
        if not path:
            return
        mx, mn, avg = self.stats
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Максимум: {mx}\nМинимум: {mn}\nСреднее: {avg:.4f}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task1()
    w.show()
    sys.exit(app.exec_())