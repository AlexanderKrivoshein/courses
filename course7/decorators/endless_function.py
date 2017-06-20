# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


def endless_function():
    print('I am endless')

    # Functions are objects!
    # Function can return a function.
    return endless_function


endless_function()()()()()()()()()()()()

x = endless_function()
print(x, x == endless_function)
