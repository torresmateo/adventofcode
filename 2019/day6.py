class Node(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.distance = 0

    def __repr__(self):
        return self.name

def compute_distance(node):
    for c in node.children:
        c.distance = node.distance+1
        compute_distance(c)

def get_path_to_root(node):
    path = [node]
    n = node
    while n.parent is not None:
        path.append(n.parent)
        n = n.parent
    return path

nodes={}
for line in open('day6.test2'):
    a, b = line.strip().split(')')
    if a not in nodes.keys():
        nodes[a] = Node(a)
    if b not in nodes.keys():
        nodes[b] = Node(b)
    nodes[a].children.append(nodes[b])
    nodes[b].parent = nodes[a]

count = 0
for n in nodes.values():
    if n.parent is None:
        compute_distance(n)
        print(f'{n.name} is a root node')       

print('part1', sum([n.distance for n in nodes.values()]))

p_me = set(get_path_to_root(nodes['YOU']))
p_santa = set(get_path_to_root(nodes['SAN']))

lca = len(p_me & p_santa)
print('part2', nodes['YOU'].distance +nodes['SAN'].distance - 2*lca)