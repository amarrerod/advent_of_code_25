#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day8.py
@Time    :   2025/12/08 18:30:01
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import List
from collections import namedtuple
import numpy as np

Distance = namedtuple("Distance", ["dist", "a", "b"])


def parse_input(
    fname: str = "test.in",
) -> np.ndarray:
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()

    points = np.asarray([list(map(int, row.split(","))) for row in content])
    return points


def calculate_distances(points: np.ndarray) -> List[Distance]:
    distances = []
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            distances.append(
                (
                    np.linalg.norm(points[i] - points[j]),
                    tuple(points[i]),
                    tuple(points[j]),
                )
            )
    distances.sort()
    return distances


def connect_junction_boxes(
    distances: List[Distance], n_connections: int, n_points: int
) -> int:
    circuits = []
    for i, (d, a, b) in enumerate(distances[:n_connections]):
        lens = [len(c) for c in circuits]
        sum_lens = sum(lens)
        print(
            f"Connection #{i + 1} A({a}), B({b}) -> {d}, ({len(circuits)},{sum_lens},{n_points - sum_lens})"
        )
        idx_a = next((i for i, c in enumerate(circuits) if a in c), None)
        idx_b = next((i for i, c in enumerate(circuits) if b in c), None)

        if idx_a is not None:
            circuits[idx_a].add(b)

            if idx_b is not None and idx_a != idx_b:
                # Both found, merge circuit
                circuits[idx_a].update(circuits[idx_b])
                circuits.pop(idx_b)

        elif idx_b is not None:
            circuits[idx_b].add(a)
        else:
            # Create a new circuit
            circuits.append({a, b})

    lens = sorted([len(c) for c in circuits], reverse=True)
    sum_lens = sum(lens)
    result = np.prod(lens[:3])
    print(
        f"We have {len(circuits)} circuits, of sizes: {lens} -> {sum_lens}. Result: {result}"
    )
    return result


def connect_until_merge(distances: List[Distance], n_points: int) -> int:
    circuits = []
    i = 0
    last_connection = []
    keep_connecting = True
    while keep_connecting:
        d, a, b = distances[i]
        idx_a = next((i for i, c in enumerate(circuits) if a in c), None)
        idx_b = next((i for i, c in enumerate(circuits) if b in c), None)

        if idx_a is not None:
            circuits[idx_a].add(b)
            if idx_b is not None and idx_a != idx_b:
                # Both found, merge circuit
                circuits[idx_a].update(circuits[idx_b])
                circuits.pop(idx_b)

        elif idx_b is not None:
            circuits[idx_b].add(a)
        else:
            # Create a new circuit
            circuits.append({a, b})

        i += 1
        if len(circuits) == 1 and len(circuits[0]) == n_points:
            last_connection = (a, b)
            keep_connecting = False

    result = last_connection[0][0] * last_connection[1][0]
    print(f"Last connection was: {last_connection}. Result: {result}")
    return result


if __name__ == "__main__":
    points = parse_input(fname="input.in")
    distances = calculate_distances(points)
    part_one = connect_junction_boxes(distances, n_connections=10, n_points=len(points))
    print(part_one)
    part_two = connect_until_merge(distances, n_points=len(points))
    print(part_two)
