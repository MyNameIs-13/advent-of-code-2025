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
    result = 0
    for line in utils.input_data_to_list(input_data):
        id_ranges = line.split(',')
        for id_range in id_ranges:
            logger.debug(f'id range: {id_range}')
            if not id_range:
                continue
            start, end = id_range.split('-')
            start = int(start)
            end = int(end)
            for id in range(start, end + 1):
                id_str = str(id)
                id_len = len(id_str)
                if id_len % 2 == 0:
                    id_len_half = id_len // 2
                    if id_str[0:id_len_half] == id_str[id_len_half:]:
                        result += id
                        logger.debug(f'Found invalid id {id}')
    return result


def solve_part_b(input_data: str) -> Any:
    result = 0
    for line in utils.input_data_to_list(input_data):
        id_ranges = line.split(',')
        for id_range in id_ranges:
            logger.debug(f'id range: {id_range}')
            if not id_range:
                continue
            start, end = id_range.split('-')
            start = int(start)
            end = int(end)
            for id in range(start, end + 1):
                id_str = str(id)
                id_len = len(id_str)
                id_len_half = id_len // 2
                if id_len % 2 == 0:
                    if id_str[0:id_len_half] == id_str[id_len_half:]:
                        result += id
                        logger.debug(f'Found invalid id {id}')
                        continue
                for i in range(id_len_half):
                    pattern = id_str[:i+1]
                    if id_str.replace(pattern, '') == '':
                        result += id
                        logger.debug(f'Found invalid id {id}')
                        break
                        
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 2
    logger.info('🎄 Running puzzle day 02...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
