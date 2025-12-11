#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day10.py
@Time    :   2025/12/10 15:25:24
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import Tuple, List
from collections import namedtuple

import re

Entry = namedtuple("Entry", ["indicators", "buttons", "joltages"])

REGEX = r"^\[([.#]+)\]\s+((?:\([\d,]+\)\s*)+)\{([\d,]+)\}$"


def parse_input(fname: str = "test.in"):
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    entries: List[Entry] = []
    for row in content:
        row = row.rstrip()
        if match := re.search(REGEX, row):
            indicators = [0 if c == "." else 1 for c in match.group(1)]
            joltages = list(map(int, match.group(3).split(",")))
            raw_group_2 = match.group(2)
            structured = list(
                tuple(int(x) for x in s.split(","))
                for s in re.findall(r"\((.*?)\)", raw_group_2)
            )
            entries.append(Entry(indicators, structured, joltages))
    return entries


def configure(Entry) -> int:
    return 0


if __name__ == "__main__":
    entries = parse_input()
    print(entries)
