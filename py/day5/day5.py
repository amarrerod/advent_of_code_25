#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day5.py
@Time    :   2025/12/05 12:44:16
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Set, Tuple, List


def parse_input(fname: str = "test.in") -> Tuple[List[Tuple[int, ...]], Set[int]]:
    available: Set[int] = set()
    with open(Path(__file__).with_name(fname), "r") as file:
        fresh_raw, available_raw = file.read().split("\n\n")

    fresh: List[Tuple[int, ...]] = list(
        tuple(map(int, f.split("-"))) for f in fresh_raw.splitlines()
    )
    fresh.sort()
    available = set(int(i) for i in available_raw.splitlines())
    return (fresh, available)


def is_available_and_fresh(available: int, fresh: List[Tuple[int, ...]]) -> bool:
    for start, end in fresh:
        if start <= available <= end:
            return True

    return False


def how_many_are_considered_fresh(fresh: List[Tuple[int, ...]]) -> int:
    sorted_fresh = sorted(fresh)
    counter = 0
    max_counter = 0
    for start, end in sorted_fresh:
        if end >= max_counter:
            counter += (end - max(start, max_counter)) + 1
            max_counter = end + 1
    return counter


if __name__ == "__main__":
    fresh, available = parse_input(fname="input.in")
    part_one = sum(is_available_and_fresh(av, fresh) for av in available)
    print(part_one)
    part_two = how_many_are_considered_fresh(fresh)
    print(part_two)
