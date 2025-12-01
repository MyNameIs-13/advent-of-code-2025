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


def solve_part_a(input_data: str) -> Any:
    current_position = 50
    result = 0
    for line in utils.input_data_to_list(input_data):
        direction = line[0]
        turns = int(line[1:])
        
        if direction == 'L':
            current_position = (current_position - turns + 100) % 100
        elif direction == 'R':
            current_position = (current_position + turns) % 100
        # logger.debug(current_position)
        if current_position == 0:
            result += 1
        
    return result


def solve_part_b(input_data: str) -> Any:
    current_position = 50
    result = 0

    for line in utils.input_data_to_list(input_data):
        direction = line[0]
        turns = int(line[1:])
        
        # Simulate each individual unit turn
        for _ in range(turns):
            if direction == 'L':
                if current_position == 0:
                    current_position = 99
                else:
                    current_position -= 1
            elif direction == 'R':
                if current_position == 99:
                    current_position = 0
                else:
                    current_position += 1
            if current_position == 0:
                result += 1
        logger.debug(f"Move '{line}': Current dial={current_position}, Total passes={result}")
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 1
    logger.info('🎄 Running puzzle day 01...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()