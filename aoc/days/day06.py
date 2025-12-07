#!/usr/bin/env python3
import logging
import operator
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

def parse_input_a(input_data: str) -> dict:
    fancy_dict = {}
    input_data_list = input_data.splitlines()
    logger.debug(f'input_data_list: {input_data_list}')
    for i, op in enumerate([x.strip() for x in input_data_list.pop(-1) if x.strip()]):
        if op == '*':
            fancy_dict[i] = {'op': operator.mul, 'result': 1}
        else:
            fancy_dict[i] = {'op': operator.add, 'result': 0}
    for line in(input_data_list):
        for i, num in enumerate(line.split()):
            fancy_dict[i]['result'] = fancy_dict[i]['op'](fancy_dict[i]['result'], int(num))
    return fancy_dict
    
    
def parse_input_b(input_data: str) -> dict:
    fancy_dict = {}
    input_data_list = input_data.splitlines()
           
    for i, op in enumerate([x.strip() for x in input_data_list.pop(-1) if x.strip()]):
        if op == '*':
            fancy_dict[i] = {'op': operator.mul, 'result': 1}
        else:
            fancy_dict[i] = {'op': operator.add, 'result': 0}


    input_data = input_data.replace(' ', '.')
    grid = utils.Grid(input_data)
    
    k = 0
    for j in range(grid.cols):        
        parse_str = ''
        for i in range(grid.rows - 1):
            c = grid[utils.Point(i, j)]
            if c:
                parse_str += c
        parse_str = parse_str.replace('.', ' ').strip()
        if not parse_str:
            k += 1
            continue
        if parse_str and parse_str.isdigit():         
            fancy_dict[k]['result'] = fancy_dict[k]['op'](fancy_dict[k]['result'], int(parse_str))
    
    return fancy_dict
    

def solve_part_a(input_data: str) -> Any:
    fancy_dict = parse_input_a(input_data)
    result = 0
    for solved in fancy_dict.values():
        logger.debug(f'solved: {solved}')
        result += solved['result']
    return result


def solve_part_b(input_data: str) -> Any:
    fancy_dict = parse_input_b(input_data)
    result = 0
    for solved in fancy_dict.values():
        logger.debug(f'solved: {solved}')
        result += solved['result']
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 6
    logger.info('🎄 Running puzzle day 06...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
