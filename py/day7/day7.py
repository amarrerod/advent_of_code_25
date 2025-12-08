#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day6.py
@Time    :   2025/12/07 13:00:57
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Tuple, List, Set, Dict
from collections import deque, Counter
import time


def parse_input(
    fname: str = "test.in",
) -> Tuple[Tuple[int, int], List[Tuple[int, int]], Tuple[int, int]]:
    beam = (0, 0)
    splitters: List[Tuple[int, int]] = []
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    rows, cols = len(content), len(content[0])
    for i, row in enumerate(content):
        for j, c in enumerate(row.rstrip()):
            if c == "S":
                beam = (i, j)
            elif c == "^":
                splitters.append((i, j))

    return beam, splitters, (rows, cols)


def simulate(
    initial_beam: Tuple[int, int],
    splitters: List[Tuple[int, int]],
    rows: int,
    cols: int,
    verbose: bool = False,
) -> int:
    beams = deque([initial_beam])
    it = 1
    visited: Set[Tuple[int, int]] = set()
    n_splits = 0
    while beams:
        b = beams.popleft()
        if b in visited:
            continue
        visited.add(b)
        (x, y) = b
        next_position = (x + 1, y)
        children = [next_position]
        if next_position[0] > rows or (next_position[1] < 0 or next_position[1] > cols):
            continue
        if next_position in splitters:
            # Create two new beams and remove the parent
            children = [(x + 1, y - 1), (x + 1, y + 1)]
            n_splits += 1

        beams.extend(children)

        if verbose:
            print(f"Iteration: {it}, Splits: {n_splits}")
            print("=" * 20)
            print_manifold(initial_beam, visited, splitters, rows, cols)
            it += 1
            time.sleep(0.01)
    return n_splits


def simulate2(
    initial_beam: Tuple[int, int],
    splitters: List[Tuple[int, int]],
    rows: int,
    cols: int,
    verbose: bool = False,
) -> int:
    beams = deque([initial_beam])
    it = 1
    visited: Set[Tuple[int, int]] = set()
    n_splits = 0
    timelines: Counter = Counter()
    while beams:
        b = beams.popleft()
        timelines.update(b)
        if b in visited:
            continue
        visited.add(b)

        (x, y) = b
        next_position = (x + 1, y)
        children = [next_position]

        if next_position[0] > rows or (next_position[1] < 0 or next_position[1] > cols):
            continue
        if next_position in splitters:
            # Create two new beams and remove the parent
            children = [(x + 1, y - 1), (x + 1, y + 1)]
            n_splits += 1

        beams.extend(children)

        if verbose:
            print(f"Iteration: {it}, Splits: {n_splits}, Timelines: {len(timelines)}")
            print("=" * 20)
            print_manifold(initial_beam, visited, splitters, rows, cols)
            it += 1
            time.sleep(0.01)
    return n_splits


def print_manifold(
    initial_beam: Tuple[int, int],
    beams: Set[Tuple[int, int]],
    splitters: List[Tuple[int, int]],
    rows: int,
    cols: int,
):
    for i in range(rows):
        for j in range(cols):
            c = "."
            if (i, j) == initial_beam:
                c = "S"
            elif (i, j) in beams:
                c = "|"
            elif (i, j) in splitters:
                c = "^"
            print(c, end="")
        print("")


if __name__ == "__main__":
    beam, splitters, (rows, cols) = parse_input(fname="test.in")
    part_one = simulate(beam, splitters, rows, cols, False)
    print(part_one)
    part_two = simulate2(beam, splitters, rows, cols, True)
    print(part_two)
