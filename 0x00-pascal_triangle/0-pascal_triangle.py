#!/usr/bin/python3
'''
pascal_triangle module

'''


def pascal_triangle(n):
    '''
    pascal_triangle function

    int n: number of rows (height of the triangle n>=0)
    return: list of lists of integers

    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], ...]
    '''

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[-1]
        """
        Another possible aproach:
          - using symmetry of the triangle
                mid = i // 2
        """

        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
