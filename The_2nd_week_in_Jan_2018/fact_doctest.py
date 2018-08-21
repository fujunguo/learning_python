def fact(n):
    """
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    >>> fact('abc')
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
