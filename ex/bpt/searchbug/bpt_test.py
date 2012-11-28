#!/usr/bin/python
import BPT_instrumented as bpt
target_module = bpt

#unit testing Node.search()
#searching in a leaf node
def searchLeaf(R):
    parent=bpt.Node(3)
    parent.leaf=False
    l_child=bpt.Node(3)
    r_child=bpt.Node(3)

    l_child.elmts=[(0,0),(3,3)]
    r_child.elmts=[(4,4),(7,7),(15,15)]

    parent.elmts=[4]
    parent.chld=[l_child,r_child]
    leaf_node=bpt.Node(3)
    leaf_node.elmts=[(0,0),(1,1),(2,2)]
    R.assertTrue(leaf_node.search(0)==0)
    R.assertTrue(leaf_node.search(1)==1)
    R.assertTrue(leaf_node.search(2)==2)
    R.assertTrue(parent.search(-1)==None)

#searching in a tree with a root node, its left and  right child nodes
def searchTree(R):
    parent=bpt.Node(3)
    parent.leaf=False
    l_child=bpt.Node(3)
    r_child=bpt.Node(3)  
    l_child.elmts=[(0,0),(3,3)]
    r_child.elmts=[(4,4),(7,7),(15,15)]
    parent.elmts=[4]
    parent.chld=[l_child,r_child]
    R.assertTrue(parent.search(0)==0 )
    R.assertTrue(parent.search(3)==3 )
    R.assertTrue(parent.search(4)==4 )
    R.assertTrue(parent.search(7)==7 )
    R.assertTrue(parent.search(15)==15 )
    R.assertTrue(parent.search(-1)==None)
    
#unit testing Node.insert()
def insertIntoLeaf(R):
    #insert without a node split
    leaf_node=bpt.Node(3)
    leaf_node.elmts=[(1,1)]
    leaf_node.insert((0,0)) #testing lines 50-56
    x=leaf_node.insert((2,2)) #testing lines 50-59
    R.assertTrue(x==None)

    #insert to test node split(testing lines 83-4)
    #leaf_node now has maximum occupancy now with 3 elements
    split=leaf_node.insert((3,3))
    R.assertTrue(split[1]==2)
    #new left child of leaf_node after split
    R.assertTrue(split[0].elmts[0]==(0,0))
    R.assertTrue(split[0].elmts[1]==(1,1))
    #new right child of leaf_node after split
    R.assertTrue(split[2].elmts[0]==(2,2))
    R.assertTrue(split[2].elmts[1]==(3,3))

def insertIntoTree(R):
    parent=bpt.Node(3)
    parent.leaf=False
    l_child=bpt.Node(3)
    r_child=bpt.Node(3)  
    l_child.elmts=[(0,0),(1,1)]
    r_child.elmts=[(3,3),(4,4),(5,5)]
    parent.elmts=[3]
    parent.chld=[l_child,r_child]
    #No split here. inserted into the left child
    R.assertTrue(parent.insert((2,2))==None) 
    #Split occurs as the leaf nodes are full
    parent.insert((6,6))
    R.assertTrue(parent.elmts[0]==3 and parent.elmts[1]==5)
    R.assertTrue(parent.chld[0].elmts[0]==(0,0))
    R.assertTrue(parent.chld[0].elmts[1]==(1,1))
    R.assertTrue(parent.chld[0].elmts[2]==(2,2))
    R.assertTrue(parent.chld[1].elmts[0]==(3,3))
    R.assertTrue(parent.chld[1].elmts[1]==(4,4))
    R.assertTrue(parent.chld[2].elmts[0]==(5,5))
    R.assertTrue(parent.chld[2].elmts[1]==(6,6))

#unit testing BPT.add()
def addToBPT(R): 
    tree=bpt.BPT(2)
    # tree.print_tree()
    for i in range(6):
        tree.add(i,i)
    # tree.print_tree()
    R.assertTrue(tree.head.elmts[0]==2)
    R.assertTrue(tree.head.elmts[1]==4)
    R.assertTrue(tree.head.chld[0].elmts[0]==(0,0))
    R.assertTrue(tree.head.chld[0].elmts[1]==(1,1))
    R.assertTrue(tree.head.chld[1].elmts[0]==(2,2))
    R.assertTrue(tree.head.chld[1].elmts[1]==(3,3))
    R.assertTrue(tree.head.chld[2].elmts[0]==(4,4))
    R.assertTrue(tree.head.chld[2].elmts[1]==(5,5))

#unit testing search using  BPT.search() and accessing fields
def searchBPT(R):
    mtree=bpt.BPT(2)
    # mtree.head.elmts = []
    # mtree.print_tree()

    for i in range(6):
        mtree.add(i, str(i) + '*')

    # mtree.print_tree()
    for i in range(6):
        R.assertTrue( mtree.search(i)==str(i) +'*')
