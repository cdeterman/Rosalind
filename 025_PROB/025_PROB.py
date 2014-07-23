
my_seq = 'ACGATACAA'
gc_array = [0.129,0.287,0.423,0.476,0.641,0.742,0.783]

prob = 1
for i in gc_array[0]:
    prob_gc = gc_array[i]/2
    prob_at = (1-gc_array[i])/2
    print prob_gc
    '''
    if my_seq[i] == 'A' or my_seq[i] == 'T'
        prob *= prob_at
    else:
        prob *= prob_gc
    '''

