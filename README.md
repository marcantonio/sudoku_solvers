$ python3 bench.py
v0: f0.0349s
v1: f0.0652s
v2: f0.0187s

Visualize:

``` python
colors = [
    'red',
    'green',
    'blue',
    'purple',
    'yellow',
    'orange',
    'white',
    'black',
    'gray',
]

from pyvis.network import Network
net = Network()
[net.add_node(node.vertex, label=f'{node.vertex}', color=colors[node.color-1]) for node in puzzle.graph.nodes]
for node in puzzle.graph.nodes:
    [net.add_edge(node.vertex, other) for other in node.connections.keys()]
#net.toggle_physics(False)
net.show('mm.html', notebook=False)
```
