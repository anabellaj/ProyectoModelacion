import networkx as nx
import graph
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tktimepicker import SpinTimePickerModern
from tktimepicker import constants
from tkinter import messagebox


class MainWindow:

    m = tk.Tk()
    options_frame = Frame(m, width=200, height=500, padx=32)
    graph_frame = Frame (m, width=500, height=500)
    result_frame = Frame(m, bg="#ececec", height=200, width=500)
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
        
        self.config_open = False 

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
            self.config_open= False
            if hasattr(self, 'configs_frame'):
                self.configs_frame.pack_forget()
            if hasattr(self, 'options_frame'):
                self.options_frame.pack_forget()
            if hasattr(self, 'graph_frame'):
                self.graph_frame.pack_forget()
            if hasattr(self, 'result_frame'):
                self.result_frame.pack_forget()

            
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
            if newCalleJ.strip() != "":
                new_cod[0] = int(newCalleJ)
            if newCarreraJ.strip() != "":
                new_cod[1] = int(newCarreraJ)
            self.cood_Javier = tuple(new_cod)

            new_cod = list(self.cood_Andreina)
            if newCalleA.strip() != "":
                new_cod[0] = int(newCalleA)
            if newCarreraA.strip() != "":
                new_cod[1] = int(newCarreraA)
            self.cood_Andreina = tuple(new_cod)
            
            # Se valida que no esté vacío el nombre
            if self.nuevoLocal.get().strip() == "" and (newCalleL.strip() != "" and newCarreraL.strip() != ""):
                messagebox.showwarning("Input Error", "Por favor, ingrese un nombre para el nuevo local.")
                return

            # Se chequea la validez de las nuevas coordenadas
            if newCalleL.strip() != "" and newCarreraL.strip() != "":
                self.locales.append({"name": self.nuevoLocal.get(), "coordinates": (int(newCalleL), int(newCarreraL))})
                get_locales_options()
                messagebox.showinfo("Cambio guardado", "El nuevo local ha sido agregado con éxito.")
            if self.nuevoLocal.get().strip() != "" and newCalleL.strip() == "" and newCarreraL.strip() == "":
                messagebox.showwarning("Input Error", "Por favor, seleccione una calle y carrera para el nuevo local.")
            
            messagebox.showinfo("Cambio guardado", "Se han guardado los cambios sin éxito")


        def build_config():
            if not self.config_open:
                self.configs_frame = Frame(self.m, background="#C3B1E1", width=1000, height=500)

                self.configs_frame.pack(expand=True, fill="both")
                self.configs_frame.pack_propagate(0)
                self.options_frame.destroy()
                self.graph_frame.destroy()
                labelConfig = Label(self.configs_frame, text= "Configuración",  background="#C3B1E1")
                labelConfig.pack()
                labelJavier = Label(self.configs_frame, text="Dirección de Javier", background="#C3B1E1")
                labelJavier.pack()
                CallelabelJavier = Label(self.configs_frame, text="Calle de Javier", background="#C3B1E1")
                CallelabelJavier.pack()
                self.comboBoxCalleJ = ttk.Combobox(self.configs_frame,state="readonly", values=[50,51,52,53,54])
                self.comboBoxCalleJ.pack()
                CarreralabelJavier = Label(self.configs_frame, text="Carrera de Javier", background="#C3B1E1")
                CarreralabelJavier.pack()
                self.comboBoxCarreraJ = ttk.Combobox(self.configs_frame,state="readonly", values=[10,11,12,13,14], background="#C3B1E1")
                self.comboBoxCarreraJ.pack()
                labelJavier = Label(self.configs_frame, text="Dirección de Andreina", background="#C3B1E1")
                labelJavier.pack()
                CallelabelAndreina = Label(self.configs_frame, text="Calle de Andreina", background="#C3B1E1")
                CallelabelAndreina.pack()
                self.comboBoxCalleA = ttk.Combobox(self.configs_frame,state="readonly", values=[50,51,52,53,54], background="#C3B1E1")
                self.comboBoxCalleA.pack()
                CarreralabelAndreina = Label(self.configs_frame, text="Carrera de Andreina", background="#C3B1E1")
                CarreralabelAndreina.pack()
                self.comboBoxCarreraA = ttk.Combobox(self.configs_frame,state="readonly", values=[10,11,12,13,14], background="#C3B1E1")
                self.comboBoxCarreraA.pack()

                labelNuevoLocal = Label(self.configs_frame, text="Agregar Nuevo Local", background="#C3B1E1")
                labelNuevoLocal.pack()
                NombreLocal = tk.Entry(self.configs_frame, textvariable=self.nuevoLocal, background="#FFFFFF")
                NombreLocal.pack()
                CallelabelNuevo = Label(self.configs_frame, text="Calle de Nuevo Local", background="#C3B1E1")
                CallelabelNuevo.pack()
                self.comboBoxCalleNuevo = ttk.Combobox(self.configs_frame,state="readonly", values=[50,51,52,53,54], background="#C3B1E1")
                self.comboBoxCalleNuevo.pack()
                CarreralabelNuevo = Label(self.configs_frame, text="Carrera de Nuevo Local", background="#C3B1E1")
                CarreralabelNuevo.pack()
                self.comboBoxCarreraNuevo = ttk.Combobox(self.configs_frame,state="readonly", values=[10,11,12,13,14], background="#C3B1E1")
                self.comboBoxCarreraNuevo.pack()

                saveButton = Button(self.configs_frame, command=save_configs, text="Guardar Cambios", background="#C3B1E1")
                saveButton.pack()

            self.config_open = True



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
            nx.draw_networkx_edges(graph.G, pos, ax=ax)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, node_size=500, node_color="#FFDE21", edgecolors="#FFDE21")
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Andreina], node_color="#C3B1E1", node_size=500)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Javier], node_color="#89CFF0", node_size=500)
            nx.draw_networkx_labels(graph.G,pos, ax=ax, font_size=8, font_color="#000")
            nx.draw_networkx_edge_labels(graph.G,pos, edge_labels=labels, ax=ax, font_size=8)

            canvas = FigureCanvasTkAgg(fig, self.graph_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()

        def create_edge_list(path):
            list_edge=[]
            for node in range(len(path)-1):
                list_edge.append((path[node], path[node+1]))
            return list_edge

        def build_path_view(result):
            self.graph_frame = Frame (self.m, width=500, height=500)
            self.graph_frame.pack(side="left")

            path_edgesJ = create_edge_list(result["route_javier"])
            path_edgesA = create_edge_list(result["route_andreina"])
            labels = nx.get_edge_attributes(graph.G,"weight")
            pos = {(x,y):(y,-x) for x,y in graph.G.nodes()}
            fig = plt.Figure(figsize=(5,5)) 
            ax = fig.add_subplot()
            nx.draw_networkx_edges(graph.G, pos, ax=ax)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, node_size=500, node_color="#FFDE21", edgecolors="#FFDE21")
            nx.draw_networkx_edge_labels(graph.G,pos, edge_labels=labels, ax=ax, font_size=10)
            nx.draw_networkx_edges(graph.G, pos, edgelist=path_edgesJ, edge_color="#89CFF0", width=5, ax=ax)
            nx.draw_networkx_edges(graph.G, pos, edgelist=path_edgesA, edge_color="#C3B1E1", width=5, ax=ax)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Javier], node_color="#89CFF0", node_size=500)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.cood_Andreina], node_color="#C3B1E1", node_size=500)
            nx.draw_networkx_nodes(graph.G, pos, ax=ax, nodelist=[self.destination], node_color="#50C878", node_size=500)
            nx.draw_networkx_labels(graph.G,pos, ax=ax, font_size=10, font_color="#000")



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
            
            # leave_javier = "{}:{} {}".format(arrival_time[0], (arrival_time[1]-result["time_javier"]), arrival_time[2])
            # leave_andreina = "{}:{} {}".format(arrival_time[0], (arrival_time[1]-result["time_andreina"]), arrival_time[2])
            leave_javier = calculate_leave_time(arrival_time, result["time_javier"])
            leave_andreina = calculate_leave_time(arrival_time, result["time_andreina"])

            self.result_frame = Frame(self.m, height=500, width=200)
            self.resultText = Label(self.result_frame, text= "Javier tarda {} minutos en llegar\nJavier tiene que salir a las {}\nAndreina tarda {} minutos\nAndreina tiene que salir a las {}".format(result["time_javier"],leave_javier, result["time_andreina"], leave_andreina))
            self.resultText.pack()
            backButton = Button(self.result_frame, text="Reiniciar", command=restart)
            backButton.pack()
            self.options_frame.destroy()
            self.graph_frame.destroy()

            self.result_frame.pack(side="left", fill="y", padx=150, pady=150)
            build_path_view(result)
            
        def calculate_leave_time (arrival_time, trip_time):
            time = arrival_time[1]-trip_time
            print(time)

            if time < 0:
                if arrival_time[0] == 1:
                    return f"12:{60-(time*-1)} {arrival_time[2]}"
                elif arrival_time[0] == 12 and arrival_time[2] == "AM":
                    return f"11:{60-(time*-1)} PM"
                elif arrival_time[0] == 12 and arrival_time[2] == "PM":
                    return f"11:{60-(time*-1)} AM"
                else:
                    return f"{arrival_time[0]-1}:{60-(time*-1)} {arrival_time[2]}"
                    
            return f"{arrival_time[0]}:{(time)} {arrival_time[2]}"
            


            
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


    