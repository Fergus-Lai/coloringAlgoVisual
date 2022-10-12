def greedyAlgorithm(colours, graph):
    for node in graph:  # Iterate Thorugh Nodes In Graph
        if node.colour != "":  # Skipping Node Colored
            continue
        usedColours = set()  # Storing color of nodes connected
        # Iterating Thorugh Nodes Storing Color
        for connectedNode in node.connected:
            usedColours.add(connectedNode.colour)
        # Iterate Thorugh List of Colours To Use and Choose First Colour Usable
        for colour in colours:
            if not colour in usedColours:
                node.colour = colour
                break
        # No Colour Available
        if node.colour == "":
            return None
    return graph
