

import * as fs from 'fs';
import * as path from 'path';

function readInput(fname: string = 'test.in'): [string, number][] {
    let rotations :  [string, number][] = [];
    const file_path = path.join(__dirname, fname);
    const lines = fs.readFileSync(file_path, 'utf-8').split('\n');
    for (const line of lines) {
        const match = line.trim().match(/^([LR])(\d+)/);
        if (match) {
            rotations.push([match[1], parseInt(match[2], 10)]);
        }
        
    }
    console.log(rotations);
    return rotations;
}


function calculatePassword(rotations: [string, number][] = [], initial_position: number = 50): [number, number]{
    
    const MAX_CLICKS = 100;
    let left_at_zero = 0;
    let times_at_zero = 0;
    let position = initial_position;
    for (const [orientation, clicks] of rotations) {
        const prev_position = position;
        if (orientation === 'L') {
            position = prev_position - clicks;
            times_at_zero += Math.floor((prev_position -1 ) / MAX_CLICKS) - Math.floor((position - 1) / MAX_CLICKS);
        } else {
            position = prev_position + clicks;
            times_at_zero += Math.floor(position / MAX_CLICKS) - Math.floor(prev_position / MAX_CLICKS);
        }
        if (position % MAX_CLICKS === 0){
            left_at_zero += 1;
        }
    }

    return [left_at_zero, times_at_zero];
}




const rotations = readInput('input.in');
const [part1, part2] = calculatePassword(rotations);
console.log(part1, part2);