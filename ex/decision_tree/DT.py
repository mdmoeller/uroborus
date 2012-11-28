#!/usr/bin/python

import math
import sys

def leaf( y ):
    def fun( x ):
        return y
    return fun

def learned_tree( X, Y ):


    n = len(X)
    if n != len(Y) or n == 0:
        print "Error: Input vectors must have same (non-zero) size!"
        return None

    m = len(X[0])

    if m == 0:
        print "Error: Nullary dataset not allowed."
        return None

    for x in X:
        if len(x) != m:
            print "Error: Not all vectors in input are " + str(m) + "-ary"
            return None
    

    # Check if all the y's are the same (we can leaf!)
    pure = True
    for y in Y:
        if y != Y[0]:
            pure = False
            break
    
    if pure:
        return leaf( Y[0] )


    # Compute entropy for Y
    y_count = {}
    for y in Y:
        if y in y_count.keys():
            y_count[y] += 1
        else:
            y_count[y] = 1

    # H is entropy(Y)
    H = 0 
    for y in Y:
        H -= (y_count[y]/float(n)) * (0 if y_count[y] == 0 else math.log( (y_count[y]/float(n)), 2 ))


    # Look for the attribute and threshold to split the tree on
    best_IG = -1
    split_on_attr = -1
    best_thresh = -1

    for j in range(m): # Every attribute (i.e. column j in X)

        L = []
        for x in X: # Find all the thresholds between them
            if x[j] not in L:
                L.append(x[j])

        L = sorted(L)
        # print "L: ", L, " for: ", j
        # sys.exit(0)

        for i in range(len(L)-1):
            thresh = (L[i] + L[i+1]) / 2.0

            # print "THRESH: ", thresh

            # Count the y's on each side of the threshold
            y_for_x_lt = {}
            y_for_x_gt = {}
            tot_lt = 0
            tot_gt = 0
            for y in Y:
                y_for_x_lt[y] = 0
                y_for_x_gt[y] = 0

            for k in range(n):
                if X[k][j] <= thresh:
                    tot_lt += 1
                    y_for_x_lt[Y[k]] += 1
                else:
                    tot_gt += 1
                    y_for_x_gt[Y[k]] += 1

            # print "Y_gt:", y_for_x_gt, "\nY_lt:", y_for_x_lt, "\n\n"


            # find info gained for this attribute j, and this threshold thresh
            HY_X = 0 # Entropy H(Y|X=x)
            for xi in X:
                for yj in Y:
                    if xi <= thresh:
                        HY_X -= 0 if y_for_x_lt[yj] == 0 else math.log(y_for_x_lt[yj]/float(tot_lt),2) / float(n**2)
                    else:
                        HY_X -= 0 if y_for_x_gt[yj] == 0 else math.log(y_for_x_gt[yj]/float(tot_gt),2) / float(n**2)


            IG = H - HY_X

            if IG > best_IG:
                best_IG = IG
                split_on_attr = j
                best_thresh = thresh


    # print "Best Thresh: ", best_thresh, "\nSplit on: ", split_on_attr, "\n\n"

    lowX = []
    lowY = []
    highX = []
    highY = []
    for i in range(n):
        if X[i][split_on_attr] <= best_thresh:
            lowX.append(X[i])
            lowY.append(Y[i])
        else:
            highX.append(X[i])
            highY.append(Y[i])
    
    lowFn = learned_tree( lowX, lowY )
    highFn = learned_tree( highX, highY )

    def branch( x ):
        if x[split_on_attr] <= best_thresh:
            return lowFn(x)
        else:
            return highFn(x) 

    return branch

# h = learned_tree( [[0],[1]], [0,1] )

# print h([0]), h([1]), h([0.25]), h([0.75]), h([0.5])


# h = learned_tree( [[2,5],[6,2],[1,1],[7,6]], [1,1,0,0] )

# h = learned_tree( [[1,9],[1,5],[2,1],[3,3],[8,2],[4,5],[3,7],[6,5],[8,3],[10,5],[8,8],[5,10],[10,10]], 5*['*']+4*['x']+4*['T'] )
# 
# line = sys.stdin.readline()
# while line != "\n":
    # sp = line.split()
    # print "h= ", h( [float(sp[0]), float(sp[1])] )
    # line = sys.stdin.readline()
