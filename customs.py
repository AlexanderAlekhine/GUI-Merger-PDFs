from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragDropMode(QListWidget.InternalMove)
        self.currentItemChanged.connect(self.renumberItems)
        self.setAlternatingRowColors(True)  # Alternar colores de fila para mejorar la visibilidad
        self.setFont(QFont('Sans Serif', 10))  

        self.setStyleSheet("""
            QListWidget {
                background-color: #f7f7f7;
                border-radius: 10px;
                padding: 10px;
                color: #333333;
            }
            QListWidget::item {
                border-bottom: 1px solid #dddddd;
                padding: 5px;
                margin: 2px;
            }
            QListWidget::item:selected {
                background-color: #a2d2ff;
                color: #ffffff;
            }
        """)

    def dropEvent(self, event):
        super().dropEvent(event)
        self.renumberItems()

    def renumberItems(self, current=None, previous=None):
        for index in range(self.count()):
            item = self.item(index)
            item.setText(f"{index + 1}. {item.data(Qt.UserRole)}")

    def addItem(self, label):
        item = QListWidgetItem(f"{self.count() + 1}. {label}")
        item.setData(Qt.UserRole, label)
        super().addItem(item)

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #5c6bc0; /* Color de fondo */
                color: #ffffff; /* Color del texto */
                border-style: none; /* Sin borde */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 10px; /* Relleno alrededor del texto */
                margin: 10px; /* Espacio alrededor del botón */
                font-size: 16px; /* Tamaño del texto */
                font-weight: bold; /* Peso de la fuente */
                font-family: "Sans Serif"; /* Tipo de fuente */
            }
            QPushButton:hover {
                background-color: #3949ab; /* Color de fondo al pasar el mouse por encima */
            }
            QPushButton:pressed {
                background-color: #283593; /* Color de fondo al presionar el botón */
            }
        """)