#!/usr/bin/env python3
import logging
from functools import lru_cache
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

def create_graph(input_data: str) -> dict:
    graph = {}
    for line in input_data.splitlines():
        from_node, to_nodes = line.split(':')
        for node in to_nodes.split():
            utils.Graph.add_edge(graph, from_node, node.strip(), 0)
    return graph


def solve_part_a(input_data: str) -> Any:
    graph = create_graph(input_data)
    all_paths, lowest_cost = utils.Graph.get_shortest_paths(graph, 'you', 'out', return_all_paths=True)
    return len(all_paths)


def solve_part_b(input_data: str) -> Any:
    
    @lru_cache(maxsize=None)
    def timeline_paths_for_endpoint(node: str, dac_found: bool, fft_found: bool) -> int:
        if node == start and dac_found and fft_found:
            return 1
        elif node == start:
            return 0
        
        if node == 'dac':
            dac_found = True
        if node == 'fft':
            fft_found = True
            
        _predecessors = predecessors.get(node)
        if not _predecessors:
            return 0
        return sum(timeline_paths_for_endpoint(p, dac_found, fft_found) for p in _predecessors)
    
    graph = create_graph(input_data)            
    start = 'svr'
    end = 'out'
    _, predecessors = utils.Graph._do_dijkstra(graph, start, return_all_paths=True)
    timelines = timeline_paths_for_endpoint(end, False, False)

    return timelines


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
