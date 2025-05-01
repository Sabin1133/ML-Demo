from heapq import heappush, heappop

from .util import comp_sign, manhattan_dist


def informed_manhattan_dist(state, box_coord, target_coord):
    test_x = box_coord[0] + comp_sign(box_coord[0], target_coord[0])
    test_y = box_coord[1] + comp_sign(box_coord[1], target_coord[1])

    obstacles_coord = state.obstacles

    if (test_x, box_coord[1]) in obstacles_coord or test_x < 0 or test_x >= state.length:
        return float("inf")
    
    if (box_coord[0], test_y) in obstacles_coord or test_y < 0 or test_y >= state.width:
        return float("inf")

    return manhattan_dist(box_coord, target_coord)


def naive_manhattan_dist_heuristic(state):
    return sum([min([manhattan_dist(box_coord, target_coord) for target_coord in state.targets]) + manhattan_dist(box_coord, (state.player.x, state.player.y)) for box_coord in state.positions_of_boxes])


def simple_manhattan_dist_heuristic(state):
    dist_sum = 0
    boxes_coord = state.positions_of_boxes
    targets_coord = state.targets

    locked = set()

    for box_coord in boxes_coord:
        nearest_target_coord = min(targets_coord, key=lambda target_coord: float("inf") if target_coord in locked else manhattan_dist(box_coord, target_coord))

        locked.add(nearest_target_coord)

        dist_sum += (manhattan_dist(box_coord, (state.player.x, state.player.y)) + manhattan_dist(box_coord, nearest_target_coord))
    
    return dist_sum


def _valid_coord(length, width, coord):
    x, y = coord

    return 0 <= x and x < length and 0 <= y and y < width


def _get_coord_neighbours(length, width, coord):
    x, y = coord

    return [neigh_coord for neigh_coord in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if _valid_coord(length, width, neigh_coord)]


def _valid_state_coord(state, coord):
    length = state.length
    width = state.width

    if not _valid_coord(length, width, coord):
        return False
    
    if coord in state.obstacles:
        return False
    
    return True


def _get_state_coord_neighbours(state, coord):
    x, y = coord

    return [neigh_coord for neigh_coord in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if _valid_state_coord(state, neigh_coord)]


def _first_closest_targets(state):
    boxes_coord = state.positions_of_boxes.keys()
    targets_coord = state.targets

    frontier = []
    visited = set()
    placement = {}

    for box_coord in boxes_coord:
        frontier.clear()
        visited.clear()

        heappush(frontier, (0, box_coord))
        visited.add(box_coord)

        while frontier:
            dist, coord = heappop(frontier)

            if coord in targets_coord and coord not in placement.values():
                placement[box_coord] = coord
                break

            for neigh_coord in _get_state_coord_neighbours(state, coord):
                if neigh_coord not in visited:
                    heappush(frontier, (1 + dist, neigh_coord))
                    visited.add(neigh_coord)

    return placement


def nearest_target_heuristic(state):
    placement = _first_closest_targets(state)

    return sum([manhattan_dist(box_coord, (state.player.x, state.player.y)) + manhattan_dist(box_coord, placement[box_coord]) for box_coord in state.positions_of_boxes])
