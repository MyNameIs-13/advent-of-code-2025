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

def parse_input(input_data: str) -> dict:
    graph_base_data = {}
    for line in input_data.splitlines():
        from_node, to_nodes = line.split(':')
        graph_base_data[from_node.strip()] = [node.strip() for node in to_nodes.split()]
    return graph_base_data


def solve_part_a(input_data: str) -> Any:
    graph_base_data = parse_input(input_data)
    logger.debug(graph_base_data)
    graph = {}
    for from_node, to_nodes in graph_base_data.items():
        for node in to_nodes:
            utils.Graph.add_edge(graph, from_node, node, 0)
    all_paths, lowest_cost = utils.Graph.get_shortest_paths(graph, 'you', 'out', return_all_paths=True)
    return len(all_paths)


def solve_part_b(input_data: str) -> Any:
    # TODO: way too slow :(
    graph_base_data = parse_input(input_data)
    logger.debug(graph_base_data)
    graph = {}
    for from_node, to_nodes in graph_base_data.items():
        for node in to_nodes:
            utils.Graph.add_edge(graph, from_node, node, 0)
    all_paths, lowest_cost = utils.Graph.get_shortest_paths(graph, 'svr', 'out', return_all_paths=True)
    problem_paths = []
    for path_to_check in all_paths:
        if all(n in path_to_check for n in ['fft', 'dac']):
            problem_paths.append(path_to_check)
    return len(problem_paths)


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
