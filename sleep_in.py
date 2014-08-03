#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. 

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True

source - http://codingbat.com/prob/p173401
"""

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

if __name__ == "__main__":
    weekday = False
    vacation = False
    print("Today is a weekday: {0} and we're on vacation: {1} so we can sleep in? {2}."
        .format(weekday, vacation, sleep_in(weekday, vacation)))