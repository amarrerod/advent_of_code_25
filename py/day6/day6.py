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
from typing import Set, Tuple, List
import numpy as np
import itertools


def parse_input(fname: str = "test.in") -> Tuple[np.ndarray, List[str]]:
    numbers = []
    operations = []
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    operations = content[-1].rstrip().split()
    numbers = np.asarray([list(map(int, row.split())) for row in content[:-1]]).T

    return numbers, operations


def parse_input_part_two(fname: str = "test.in") -> Tuple[np.ndarray, List[str]]:
    numbers = []
    operations = []
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    operations = content[-1].rstrip().split()[::-1]
    numbers = []
    for row in content[:-1]:
        row_with_zeros = row.rstrip().replace(" ", "0")
        numbers.append(row_with_zeros[::-1])
    max_columns = max(len(n) for n in numbers)
    rows = len(numbers)

    for i in range(len(numbers)):
        if len(numbers[i]) != max_columns:
            numbers[i] = "0" + numbers[i]

    right_numbers = []
    for i in range(max_columns):
        values = [n[i] for n in numbers]
        if all(v == "0" for v in values):
            continue
        else:
            right_numbers.append(int("".join(filter(lambda v: v != "0", values))))
    right_numbers = np.asarray(
        [right_numbers[i : i + rows] for i in range(0, len(right_numbers), rows)]
    )
    return right_numbers, operations


def do_the_math(numbers, operation: str) -> np.int32:
    r = 0
    if operation == "+":
        r = np.sum(numbers)
    else:
        r = np.prod(numbers)

    print(f"Numbers: {numbers}, Op: {operation} --> {r}")
    return r


if __name__ == "__main__":
    FILE = "input.in"
    numbers, operations = parse_input(fname=FILE)
    part_one = sum(do_the_math(n, op) for n, op in zip(numbers, operations))
    print(part_one)
    numbers, operations = parse_input_part_two(fname=FILE)
    part_two = sum(do_the_math(n, op) for n, op in zip(numbers, operations))
    print(part_two)
