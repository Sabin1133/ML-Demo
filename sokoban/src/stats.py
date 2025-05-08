import time

import numpy as np
import matplotlib.pylab as plt

from sokoban import Map

from search_methods.heuristics import (
    naive_manhattan_dist_heuristic,
    simple_manhattan_dist_heuristic,
    nearest_target_heuristic,
)

from search_methods.lrta_star import LRTAStarSearch
from search_methods.beam_search import LocalBeamSearch

from search_methods.solver import Solver


def plot_nr_states():
    maps_file_name = [
        "easy_map1.yaml",
        "easy_map2.yaml",
        "medium_map1.yaml",
        "medium_map2.yaml",
        "hard_map1.yaml",
        "hard_map2.yaml",
        "super_hard_map1.yaml",
        "large_map1.yaml",
        "large_map2.yaml",
    ]

    lrta_results = []
    beam_results = []

    for map_file_name in maps_file_name:
        map_from_yaml = Map.from_yaml("../resources/tests/" + map_file_name)

        solver = Solver(LRTAStarSearch(map_from_yaml, nearest_target_heuristic), map_from_yaml)

        start_time = time.time()

        solver.solve()

        end_time = time.time()

        results = solver.get_results()

        # lrta_results.append(end_time - start_time)
        lrta_results.append(results[1])

        solver = Solver(LocalBeamSearch(map_from_yaml, nearest_target_heuristic, 10), map_from_yaml)

        start_time = time.time()

        solver.solve()

        end_time = time.time()

        results = solver.get_results()

        # beam_results.append(end_time - start_time)
        beam_results.append(results[1])

    bar_width = 0.35
    index = np.arange(len(maps_file_name))

    plt.figure(figsize=(12, 8))

    rects1 = plt.bar(index, lrta_results, bar_width, color="blue", label="LRTA*")

    rects2 = plt.bar(index + bar_width, beam_results, bar_width, color="purple", label="Local Beam")

    plt.ylabel("Runtime (s)")
    plt.title("Runtime using Nearest Neighbour Heuristic")
    plt.xticks(index + bar_width / 2, maps_file_name)
    plt.legend()

    plt.xticks(rotation=20, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()


def plot_time():
    map_file_name = "../resources/tests/medium_map2.yaml"

    heuristics_name = [
        "Naive Manhattan",
        "Simple Manhattan",
        "Nearest Neighbour"
    ]

    heuristics = [
        naive_manhattan_dist_heuristic,
        simple_manhattan_dist_heuristic,
        nearest_target_heuristic
    ]

    lrta_results = []
    beam_results = []

    for heuristic in heuristics:
        map_from_yaml = Map.from_yaml(map_file_name)

        solver = Solver(LRTAStarSearch(map_from_yaml, heuristic), map_from_yaml)

        start_time = time.time()

        solver.solve()

        end_time = time.time()

        lrta_results.append(end_time - start_time)

        solver = Solver(LocalBeamSearch(map_from_yaml, heuristic, 10), map_from_yaml)

        start_time = time.time()

        solver.solve()

        end_time = time.time()

        beam_results.append(end_time - start_time)

    bar_width = 0.35
    index = np.arange(len(heuristics_name))

    plt.figure(figsize=(12, 8))

    rects1 = plt.bar(index, lrta_results, bar_width, color="blue", label="LRTA*")

    rects2 = plt.bar(index + bar_width, beam_results, bar_width, color="purple", label="Local Beam")

    plt.ylabel("Runtime (s)")
    plt.title("Runtime in Medium Map 2")
    plt.xticks(index + bar_width / 2, heuristics_name)
    plt.legend()

    plt.xticks(rotation=20, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()


if __name__ == '__main__':
    plot_nr_states()
