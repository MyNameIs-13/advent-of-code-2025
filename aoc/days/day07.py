#!/usr/bin/env python3
import logging
from typing import Any

from aocd.models import Puzzle

from shared import utils
from shared.logger import logger

logger.setLevel(logging.INFO)
EXAMPLE_DATA = False
SUBMIT = True

# HACK: Overwrites
# SUBMIT = False
# logger.setLevel(logging.DEBUG)
# EXAMPLE_DATA = True

def find_start(grid: utils.Grid) -> utils.Point:
    for p, value in grid:
        if value == 'S':
            return p
    else:
        raise ValueError('No start found')


def find_beam_splitter(reached_splitter_positions: set, grid: utils.Grid, start: utils.Point, running_beams_set: set | None = None) -> None:
    if running_beams_set is None:
        running_beams_set = set()
    next_p = start + utils.DIRECTIONS['down']
    if next_p in running_beams_set:
        return
    running_beams_set.add(next_p)
    while grid.in_bounds(next_p):
        if grid[next_p] == '^':
            reached_splitter_positions.add(next_p)
            left_new = next_p + utils.DIRECTIONS['left']
            right_new = next_p + utils.DIRECTIONS['right']
            if grid.in_bounds(left_new):
                find_beam_splitter(reached_splitter_positions, grid, left_new, running_beams_set)
            if grid.in_bounds(right_new):
                find_beam_splitter(reached_splitter_positions, grid, right_new, running_beams_set)                
            break
        else:
            next_p += utils.DIRECTIONS['down']
        logger.debug(f'next_p: {next_p}')
        
        
def solve_part_a(input_data: str) -> Any:
    grid = utils.Grid(input_data)
    start = find_start(grid)
    reached_splitter_positions = set()
    find_beam_splitter(reached_splitter_positions, grid, start)
    logger.debug(f'reached_splitter_positions: {reached_splitter_positions}')
    return len(reached_splitter_positions)


def solve_part_b(input_data: str) -> Any:
    # TODO: implement solution for part B
    result = None
    for line in utils.input_data_to_list(input_data):
        logger.debug(line)
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 7
    logger.info('🎄 Running puzzle day 07...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
