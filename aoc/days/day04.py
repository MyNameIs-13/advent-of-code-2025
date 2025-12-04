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

def can_forklift(grid: utils.Grid, p: utils.Point, total_neighbors_set: set | None = None) -> int:
    neighbors = grid.get_neighbors(p, include_diagonal=True, include_straight=True)
    neighbors_set = {n for n in neighbors if grid[n] == '@'}
    if len(neighbors_set) < 4:
        if total_neighbors_set is not None:
            grid[p] = '.'
            total_neighbors_set.discard(p)
            total_neighbors_set.update(neighbors_set)        
        return 1
    return 0


def remove_paper_rolls(grid: utils.Grid, total_neighbors_set: set | None = None) -> int:
    result = 0
    for p, value in grid:
        if value == '@':
            result += can_forklift(grid, p, total_neighbors_set)
    return result


def solve_part_a(input_data: str) -> Any:
    grid = utils.Grid(input_data)
    result = remove_paper_rolls(grid)
    return result


def solve_part_b(input_data: str) -> Any:
    grid = utils.Grid(input_data)
    total_neighbors_set = set()
    result = remove_paper_rolls(grid, total_neighbors_set)
    while total_neighbors_set:
        p = total_neighbors_set.pop()
        result += can_forklift(grid, p, total_neighbors_set)
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 4
    logger.info('🎄 Running puzzle day 04...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
