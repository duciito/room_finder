from collections import deque


def obstacle_search(start, end, building, obstacle):
    """Търсене на път до стая, като се избягва определен тип преход."""

    if not (building.contains_room(start) and building.contains_room(end)):
        return None, None, None

    search_queue = deque()
    median_rooms = []
    search_queue.append([building.get_room(start)])

    while search_queue:
        path = search_queue.popleft()
        room = path[-1]
        if room.name not in median_rooms:
            median_rooms.append(room.name)

        if room.name == end:
            final_path = [f'{r.name} ({r.room_type})' for r in path if not isinstance(r, int)]
            total_cost = sum([cost for cost in path if isinstance(cost, int)])
            return median_rooms, final_path, total_cost

        room.visited = True

        for connection in room.connections:

            if connection.link_type == obstacle:
                continue

            current_room = building.get_room(connection.to)

            if not current_room.visited and current_room not in path:
                new_path = list(path)
                new_path.append(int(connection.cost))
                new_path.append(current_room)
                search_queue.append(new_path)

    return median_rooms, None, None


def lift_search(start, end, building):
    """Търсене на път до стая, като се използва lift м/у етажите."""

    if not (building.contains_room(start) and building.contains_room(end)):
        return None, None, None

    search_queue = deque()
    median_rooms = []
    search_queue.append([building.get_room(start)])
    start_floor = int(building.get_room(start).floor_num)
    end_floor = int(building.get_room(end).floor_num)

    if start_floor > end_floor:
        start_floor += 1
    else:
        end_floor +=1

    if start_floor > end_floor:
        floor_range = range(start_floor, end_floor)
        if start_floor - end_floor == 2:
            floor_range = range(end_floor, start_floor)
    else:
        floor_range = range(end_floor, start_floor)

    while search_queue:
        path = search_queue.popleft()
        room = path[-1]
        if room.name not in median_rooms:
            median_rooms.append(room.name)

        if room.name == end:
            final_path = [f'{r.name} ({r.room_type})' for r in path if not isinstance(r, int)]
            total_cost = sum([cost for cost in path if isinstance(cost, int)])
            return median_rooms, final_path, total_cost

        room.visited = True
        has_lift = any('lift' == conn.link_type for conn in room.connections if conn.to not in [roo.name for roo in path if not isinstance(roo, int)])

        for connection in room.connections:

            if connection.link_type == 'climb' and has_lift and int(building.get_room(connection.to).floor_num) not in floor_range:
                print()
                continue

            current_room = building.get_room(connection.to)

            if not current_room.visited and current_room not in path:
                new_path = list(path)
                new_path.append(int(connection.cost))

                if connection.link_type == 'climb':
                    new_path[-1] += int(connection.cost)

                new_path.append(current_room)
                search_queue.append(new_path)

    return median_rooms, None, None
