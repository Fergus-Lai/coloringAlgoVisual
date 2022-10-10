from node import Node


def greedyAlgorithm(colours, graph):
    for node in graph:
        if node.colour != "":
            continue
        usedColours = set()
        for connectedNode in node.connected:
            usedColours.add(connectedNode.colour)
        for colour in colours:
            if not colour in usedColours:
                node.colour = colour
                break
        if node.colour == "":
            return None
    return graph
