"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 03-29-2026
Description: Main entry point for Black Oystercatcher Data Management System
             Practical Project Part 3 — GUI Edition.

This program extends Practical Project Part 2 by replacing the console-based
presentation layer with a Tkinter GUI (the advanced programming topic selected
for PP3). The business layer (DataManager) and persistence layer (FileHandler)
are entirely unchanged from PP2, demonstrating the key advantage of N-Layered
architecture: individual layers can be replaced without affecting other layers.

Architecture:
    Presentation Layer  →  presentation/gui.py       (NEW in PP3)
    Business Layer      →  business/data_manager.py  (unchanged from PP2)
    Persistence Layer   →  persistence/file_handler.py (unchanged from PP2)
    Model               →  model/oystercatcher_record.py (unchanged from PP2)

References:
[1] Parks Canada. (Oct 1, 2017). "Black Oystercatcher Population - Pacific Rim."
    open.canada.ca. [Online]. Available:
    https://open.canada.ca/data/en/dataset/d87383f6-5313-430d-8416-1b6d6e377e02
    [Accessed: Dec 23, 2025]
[2] Python Software Foundation. (2026). "tkinter - Python interface to Tcl/Tk."
    Python.org. [Online]. Available: https://docs.python.org/3/library/tkinter.html
    [Accessed: Mar 1, 2026]
[3] Government of Canada. (n.d.). "Open Government License - Canada."
    open.canada.ca. [Online]. Available:
    https://open.canada.ca/en/open-government-licence-canada
    [Accessed: Feb 1, 2026]
"""

import tkinter as tk
from business.data_manager import DataManager
from presentation.gui import GUI

# Constants
STUDENT_NAME = "Felgine Touko Lina"
CSV_FILENAME  = "black_oystercatcher_data.csv"


def main():

    # Initialize business layer (unchanged from PP2)
    data_manager = DataManager(CSV_FILENAME)

    # Create Tkinter root window
    root = tk.Tk()

    # Initialize GUI presentation layer (new in PP3)
    GUI(root, data_manager, STUDENT_NAME)

    # Start Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
