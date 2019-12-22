#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Bryan"

import cProfile
import pstats
# import functools
import timeit


def profile_decorator(original_func):
    def inner_function(*args, **kwargs):

        cP = cProfile.Profile()  # cProfile object
        cP.enable()  # enables logging and recording
        original_func(*args, **kwargs)       # should be main() function
        cP.disable()
        cP.dump_stats('function_data')  # creates a file
        # cP.print_stats()
        ps = pstats.Stats('function_data')  # reads from file
        ps.sort_stats('cumtime')
        ps.print_stats()

        print("This is the inner function\n")

        return original_func(*args, **kwargs)

    return inner_function


# @profile_decorator
def read_movies(src):
    """Returns a list of movie titles"""
    print('\nReading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


# @profile_decorator
def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    if title in movies:
        return True
    # for movie in movies:
    #     if movie == title:
    #         return True
    return False


@profile_decorator
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()

        # if is_duplicate(movie, movies):
        if movie in movies:
            duplicates.append(movie)
    return duplicates


def timeit_helper(funct):
    """Part A:  Obtain some profiling measurements using timeit"""

    t = timeit.Timer(funct)
    x = t.repeat(repeat=7, number=3)
    averages_list = []

    for each in x:
        averages_list.append(each/3)

    print(averages_list)
    minimum = min(averages_list)

    print("\nBest time across 7 repeats of 3 " +
          "per repeat: {} sec".format(minimum))


# @profile_decorator
def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    # timeit_helper(main)
    main()
