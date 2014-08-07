from collections import OrderedDict

#s1 = [3, 10, 8, 2, 5, 4, 7, 1, 6, 9]
#s2 = [5, 2, 3, 1, 7, 4, 10, 8, 6, 9]
s1 = range(1,11)
s2 = [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]



empty_dict = OrderedDict.fromkeys(s1)
for i in xrange(1, len(empty_dict)+1):
    empty_dict[empty_dict.keys()[i-1]] = i

new_s2 = []
for i in xrange(len(empty_dict)):
    new_s2.append(empty_dict[s2[i]])


def findBreaks(perm):
    breaks = []
    n = len(perm)
    for i in xrange(len(perm)):
        if i == 0 and perm[i] != 1:
            breaks.append(0)
        elif abs(perm[i-1] - perm[i]) != 1:
            breaks.append(i)
    return breaks

def reverse(perm, reversal):
    start = reversal[0]
    end = reversal[1]
    perm[start:end] = perm[start:end][::-1]
    return perm

def bestReversals(perm, brakes):

    def findDiff(perm, brakes):
        old_s2 = list(perm)
        brake_list = {}
        for i in range(len(brakes)):
            for j in range(i+1, len(brakes)):
                perm = list(old_s2)
                perm[brakes[i]:brakes[j]] = perm[brakes[i]:brakes[j]][::-1]
                brake_list[str(brakes[i])+str(brakes[j])] = findBreaks(perm)
        return brake_list
    brake_list = findDiff(perm, brakes)

    # if multiple options of minimum length run each and see if improve
    new_brakes = []
    brakes_lens = map(len, brake_list.values())
    min_brakes = min(brakes_lens)
    if brakes_lens.count(min_brakes) > 1:
        tmp_brakes = []
        for key, value in brake_list.iteritems():
            if len(value) == min_brakes:
                tmp_brakes.append(value)
        tmp_dict = {}
        brakes_dict = {}
        for i in tmp_brakes:
            inner_brake_list = findDiff(perm, i)
            diff = list(set(brakes)-set(min(inner_brake_list.values(), key=len)))
            tmp_dict[len(diff)] = i
            brakes_dict[len(diff)] = inner_brake_list
        new_brakes = tmp_dict[min(tmp_dict)]
        for key, value in brake_list.iteritems():
            if value == new_brakes:
                diff = map(int, list(key))
    else:
        diff = list(set(brakes)-set(min(brake_list, key=len)))
    if not new_brakes:
        brakes_lens = map(len, brake_list.values())
        min_brakes = min(brakes_lens)
        for key, value in brake_list.iteritems():
            if len(value) == min_brakes:
                new_brakes = value
    return diff, new_brakes


def countReversals(perm):
    breaks = findBreaks(perm)
    reversal, new_breaks = bestReversals(perm, breaks)
    perm = reverse(perm, reversal)
    n = len(new_breaks)
    count = 1
    while n != 1:
        reversal, new_breaks = bestReversals(perm, new_breaks)
        perm = reverse(perm, reversal)
        n = len(new_breaks)
        count += 1
    return count

print countReversals(new_s2)
