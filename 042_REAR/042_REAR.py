'''
My solution to Rosalind Bioinformatics Problem 042

Title: Creating a Distance Matrix
Rosalind ID: REAR
Rosalind #: 042
URL: http://rosalind.info/problems/rear

Goal to return the minimum number of reversals necessary
to make two permutations equivalent.
'''

from itertools import groupby
from collections import OrderedDict
import numpy as np
from operator import itemgetter
import scipy.spatial.distance as ssd
import os


def startOrder(s1, s2):
    empty_dict = OrderedDict.fromkeys(s1)
    for i in xrange(1, len(empty_dict)+1):
        empty_dict[empty_dict.keys()[i-1]] = i

    seq = [0]
    for i in xrange(len(empty_dict)):
        seq.append(empty_dict[s2[i]])
    seq.append(11)

    return seq


def findBreaks(perm):
    breaks = []
    n = len(perm)
    for i in xrange(1, len(perm)):
        if abs(perm[i] - perm[i-1]) != 1:
            breaks.append(i)
    return breaks


def getStrips(seq):
    deltas = np.array([seq[i+1] - seq[i] for i in xrange(len(seq)-1)])
    increasing = list()
    decreasing = list()
    strips_dec = np.where(deltas == -1)[0]
    strips_inc = np.where(deltas == 1)[0]
    ranges = []
    for k, g in groupby(enumerate(strips_dec), lambda (i,x):i-x):
        group = map(itemgetter(1), g)
        decreasing.append((group[0], group[-1]+2))
    for k, g in groupby(enumerate(strips_inc), lambda (i,x):i-x):
        group = map(itemgetter(1), g)
        increasing.append((group[0], group[-1]+2))
    return increasing, decreasing



def reverse2_inc(perm, reversal):
    end = reversal[1]
    #print reversal
    rev_index = perm.index(perm[end-1]+1)
    if rev_index > end and perm[reversal[0] != 0]:
        start = reversal[0]
        rev_index = perm.index(perm[start]-1)
        perm[start:rev_index] = perm[start:rev_index][::-1]
    else:
        perm[(rev_index+1):end] = perm[(rev_index+1):end][::-1]
    return perm


def reverse2_dec(perm, reversal):
    start = reversal[0]
    tmp_perm = list(perm)
    index = tmp_perm.index(tmp_perm[start]+1)
    if index < tmp_perm[start]:
        end = reversal[1]
        tmp_2 = list(tmp_perm)
        tmp_2[start:index] = tmp_2[start:index][::-1]
        if len(findBreaks(tmp_2)) == len(findBreaks(tmp_perm)):
            index = perm.index(perm[end-1]-1)
            tmp_perm[(index+1):end] = tmp_perm[(index+1):end][::-1]
        else:
            tmp_perm = tmp_2
    else:
        end = reversal[1]
        tmp_2 = list(tmp_perm)
        tmp_2[start:index] = tmp_2[start:index][::-1]
        if len(findBreaks(tmp_2)) == len(findBreaks(tmp_perm)):
            index = perm.index(perm[end-1]-1)
            tmp_perm[(index+1):end] = tmp_perm[(index+1):end][::-1]
        else:
            tmp_perm[start:index] = tmp_perm[start:index][::-1]
    return tmp_perm

def next_min_perm(bks, new_perm, tmp_perm, incr):
    if not bks: # if bks is blank
        bks[len(findBreaks(new_perm))] = new_perm
    elif len(findBreaks(new_perm)) < min(bks):
        bks[len(findBreaks(new_perm))] = new_perm
    elif len(findBreaks(new_perm)) == min(bks) and new_perm not in bks.values():
        new_incr = "".join(['.', str(incr)])
        bks[float("".join([str(len(findBreaks(new_perm))), new_incr]))] = new_perm
        incr += 1
    return bks, incr
    

# separate duplicates of minimum number of breaks
def dup_perms(bks, perm, incr, strip, inc_or_dec):
    for st in strip:
        tmp_perm = list(perm) # perm -> test
        #print perm
        if inc_or_dec == "decreasing":
            new_perm = reverse2_dec(tmp_perm, st)
        elif inc_or_dec == "increasing":
            #print st[1]
            if st[1] != 12:
                new_perm = reverse2_inc(tmp_perm, st)
        elif abs(strip[1] - strip[2]) == 2:
            breaks = findBreaks(tmp_perm)
            new_perm = reverseBreaks(tmp_perm, breaks)
        bks, incr = next_min_perm(bks, new_perm, tmp_perm, incr)
    return bks, incr


### NEED TO UPDATE TO INCLUDE DISTANCE METRIC!!! ###

