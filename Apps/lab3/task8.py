import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QPainter, QPen, QTransform, QPolygonF
from PyQt5.QtCore import Qt, QPointF
from ftask8 import Ui_Form


class LSystemWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.drawing = ""
        self.angle = 60.0

    def paintEvent(self, event):
        if not self.drawing:
            return
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.darkGreen, 1)
        p.setPen(pen)

        # определяем масштаб по размеру виджета и длине строки
        step = max(2.0, min(self.width(), self.height()) / (len(self.drawing) ** 0.5 + 10))

        pos = QPointF(0, 0)
        # старт: снизу по центру
        pos = QPointF(self.width() / 2, self.height() - 20)
        direction = -90.0  # вверх

        for ch in self.drawing:
            if ch in "Ff":
                rad = math.radians(direction)
                new_pos = QPointF(
                    pos.x() + step * math.cos(rad),
                    pos.y() + step * math.sin(rad),
                )
                p.drawLine(pos, new_pos)
                pos = new_pos
            elif ch == "+":
                direction += self.angle
            elif ch == "-":
                direction -= self.angle


class Task8(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # заменяем canvas на LSystemWidget
        self.canvas_widget = LSystemWidget(self)
        self.verticalLayout.replaceWidget(self.canvas, self.canvas_widget)
        self.canvas.deleteLater()

        self.btnOpen.clicked.connect(self.open_file)
        self.sliderStep.valueChanged.connect(self.update_step)

        self.name = ""
        self.axiom = ""
        self.rules = {}
        self.angle = 60.0
        self.steps = []

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть", "", "Text (*.txt)")
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f if line.strip() != ""]
        except OSError as e:
            self.lblInfo.setText(f"Ошибка: {e}")
            return

        if len(lines) < 4:
            self.lblInfo.setText("Некорректный файл: мало строк")
            return

        try:
            self.name = lines[0]
            n_angles = int(lines[1])
            self.angle = 360.0 / n_angles
            self.axiom = lines[2]
            self.rules = {}
            for line in lines[3:]:
                lhs = line[0]
                rhs = line[1:]
                self.rules[lhs] = rhs
        except (ValueError, IndexError) as e:
            self.lblInfo.setText(f"Ошибка формата: {e}")
            return

        self.steps = [self.axiom]
        self.sliderStep.setRange(0, 5)
        self.sliderStep.setValue(0)
        self.update_step(0)

    def update_step(self, step):
        while len(self.steps) <= step:
            prev = self.steps[-1]
            nxt = "".join(self.rules.get(ch, ch) for ch in prev)
            self.steps.append(nxt)
        self.canvas_widget.drawing = self.steps[step]
        self.canvas_widget.angle = self.angle
        self.lblInfo.setText(f"{self.name}, шаг {step}")
        self.canvas_widget.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task8()
    w.show()
    sys.exit(app.exec_())