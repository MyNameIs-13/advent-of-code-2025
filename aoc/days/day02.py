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


def get_id_ranges(input_data: str) -> list:
    if EXAMPLE_DATA:
        input_data.replace('\n', '')
    return  [tuple(map(int, id_range.split('-'))) for id_range in input_data.split(',')]


def get_invalid_ids(id_ranges_list: list, part_b: bool = False) -> list:
    """returns ids wich are constructed with a silly pattern"""
    invalid_ids = []
    for start, end in id_ranges_list:
        for id in range(start, end + 1):
            id_str = str(id)
            id_len_half = len(id_str) // 2
            # Check if the first half of the id is the same as the second half
            if id_str[0:id_len_half] == id_str[id_len_half:]:
                invalid_ids.append(id)
            elif part_b:
                # Check if any pattern occurs at least twice (check all pattern from 1 char to half of the length of the id)
                for i in range(id_len_half):
                    pattern = id_str[:i+1]
                    if id_str.replace(pattern, '') == '':
                        invalid_ids.append(id)
                        break
    return invalid_ids
    

def solve_part_a(input_data: str) -> Any:
    id_ranges_list = get_id_ranges(input_data)
    invalid_ids = get_invalid_ids(id_ranges_list)
    logger.debug(f'Invalid ids: {invalid_ids}')
    result = sum(invalid_ids)
    return result
    

def solve_part_b(input_data: str) -> Any:
    id_ranges_list = get_id_ranges(input_data)
    invalid_ids = get_invalid_ids(id_ranges_list, part_b=True)
    logger.debug(f'Invalid ids: {invalid_ids}')
    result = sum(invalid_ids)
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
