from os.path import basename

from PyQt5.QtWidgets import (QMainWindow, QWidget, #QDialog,
                             QHBoxLayout, QVBoxLayout, QFileDialog)
from PyQt5.QtCore import Qt

from customs import ListWidget, Button
from pdf_tools import createPDF
from i18n import Translator

class MainWindow(QMainWindow):
    def __init__(self, language):
        super().__init__()
        self.setWindowTitle('Unir PDFs')
        self.setWindowIcon(self.style().standardIcon(13))
        self.setGeometry(550, 230, 700, 500)

        self.t = Translator(language)

        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()

        layout_h = QHBoxLayout()

        button_add = Button(self.t.gettext('button_add'), self)
        button_add.clicked.connect(self.openFileNameDialog)
        layout_h.addWidget(button_add)

        button_delete = Button(self.t.gettext('button_delete'), self)
        button_delete.clicked.connect(self.deleteSelectedItem)
        layout_h.addWidget(button_delete)
        
        button_create = Button(self.t.gettext('button_create'), self)
        button_create.clicked.connect(self.createPDF)

        self.list_widget = ListWidget()
        self.items = {}

        layout.addWidget(self.list_widget)
        layout.addLayout(layout_h)
        layout.addWidget(button_create)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def createPDF(self):
        items = (self.list_widget.item(i).text().split(' ', 1)[1] for i in range(self.list_widget.count()))
        paths = [self.items[item] for item in items]
        #paths = self.items.values() # Misma idea pero no cuenta con posibles archivos repetidos.
        output = 'PDF_merged.pdf' # Se puede crear una venta QDialog para que el usuario elija el nombre. #Pero no me da la gana ;).
        createPDF(paths, output)

    def openFileNameDialog(self):
        options = QFileDialog.Options() #options |= QFileDialog.DontUseNativeDialog

        files_types = """All Files (*);;PDF Files (*.pdf);;Images (*.png, *.jpg, *.jpeg)"""
       
        files, _ = QFileDialog.getOpenFileNames(self, "Seleciona archivos", "",
                                                files_types, options=options)
        
        # Para mostrar solo el nombre del archivo en la lista.
        files = {basename(file): file for file in files} # os.path.basename(file)

        if files: 
            keys = list(files.keys())
            for file in keys: # Esta parte es para evitar que se repitan los nombres de los archivos.
                if file in self.items.keys(): # Y así poder agrear distintos archivos con el mismo nombre.
                    if not(files[file] == self.items[file]): 
                        i = 1
                        f = file
                        while file in self.items.keys():
                            file = f'{f} ({i})'
                            i += 1
                            try:
                                if files[f] == self.items[file]: break
                            except KeyError:
                                pass
                        
                        files[file] = files.pop(f)

                self.list_widget.addItem(file) # Agregar el ítem a la lista.
            self.items.update(files) # Agregar los ítems al diccionario.

    def deleteSelectedItem(self):
        # Elimina el ítem seleccionado.
        listItems = self.list_widget.selectedItems()
        items = (self.list_widget.item(i).text().split(' ', 1)[1] for i in range(self.list_widget.count()))
        count = len(it for it in items if it == listItems[0].text().split(' ', 1)[1])
        if count == 1: # Si solo hay un ítem con ese nombre, lo elimina del diccionario. 
            del self.items[listItems[0].text().split(' ', 1)[1]] #Si hay más, no debe eliminarlo. 
            #Esto permite que se puedan agregar el msimo archivo.

        if not listItems: return   

        for item in listItems: #Si selecciona más de un item, los elimina todos. Aunque no debería ser posible.
            self.list_widget.takeItem(self.list_widget.row(item))
            _ = self.items.pop(item.text().split(' ', 1)[1], None)
        self.list_widget.renumberItems()

    def keyPressEvent(self, event): # ATAJOS DE TECLADO
        if event.key() == Qt.Key_Delete:
            self.deleteSelectedItem()
        elif event.key() == Qt.Key_Insert:
            self.openFileNameDialog()
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.createPDF()
        else:
            super().keyPressEvent(event)