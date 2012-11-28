import BPT_instrumented as bpt
from RuntimeOracle import RuntimeOracle

R = RuntimeOracle("BPT_passfail.txt")
bpt.R=R

parent=bpt.Node(3)
parent.leaf=False
l_child=bpt.Node(3)
r_child=bpt.Node(3)

l_child.elmts=[(0,0),(3,3)]
r_child.elmts=[(4,4),(7,7),(15,15)]

parent.elmts=[4]
parent.chld=[l_child,r_child]
#unit testing Node.search()

R.assertTrue(parent.search(0)==0 )
R.assertTrue(parent.search(3)==3 )
R.assertTrue(parent.search(4)==4 )
R.assertTrue(parent.search(7)==7 )
R.assertTrue(parent.search(15)==15 )

#unit testing Node.insert()

l_child.insert((4,4)) 
lc=l_child.insert((1,1)) 
R.assertTrue( str(lc[2].elmts[0]) == (3,3))
R.assertTrue( str(lc[2].elmts[1]) == (4,4))
R.assertTrue( str(lc[0].elmts[0]) == (0,0))
R.assertTrue( str(lc[0].elmts[1]) == (1,1))

R.assertTrue( lc[1]==3)


parent=bpt.Node(2)
parent.leaf=False
parent.elmts=[3,5]
parent.chld=[bpt.Node([(1,1),(2,2)],[],d=2),bpt.Node([(3,3),(4,4)],[],d=2),bpt.Node([(5,5),(6,6)],[],d=2)]
parent.insert((7,7))
print parent.elmts[0]

# testing BPT.search()
tree=bpt.BPT(2)
tree.head=parent
for i in range(8)[1:]:
	R.assertTrue( tree.search(i)==i)

# testing BPT.add()
tree.add(0,0)
for i in range(8):
        R.assertTrue( tree.search(i)==i)
