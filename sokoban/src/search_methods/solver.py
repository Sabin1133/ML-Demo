import time

from sokoban.moves import moves_meaning, is_move_pull


class Solver:
    def __init__(self, graph_search, initial_state):
        self._graph_search = graph_search
        self._state = initial_state

        self._nr_iters = 0

        # TODO remove
        self._nr_pull_iters = 0

        self._nr_states = 1
        self._path = []

    def solve(self, frame_interval=0):
        while not self._graph_search.has_finished():
            self._graph_search.next_iter(frame_interval)

        # self._nr_iters, self._nr_states, self._path = self._graph_search.get_results()
        # TODO remove
        self._nr_iters, self._nr_states, self._path, self._nr_pull_iters = self._graph_search.get_results()

    def get_results(self):
        return self._nr_iters, self._nr_states, self._path, self._nr_pull_iters

    def print_path(self, frame_interval=0.0):
        nr_moves = len(self._path)
        nr_pull_moves = len([move for move in self._path if is_move_pull(move)])

        print(str(self._state))
        print("\033[2K", "move - ", moves_meaning[self._path[0]] if self._path else "", sep='')
        print()
        print("\033[2K", "nr iter - ", self._nr_iters, sep='')
        print("\033[2K", "nr states - ", self._nr_states, sep='')
        print("\033[2K", "nr moves - ", nr_moves, sep='')
        print("\033[2K", "nr pull iters - ", self._nr_pull_iters, sep='')
        print("\033[2K", "nr pull moves - ", nr_pull_moves, sep='')

        if not self._path or frame_interval == 0:
            return

        # print(f"\033[{self._state.length + 5}A", end='')
        # TODO remove
        print(f"\033[{self._state.length + 7}A", end='')

        if frame_interval == -1:
            input()
            print("\033[A", end='')
        else:
            time.sleep(frame_interval)

        self._state.apply_move(self._path[0])

        for move in self._path[1:]:
            print(str(self._state))
            print("\033[2K", "move - ", moves_meaning[move], sep='')

            print(f"\033[{self._state.length + 1}A", end='')

            if frame_interval == -1:
                input()
                print("\033[A", end='')
            else:
                time.sleep(frame_interval)

            self._state.apply_move(move)

        print(str(self._state))
        print("\033[2K", "move - ", sep='')

        # print("\033[4B", end='')
        # TODO remove
        print("\033[6B", end='')
