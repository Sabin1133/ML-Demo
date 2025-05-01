import time
import random
from copy import deepcopy

from sokoban.moves import moves_meaning, is_pull

from .graph_search import GraphSearch


class LRTAStarSearch(GraphSearch):
    def __init__(self, initial_state, heuristic_function):
        self._nr_iters = 0
        self._nr_states = 1
        self._path = []

        self._initial_rstate = str(initial_state)

        self._prev_s = deepcopy(initial_state)
        self._prev_a = None
        self._curr_s = deepcopy(initial_state)
        self._curr_a = None

        self._action_and_next_rstate = {}

        self._h = heuristic_function
        self._real_h = {str(self._curr_s): self._h(self._curr_s)}
    
    def _cost(self, action, neigh_state):
        return 1 + (self._real_h[str(neigh_state)] if str(neigh_state) in self._real_h else self._h(neigh_state))

    def _best_next_cost(self, current_state):
        actions = current_state.filter_possible_moves()
        neigh_states = current_state.get_neighbours()

        return min([self._cost(action, neigh_s) for action, neigh_s in zip(actions, neigh_states)])

    def _next_action(self, current_state):
        actions = current_state.filter_possible_moves()
        neigh_states = current_state.get_neighbours()

        min_eval = min([self._cost(action, neigh_s) for action, neigh_s in zip(actions, neigh_states)])

        random.seed(1)
        return random.choice([action for action, neigh_s in zip(actions, neigh_states) if self._cost(action, neigh_s) == min_eval])

    def next_iter(self, frame_interval=0):
        if self._curr_s.is_solved():
            return 0

        if str(self._curr_s) not in self._real_h:
            self._real_h[str(self._curr_s)] = self._h(self._curr_s)

            self._nr_states += 1

        if self._nr_iters > 0:
            self._real_h[str(self._prev_s)] = self._best_next_cost(self._prev_s)

        self._curr_a = self._next_action(self._curr_s)

        self._check_debug(frame_interval)

        if self._nr_iters > 0:
            self._prev_s.apply_move(self._prev_a)

        self._curr_s.apply_move(self._curr_a)

        self._prev_a = self._curr_a

        self._action_and_next_rstate[str(self._prev_s)] = (self._prev_a, str(self._curr_s))

        self._nr_iters += 1

        if self._curr_s.is_solved():
            self._check_debug(frame_interval)

            rstate = str(self._initial_rstate)

            while rstate in self._action_and_next_rstate:
                action, rstate = self._action_and_next_rstate[rstate]

                self._path.append(action)

        return 1
    
    def get_results(self):
        return (self._nr_iters, self._nr_states, self._path)
    
    def has_finished(self):
        return self._curr_s.is_solved()
    
    def _check_debug(self, frame_interval):
        if frame_interval == 0:
            return
        
        self._print_debug()

        if frame_interval == -1:
            input()
            print("\033[A", end='')
        else:
            time.sleep(frame_interval)

    def _print_debug(self):
        print(self._curr_s)
        print("\033[2K", "action - ", moves_meaning[self._curr_a] if not self._curr_s.is_solved() else "", sep='')

        print()

        print("\033[2K", "nr iter - ", self._nr_iters, sep='')
        print("\033[2K", "nr states - ", self._nr_states, sep='')

        print("\033[2K", "h current - ", self._real_h[str(self._curr_s)] if str(self._curr_s) in self._real_h else self._h(self._curr_s), sep='')
        
        if not self._curr_s.is_solved():
            print("\033[2K\n" * 8, "\033[8A", sep='', end='')

            actions = self._curr_s.filter_possible_moves()
            neigh_states = self._curr_s.get_neighbours()

            for action, neigh_s in zip(actions, neigh_states):
                print(f"f {moves_meaning[action]} - ", self._cost(action, neigh_s), sep='')

            print(f"\033[{self._curr_s.length + 5 + len(actions)}A", end='')
