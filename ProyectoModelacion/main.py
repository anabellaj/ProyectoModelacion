
import graph
import interface






def main():
    
    BogotaGraph = graph.Graph()
    result = BogotaGraph.determine_best_route((54,14), (52,13), (50,12))

    interface.MainWindow(BogotaGraph.G)
    




main()