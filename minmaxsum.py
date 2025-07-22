import re
import random
import math
import sys
def minmaxsum(arr):
    total=sum(arr)
    minn=min(arr)
    maxx=max(arr)
    maxsum=total-maxx
    minsum=total-minn
    print(maxsum,minsum)
if __name__ == '__main__':

    arr = list(map(int, input("enter array").rstrip().split()))

    minmaxsum(arr)

