import pandas as pd

'''
Custom functions to help monkey do
'''

def glympse(x,width = 5):
    """
    :x is an object to glimpse at.
    :width is Width of output: defaults to 5.
    """

    # This is like a transposed version of print(): columns run down the page, and data runs across.
    # This makes it possible to see every column in a data frame.
    # 'Borrowed' from R

    print(f'Observations: {x.shape[0]}')
    print(f'Variables: {x.shape[1]}')
    
    # get length of the longest variable name
    c_len = max([len(c) for c in x.columns])
    c_len = '>'+str(c_len)
    
    ## loop and print over columns transposed
    for c in x.columns:
        c_name = c
        t_name = str(x[c].dtypes)
        xhead = list(x[c][:width])
        print(f"{format(c_name,c_len)}\t <{t_name}> \t{xhead} ")
    return
