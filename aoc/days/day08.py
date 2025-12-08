#!/usr/bin/env python3
import logging
import math
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

def parse_input(input_data: str) -> set:
    junction_boxes = set()
    for line in input_data.splitlines():
        t = tuple(int(x) for x in line.split(','))
        junction_boxes.add(t)
    return junction_boxes


def fill_distances_dict(distances_dict :dict, junction_boxes: set) -> None:
    while junction_boxes:
        ref_box = junction_boxes.pop()
        for junction_box in junction_boxes:
            dist = math.dist(ref_box, junction_box)
            # distances_dict.setdefault(dist, []).append((ref_box, junction_box))
            distances_dict[dist] = {ref_box, junction_box}


def build_circuits(distances_dict: dict, junction_boxes: set, shortest_connection_count: int | None = None) -> list:
    circuits: list[set] = [{x} for x in junction_boxes]
    shortest_distances = sorted(distances_dict.keys())
    i: int = 0
    while True:
        points: set = distances_dict[shortest_distances[i]]
        new_circuit = points.copy()
        new_circuits: list[set] = []
        for circuit in circuits:
            if points.intersection(circuit):
                new_circuit.update(circuit)
            else:
                new_circuits.append(circuit)
        circuits = new_circuits
        circuits.append(new_circuit)
        if shortest_connection_count is None and len(circuits) == 1:
            logger.debug(points)
            return list(points)
        elif shortest_connection_count and i >= shortest_connection_count:
            break
        i += 1
    circuits.sort(key=len, reverse=True)
    return circuits
        

def solve_part_a(input_data: str) -> Any:
    junction_boxes = parse_input(input_data)
    distances_dict = {}
    fill_distances_dict(distances_dict, junction_boxes.copy())
    # logger.debug(distances_dict)
    shortest_connection_count = 10 if EXAMPLE_DATA else 1000
    circuits = build_circuits(distances_dict, junction_boxes, shortest_connection_count)
    logger.debug(circuits)
    result = 1
    for i in range(3):
        result *= len(circuits[i])
    return result


def solve_part_b(input_data: str) -> Any:
    junction_boxes = parse_input(input_data)
    distances_dict = {}
    fill_distances_dict(distances_dict, junction_boxes.copy())
    # logger.debug(distances_dict)
    last_points = build_circuits(distances_dict, junction_boxes)
    logger.debug(f'last_points: {last_points}')
    result = 1
    for point in last_points:
        result *= point[0]
    return result


def main() -> None:
    """
    Execute the solve functions for each part and submit the solution for the specified year and day
    This is part of the template and does not need to be changed
    """
    year = 2025
    day = 8
    logger.info('🎄 Running puzzle day 08...')
    puzzle = Puzzle(year=year, day=day)

    part_a_solution = utils.solve_puzzle_part(puzzle, solve_part_a, 'a', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)
    if part_a_solution is not None and part_a_solution != 'None':
        utils.solve_puzzle_part(puzzle, solve_part_b, 'b', example_data=EXAMPLE_DATA, submit_solution=SUBMIT)

    return None

if __name__ == '__main__':
    main()
