#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fillMissingBrackets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def fillMissingBrackets(s):
    # Write your code here
    def is_balanced(s):
        left_paren = 0
        left_square = 0
        question = 0
        for char in s:
            if char == '(':
                left_paren += 1
            elif char == ')':
                if left_paren > 0:
                    left_paren -= 1
                elif question >0 :
                    question -= 1
                else:
                    return False
            elif char == '[':
                left_square += 1
            elif char == ']':
                if left_square >0:
                    left_square -= 1
                elif question > 0:
                    question -= 1
                else:
                    return False
            elif char == '?':
                question += 1

        if left_paren + left_square <= question:
            return True
        
    n = len(s)
    count = 0
    for i in range(1, n):
        s1 = s[:i]
        s2 = s[i:]
        if is_balanced(s1) and is_balanced(s2):
            count += 1
    return count
    

        
print(fillMissingBrackets('(?]['))