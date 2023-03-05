#!/bin/python3
'''
'''


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest

    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    ixs = 0
    iys = 0
    ret = []
    while ixs < len(xs) and iys < len(ys):
        if cmp(xs[ixs], ys[iys]) == -1:
            ret.append(xs[ixs])
            ixs += 1
        else:
            ret.append(ys[iys])
            iys += 1

    while ixs < len(xs):
        ret.append(xs[ixs])
        ixs += 1

    while iys < len(ys):
        ret.append(ys[iys])
        iys += 1

    return ret


def merge_sorted(xs, cmp=cmp_standard):
    '''
    '''

    if len(xs) == 0 or len(xs) == 1:
        return xs
    else:
        mid = len(xs)//2
        left_half = xs[mid:]
        right_half = xs[:mid]
        left_sorted = merge_sorted(left_half, cmp=cmp)
        right_sorted = merge_sorted(right_half, cmp=cmp)
        return _merged(left_sorted, right_sorted, cmp=cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    '''
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs) // 2
        pivot = xs[mid]
        xs_lt = [x for x in xs if cmp(x, pivot) == -1]
        xs_gt = [x for x in xs if cmp(x, pivot) == 1]
        xs_eq = [x for x in xs if cmp(x, pivot) == 0]
        xs_lt = quick_sorted(xs_lt, cmp=cmp)
        xs_gt = quick_sorted(xs_gt, cmp=cmp)
        return xs_lt + xs_eq + xs_gt


def quick_sort(xs, cmp=cmp_standard):
    '''
    '''
