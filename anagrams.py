#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line utility that accepts a word file and prints a dictionary of
anagrams for that file.

Module provides a function find_anagrams which can be used to do the same
for an arbitrary list of strings.
"""

import sys

# Your name here, and any other people/sources who helped.
# Give credit where credit is due.
__author__ = "katran009"


def alphabetize(string):
    """Returns alphabetized version of the string"""
    return "".join(sorted(string.lower()))


# def alphabetize(word):
#     """Returns word in alphabetical order."""
#     t = list(word)
#     t.sort()
#     t = ''.join(t)
#     return t


# def find_anagrams(words):
#     """
#     Returns a dictionary with keys that are alphabetized words and values
#     that are all words that, when alphabetized, match the key.
#     Example:
#     {'dgo': ['dog'], 'act': ['cat', 'act']}
#     """
#     anagrams = {}
#     alphabetize(word):
#         for w in words
#             if alphabetize(w) == alphabetize(word)
#         for word in words:
#     return anagrams

def find_anagrams(words):
    """
    Returns a dictionary with keys that are alphabetized words and values
    that are all words that, when alphabetized, match the key.
    Example:
    {'dgo': ['dog'], 'act': ['cat', 'act']}
    """
    anagrams = {}
    for w in words:
        s = alphabetize(w)
        if s not in anagrams:
            anagrams[s] = [w]
        else:
            anagrams[s].append(w)
    return anagrams


def main(args):
    # run find_anagrams() on first argument filename
    if len(args) < 1:
        print("Please specify a word file!")
        sys.exit(1)

    with open(args[0]) as f:
        words = f.read().split()
    anagram_dict = find_anagrams(words)
    for k, v in anagram_dict.items():
        print("{} : {}".format(k, v))


if __name__ == "__main__":
    main(sys.argv[1:])
