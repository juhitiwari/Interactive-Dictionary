#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:14:52 2018

@author: slytherin
"""

import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))
def translate(word):
    
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word,data.keys())):
        yn=input("did you mean %s instead? press Y is yes or N if no" % get_close_matches(word, data.keys())[0] )
        if yn=="Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn=="N":
            return "word doesnt exist"
        else:
            return "we didnt understand your entry"
        
    else:
        return "word doesnt exist"
    
word = input("Enter word: ")
output =translate(word)
for item in output:
    print(item)
