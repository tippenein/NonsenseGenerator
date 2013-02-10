#!/usr/bin/env python
'''
USE THIS TO CREATE YOUR OWN RAMBLING PARANOID NEWS FEED!
'''

import random

def makeNonsense(part1, part2, part3, n=10):
    """return n random sentences"""
    #convert to lists
    p1 = part1.split('\n')
    p2 = part2.split('\n')
    p3 = part3.split('\n')
    #shuffle the lists
    [ random.shuffle( p ) for p in [p1,p2,p3] ]
    #concatinate the sentences
    sentence = []
    for k in range(n):
        try:
            s = p1[k] + ' ' + p2[k] + ' ' + p3[k] 
            # THE LOUDER YOU YELL, THE RIGHTER YOU ARE!!
            s += '!!!'
            sentence.append(s)
        except IndexError:
            break
    return sentence

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# break a typical sentence into 3 parts
# first part of a sentence (subject)

#-----------------------------------------------
part1 = """\
The pope
The Military Industrial Complex
FEMA
HAARP
Flouride
Chemtrails
9/11"""

#-----------------------------------------------

# (action)
part2 = """\
is taking away
will take away
banned
censored
exposed"""

#-----------------------------------------------

# (object)
part3 = """\
Weaponized Babboons
your Freedom
your guns
your future"""


if __name__ == '__main__':
    for nonsense in makeNonsense(part1, part2, part3):
        print nonsense.upper()
