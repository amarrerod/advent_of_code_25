#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day4.py
@Time    :   2025/12/04 15:36:09
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Set, Tuple


def parse_input(fname: str = "test.in"):
    rolls: Set[Tuple[int, int]] = set()
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()
    for i, line in enumerate(content):
        for j, char in enumerate(line.rstrip()):
            if char == "@":
                rolls.add((i, j))
    rows, cols = len(content), len(content[0].rstrip())
    return rolls, rows, cols


def is_accessible(
    roll: Tuple[int, int], rolls: Set[Tuple[int, int]], rows: int, cols: int
) -> bool:
    adjacent_rolls = 0
    i, j = roll
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for ni, nj in neighbours:
        (x, y) = (i + ni, j + nj)
        if x < 0 or x > rows:
            continue
        if y < 0 or y > cols:
            continue
        if (x, y) in rolls:
            adjacent_rolls += 1
    return adjacent_rolls < 4


def remove_amap(rolls: Set[Tuple[int, int]], rows: int, cols: int):
    to_remove = 1
    removed = 0
    while to_remove > 0:
        rolls_to_remove = list(
            filter(lambda roll: is_accessible(roll, rolls, rows, cols), rolls)
        )
        rolls -= set(rolls_to_remove)
        removed += len(rolls_to_remove)
        print(f"Can be removed: {len(rolls_to_remove)} --> Total: {removed}")
        to_remove = len(rolls_to_remove)
    return removed


if __name__ == "__main__":
    rolls, rows, cols = parse_input(fname="test.in")
    print(rolls, len(rolls), rows, cols)
    part_one = sum(is_accessible(roll, rolls, rows, cols) for roll in rolls)
    print(part_one)
    part_two = remove_amap(rolls, rows, cols)
    print(part_two)
