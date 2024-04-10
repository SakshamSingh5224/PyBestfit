from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QTextEdit
from memory import MemoryManager

class BestfitApp(QMainWindow):
  def __init__(self):
    super().__init__()
    self.memory_manager = MemoryManager(10)  # Create a memory manager with 10 blocks
    self.init_ui()

  def init_ui(self):
    self.setWindowTitle("Best-Fit Memory Management")

    # Layout
    self.main_layout = QV


