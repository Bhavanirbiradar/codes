import re
import math
import random
import sys
def timeconversion(s):
    period=s[-2:]
    hour=int(s[:2])
    rest=s[2:-2]
    if period=="AM":
        if hour==12:
            hour=0
    else:
        if hour!=12:
            hour+=12
    return '{:02d}{}'.format(hour,rest)
if __name__== '__main__':
    sh=input("enter time")
    result=timeconversion(sh)
    print("the time is",result)