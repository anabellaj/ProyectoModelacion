import networkx as nx

import matplotlib.pyplot as plt
import graph


def main():
    BogotaGraph = graph.Graph()
    result = BogotaGraph.determine_best_route((54,14), (52,13), (50,12))

    print("Javier se tarda {},\nAndreina se tarda {} \nLa suma de sus tiempos es {}".format(result["time_javier"], result["time_andreina"], result["time_total"]))

main()