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
    for c in x.columns:
        c_name = c
        t_name = x[c].dtypes
        xhead = list(x[c][:width])
        print(f'{c_name} <{t_name}> {xhead} ')
    return
