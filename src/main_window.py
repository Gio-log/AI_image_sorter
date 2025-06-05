from PyQt5.QtWidgets import QMainWindow, QPushButton, QGridLayout, QWidget, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from src.image_view import ImageView
from src.sorter import Sorter
import shutil
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.label = QLabel("AI Image Sorter")
        self.count = QLabel("No images waiting to be sorted yet.")
        self.photo_view = ImageView()

        layout = QGridLayout()

        self.setWindowTitle("AI Image Sorter")
        button = QPushButton("Sort Images")
        button.clicked.connect(self.sort)

        self.setMinimumSize(QSize(400, 300))

        layout.addWidget(self.photo_view, 0, 0, 2, 1)
        layout.addWidget(self.label, 0, 1)
        layout.addWidget(self.count, 1, 1)
        layout.addWidget(button, 2, 0, 1, 2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasImage:
                event.setDropAction(Qt.CopyAction)
                dest_dir = 'assets/test_images'
                self.image = []
                files = event.mimeData().urls()
                self.count.setText(f"{len(files)} images waiting to be sorted.")
                for path in files:
                    image_path = path.toLocalFile()
                    file_name = os.path.basename(image_path)
                    os.makedirs(dest_dir, exist_ok=True)
                    dest_path = os.path.join(dest_dir, file_name)
                    shutil.copy(image_path, dest_path)
                    self.image.append(dest_path)
                self.set_image()
                event.accept()
            else:
                event.ignore()

        except Exception as e:
            self.label.setText(f"Error: {str(e)}")
            print(f"Error: {str(e)}")
            event.ignore()
    
    def set_image(self):
        self.photo_view.setPixmap(QPixmap(self.image[0]))

    def sort(self):
        categories = []
        label = Sorter().predict(self.image[0])
        self.label.setText(f"Predicted label for current image: {label}")
        for image in self.image:
            sort = Sorter().predict(image)
            os.makedirs(f'assets/sorted/{sort}', exist_ok=True)
            shutil.copy(image, f'assets/sorted/{sort}')
            if sort not in categories:
                categories.append(sort)
        self.count.setText(f"Sorted {len(self.image)} images into {len(categories)} categories.")
        