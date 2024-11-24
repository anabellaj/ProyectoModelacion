import networkx as nx

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


class Graph:

    G= nx.Graph()

    #constructor del Grafo, se genera la cuadrícula de la ciudad de Bogotá según las distancias en tiempo de Javier

    def __init__(self):
        self.G.add_nodes_from(((i, j) for i in range(50,55) for j in range(10,15)), weight=4)
        self.G.add_edges_from((((i, j), (pi, j)) for pi, i in nx.utils.pairwise(range(50,55)) for j in range(10,15)), weight=4)
        self.G.add_edges_from((((i, j), (i, pj)) for i in range(50,55) for pj, j in nx.utils.pairwise(range(10,15))), weight=4)

        for i in range(10,15):
            edge_modify = ((51, i),(51,i+1))
            nx.set_edge_attributes(self.G, {edge_modify: {"weight": 8}})

        for i in range(12,15):
            for j in range(50,55):
                edge_modify= ((j, i), (j+1, i))
                nx.set_edge_attributes(self.G, {edge_modify: {"weight": 6}})

    #función para mostrar el grafo

    def show_graph(self):
        labels = nx.get_edge_attributes(self.G,"weight")
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_edge_labels(self.G,pos, edge_labels=labels)
        nx.draw(self.G, pos)
        return figure(figsize=(5,5), dpi=100)

    #Encuentra los caminos más cortos desde dos origenes hasta un mismo destino, para el segundo origen elimina las aristas
    #usadas en el primero para evitar coincidencias en las rutas

    def shortest_paths(self,origin1, origin2, destination):
        path1 = nx.dijkstra_path(self.G, origin1, destination)
        time1 = nx.dijkstra_path_length(self.G, origin1, destination)
        auxG = self.G.copy()
        for i in range(0, len(path1)-1):
            auxG.remove_edge(path1[i], path1[i+1])
        path2 = nx.dijkstra_path(auxG, origin2, destination)
        time2 = nx.dijkstra_path_length(auxG, origin2, destination)
        return [path1, time1, path2, time2]
    
    #Analiza los dos escenarios si Javier sale sin restricciones o si Andreina sale sin restricciones para determinar la 
    #ruta más rápida para los dos

    #RETORNA UNA DICCIONARIO QUE TIENE: la ruta para Javier, la ruta para Andreina, el tiempo de Javier, el tiempo de Andreina, y el tiempo total

    def determine_best_route(self, originJ, originA, destination):
        #ruta si Javier no tiene restricciones
        best_route_javier = self.shortest_paths(originJ, originA, destination)
        time_andreina = best_route_javier[3]+(2*(len(best_route_javier[2])-1))
        best_route_javier[3]=max(time_andreina, 0)
        total_time_javier = best_route_javier[1]+time_andreina


        #ruta si Andreina no tiene restricciones
        best_route_andreina = self.shortest_paths(originA, originJ, destination)
        time_andreina=best_route_andreina[1]+(2*(len(best_route_andreina[0])-1))
        best_route_andreina[1]=max(time_andreina, 0)
        total_time_andreina = best_route_andreina[3]+time_andreina

        if(total_time_javier<total_time_andreina):
            
            return {"route_javier" : best_route_javier[0], 
                    "route_andreina": best_route_javier[2], 
                    "time_javier": best_route_javier[1], 
                    "time_andreina": best_route_javier[3], 
                    "time_total": total_time_javier}
        else:
            
            return {"route_javier" : best_route_andreina[0], 
                    "route_andreina": best_route_andreina[2], 
                    "time_javier": best_route_andreina[1], 
                    "time_andreina": best_route_andreina[3], 
                    "time_total": total_time_andreina}




        
