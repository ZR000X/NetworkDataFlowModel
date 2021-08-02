nodes = []

class relship:
    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2
        pass

class node:
    def __init__(self, rel: list = [relship], addrs: list = [[0]], flow_h: float = 0, flow_v: float = -1, data = 0) -> None:
        self.rel = rel
        self.addrs = addrs
        self.flow_h = flow_h
        self.flow_v = flow_v
        self.data = data
        pass

    def update(self):
        self.data += 1
        pass





def props(n):
    print(n.rel,"\n", n.addrs,"\n" ,n.flow_h, "\n",n.flow_v, "\n",n.data)

n1 = node()

props(n1)