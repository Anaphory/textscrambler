#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random
import sys

letters = "abcdefghijklmnopqrstuvwxyzäöüßéłABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜÉŁ"
nonletters = " \t\n()[]\"',.;:–0123456789*/+-"

def scramble(word, front=1, end=1):
    word="".join(word)
    if len(word)>front+end:
        w = list(word[front:-end])
        random.shuffle(w)
        w = list(word[:front])+w+list(word[-end:])
        return "".join(w)
    else:
        return word

def obfuscate(text):
    newtext = ""
    word = []
    for l in text:
        if l in letters:
            word.append(l)
        else:
            if l not in nonletters:
                sys.stderr.write(l)
            if word:
                newtext += scramble(word)
                word = []
            newtext += l
    return newtext

for line in sys.stdin:
    print obfuscate(line)
        
