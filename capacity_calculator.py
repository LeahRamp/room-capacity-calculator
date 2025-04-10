def calculate_room_capacity(length, width, spacing_per_person=1.5):
    """
    Calculate the maximum number of people that can safely fit in a room.

    Args:
        length (float): The length of the room in meters.
        width (float): The width of the room in meters.
        spacing_per_person (float): The area required per person (in square meters).

    Returns:
        int: Maximum number of people that can fit in the room.
    """
    if length <= 0 or width <= 0 or spacing_per_person <= 0:
        raise ValueError("All dimensions must be positive numbers.")

    room_area = length * width
    capacity = int(room_area // spacing_per_person)
    return capacity
