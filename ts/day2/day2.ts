/**
*  @File    :   day2.ts
*  @Time    :   2025/12/02 14:24:00
*  @Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
*  @Version :   1.0
*  @Contact :   amarrerd@ull.edu.es
*  @License :   (C)Copyright 2025, Alejandro Marrero
*  @Desc    :   None
**/


import * as fs from 'fs';
import * as path from 'path';
import { start } from 'repl';

function readInput(fname: string = 'test.in'): [number, number][] {
    let ranges :  [number, number][] = [];
    const file_path = path.join(__dirname, fname);
    const lines = fs.readFileSync(file_path, 'utf-8').split(',');

    for (const line of lines) {
        const [start, end] = line.split('-');
        ranges.push([+start, +end]);

    }
    return ranges;
}


function invalids(start: number, end: number, regex: RegExp = /(.+)\1/): number {
    let total = 0;
    for (let i = start; i <= end; i++){
        const s = i.toString();
        const match = s.match(regex);
        if (match && match[0].length == s.length) {
            total += i;
        }
    }
    return total;
}




const ranges = readInput('input.in');
const part_one = ranges.reduce((acc, [start, end]) => acc + invalids(start, end), 0);
const re_part_two: RegExp = /^(.+)\1+$/
const part_two = ranges.reduce((acc, [start, end]) => acc + invalids(start, end, re_part_two), 0);
console.log(part_one, part_two);