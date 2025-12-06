#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day6.py
@Time    :   2025/12/06 08:49:36
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Tuple, List
import numpy as np


def parse_input(fname: str = "test.in") -> Tuple[np.ndarray, List[str]]:
    numbers = []
    operations = []
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    operations = content[-1].rstrip().split()
    numbers = np.asarray([list(map(int, row.split())) for row in content[:-1]]).T

    return numbers, operations


def part_two(fname: str = "test.in"):
    with open(Path(__file__).with_name(fname), "r") as file:
        content = [line for line in file.readlines()]

    operation = content[-1][0]
    rows, cols = len(content), len(content[0])
    results = []
    buffer: List[int] = []
    for j in range(cols - 1):
        row_content = "".join(content[i][j] for i in range(rows))
        next_operator = row_content[-1]
        if all(c == " " for c in row_content):
            # Time to operate
            results.append(do_the_math(buffer, operation))
            buffer.clear()
        else:
            buffer.append(int(row_content[:-1]))
        if next_operator not in (" ", operation):
            operation = next_operator
    if buffer:
        results.append(do_the_math(buffer, operation))
    return np.sum(results)


def do_the_math(numbers, operation: str) -> np.int32:
    if operation == "+":
        return np.sum(numbers)
    else:
        return np.prod(numbers)


if __name__ == "__main__":
    FILE = "input.in"
    numbers, operations = parse_input(fname=FILE)
    part_one = sum(do_the_math(n, op) for n, op in zip(numbers, operations))
    print(part_one)
    part_two_result = part_two(fname=FILE)
    print(part_two_result)
