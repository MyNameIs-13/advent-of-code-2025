#!/usr/bin/env python3
import logging
from itertools import combinations, combinations_with_replacement
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

def parse_machine(line: str) -> tuple[list, list, list]:
    # Example: [.##.] (3) (1,3) (2,3) (0,2) (0,1) {3,5,4,7}
    parts = line.split()
    pattern = parts[0].strip('[]')
    target = [True if c == '#' else False for c in pattern]

    buttons = []
    joltages = []
    for p in parts[1:]:
        if p.startswith('('):
            inside = p.strip('()')
            if inside == '':
                buttons.append([])
            else:
                buttons.append(list(map(int, inside.split(','))))
        elif p.startswith('{'):
            inside = p.strip('{}')
            if inside:
                joltages = list(map(int, inside.split(',')))

    return target, buttons, joltages


def solve_part_a(input_data: str) -> Any:
    result = 0
    for line in input_data.splitlines():
        target, buttons, _ = parse_machine(line)
        target_solved = False
        for presses in range(1, len(buttons) + 1):
            button_combis = combinations(buttons, presses)
            for button_combi in button_combis:
                state = [False for i in range(len(target))]
                for button in button_combi:
                    for button_light in button:
                        state[button_light] = not state[button_light]
                    if state == target:
                        logger.debug(f'Found solution for {target} with {presses} pressed - buttons: {button_combi}')
                        result += presses
                        target_solved = True
                        break
                if target_solved:
                    break
            if target_solved:
                break
    return result


def solve_part_b(input_data: str) -> Any:
    # TODO: way too slow :(
    result = 0
    for line in input_data.splitlines():
        _, buttons, joltages = parse_machine(line)
        joltages_reached = False
        presses = 1
        while presses < 1000:  # sanity check
            button_combis = combinations_with_replacement(buttons, presses)
            for button_combi in button_combis:
                state = [0 for i in range(len(joltages))]
                for button in button_combi:
                    for button_light in button:
                        state[button_light] += 1
                    if state == joltages:
                        logger.info(f'Found solution for {joltages} with {presses} pressed - buttons: {button_combi}')
                        result += presses
                        joltages_reached = True
                        break
                if joltages_reached:
                    break
            if joltages_reached:
                break
            presses += 1
        else:
            logger.warning(f'No solution found for {joltages} with {presses} pressed')
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 10
    logger.info('🎄 Running puzzle day 10...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
