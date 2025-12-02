#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day2.py
@Time    :   2025/12/02 13:24:36
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
import re
from typing import List, Tuple


def parse_input(fname: str = "test.in") -> List[Tuple[int, int]]:
    ranges = []
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readline().split(",")
    for rid in content:
        start, end = rid.split("-")
        ranges.append((int(start), int(end)))

    return ranges


def invalids(start: int, end: int, regex: str = r"(.+)\1") -> int:
    total = 0
    for i in range(start, end + 1):
        s = str(i)
        match = re.match(regex, s)
        if match and len(match.group(0)) == len(s):
            total += i

    return total


if __name__ == "__main__":
    ranges = parse_input(fname="input.in")
    part_one: int = sum(invalids(start, end) for start, end in ranges)
    re_two = r"^(.+)\1+$"
    part_two: int = sum(invalids(start, end, regex=re_two) for start, end in ranges)
    print(part_one, part_two)
