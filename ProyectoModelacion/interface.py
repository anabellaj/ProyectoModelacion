import networkx as nx
import graph
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tktimepicker import SpinTimePickerModern
from tktimepicker import constants

class MainWindow:

    m = tk.Tk()
    

    def __init__(self, graph: graph.Graph):
        def select_option(event):
            selected = comboBoxLocal.get()
            labelComboBox.config(text="Seleccionado: {}".format(selected))

        def execute_function():
            selected = comboBoxLocal.get()
            if(selected=="Discoteca The Darkness"):
                destination = (50,14)
            elif (selected == "Bar La Pasión"):
                destination=(54,11)
            else:
                destination = (50,12)
            result = graph.determine_best_route((54,14), (52,13), destination)
            resultFrame = Frame(columnA, background="#5F9EA0", height=100, width=100)
            resultFrame.pack(side="bottom")
            arrival_time= time_picker.time()

            leave_javier = "{}:{} {}".format(arrival_time[0], (arrival_time[1]-result["time_javier"]), arrival_time[2])
            leave_andreina = "{}:{} {}".format(arrival_time[0], (arrival_time[1]-result["time_andreina"]), arrival_time[2])

            resultText = Label(resultFrame, text= "Javier tarda {} minutos en llegar\nJavier tiene que salir a las {}\nAndreina tarda {} minutos\nAndreina tiene que salir a las {}".format(result["time_javier"],leave_javier, result["time_andreina"], leave_andreina))
            resultText.pack()



            
        
        self.m.title("Javier y Andreina - Proyecto Modelación")
        columnA = Frame(self.m, width=500, height=500, padx=32)
        columnA.pack(side="left")
        columnB = Frame (self.m, width=200, height=500)
        columnB.pack(side="left")
    
        labels = nx.get_edge_attributes(graph.G,"weight")
        pos = nx.spring_layout(graph.G)
        fig = plt.Figure(figsize=(5,5)) 
        ax = fig.add_subplot()  
    
        nx.draw_networkx_edge_labels(graph.G,pos, edge_labels=labels, ax=ax)
        nx.draw(graph.G, pos, ax=ax)

        canvas = FigureCanvasTkAgg(fig, columnB)
        canvas.get_tk_widget().pack()
        canvas.draw()



        labelComboBox = Label(columnA, text="Seleccione un local")
        labelComboBox.pack(padx=32, ipadx=24)
        comboBoxLocal = ttk.Combobox(columnA,state="readonly", values=["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita"])
        comboBoxLocal.pack()
        comboBoxLocal.set("Discoteca The Darkness")
        comboBoxLocal.bind("<<ComboboxSelected>>", select_option)
        
        labelTimePicker = Label(columnA, text="Seleccione la hora a la que Javier y Andreina llegan al local")
        labelTimePicker.pack(padx=32, ipadx=24)

        time_picker = SpinTimePickerModern(columnA)
        time_picker.addAll(constants.HOURS12)  # adds hours clock, minutes and period
        time_picker.pack(expand=False, fill="both", pady=12)

        execute = Button(columnA, command=execute_function, text="Obtener la mejor ruta")
        execute.pack()



        self.m.mainloop()



    