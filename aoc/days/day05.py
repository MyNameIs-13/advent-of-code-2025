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


def parse_input(input_data: str) -> tuple[list, list]:
    raw_fresh_ingredients_ranges, raw_available_ingredients = input_data.split('\n\n', maxsplit=1)
    fresh_ingredients_ranges =[[int(start), int(end)] for line in raw_fresh_ingredients_ranges.splitlines() for start, end in [line.split('-')]]
    available_ingredients = [int(x) for x in raw_available_ingredients.splitlines()]
    return fresh_ingredients_ranges, available_ingredients


def get_available_fresh_ingredients(available_ingredients: list, fresh_ingredients_ranges: list) -> list:
    available_fresh_ingredients = []
    for available_ingredient in available_ingredients:
        spoiled = True
        for start, end in fresh_ingredients_ranges:
            if  start <= available_ingredient <= end:
                spoiled = False
                break
        if not spoiled:
            available_fresh_ingredients.append(available_ingredient)
    return available_fresh_ingredients
    


def sort_and_merge_ranges(fresh_ingredients_ranges):
    # Sort ranges by their start value. If start values are equal, sort by end value.
    fresh_ingredients_ranges.sort()
    logger.debug(f'Sorted fresh ingredients ranges: {fresh_ingredients_ranges}')

    merged_ranges = []
    current_start, current_end = fresh_ingredients_ranges[0]

    for current_range in fresh_ingredients_ranges[1:]:
        next_start, next_end = current_range

        # If the next range overlaps or is contiguous with the current merged range, extend the end
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            # No overlap, so add the current merged range and start a new one
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end

    # Add the last merged range
    merged_ranges.append((current_start, current_end))

    return merged_ranges


def solve_part_a(input_data: str) -> Any:
    fresh_ingredients_ranges, available_ingredients = parse_input(input_data)
    logger.debug(f'Fresh ingredients ranges: {fresh_ingredients_ranges}')
    logger.debug(f'Available ingredients: {available_ingredients}')
    available_fresh_ingredients = get_available_fresh_ingredients(available_ingredients, fresh_ingredients_ranges)
    logger.debug(f'Available fresh ingredients: {available_fresh_ingredients}')
    return len(available_fresh_ingredients)


def solve_part_b(input_data: str) -> Any:
    fresh_ingredients_ranges, _ = parse_input(input_data)
    logger.debug(f'Fresh ingredients ranges: {fresh_ingredients_ranges}')
    sorted_and_merged_fresh_ingredients_ranges = sort_and_merge_ranges(fresh_ingredients_ranges)
    logger.debug(f'Sorted and merged fresh ingredients ranges: {sorted_and_merged_fresh_ingredients_ranges}')
    all_fresh_ingredients_count = 0
    for start, end in sorted_and_merged_fresh_ingredients_ranges:
        all_fresh_ingredients_count += (end - start + 1)
    logger.debug(f'Total fresh ingredients count: {all_fresh_ingredients_count}')
    return all_fresh_ingredients_count


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 5
    logger.info('🎄 Running puzzle day 05...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
