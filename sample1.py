import networkx as nx
import copy as cp


G1 = nx.Graph()
G1.add_node("abb")
G1.add_node("abc")
nx.draw(G1)

G2 = cp.deepcopy(G1)
nx.draw(G2)