# see if where multiple instances of the lowest number of breaks
def consolidate_mins(bks):
    if not all(isinstance(n,int) for n in bks.keys()):
        #print "dups"
        tmp_dict = {}
        dist_dict ={}
        eucl_dict = {}

        # get indices of which elements are duplicates of the minimum
        indices = [i for i, x in enumerate(map(int, bks.keys())) if x == min(bks)]

        # get index of which one has the smallest 'distance'
        # checks both hamming and euclidean
        for i in indices:
            cur_dup_perm = bks[bks.keys()[i]]
            dist_dict[i] = rd_dist(cur_dup_perm, "hamming")
            eucl_dict[i] = rd_dist(cur_dup_perm, "euclidean")

        # if the index of the two distance metrics don't equal, run recursive reversal distance
        hamm_min = min(dist_dict, key = dist_dict.get)
        eucl_min = min(eucl_dict, key = eucl_dict.get)
        if hamm_min != eucl_min:
            hamm_revs = rd(bks[bks.keys()[hamm_min]], True)
            eucl_revs = rd(bks[bks.keys()[eucl_min]], True)
            if hamm_revs < eucl_revs:
                keep = hamm_min
            elif eucl_revs < hamm_revs:
                keep = eucl_min
            else:
                # default to hamming
                keep = hamm_min
        else:
            keep = min(dist_dict, key = dist_dict.get)

        new_key = bks.keys()[keep]
        bks = {int(new_key): bks[new_key]}
    return bks

def reverseStrips(perm, increasing, decreasing):
    bks = {}
    if not decreasing and not increasing:
        tmp_perm = list(perm)
        breaks = findBreaks(tmp_perm)
        new_perm = reverseBreaks(tmp_perm, breaks)
    elif decreasing:
        if len(decreasing) > 1:
            bks = {}
            incr = 2
            
            # separate duplicates of minimum number of breaks
            bks, incr = dup_perms(bks, perm, incr, strip = decreasing, inc_or_dec = "decreasing") 
            
            # quick check if reverse of a non-strip is better
            tmp_perm = list(perm)            
            breaks = findBreaks(tmp_perm)
            new_perm = reverseBreaks(tmp_perm, breaks)

            if len(findBreaks(new_perm)) <= min(bks):
                bks, incr = next_min_perm(bks, new_perm, tmp_perm, incr)
            
            # see if where multiple instances of the lowest number of breaks
            if(len(bks) > 1):
                bks = consolidate_mins(bks)
        else:
            tmp_perm = list(perm)
            new_perm = reverse2_dec(tmp_perm, decreasing[0])
            # initialize dictionary
            bks = {len(findBreaks(new_perm)): new_perm}
            
            # quick check if reverse of a non-strip is better
            tmp_perm = list(perm)            
            breaks = findBreaks(tmp_perm)
            new_perm = reverseBreaks(tmp_perm, breaks)

            incr = 2
            if len(findBreaks(new_perm)) <= min(bks): 
                bks, incr = next_min_perm(bks, new_perm, tmp_perm, incr)

            # see if where multiple instances of the lowest number of breaks
            if(len(bks) > 1):
                bks = consolidate_mins(bks)

    ###increasing block###
    else:
        if len(increasing) == 1 and increasing[0][1]-increasing[0][0] == 12:
            new_perm = list(perm)
        elif len(increasing) > 1:
            bks = {}
            incr = 2
            
            # separate duplicates of minimum number of breaks
            bks, incr = dup_perms(bks, perm, incr, strip=increasing, inc_or_dec = "increasing")
            
            # quick check if reverse of a non-strip is better
            tmp_perm = list(perm)            
            breaks = findBreaks(tmp_perm)
            new_perm = reverseBreaks(tmp_perm, breaks)
            
            # separate duplicates of minimum number of breaks
            bks, incr = next_min_perm(bks, new_perm, tmp_perm, incr)
            
            # see if where multiple instances of the lowest number of breaks
            bks = consolidate_mins(bks)
        else:
            bks = {}
            incr = 2
            tmp_perm = list(perm)
            if increasing[0][1] != 12:
                new_perm = reverse2_inc(tmp_perm, increasing[0])
                bks[len(findBreaks(new_perm))] = new_perm

            tmp_perm = list(perm)
            # quick check if reverse of a non-strip is better
            breaks = findBreaks(tmp_perm)
            new_perm = reverseBreaks(tmp_perm, breaks)
            
            # separate duplicates of minimum number of breaks
            bks, incr = next_min_perm(bks, new_perm, tmp_perm, incr)
            
            # see if where multiple instances of the lowest number of breaks
            bks = consolidate_mins(bks)
            
    if bks:
        return bks[min(bks)]
    else:
        return new_perm


