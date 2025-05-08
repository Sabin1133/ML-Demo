from copy import deepcopy
from heapq import heappush

from sokoban.moves import is_move_pull

from .graph_search import GraphSearch


class LocalBeamSearch(GraphSearch):
    def __init__(self, initial_state, heuristic_function, k):
        self._nr_iters = 0

        # TODO remove
        self._nr_pull_iters = 0

        self._nr_states = 1
        self._path = []

        self._initial_rstate = str(initial_state)

        self._best_states = [deepcopy(initial_state)]

        self._explored_states = {str(initial_state)}

        self._h = heuristic_function
        self._cached_h = {str(initial_state): self._h(initial_state)}

        self._k = k

        self._found_final_state = False

    def _get_h(self, state):
        if str(state) not in self._cached_h:
            self._cached_h[str(state)] = self._h(state)
        else:
            self._cached_h[str(state)] += 10

        return self._cached_h[str(state)]
    
    def next_iter(self, frame_interval=0):
        if self._found_final_state:
            return 0

        best_next_h_and_states = []

        for state in self._best_states:
            # for neigh_s in state.get_neighbours():
            # TODO remove
            for action, neigh_s in zip(state.filter_possible_moves(), state.get_neighbours()):
                if str(neigh_s) in self._explored_states:
                    continue

                # TODO remove
                if is_move_pull(action):
                    self._nr_pull_iters += 1


                self._explored_states.add(str(neigh_s))

                heappush(best_next_h_and_states, (self._get_h(neigh_s), neigh_s))

                if neigh_s.is_solved():
                    self._found_final_state = True
                    break

        best_next_states = [next_state for _, next_state in best_next_h_and_states]

        for state in self._best_states + best_next_states[self._k:]:
            self._explored_states.remove(str(state))

        self._best_states = best_next_states[:self._k]

        self._nr_states += len(self._best_states)

        self._nr_iters += 1

        return len(self._best_states)
    
    def get_results(self):
        # return (self._nr_iters, self._nr_states, [])
        # TODO remove
        return (self._nr_iters, self._nr_states, [], self._nr_pull_iters)
    
    def has_finished(self):
        return self._found_final_state
