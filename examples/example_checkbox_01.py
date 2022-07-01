#!/usr/bin/env python3
# -------------------------------------------
# add path for local tksheet
import os
import sys
from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(os.path.dirname(SCRIPT_DIR))
# -------------------------------------------

import tkinter as tk
from tksheet import Sheet

class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.data_header = ["val1", "val2", "val3","val4"]
        self.data = [
            ["this_is_true",  "AAA1",  False, "AAA2"],
            ["",              "BBBB1", False, "BBBB2"],
            ["this_is_false", "CCCCC1",False, "CCCCC2"],
        ]
 
        self.frame = tk.Frame(self)
        self.sheet = Sheet(self.frame, data=self.data, headers=self.data_header)
        self.sheet.enable_bindings((
            "single_select",  # "single_select" or "toggle_select"
            "arrowkeys",
            "edit_cell",
            "column_width_resize",
        ))
        self.sheet.extra_bindings("end_edit_cell", self.end_edit_cell)

        self.create_checkbox_val1(0, 0)
        self.create_checkbox_val1(1, 0)
        self.create_checkbox_val1(2, 0)
        
        self.sheet.create_checkbox(r = "all", c = 2, checked = False, text = "Checkbox ")

        self.sheet.see(0,0)
        self.sheet.set_all_cell_sizes_to_text() # cell resizing moved here

        self.button = tk.Button(self.frame, text="print data", command=self.print_data)

        self.button.pack()
        self.sheet.pack(fill=tk.BOTH, expand=tk.YES)
        self.frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_checkbox_val1(self, row, col):
        value = self.sheet.get_cell_data(row, col)
        checked = True if  value == "this_is_true" else False
        self.sheet.create_checkbox(row, col, checked=checked, onvalue="this_is_true", offvalue="this_is_false", redraw=True)

        print("create_checkbox: row=" + str(row) + " col=" + str(col) + " value=" + str(value) + " checked=" + str(checked))

    def end_edit_cell(self, event):
        print("end_edit_cell: event=" + str(event))

    def print_data(self):
        print("sheet=" + str(self.sheet.get_sheet_data()))


app = demo()
app.mainloop()
