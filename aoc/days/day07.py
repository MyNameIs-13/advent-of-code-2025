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

def find_start(grid: utils.Grid) -> utils.Point:
    for p, value in grid:
        if value == 'S':
            return p
    else:
        raise ValueError('No start found')


def find_beam_splitter(reached_splitter_positions: set, grid: utils.Grid, start: utils.Point, graph: dict, running_beams_set: set | None = None) -> None:
    if running_beams_set is None:
        running_beams_set = set()
    next_p = start + utils.DIRECTIONS['down']
    if next_p in running_beams_set:
        return
    running_beams_set.add(next_p)
    utils.Graph.add_edge(graph, start, next_p, 0)
    while True:
        if grid[next_p] == '^':
            reached_splitter_positions.add(next_p)
            left_new = next_p + utils.DIRECTIONS['left']
            right_new = next_p + utils.DIRECTIONS['right']
            if grid.in_bounds(left_new):
                utils.Graph.add_edge(graph, next_p, left_new, 0)
                find_beam_splitter(reached_splitter_positions, grid, left_new, graph, running_beams_set)
            if grid.in_bounds(right_new):
                utils.Graph.add_edge(graph, next_p, right_new, 0)
                find_beam_splitter(reached_splitter_positions, grid, right_new, graph, running_beams_set)                
            break
        next_p_plus = next_p + utils.DIRECTIONS['down']
        if grid.in_bounds(next_p_plus):
            if grid[next_p] != '^':
                utils.Graph.add_edge(graph, next_p, next_p_plus, 0)
            next_p = next_p_plus
        else:
            break
        logger.debug(f'next_p: {next_p}')
      
        
def solve_part_a(input_data: str) -> Any:
    grid = utils.Grid(input_data)
    start = find_start(grid)
    reached_splitter_positions = set()
    find_beam_splitter(reached_splitter_positions, grid, start, {})
    logger.debug(f'reached_splitter_positions: {reached_splitter_positions}')
    return len(reached_splitter_positions)


def solve_part_b(input_data: str) -> Any:
    
    @lru_cache(maxsize=None)
    def timeline_paths_for_endpoint(end: utils.Point) -> int:
        if end == start:
            return 1
        _predecessors = predecessors.get(end)
        if not _predecessors:
            return 0
        return sum(timeline_paths_for_endpoint(p) for p in _predecessors)    
    
    grid = utils.Grid(input_data)
    start = find_start(grid)
    reached_splitter_positions = set()
    graph = {}
    find_beam_splitter(reached_splitter_positions, grid, start, graph)

    _, predecessors = utils.Graph._do_dijkstra(graph, start, return_all_paths=True)
  
    predecessors_keys = predecessors.keys()
    timelines = 0
    for i in range(grid.cols):
        end = utils.Point(grid.rows - 1, i)
        if end in predecessors_keys:
            timelines += timeline_paths_for_endpoint(end)

    return timelines


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 7
    logger.info('🎄 Running puzzle day 07...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
