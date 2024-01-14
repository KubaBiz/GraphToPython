import networkx as nx
import copy as cp


G1 = nx.Graph()
G1.add_node("abb")
G1.add_node("abc")
G2 = cp.deepcopy(G1)
