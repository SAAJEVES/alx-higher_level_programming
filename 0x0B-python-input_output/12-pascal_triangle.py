#!/usr/bin/python3

'''function that returns a list of lists of 
integers representing the Pascal’s triangle of n'''

def pascal_triangle(n):
    '''Pascal's triangle of n

    Args:
        n: the power
    
    Returns:
        a lists of lists of integers representing 
        Pascal's triangle of n
    '''
    if (n <= 0):
        return []
    
    array = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = array[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        array.append(row)
    return array
