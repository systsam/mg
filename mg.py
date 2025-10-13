#!/usr/bin/env python
# coding: utf-8

# In[1]:


### import math
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def f(x):
    return 3*x**2 - 4*x + 5


# In[3]:


f(3.0)


# In[4]:


xs = np.arange(-5, 5, 0.25) # range from -5 to 5, step .25
ys = f(xs) # applying function to set of x's to yield y's
plt.plot(xs,ys) # x = 3, y = 20 confirmed by graph


# In[5]:


h = 0.001
x = 3.0
f(x+h) # yields function output of x + h
(f(x+h) - f(x))/h # yields slope


# In[6]:


# more complex
a = 2.0
b = -3.0
c = 10.0
d = a*b + c
print(d)


# In[7]:


h = .0001

#inputs
a = 2.0
b = -3.0
c = 10.0

d1 = a*b + c
a += h
d2 = a*b + c
print('d1', d1)
print('d2', d2)
# function change per change in input a
print('slope', (d2 - d1)/h)


# In[8]:


h = .0001

#inputs
a = 2.0
b = -3.0
c = 10.0

d1 = a*b + c
b += h # change in b
d2 = a*b + c
print('d1', d1)
print('d2', d2)
# function change per change in input b
print('slope', (d2 - d1)/h)


# In[1]:


# value object data structure

class Value:

    def __init__(self, data, _children=(), _op='', label=''): # i think 'self' is used to tie specific data to class instances
        self.data = data # assigns argument to specific instance of self
        self.grad = 0.0
        self._prev = set(_children) # _children =() is an empty tuple turned into a 'set' within class
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data})" # print formatting

# use class operations to operate on class data
    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+') # essentially running a.__add__(b) -- a = self, b = other
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out
# magic methods link __add__, __mul__ to +, * respectively

a = Value(2.0, label='a')
b = Value(-3.0, label ='b')
c = Value(10.0, label ='c')
e = a*b; e.label = 'e'
d = e + c; d.label = 'd'
f = Value(-2.0, label='f')
L = d * f; L.label = 'L'
L
# (a.__mul__(b)).__add__(c) = a is the self who * other.data b > that value as self + other c
#d = (a.__add__(b)).__mul__(c)
#d


# In[10]:


L._prev # children values of d = a*b = 6 and c = 10
#c.data


# In[11]:


L._op


# In[2]:


from graphviz import Digraph

def trace(root):
    # builds set of nodes and edges in a graph
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        # for any value in graph, create rectangle ('record') node
        dot.node(name = uid, label = "{ %s | data %.4f | grad %.4f }" % (n.label, n.data, n.grad), shape='record')
        if n._op:
            # op node created when value is result of operation
            dot.node(name = uid + n._op, label = n._op)
            # connect
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        # connect n1 to op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot



# In[14]:


draw_dot(L) # showing value object progression to get argument


# In[ ]:


dd / dc = 1.0
dd / de = 1.0
d = c + e


# In[ ]:


L = d * f

dL/dd = ? f # d's cancel leaving L/d = f since L = d * f ?

f(x+h)-f(x))/h

((d+h)*f - d*f)/h
(d*f + h*f - d*f) / h
(h*f)/h
f


# In[12]:


f.grad = 4.0
d.grad = -2.0


# In[24]:


def lol():

    h = 0.001

    a = Value(2.0, label='a')
    b = Value(-3.0, label ='b')
    c = Value(10.0, label ='c')
    e = a*b; e.label = 'e'
    d = e + c; d.label = 'd'
    f = Value(-2.0, label='f')
    L = d * f; L.label = 'L'
    L1 = L.data

    a = Value(2.0, label='a')
    b = Value(-3.0, label ='b')
    c = Value(10.0 + h, label ='c')
    e = a*b; e.label = 'e'
    d = e + c; d.label = 'd'
    d.data
    f = Value(-2.0, label='f')
    L = d * f; L.label = 'L'
    L2 = L.data

    print((L2 - L1)/h) # showing the derivative of h?

lol()


# In[ ]:




