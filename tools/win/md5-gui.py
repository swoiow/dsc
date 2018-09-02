#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import hashlib
import os
import tkinter
from functools import partial
from tkinter import ttk


class AddWidget(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.resizable(width=False, height=False)

        for k, v in h.items():
            setattr(self, k, v)

        self.on_validate = self.register(self._on_validate)
        self.init_gui()

    def _on_validate(self, val, name):
        _val = getattr(self, name, "")
        if val.strip() == str(_val):
            self.answer_label["text"] = name.upper() + " Match!"
            return True
        else:
            self.answer_label["text"] = name.upper() + " No match!"
            return False

    def _addto_clipboard(self, name):
        _val = getattr(self, name, "")
        command = "echo " + str(_val).strip() + "| clip"
        os.popen(command)
        return True

    def init_gui(self):
        Entry = partial(ttk.Entry, width=60, validate="focusout")

        self.root.title("File Hash Checker")
        self.grid(column=0, row=0, sticky="nsew")

        self.input_md5 = Entry(self, validatecommand=(self.on_validate, "%P", "md5"))
        self.input_md5.grid(column=0, row=2)

        self.input_sha1 = Entry(self, validatecommand=(self.on_validate, "%P", "sha1"))
        self.input_sha1.grid(column=0, row=4)

        self.input_sha256 = Entry(self, validatecommand=(self.on_validate, "%P", "sha256"))
        self.input_sha256.grid(column=0, row=6)

        ttk.Label(self, text="MD5: %s" % self.md5).grid(column=0, row=1, sticky="w")
        ttk.Label(self, text="SHA1: %s" % self.sha1).grid(column=0, row=3, sticky="w")
        ttk.Label(self, text="SHA256: %s" % self.sha256).grid(column=0, row=5, sticky="w")

        self.btn_frame = ttk.Frame(self)
        self.btn_frame.grid(column=0, row=7)
        ttk.Button(self.btn_frame, text="MD5", command=lambda: self._addto_clipboard("md5")). \
            grid(column=0, row=0)
        ttk.Button(self.btn_frame, text="SHA1", command=lambda: self._addto_clipboard("sha1")). \
            grid(column=1, row=0)
        ttk.Button(self.btn_frame, text="SHA256", command=lambda: self._addto_clipboard("sha256")). \
            grid(column=2, row=0)

        self.answer_frame = ttk.LabelFrame(self, text="Result For: %s" % filename, height=100)
        self.answer_frame.grid(column=0, row=8, sticky="nesw")

        self.answer_label = ttk.Label(self.answer_frame, text="", font=("Consolas", 16))
        self.answer_label.grid(column=0, row=0)

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=5)


def sum_md5(input_file, **kwargs):
    global filename
    filename = input_file
    _map = [("md5", hashlib.md5), ("sha1", hashlib.sha1), ("sha256", hashlib.sha256)]

    with open(input_file, "rb") as _rf:
        hash_result = [(kind, func()) for kind, func in _map]

        while True:
            _bin = _rf.read(10 * 1024 * 1024)
            if not _bin:
                break
            for _, hash_type in hash_result:
                hash_type.update(_bin)

                # for kind, hash_type in hash_result:
                #     print(kind.ljust(8) + ": " + hash_type.hexdigest())
    return {k: v.hexdigest() for k, v in hash_result}


def main():
    parser = argparse.ArgumentParser(description="Calculation file md5.")

    parser.add_argument("-i", dest="input", required=True, help="input abspath of the file")

    args = parser.parse_args()
    if args.input:
        return sum_md5(args.input)


if __name__ == "__main__":
    # h = {"md5": 1, "sha1": "2", "sha256": "3"}
    h = main()
    if h:
        frame = tkinter.Tk()
        AddWidget(frame)
        frame.mainloop()
