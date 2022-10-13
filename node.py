class Node:
    def __init__(self, rect):
        self.colour = ""
        self.connected = []
        self.rect = rect

    def connectTo(self, b):
        self.connected.append(b)
        self.connected = [*set(self.connected)]

    @staticmethod
    def connect(a, b):
        a.connectTo(b)
        b.connectTo(a)
