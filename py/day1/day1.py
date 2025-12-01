#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day1.py
@Time    :   2025/12/01 15:37:02
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Tuple, List
import re


def read_input(fname: str = "day1/test.in") -> List[Tuple[str, int]]:
    rotations = []
    with open(Path(__file__).with_name(fname)) as file:
        lines = file.readlines()

    for line in lines:
        if match := re.match(r"([LR])(\d+)", line.rstrip()):
            rotations.append((match[1], int(match[2])))
    print(rotations)
    return rotations


def calculate_password(
    rotations: List[Tuple[str, int]], initial_position: int = 50
) -> int:
    MAX_CLICKS = 100
    left_at_zero = 0
    times_at_zero = 0
    position = initial_position
    for orientation, clicks in rotations:
        print(
            f"Position: {position}, Orientation: {orientation}, Clicks: {clicks}, Next Position:",
            end="",
        )
        prev_position = position
        if orientation == "L":
            position = prev_position - clicks
            times_at_zero += (prev_position - 1) // MAX_CLICKS - (
                position - 1
            ) // MAX_CLICKS
        else:
            position = prev_position + clicks
            times_at_zero += position // MAX_CLICKS - prev_position // MAX_CLICKS
        print(f" {position}")
        if position % MAX_CLICKS == 0:
            left_at_zero += 1

    return left_at_zero, times_at_zero


if __name__ == "__main__":
    rotations = read_input(fname="input.in")
    passwd = calculate_password(rotations)
    print(f"The password is: {passwd}")
