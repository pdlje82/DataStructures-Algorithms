import math
import json

def shortest_path(M, start, target):
    print("\nshortest path called")
    visited = {}  # closed nodes
    f_dict = {}  # - f = g + h
    g_dict = {}  # - g... path cost so far
    h_dict = {}  # - heuristic straight start_2_target distances
    p_dict = {}  # shows parent for each node
    path = [start]  # shortest path from start to goal

    if start == target:
        return path

    # expand from start-point
    current_point = start
    print('- start with current point: ', current_point)
    g_dict[current_point] = 0
    h_dict[current_point] = direct_dist(M, current_point, target)
    f_dict[current_point] = h_dict[current_point]
    p_dict[current_point] = None
    while f_dict:
        for point in M.roads[current_point]:
            if point not in f_dict and point not in visited:
                # Calculate heuristic distance to target
                h_dict[point] = direct_dist(M, current_point, target)

            if point not in visited and point not in f_dict or \
                    g_dict[point] > g_dict[current_point] + direct_dist(M, current_point, point):
                # Calculate the total way-costs g
                g_point = direct_dist(M, point, current_point) + g_dict[current_point]
                g_dict[point] = round(g_point, 3)
                # Calculate f costs
                f_point = g_dict[point] + h_dict[point]
                f_dict[point] = round(f_point, 3)
                p_dict[point] = current_point
        visited[current_point] = True
        current_point = min(f_dict, key=f_dict.get)
        f_dict.pop(current_point)
    visited[current_point] = True
    if path is not []:
        path = output_path(start, target, p_dict)
    else:
        return None
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


def output_path(start, target, p_dict):
    path = [target]
    node = target
    while node != start:
        parent_node = p_dict[node]
        path.append(parent_node)
        node = parent_node
    return path[::-1]

