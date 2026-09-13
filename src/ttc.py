def calculate_TTC(distance, v_front, v_back):

    relative_speed = v_back - v_front

    if relative_speed <= 0:
        return float("inf")

    return distance / relative_speed