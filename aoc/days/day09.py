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


def parse_input(input_data: str) -> set:
    red_tiles = set()
    for line in input_data.splitlines():
        t = tuple(int(x) for x in line.split(','))
        red_tiles.add(t)
    return red_tiles


def fill_rectangles_dict(rectangles_dict: dict, red_tiles: set) -> None:
    while red_tiles:
        ref_tile = red_tiles.pop()
        for tile in red_tiles:
            length = abs(tile[0] - ref_tile[0]) + 1
            width = abs(tile[1] - ref_tile[1]) + 1
            rectangle =  length * width
            rectangles_dict.setdefault(rectangle, []).append((ref_tile, tile))


def solve_part_a(input_data: str) -> Any:
    red_tiles = parse_input(input_data)
    rectangles_dict = {}
    fill_rectangles_dict(rectangles_dict, red_tiles)    
    largest_rectangle = sorted(rectangles_dict.keys())[-1]
    return largest_rectangle


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
    day = 9
    logger.info('🎄 Running puzzle day 09...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
