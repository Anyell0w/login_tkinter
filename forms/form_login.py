import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel

class App:

  def __init__(self):
      self.ventana = tk.Tk()
      self.ventana.title("Login")
      self.ventana.geometry("800x500")
      self.ventana.config(bg="#fcfcfc")
      self.ventana.resizable(0,0)
      utl.centrar_ventana(self.ventana, 800, 500)
      self.ventana.mainloop()