from PyQt5.QtWidgets import QApplication, QMainWindow  # Import specific classes
# Import other necessary classes from ui_manager (if any)
from ui_manager import *
if __name__ == "__main__":
    app = QApplication(['BestFit Algorithm'])  # Initialize the application
    window = BestfitApp()  # Assuming BestfitApp is defined elsewhere
    window.show()  # Make the window visible
    sys.exit(app.exec_())  # Start the event loop and exit gracefully

