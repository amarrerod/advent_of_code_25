#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day9.py
@Time    :   2025/12/09 13:51:40
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Tuple, List
from itertools import combinations, pairwise
from shapely.geometry import Polygon, box


def parse_input(
    fname: str = "test.in",
) -> List[Tuple[int, int]]:
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()
    tiles = list([tuple(map(int, coords.split(",")))[::-1] for coords in content])
    return tiles


def print_theater(
    red_tiles: List[Tuple[int, int]],
    green_tiles: List[Tuple[int, int]],
    rows: int = 9,
    cols: int = 14,
):
    for i in range(rows):
        for j in range(cols):
            if (i, j) in red_tiles:
                print("#", end="")
            elif (i, j) in green_tiles:
                print("X", end="")
            else:
                print(".", end="")
        print()


def generate_combinations(tiles: List[Tuple[int, int]]):
    for (x, y), (z, t) in combinations(tiles, r=2):
        if x != z and y != t:
            area = (abs(x - z) + 1) * (abs(y - t) + 1)
            yield area


def generate_green_tiles(tiles: List[Tuple[int, int]]):
    poly = Polygon(tiles)
    max_area = -1
    for a, b in combinations(tiles, r=2):
        min_x, max_x = min(a[0], b[0]), max(a[0], b[0])
        min_y, max_y = min(a[1], b[1]), max(a[1], b[1])
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
        if area > max_area and poly.covers(box(min_x, min_y, max_x, max_y)):
            max_area = area

    return max_area


if __name__ == "__main__":
    red_tiles = parse_input(fname="input.in")
    print(red_tiles)
    print_theater(red_tiles, [])
    part_one = max(generate_combinations(red_tiles))
    print(part_one)
    part_two = generate_green_tiles(red_tiles)
    print(part_two)
