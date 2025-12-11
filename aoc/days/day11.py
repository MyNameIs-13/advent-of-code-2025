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

def create_graph(input_data: str) -> utils.Graph:
    graph = utils.Graph()
    for line in input_data.splitlines():
        from_node, to_nodes = line.split(':')
        for node in to_nodes.split():
            graph.add_connection(from_node, node.strip(), 0)
    return graph


def apply_bitmask_for_node(node: Any, bitmask: int) -> int:
    if node == 'dac':
        return bitmask | 1
    elif node == 'fft':
        return bitmask | 2
    return bitmask
    

def solve_part_a(input_data: str) -> Any:
    graph = create_graph(input_data)
    return graph.count_shortest_paths('you', 'out')


def solve_part_b(input_data: str) -> Any:
    graph = create_graph(input_data)
    return graph.count_shortest_paths('svr', 'out', bitmask_goal=3, bitmask_for_node_function=apply_bitmask_for_node)


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 11
    logger.info('🎄 Running puzzle day 11...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
