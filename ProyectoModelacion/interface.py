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
    options_frame = Frame(m, width=200, height=500, padx=32)
    graph_frame = Frame (m, width=500, height=500)
    result_frame = Frame(m, background="#5F9EA0", height=200, width=500)
    configs_frame = Frame(m, width=1000, height=500)

    #elementos de la pantalla de simulación
    labelComboBox = Label(options_frame, text="Seleccione un local")
    comboBoxLocal = ttk.Combobox(options_frame,state="readonly", values=["Discoteca The Darkness", "Bar La Pasión", "Cervecería Mi Rolita"])
    time_picker = SpinTimePickerModern(options_frame)
    resultText = Label(result_frame)

    #elementos de la pantalla de configuración
    comboBoxCalleJ = ttk.Combobox(configs_frame,state="readonly", values=[50,51,52,53,54])
    comboBoxCarreraJ = ttk.Combobox(configs_frame,state="readonly", values=[10,11,12,13,14])
    comboBoxCalleA = ttk.Combobox(configs_frame,state="readonly", values=[50,51,52,53,54])
    comboBoxCarreraA = ttk.Combobox(configs_frame,state="readonly", values=[10,11,12,13,14])
    comboBoxCalleNuevo = ttk.Combobox(configs_frame,state="readonly", values=[50,51,52,53,54])
    comboBoxCarreraNuevo = ttk.Combobox(configs_frame,state="readonly", values=[10,11,12,13,14])


    locales = [{"name":"Discoteca The Darkness", "coordinates":(50,14)}, {"name":"Bar La Pasión", "coordinates":(54,11)}, {"name":"Cervecería Mi Rolita", "coordinates":(50,12)}]
    nuevoLocal = tk.StringVar()
    local_names=[]
    

    cood_Javier = (54,14)
    cood_Andreina = (52,13)
    destination=()



    def __init__(self, graph: graph.Graph):

        def get_locales_options():
            new_locales=[]
            for local in self.locales:
                new_locales.append(local["name"])
            self.local_names = new_locales

        def get_local_coordinates(selected):
            for local in self.locales:
                if(local["name"]==selected):
                    self.destination = local["coordinates"]

        def build_simulation():
            self.configs_frame.destroy()
            build_options()
            build_graph_view()



        def save_configs():
            newCalleJ = self.comboBoxCalleJ.get()
            newCarreraJ = self.comboBoxCarreraJ.get()
            newCalleA = self.comboBoxCalleA.get()
            newCarreraA = self.comboBoxCarreraA.get()
            newCalleL = self.comboBoxCalleNuevo.get()
            newCarreraL = self.comboBoxCarreraNuevo.get()

            new_cod = list(self.cood_Javier)
            if(newCalleJ.strip()!=""):
                new_cod[0] = int(newCalleJ)
            if(newCarreraJ.strip()!=""):
                new_cod[1] = int(newCarreraJ)
            self.cood_Javier= tuple(new_cod)
            new_cod = list(self.cood_Andreina)
            if(newCalleA.strip()!=""):
                new_cod[0] = int(newCalleA)
            if(newCarreraA.strip()!=""):
                new_cod[1] = int(newCarreraA)
            self.cood_Andreina= tuple(new_cod)
            if(self.nuevoLocal.get().strip()!="" and newCalleL.strip()!= "" and newCarreraL.strip()!=""):
                self.locales.append({"name": self.nuevoLocal.get(), "coordinates":(int(newCalleL), int(newCarreraL))})
                get_locales_options()




        def build_config():
            self.configs_frame = Frame(self.m, width=1000, height=500)

            self.configs_frame.pack(expand=True, fill="both")
            self.configs_frame.pack_propagate(0)
            self.options_frame.destroy()
            self.graph_frame.destroy()
            labelConfig = Label(self.configs_frame, text= "Configuración")
            labelConfig.pack()
            labelJavier = Label(self.configs_frame, text="Dirección de Javier")
            labelJavier.pack()
            CallelabelJavier = Label(self.configs_frame, text="Calle de Javier")
            CallelabelJavier.pack()
            self.comboBoxCalleJ = ttk.Combobox(self.configs_frame,state="readonly", values=[50,51,52,53,54])
            self.comboBoxCalleJ.pack()
            CarreralabelJavier = Label(self.configs_frame, text="Carrera de Javier")
            CarreralabelJavier.pack()
            self.comboBoxCarreraJ = ttk.Combobox(self.configs_frame,state="readonly", values=[10,11,12,13,14])
            self.comboBoxCarreraJ.pack()
            labelJavier = Label(self.configs_frame, text="Dirección de Andreina")
            labelJavier.pack()
            CallelabelAndreina = Label(self.configs_frame, text="Calle de Andreina")
            CallelabelAndreina.pack()
            self.comboBoxCalleA = ttk.Combobox(self.configs_frame,state="readonly", values=[50,51,52,53,54])
            self.comboBoxCalleA.pack()
            CarreralabelAndreina = Label(self.configs_frame, text="Carrera de Andreina")
            CarreralabelAndreina.pack()
            self.comboBoxCarreraA = ttk.Combobox(self.configs_frame,state="readonly", values=[10,11,12,13,14])
            self.comboBoxCarreraA.pack()

            labelNuevoLocal = Label(self.configs_frame, text="Agregar Nuevo Local")
            labelNuevoLocal.pack()
            NombreLocal = tk.Entry(self.configs_frame, textvariable=self.nuevoLocal)
            NombreLocal.pack()
            CallelabelNuevo = Label(self.configs_frame, text="Calle de Nuevo Local")
            CallelabelNuevo.pack()
            self.comboBoxCalleNuevo = ttk.Combobox(self.configs_frame,state="readonly", values=[50,51,52,53,54])
            self.comboBoxCalleNuevo.pack()
            CarreralabelNuevo = Label(self.configs_frame, text="Carrera de Nuevo Local")
            CarreralabelNuevo.pack()
            self.comboBoxCarreraNuevo = ttk.Combobox(self.configs_frame,state="readonly", values=[10,11,12,13,14])
            self.comboBoxCarreraNuevo.pack()

            saveButton = Button(self.configs_frame, command=save_configs, text="Guardar Cambios")
            saveButton.pack()




        def select_option(event):
            selected = self.comboBoxLocal.get()
            self.labelComboBox.config(text="Seleccionado: {}".format(selected))
        
        def build_options():
            self.options_frame = Frame(self.m, width=200, height=500, padx=32)
            self.options_frame.pack(side="left")
            self.labelComboBox = Label(self.options_frame, text="Seleccione un local")
            self.labelComboBox.pack(padx=32, ipadx=24)
            self.comboBoxLocal = ttk.Combobox(self.options_frame,state="readonly", values=self.local_names)
            self.comboBoxLocal.pack()
            self.comboBoxLocal.set("Discoteca The Darkness")
            self.comboBoxLocal.bind("<<ComboboxSelected>>", select_option)
        
            labelTimePicker = Label(self.options_frame, text="Seleccione la hora a la que Javier y Andreina llegan al local")
            labelTimePicker.pack(padx=32, ipadx=24)

            self.time_picker = SpinTimePickerModern(self.options_frame)
            self.time_picker.addAll(constants.HOURS12)  # adds hours clock, minutes and period
            self.time_picker.pack(expand=False, fill="both", pady=12)

            execute = Button(self.options_frame, command=execute_function, text="Obtener la mejor ruta")
            execute.pack()
        
        def build_graph_view():
            self.graph_frame = Frame (self.m, width=200, height=500)
            self.graph_frame.pack(side="left")

            labels = nx.get_edge_attributes(graph.G,"weight")
            pos = {(x,y):(y,-x) for x,y in graph.G.nodes()}
            fig = plt.Figure(figsize=(5,5)) 
            ax = fig.add_subplot()  
            nx.draw(graph.G, pos, ax=ax)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, node_size=50)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Andreina], node_color="r")
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Javier], node_color="b")
            nx.draw_networkx_edge_labels(graph.G,pos, edge_labels=labels, ax=ax)

            canvas = FigureCanvasTkAgg(fig, self.graph_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()

        def create_edge_list(path):
            list_edge=[]
            for node in range(len(path)-1):
                list_edge.append((path[node], path[node+1]))
            return list_edge

        def build_path_view(result):
            self.graph_frame = Frame (self.m, width=200, height=500)
            self.graph_frame.pack(side="left")

            path_edgesJ = create_edge_list(result["route_javier"])
            path_edgesA = create_edge_list(result["route_andreina"])
            labels = nx.get_edge_attributes(graph.G,"weight")
            pos = {(x,y):(y,-x) for x,y in graph.G.nodes()}
            fig = plt.Figure(figsize=(5,5)) 
            ax = fig.add_subplot()

            nx.draw(graph.G, pos, ax=ax)
            nx.draw_networkx_edge_labels(graph.G,pos, edge_labels=labels, ax=ax)
            nx.draw_networkx_edges(graph.G, pos, edgelist=path_edgesJ, edge_color="r", width=5, ax=ax)
            nx.draw_networkx_edges(graph.G, pos, edgelist=path_edgesA, edge_color="b", width=5, ax=ax)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, node_size=50)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Javier], node_color="r")
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Andreina], node_color="b")
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.destination], node_color="g")


            canvas = FigureCanvasTkAgg(fig, self.graph_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        
        def restart():
                self.result_frame.destroy()
                self.graph_frame.destroy()
                
                build_options()

                build_graph_view()


        def execute_function():
            selected = self.comboBoxLocal.get()
            get_local_coordinates(selected)
            result = graph.determine_best_route(self.cood_Javier, self.cood_Andreina, self.destination)
            
            arrival_time= self.time_picker.time()

            leave_javier = "{}:{} {}".format(arrival_time[0], (arrival_time[1]-result["time_javier"]), arrival_time[2])
            leave_andreina = "{}:{} {}".format(arrival_time[0], (arrival_time[1]-result["time_andreina"]), arrival_time[2])

            self.result_frame = Frame(self.m, background="#5F9EA0", height=500, width=200)
            self.resultText = Label(self.result_frame, text= "Javier tarda {} minutos en llegar\nJavier tiene que salir a las {}\nAndreina tarda {} minutos\nAndreina tiene que salir a las {}".format(result["time_javier"],leave_javier, result["time_andreina"], leave_andreina))
            self.resultText.pack()
            backButton = Button(self.result_frame, text="Reiniciar", command=restart)
            backButton.pack()
            self.options_frame.destroy()
            self.graph_frame.destroy()

            self.result_frame.pack(side="left")
            build_path_view(result)


            
        menu_bar = Menu(self.m)
        menu_options = Menu(menu_bar, tearoff=0)
        menu_options.add_command(label="Simulación", command=build_simulation)
        menu_options.add_command(label="Configuración", command=build_config)
        menu_bar.add_cascade(label="Opciones", menu=menu_options)
        self.m.config(menu=menu_bar)
        self.m.title("Javier y Andreina - Proyecto Modelación")
        get_locales_options()
        build_options()
        build_graph_view()
       



        self.m.mainloop()


    