import re
import random
import sys
import math
def recordbreak(score):
    max_score=score[0]
    min_score=score[0]
    max_count=0
    min_count=0
    for s in score[1:]:
        if s>max_score:
            max_score=s
            max_count +=1
        elif s<min_score:
            min_score=s
            min_count +=1
    return [max_count,min_count]
if __name__=='__main__':
    scores = list(map(int, input("Enter scores separated by space: ").split()))
    result=recordbreak(scores)
    print(result)