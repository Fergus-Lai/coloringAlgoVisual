class Node:
    def __init__(self):
        self.colour = ""
        self.connected = []

    def connectTo(self, b):
        self.connected.append(b)
        self.connected = [*set(self.connected)]

    @staticmethod
    def connect(a, b):
        a.connectTo(b)
        b.connectTo(a)
