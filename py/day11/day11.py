#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day11.py
@Time    :   2025/12/11 11:30:17
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from collections import deque
import re

REGEX = r"^(?P<input>[a-z]+):\s+(?P<output>(?:[a-z]{3}(?:\s+|$))+)"


def parse_input(fname: str = "test.in"):
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    devices = {}
    for row in content:
        row = row.rstrip()
        if matches := re.findall(REGEX, row)[0]:
            devices[matches[0]] = matches[1].split(" ")
    return devices


def find_output_path(devices, start: str = "you", goal: str = "out") -> int:
    output_paths = 0
    to_visit = deque([start])
    visited = set([start])
    while to_visit:
        connection = to_visit.popleft()
        if connection == goal:
            output_paths += 1
        else:
            next_connections = filter(lambda n: n not in visited, devices[connection])
            to_visit.extend(next_connections)
    return output_paths


if __name__ == "__main__":
    devices = parse_input(fname="input.in")
    print(devices)
    part_one = find_output_path(devices)
    print(part_one)
