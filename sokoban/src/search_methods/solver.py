import os
import time
import random
from copy import deepcopy

from sokoban.moves import moves_meaning
from sokoban.map import Map


class Solver:
    def __init__(self, graph_search, initial_state):
        self._graph_search = graph_search
        self._state = initial_state

        self._nr_iters = 0
        self._nr_states = 1
        self._path = []

    def solve(self, frame_interval=0):
        while not self._graph_search.has_finished():
            self._graph_search.next_iter(frame_interval)

        self._nr_iters, self._nr_states, self._path = self._graph_search.get_results()

    def get_results(self):
        return self._nr_iters, self._nr_states, self._path

    def print_path(self, frame_interval=0.2):
        len_path = len(self._path)

        print(str(self._state))
        print("\033[2K", "move - ", moves_meaning[self._path[0]] if self._path else "", sep='')
        print()
        print("\033[2K", "nr iter - ", self._nr_iters, sep='')
        print("\033[2K", "nr states - ", self._nr_states, sep='')
        print("\033[2K", "nr moves - ", len_path, sep='')

        if not self._path:
            return

        print(f"\033[{self._state.length + 5}A", end='')
        time.sleep(frame_interval)

        self._state.apply_move(self._path[0])

        for move in self._path[1:]:
            print(str(self._state))
            print("\033[2K", "move - ", moves_meaning[move], sep='')
            print(f"\033[{self._state.length + 1}A", end='')
            time.sleep(frame_interval)

            self._state.apply_move(move)

        print(str(self._state))
        print("\033[2K", "move - ", sep='')
        print("\033[4B", end='')
