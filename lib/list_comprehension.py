#!/usr/bin/env python3

# list_comprehension.py

def return_evens(num_list):
    """Returns a list of even numbers from num_list"""
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    """Adds an exclamation mark to each sentence in sentence_list"""
    return [sentence + "!" for sentence in sentence_list]
