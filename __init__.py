import sys
from PyQt5.QtWidgets import QApplication
from main import MainWindow
import argparse

# Iniciar la aplicación+
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    languages = ["en", "es", "fr", "de", "it", "pt", "ru", "zh", "ja", "ko"]
    parser.add_argument('--language', '-l', type=str, help=f"{', '.join(languages)} are supported.", default='es')
    language = parser.parse_args().language
    if language not in languages:
        raise ValueError(f"Language '{language}' not supported. Only {', '.join(languages)} are supported.")
    
    app = QApplication(sys.argv)
    ex = MainWindow(language)
    sys.exit(app.exec_())
