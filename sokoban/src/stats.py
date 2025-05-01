import numpy as np
import matplotlib.pylab as plt

from representation import Map

from search_methods.heuristics import (
    naive_manhattan_dist_heuristic,
    simple_manhattan_dist_heuristic,
    nearest_target_heuristic,
)

from search_methods.lrta_star import LRTAStarSearch
from search_methods.beam_search import LocalBeamSearch

from search_methods.solver import Solver


if __name__ == '__main__':
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

    lrta_nr_states = []
    beam_nr_states = []

    for map_file_name in maps_file_name:
        map_from_yaml = Map.from_yaml("../resources/tests/" + map_file_name)

        solver = Solver(LRTAStarSearch(map_from_yaml, simple_manhattan_dist_heuristic), map_from_yaml)

        solver.solve()

        results = solver.get_results()

        lrta_nr_states.append(results[1])

        solver = Solver(LocalBeamSearch(map_from_yaml, simple_manhattan_dist_heuristic, 10), map_from_yaml)

        solver.solve()

        results = solver.get_results()

        beam_nr_states.append(results[1])

    bar_width = 0.35
    index = np.arange(len(maps_file_name))

    plt.figure(figsize=(12, 8))

    rects1 = plt.bar(index, lrta_nr_states, bar_width, color="blue", label="LRTA*")

    rects2 = plt.bar(index + bar_width, beam_nr_states, bar_width, color="purple", label="Local Beam")

    plt.ylabel("Runtime (s)")
    plt.title("Runtime using Nearest Neighbour Heuristic")
    plt.xticks(index + bar_width / 2, maps_file_name)
    plt.legend()

    plt.xticks(rotation=20, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()
