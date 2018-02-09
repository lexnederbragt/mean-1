# make average of list
import numpy as np
def makeavg(num_list):
    if len(num_list) == 0:
        raise Exception("Cannot compute the mean value of an empty list")
    # assert len(num_list) > 0
    # only use assert if you cannot recover, else try to use exception
    else:
        return sum(num_list)/len(num_list)

'''
a = np.logspace(-10,1,11)
print(makeavg(a))

'''
