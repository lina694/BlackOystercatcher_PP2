"""
Author: Felgine Touko Lina
Course: CST8002 - Programming Language Research
Professor: Stanley Pieda
Due Date: 03-29-2026
Description: Presentation layer - Graphical User Interface (GUI) using Tkinter.

This module replaces the console-based menu from Practical Project Part 2
with a full Tkinter GUI. The business layer (DataManager) and persistence
layer (FileHandler) are completely unchanged, demonstrating the key benefit
of N-Layered architecture: the presentation layer can be fully replaced
without touching any other layer.

The GUI provides:
 - A ttk.Treeview widget displaying all loaded records
 - Buttons for all CRUD operations (Load, Add, Edit, Delete, Save)
 - A status bar showing success/error messages
 - Student name permanently visible in the title bar and header label

References:
[1] Python Software Foundation. (2026). "tkinter - Python interface to Tcl/Tk."
    Python.org. [Online]. Available: https://docs.python.org/3/library/tkinter.html
    [Accessed: Mar 1, 2026]
[2] Python Software Foundation. (2026). "tkinter.ttk - Tk themed widgets."
    Python.org. [Online]. Available:
    https://docs.python.org/3/library/tkinter.ttk.html
    [Accessed: Mar 1, 2026]
[3] Real Python. (2026). "Python GUI Programming With Tkinter."
    realpython.com. [Online]. Available:
    https://realpython.com/python-gui-tkinter/
    [Accessed: Mar 1, 2026]
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class GUI:
    """
    Main graphical user interface for the Black Oystercatcher
    Data Management System.

    Provides a Tkinter window with a Treeview record display,
    CRUD operation buttons, and a status bar. Delegates all
    data operations to the DataManager business layer.
    """

    # Column definitions matching the CSV dataset field names
    COLUMNS = (
        "visit_date",
        "site_identification",
        "species",
        "total_black_oystercatcher_adults"
    )

    COLUMN_HEADERS = (
        "Visit Date",
        "Site Identification",
        "Species",
        "Total Adults"
    )

    def __init__(self, root, data_manager, student_name):
        """
        Initialize the GUI with a Tkinter root window and data manager.

        Args:
            root (tk.Tk): The root Tkinter window
            data_manager (DataManager): Business layer object
            student_name (str): Student full name to display on screen
        """
        self.root = root
        self.data_manager = data_manager
        self.student_name = student_name

        # Configure root window
        self.root.title(
            f"Black Oystercatcher Data Management System "
            f"- {self.student_name}"
        )
        self.root.geometry("1000x620")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f4f8")

        # Build all UI components
        self._build_header()
        self._build_treeview()
        self._build_buttons()
        self._build_status_bar()

        # Load data on startup
        self._load_data()

    def _build_header(self):
        """Build the header frame displaying the program title and student name."""
        header_frame = tk.Frame(self.root, bg="#2E4057", pady=10)
        header_frame.pack(fill=tk.X)

        tk.Label(
            header_frame,
            text="Black Oystercatcher Data Management System",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#2E4057"
        ).pack()

        tk.Label(
            header_frame,
            text=f"by {self.student_name}",
            font=("Arial", 11),
            fg="#cce0ff",
            bg="#2E4057"
        ).pack()

    def _build_treeview(self):
        """
        Build the ttk.Treeview widget and scrollbars for displaying records.

        The Treeview uses columns matching the Parks Canada dataset field names:
        visit_date, site_identification, species,
        total_black_oystercatcher_adults.
        """
        tree_frame = tk.Frame(self.root, bg="#f0f4f8", padx=10, pady=8)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        # Vertical and horizontal scrollbars
        v_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
        h_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)

        self.tree = ttk.Treeview(
            tree_frame,
            columns=self.COLUMNS,
            show="headings",
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set,
            selectmode="browse"
        )

        v_scroll.config(command=self.tree.yview)
        h_scroll.config(command=self.tree.xview)

        # Configure column headings and widths
        col_widths = [120, 160, 220, 130]
        for col, header, width in zip(
                self.COLUMNS, self.COLUMN_HEADERS, col_widths):
            self.tree.heading(col, text=header, anchor=tk.W)
            self.tree.column(col, width=width, anchor=tk.W, minwidth=80)

        # Alternating row colours
        self.tree.tag_configure("evenrow", background="#e8f0f7")
        self.tree.tag_configure("oddrow",  background="#ffffff")

        self.tree.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        tree_frame.rowconfigure(0, weight=1)
        tree_frame.columnconfigure(0, weight=1)

    def _build_buttons(self):
        """
        Build the button panel with all CRUD operation buttons.

        Each button calls the corresponding method which delegates
        to the DataManager business layer.
        """
        btn_frame = tk.Frame(self.root, bg="#dce8f5", pady=8)
        btn_frame.pack(fill=tk.X, padx=10)

        btn_style = {
            "font": ("Arial", 10, "bold"),
            "width": 14,
            "pady": 5,
            "relief": tk.RAISED,
            "cursor": "hand2"
        }

        buttons = [
            ("Load Data",    "#2E7D32", "#ffffff", self._load_data),
            ("Add Record",   "#1565C0", "#ffffff", self._add_record),
            ("Edit Record",  "#E65100", "#ffffff", self._edit_record),
            ("Delete Record","#B71C1C", "#ffffff", self._delete_record),
            ("Save to File", "#4A148C", "#ffffff", self._save_data),
        ]

        for text, bg, fg, cmd in buttons:
            tk.Button(
                btn_frame,
                text=text,
                bg=bg,
                fg=fg,
                command=cmd,
                **btn_style
            ).pack(side=tk.LEFT, padx=6)

        # Record count label on the right
        self.count_var = tk.StringVar(value="Records: 0")
        tk.Label(
            btn_frame,
            textvariable=self.count_var,
            font=("Arial", 10, "bold"),
            bg="#dce8f5",
            fg="#2E4057"
        ).pack(side=tk.RIGHT, padx=10)

    def _build_status_bar(self):
        """
        Build the status bar at the bottom of the window.

        Displays success and error messages from all operations,
        replacing the print() statements used in the console menu.
        """
        status_frame = tk.Frame(self.root, bg="#2E4057", pady=4)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.status_var = tk.StringVar(value="Ready.")
        tk.Label(
            status_frame,
            textvariable=self.status_var,
            font=("Arial", 9),
            fg="#cce0ff",
            bg="#2E4057",
            anchor=tk.W,
            padx=10
        ).pack(fill=tk.X)

    # ── private helpers ───────────────────────────────────────────────────────

    def _set_status(self, message):
        """
        Update the status bar message.

        Args:
            message (str): Message to display in the status bar
        """
        self.status_var.set(message)
        self.root.update_idletasks()

    def _refresh_treeview(self):
        """
        Clear and repopulate the Treeview with current records from memory.

        Called after any CRUD operation to keep the display in sync
        with the in-memory data structure managed by DataManager.
        """
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Repopulate from DataManager
        records = self.data_manager.get_all_records()
        for i, record in enumerate(records):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            self.tree.insert("", tk.END, iid=str(i), tags=(tag,), values=(
                record.get_visit_date(),
                record.get_site_identification(),
                record.get_species(),
                record.get_total_black_oystercatcher_adults()
            ))

        self.count_var.set(f"Records: {self.data_manager.get_record_count()}")

    def _get_selected_index(self):
        """
        Get the index of the currently selected Treeview row.

        Returns:
            int or None: Zero-based index of selected row, or None if
                         no row is selected.
        """
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(
                "No Selection", "Please select a record first.")
            return None
        return int(selected[0])

    def _open_record_dialog(self, title,
                            date="", site="", species="", adults=""):
        """
        Open a Toplevel dialog window for entering or editing record data.

        Args:
            title (str): Dialog window title
            date (str): Pre-filled visit date value
            site (str): Pre-filled site identification value
            species (str): Pre-filled species value
            adults (str): Pre-filled adult count value

        Returns:
            tuple or None: (date, site, species, adults) strings if OK clicked,
                           None if cancelled.
        """
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("420x260")
        dialog.resizable(False, False)
        dialog.configure(bg="#f0f4f8")
        dialog.grab_set()  # Modal window

        # Field labels and entry widgets
        fields = [
            ("Visit Date (DD/MM/YYYY):", date),
            ("Site Identification:",      site),
            ("Species:",                  species),
            ("Total Adults:",             adults),
        ]
        entries = []
        for row_idx, (label_text, default) in enumerate(fields):
            tk.Label(
                dialog, text=label_text,
                font=("Arial", 10), bg="#f0f4f8", anchor=tk.W
            ).grid(row=row_idx, column=0, padx=15, pady=8, sticky=tk.W)

            entry = tk.Entry(dialog, font=("Arial", 10), width=25)
            entry.insert(0, default)
            entry.grid(row=row_idx, column=1, padx=10, pady=8)
            entries.append(entry)

        result = [None]

        def on_ok():
            """Collect values and close dialog."""
            values = [e.get().strip() for e in entries]
            if not all(values):
                messagebox.showwarning(
                    "Missing Fields",
                    "All fields are required.",
                    parent=dialog
                )
                return
            result[0] = tuple(values)
            dialog.destroy()

        def on_cancel():
            """Cancel and close dialog."""
            dialog.destroy()

        btn_row = tk.Frame(dialog, bg="#f0f4f8")
        btn_row.grid(row=len(fields), column=0, columnspan=2, pady=12)
        tk.Button(btn_row, text="OK",     width=10,
                  command=on_ok,     bg="#1565C0", fg="white",
                  font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=8)
        tk.Button(btn_row, text="Cancel", width=10,
                  command=on_cancel, bg="#555555", fg="white",
                  font=("Arial", 10)).pack(side=tk.LEFT, padx=8)

        self.root.wait_window(dialog)
        return result[0]

    # ── button handlers ───────────────────────────────────────────────────────

    def _load_data(self):
        """
        Load (or reload) 100 records from the CSV file via the DataManager.

        Calls DataManager.load_data() and refreshes the Treeview display.
        """
        success, message = self.data_manager.load_data(num_records=100)
        self._refresh_treeview()
        self._set_status(message)

    def _add_record(self):
        """
        Open a dialog to collect input and create a new record.

        Calls DataManager.create_record() with the user-entered values
        and refreshes the Treeview to show the new record.
        """
        result = self._open_record_dialog("Add New Record")
        if result:
            date, site, species, adults = result
            success, message = self.data_manager.create_record(
                date, site, species, adults)
            self._refresh_treeview()
            self._set_status(message)

    def _edit_record(self):
        """
        Open a dialog pre-filled with the selected record's data for editing.

        Retrieves the selected record from DataManager, pre-fills the dialog,
        then calls DataManager.update_record() with the new values.
        """
        index = self._get_selected_index()
        if index is None:
            return

        success, record = self.data_manager.get_record_by_index(index)
        if not success:
            self._set_status(f"Error: {record}")
            return

        result = self._open_record_dialog(
            f"Edit Record {index}",
            date=record.get_visit_date(),
            site=record.get_site_identification(),
            species=record.get_species(),
            adults=record.get_total_black_oystercatcher_adults()
        )
        if result:
            date, site, species, adults = result
            success, message = self.data_manager.update_record(
                index, date, site, species, adults)
            self._refresh_treeview()
            self._set_status(message)

    def _delete_record(self):
        """
        Delete the selected record after confirmation.

        Shows a confirmation dialog before calling
        DataManager.delete_record(). Refreshes the Treeview after deletion.
        """
        index = self._get_selected_index()
        if index is None:
            return

        success, record = self.data_manager.get_record_by_index(index)
        if not success:
            self._set_status(f"Error: {record}")
            return

        confirmed = messagebox.askyesno(
            "Confirm Delete",
            f"Delete this record?\n\n{record}",
        )
        if confirmed:
            success, message = self.data_manager.delete_record(index)
            self._refresh_treeview()
            self._set_status(message)

    def _save_data(self):
        """
        Save all current records to a new CSV file with a UUID filename.

        Calls DataManager.save_data() and displays the generated
        filename in the status bar.
        """
        success, message = self.data_manager.save_data()
        self._set_status(message)
        if success:
            messagebox.showinfo("Save Successful", message)
