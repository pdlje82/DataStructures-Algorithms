import math
import json

def shortest_path(M, start, target):
    print("\nshortest path called")
    currents = []  # currently open nodes
    visited = []  # closed nodes
    # dict with:
    # - straight s2t distances
    # - g... path cost so
    # - h... estimated distance to target
    # - f = g + h
    frontier_dict = {}
    path = [start]  # shortest path from start to goal
    # calculate straight line distances from goal point to all other points
    for point in M.intersections:
        frontier_dict[point] = {'g': None,
                                'heuristic_distance': direct_dist(M, point, target),
                                'f': None,
                                'parent': None}
    # print('initialized frontier_dict with:\n ', frontier_dict)

    if start == target:
        return path

    # expand from start-point
    current_point = start
    print('- start with current point: ', current_point)
    frontier_dict[current_point]['g'] = 0  # cost from start is 0
    frontier_dict[current_point]['f'] = frontier_dict[current_point]['heuristic_distance']
    # print('- f_dict for start {} is to : {}'.format(start, frontier_dict[start]))
    # print('\n------------------------------------------------------------------------------')
    while current_point is not target:
        print('\nWHILE_loop: current point is {} with neighbors {}'.format(current_point, M.roads[current_point]))
        for point in M.roads[current_point]:
            if point not in visited and \
                    point not in currents:
                currents.append(point)
            if frontier_dict[point]['f'] is None or \
                    frontier_dict[point]['g'] > frontier_dict[current_point]['g'] + direct_dist(M, current_point, point):
                # print('- FOR_loop: f-value for {} is: {} --> writing g-, f-, and parent values in frontier_dict:'.
                #       format(point, frontier_dict[point]['f']))
                # Calculate the total way-costs g
                g_point = direct_dist(M, point, current_point) + frontier_dict[current_point]['g']
                frontier_dict[point]['g'] = round(g_point, 3)
                # Calculate f costs
                f_point = frontier_dict[point]['g'] + frontier_dict[point]['heuristic_distance']
                frontier_dict[point]['f'] = round(f_point, 3)
                # set parent to actual current_point
                frontier_dict[point]['parent'] = current_point
                # print('- FOR_loop: f_dict for point {} changed to : {}\n'.format(point, frontier_dict[point]))
        visited.append(current_point)
        # print('- VISIT of current_point {} is now COMPLETE'.format(current_point))
        # print('-- f_dict for point {} is: {}'.format(current_point, frontier_dict[current_point]))
        # print('-- current_list is: ', currents)
        # print('-- visited list is: ', visited)
        # find min f value in frontier dict
        min_list = [frontier_dict[point]['f'] for point in currents]
        current_point = currents[min_list.index(min(min_list))]
        # print('- new current point is {} with min. f-value of {}'.format(current_point,
        #                                                                        frontier_dict[current_point]['f']))
        currents.remove(current_point)
    visited.append(current_point)
    print('WHILE_loop end')
    # print(json.dumps(frontier_dict, indent=1))
    path = output_path(start, target, frontier_dict)
    print(path)
    return path


def direct_dist(M, start, target):
    # calculate direct distance between 2 points
    p1 = M.intersections[start]
    p2 = M.intersections[target]
    y = p2[1] - p1[1]
    x = p2[0] - p1[0]
    distance = math.sqrt(x ** 2 + y ** 2)
    return round(distance, 3)


def output_path(start, target, frontier_dict):
    path = [target]
    node = target
    while node != start:
        parent_node = frontier_dict[node]['parent']
        path.append(parent_node)
        node = parent_node
    return path[::-1]

