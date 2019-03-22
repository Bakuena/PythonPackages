def sum_array(array):
    return array[0] + sum_array(array[1:]) if array else 0
    '''Return sum of all items in array'''


def fibonacci(n):
    if n <= 1:
        return n

    else:
        return fibonacci(n- 1) + fibonacci(n- 2)

    '''Return nth term in fibonacci sequence'''



def factorial(n):
    if n<= 1:
        return n

    else:
        return n* factorial(n- 1)
    '''Return n!'''


def reverse(word):
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
    '''Return word in reverse'''
