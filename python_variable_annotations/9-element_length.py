#!/usr/bin/env python3
"""
A type-annotated function that takes input lst and returns
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where the first element of a tuple is the
    length of the sequence and the second element is the sequence itself
    """
    return [(i, len(i)) for i in lst]