def reverse(perm, reversal):
    start = reversal[0]
    end = reversal[1]
    perm[start:end] = perm[start:end][::-1]
    return perm


def reverseBreaks(perm, breaks):
    rev_dict = {}
    dist_dict ={}
    incr = 1
    for i in range(len(breaks)):
        for j in range(i+1, len(breaks)):
            old_perm = list(perm)
            new_perm = reverse(old_perm, [breaks[i],breaks[j]])
            if not rev_dict:
                rev_dict[len(findBreaks(new_perm))] = new_perm
            elif len(findBreaks(new_perm)) < min(rev_dict):
                rev_dict[len(findBreaks(new_perm))] = new_perm
            elif len(findBreaks(new_perm)) == min(rev_dict) and new_perm not in rev_dict.values():
                new_incr = "".join(['.', str(incr)])
                rev_dict[float("".join([str(len(findBreaks(new_perm))), new_incr]))] = new_perm
                incr += 1
    
    # get indices of which elements are duplicates of the minimum
    indices = [i for i, x in enumerate(map(int, rev_dict.keys())) if x == min(rev_dict)]

    # get index of which one has the smallest 'distance'
    for i in indices:
        cur_dup_perm = rev_dict[rev_dict.keys()[i]]
        dist_dict[i] = rd_dist(cur_dup_perm, "hamming")
    keep = min(dist_dict, key = dist_dict.get)
    new_key = rev_dict.keys()[keep]
    return rev_dict[new_key]

def rd_dist(new_perm, dist_metric):
    #some metric where
    # [0, 9, 8, 1, 2, 3, 4, 7, 5, 6, 10, 11]
    # is worse than
    # [0, 1, 2, 3, 8, 9, 4, 7, 5, 6, 10, 11] or [0, 3, 2, 1, 4, 9, 8, 7, 5, 6, 10, 11]
    # beta = 0.5
    goal = range(len(new_perm))
    # metric = ((beta**2 + 1) * ssd.hamming(goal, new_perm) * ssd.euclidean(goal, new_perm))/((beta**2) * ssd.hamming(goal, new_perm) + ssd.euclidean(goal,new_perm))
    # metric = ssd.hamming(goal, new_perm) + ssd.euclidean(goal, new_perm)
    if dist_metric == "hamming":
        metric = ssd.hamming(goal, new_perm)
    elif dist_metric == "euclidean":
        metric = ssd.euclidean(goal, new_perm)
        
    return metric


def reverseWrapper(new_perm):
    increasing, decreasing = getStrips(new_perm)
    if len(decreasing) == 1:
        if decreasing[0][1] - decreasing[0][0] == 2:
            # search for removing most breaks
            breaks = findBreaks(new_perm)
            new_perm = reverseBreaks(new_perm, breaks)
        else:
            new_perm = reverseStrips(new_perm, increasing, decreasing)
    elif len(decreasing) > 1:
        if len(decreasing) == 0 and len(increasing) == 2:
            if increasing[0][1] - increasing[0][0] == 2:
                breaks = findBreaks(new_perm)
                new_perm = reverseBreaks(new_perm, breaks)
            else:
                new_perm = reverseStrips(new_perm, increasing, decreasing)
        else:
            new_perm = reverseStrips(new_perm, increasing, decreasing)
    else:
        new_perm = reverseStrips(new_perm, increasing, decreasing)
    
    return new_perm


def rd(seq, recursive = False):
    count = 0
    new_perm = list(seq)
    while len(findBreaks(new_perm)) > 0:
        
        if len(findBreaks(new_perm)) == 11:
            orig_breaks = findBreaks(new_perm)
            tmp_perm = reverseBreaks(new_perm, findBreaks(new_perm))
            new_breaks = findBreaks(tmp_perm)
            if len(orig_breaks) - len(new_breaks) == 1:
                count = 9
                break
            else:
                new_perm = reverseWrapper(new_perm)
        else:
            new_perm = reverseWrapper(new_perm)

        count += 1
    return count


if __name__ == '__main__':

    # Read input data
    data = open(os.path.join(os.path.split(os.getcwd())[0], "data", "rosalind_rear.txt")).readlines()
    data = [x.rstrip('\n') for x in data]

    x_list = [ x.split(' ') for x in data[::3] ]
    y_list = [ x.split(' ') for x in data[1::3] ]

    # empty list for the needed size
    counts = [None] * len(x_list)

    for i in range( len( x_list ) ):
        final_count = rd(startOrder(x_list[i], y_list[i]))
        counts[i] = final_count
        #print final_count

    print ' '.join(map(str, counts))
    

