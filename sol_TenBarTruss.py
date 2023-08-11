import math
import numpy
class Node:
    def __init__(self, x, y, node_id):
        self.x = x
        self.y = y
        self.node_id = node_id

node1 = Node(18.28, 9.14, 1)
node2 = Node(18.28, 0, 2)
node3 = Node(9.14, 9.14, 3)
node4 = Node(9.14, 0, 4)
node5 = Node(0, 9.14, 5)
node6 = Node(0, 0, 6)

class Element:
    def __init__(self, nodei, nodej, r):
        self.nodei = nodei
        self.nodej = nodej
        self.E = 200
        self.A = math.pi*(r**2)
        self.L = math.sqrt((nodei.x-nodej.x)**2+(nodei.y-nodej.y)**2)
        self.cos = (nodej.x-nodei.x)/self.L
        self.sin = (nodej.y-nodei.y)/self.L
        c = self.cos
        s = self.sin
        k = numpy.array([[c**2, c*s, -c**2, -c*s], [c*s, s**2, -c*s, -s**2], [-c**2, -c*s, c**2, c*s], [-c*s, -s**2, c*s, s**2]])
        self.k = k

r1 = 10
r2 = 15

element1 = Element(node3, node5, r1)
element2 = Element(node1, node3, r1)
element3 = Element(node4, node6, r1)
element4 = Element(node2, node4, r1)
element5 = Element(node3, node4, r1)
element6 = Element(node1, node2, r1)
element7 = Element(node4, node5, r2)
element8 = Element(node3, node6, r2)
element9 = Element(node2, node3, r2)
element10 = Element(node1, node4, r2)

elements = [element1, element2, element3, element4, element5, element6, element7, element8, element9, element10]

for i in range(10):
    print(elements[i].k)

K = numpy.zeros((12,12))
for i in range(10):
    a = elements[i].nodei.node_id*2-1
    b = elements[i].nodej.node_id*2-1
    
    k_temp  = elements[i].k
    K[a-1:a+1, a-1:a+1] = K[a-1:a+1, a-1:a+1]+ k_temp[0:2, 0:2]
    K[a-1:a+1, b-1:b+1] = K[a-1:a+1, b-1:b+1]+ k_temp[0:2, 2:4]
    K[b-1:b+1, a-1:a+1] = K[b-1:b+1, a-1:a+1]+ k_temp[2:4, 0:2]
    K[b-1:b+1, b-1:b+1] = K[b-1:b+1, b-1:b+1]+ k_temp[2:4, 2:4]
    print("K now:")
    print(K)

print(K)
