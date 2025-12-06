/**
 *  @File    :   day4.ts
 *  @Time    :   2025/12/04 16:08:13
 *  @Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
 *  @Version :   1.0
 *  @Contact :   amarrerd@ull.edu.es
 *  @License :   (C)Copyright 2025, Alejandro Marrero
 *  @Desc    :   None
 **/

import * as fs from "fs";
import * as path from "path";

const toKey = (r: number, c: number): string => `${r},${c}`;

const fromKey = (k: string): [number, number] => {
  const parts = k.split(",").map(Number);
  return [parts[0], parts[1]];
};

function readInput(fname: string = "test.in"): [Set<string>, number, number] {
  let rolls: Set<string> = new Set();
  const file_path = path.join(__dirname, fname);
  const lines = fs.readFileSync(file_path, "utf-8").split("\n");
  lines.forEach((line, i) => {
    line = line.trimEnd();
    line.split("").forEach((char, j) => {
      if (char === "@") {
        rolls.add(toKey(i, j));
      }
    });
  });
  const rows = lines.length;
  const cols = lines[0].trim().split("").length;
  return [rolls, rows, cols];
}

function is_accessible(
  roll: string,
  rolls: Set<string>,
  rows: number,
  cols: number
): boolean {
  let adjacent_rolls: number = 0;
  const [i, j] = fromKey(roll);
  const neighbours: [number, number][] = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1],
  ];
  for (const [ni, nj] of neighbours) {
    const [x, y] = [i + ni, j + nj];

    if (x < 0 || x > rows) continue;
    if (y < 0 || y > cols) continue;
    if (rolls.has(toKey(x, y))) {
      adjacent_rolls += 1;
    }
  }
  return adjacent_rolls < 4;
}

function remove_amap(rolls: Set<string>, rows: number, cols: number): number {
  let to_remove = 1;
  let removed = 0;
  while (to_remove > 0) {
    const rolls_to_remove = [...rolls].filter((r) =>
      is_accessible(r, rolls, rows, cols)
    );
    removed += rolls_to_remove.length;
    to_remove = rolls_to_remove.length;
    rolls_to_remove.forEach((r) => rolls.delete(r));
  }
  return removed;
}

const [rolls, rows, cols] = readInput("input.in");
const part_one = [...rolls].reduce((acc, roll) => {
  const value = is_accessible(roll, rolls, rows, cols) ? 1 : 0;
  return acc + value;
}, 0);

const part_two = remove_amap(rolls, rows, cols);
console.log(part_one, part_two);
