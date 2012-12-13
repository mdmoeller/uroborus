#!/usr/bin/python

# Implements a B+ Tree with insertion and search only

class Node:
    """A node in a B+ Tree"""
    # For non-leaves:
    #   Need to always maintain that len(chld) == len(elmts) + 1
    #   elmts are keys, chld are Nodes
    # For leaves:
    #   Values are stored in elmts; chld = []
    def __init__(self, L = None, C = None, leaf = True, d = 3):
        self.elmts = [] if L is None else L
        self.chld = [] if C is None else C
        self.leaf = leaf
        self.d = d

    def search(self, key):
        """Returns the value, if an element with key 'key' exists"""

        if self.leaf:
            for e in self.elmts:
                if e[0] == key:
                    return e[1]
            return None

        for i in range(len(self.elmts)):
            if key < self.elmts[i]:   # THIS IS A BUG!!! SHOULD BE <, not <=
                return self.chld[i].search(key)

        return self.chld[-1].search(key)

    # ignoring d for right now.
    def insert(self, pair, root=False):
        # Don't recurse; just insert
        if self.leaf: 
            inserted = False
            for i in range(len(self.elmts)):
                if pair[0] < self.elmts[i][0]:
                    self.elmts.insert(i, pair)
                    inserted = True
                    break

            if not inserted:
                self.elmts.append(pair)

        # Need to recurse
        else: 
            # Find which subtree to recurse on
            for i in range(len(self.elmts)):
                correct_child = None
                if pair[0] < self.elmts[i]:
                    correct_child = self.chld[i]
                    break
            if correct_child is None:
                correct_child = self.chld[-1]

            # Recurse on that subtree, and incorporate a split
            #  if that subtree needed to do one.
            cc_ind = self.chld.index(correct_child)
            split = correct_child.insert(pair)
            if split:
                self.chld[cc_ind : cc_ind+1] = [split[0], split[2]]
                self.elmts.insert(cc_ind, split[1])

        # Check if we have to split at THIS level:

        # We do have to split:
        size = len(self.elmts)
        if size > self.d:

            cut = int(size / 2.0 + 0.5) # Cut evenly, with extra one on the left for odd size
            # print cut
            if self.leaf:
                left = Node(self.elmts[:cut], [], leaf=True, d = self.d)
                # print "left" + str(left)
                right = Node(self.elmts[cut:], [], leaf=True, d = self.d)
                # print "right" + str(right)
                key = right.elmts[0][0]  # Key only of left-most elmt of right cut
                return (left, key, right)
            else:
                left = Node(self.elmts[:cut-1], self.chld[:cut], leaf=False, d = self.d)
                right = Node(self.elmts[cut:], self.chld[cut:], leaf=False, d = self.d)
                key = self.elmts[cut-1]  # (already key only) from right-most of left cut
                return (left, key, right)

        # Don't need to split, just return
        else:
            return None
    

        

class BPT:
    head = None
    def __init__(self, order, FILE=None):
        """ Create a B+ Tree of given order, where order is max size of any node. Min node size is int(order/2)"""
        self.head = Node(d = order)
        
        # Allows you to input to the B+ Tree values from a file
        if FILE is not None:
            lines = FILE.readlines()
            for line in lines:
                self.add( int(line), str(int(line)) + "*" )
    
    def add(self, x, y=None):
        if y is not None:
            self.add((x,y))
        else:
            split = self.head.insert(x, root=True)

            if split:
                self.head = Node([split[1]], [split[0], split[2]], False, self.head.d)
            # self.print_tree()

    def search(self, x):
        return self.head.search(x)
