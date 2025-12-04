#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   day3.py
@Time    :   2025/12/03 09:03:51
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2025, Alejandro Marrero
@Desc    :   None
"""

from pathlib import Path
from typing import List


def parse_input(fname: str = "test.in") -> List[str]:
    banks = []
    with open(Path(__file__).with_name(fname), "r") as file:
        content = file.readlines()
    for bank in content:
        banks.append(bank.rstrip())

    return banks


def max_joltage(bank: List[str]) -> int:
    current_jolt = 0
    joltages = ["0", "0"]
    MAX_POSSIBLE_JOLT = 99
    for i in range(len(bank) - 1):
        for j in range(i + 1, len(bank)):
            if bank[j] < joltages[1]:
                continue
            jolt = int(bank[i] + bank[j])
            print(f"{bank[i]}{bank[j]} --> {jolt} / {current_jolt}")
            if current_jolt < jolt:
                current_jolt = jolt
                joltages[0] = bank[i]
                joltages[1] = bank[j]
            if current_jolt == MAX_POSSIBLE_JOLT:
                return current_jolt
        joltages = ["0", "0"]
    return current_jolt


def max_joltage2(bank: str, length: int) -> str:
    if length == 0:
        return ""
    next_digit: str = max(bank[: len(bank) - length + 1])
    next_digit_pos: int = bank.find(next_digit)
    return next_digit + max_joltage2(bank[next_digit_pos + 1 :], length - 1)


if __name__ == "__main__":
    banks = parse_input(fname="input.in")
    print(banks)
    part_one = sum(int(max_joltage2(bank, length=2)) for bank in banks)
    print(part_one)
    part_two = sum(int(max_joltage2(bank, 12)) for bank in banks)
    print(part_two)
