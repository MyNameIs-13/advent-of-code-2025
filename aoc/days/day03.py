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


def get_battery_banks(input_data: str) -> list[list[int]]:
    return [[int(x) for x in line] for line in input_data.splitlines()]


def get_highest_joltages(battery_banks: list, total_batteries_to_enable: int) -> list:
    highest_joltages = []
    for battery_bank in battery_banks:
        joltage = 0
        range_start = 0
        # Calculate maximal possible joltage for this battery bank
        for batteries_enabled in range(1, total_batteries_to_enable + 1):
            batteries_left_to_enable = total_batteries_to_enable - batteries_enabled
            logger.debug(f'batteries_left_to_enable: {batteries_left_to_enable}')
            # at least this many numbers are still needed to enable the remaining batteries
            range_stop = len(battery_bank) - batteries_left_to_enable
            logger.debug(f'range_start: {range_start}, range_stop: {range_stop}')
            logger.debug(f'battery_bank_sliced: {battery_bank[range_start : range_stop]}')
            battery_value = max(battery_bank[range_start : range_stop])
            logger.debug(f'battery_value: {battery_value}')
            # detect index of value that is added to joltage and add this index to the range start to find the next battery after this index
            range_start += battery_bank[range_start : range_stop].index(battery_value) + 1 
            # multiply with ... 10000, 1000, 100, 10 ... depen
            joltage += battery_value * pow(10, batteries_left_to_enable)
            logger.debug('')
        highest_joltages.append(joltage)
        
    return highest_joltages


def solve_part_a(input_data: str) -> Any:
    battery_banks = get_battery_banks(input_data)
    logger.debug(battery_banks)
    highest_joltages = get_highest_joltages(battery_banks, 2)
    logger.debug(highest_joltages)
    return sum(highest_joltages)


def solve_part_b(input_data: str) -> Any:
    battery_banks = get_battery_banks(input_data)
    logger.debug(battery_banks)
    highest_joltages = get_highest_joltages(battery_banks, 12)
    logger.debug(highest_joltages)
    return sum(highest_joltages)


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 3
    logger.info('🎄 Running puzzle day 03...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
