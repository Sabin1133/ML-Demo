from sys import argv

from representation import Map

from search_methods.heuristics import (
    naive_manhattan_dist_heuristic,
    simple_manhattan_dist_heuristic,
    nearest_target_heuristic,
)

from search_methods.lrta_star import LRTAStarSearch
from search_methods.beam_search import LocalBeamSearch

from search_methods.solver import Solver


def main():
    if len(argv) < 3 or len(argv) > 4:
        print("Incorrect number of parameters")
        return
    
    algorithm_name = argv[1]
    map_file_name = argv[2]

    map_from_yaml_file = Map.from_yaml(map_file_name)

    match algorithm_name:
        case "lrta*":
            solver = Solver(LRTAStarSearch(map_from_yaml_file, nearest_target_heuristic), map_from_yaml_file)
        case "beam-search":
            solver = Solver(LocalBeamSearch(map_from_yaml_file, nearest_target_heuristic, 10), map_from_yaml_file)
        case _:
            print("Unknown algorithm")
            return
        
    if len(argv) == 3:
        solver.solve()
    elif argv[3] == "pause":
        solver.solve(-1)
    else:
        try:
            solver.solve(float(argv[3]))
        except ValueError:
            solver.solve()

    solver.print_path()


if __name__ == '__main__':
    main()
