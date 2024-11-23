import networkx as nx

import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class MainWindow:

    m = tk.Tk().title("Javier y Andreina - Proyecto Modelación")

    def __init__(self, graph):
        def select_option(event):
            selected = comboBoxLocal.get()
            labelComboBox.config(text="Seleccionado: {}".format(selected))
        

        columnA = Frame(self.m, width=500, height=500, padx=32)
        columnA.pack(side="left")
        columnB = Frame (self.m, width=200, height=500)
        columnB.pack(side="left")
    
        labels = nx.get_edge_attributes(graph,"weight")
        pos = nx.spring_layout(graph)
        fig = plt.Figure(figsize=(5,5)) 
        ax = fig.add_subplot()  
    
        nx.draw_networkx_edge_labels(graph,pos, edge_labels=labels, ax=ax)
        nx.draw(graph, pos, ax=ax)

        canvas = FigureCanvasTkAgg(fig, columnB)
        canvas.get_tk_widget().pack()
        canvas.draw()



        labelComboBox = Label(columnA, text="Seleccione un local")
        labelComboBox.pack(padx=32, ipadx=24)
        comboBoxLocal = ttk.Combobox(columnA,state="readonly", values=["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita"])
        comboBoxLocal.pack()
        comboBoxLocal.set("Discoteca The Darkness")
        comboBoxLocal.bind("<<ComboboxSelected>>", select_option)

        self.m.mainloop()


    