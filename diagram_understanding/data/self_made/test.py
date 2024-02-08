import matplotlib.pyplot as plt
import numpy as np

def is_point_in_rect(point, rect_bottom_left, rect_top_right):
    """Check if a point is inside a given rectangle."""
    return rect_bottom_left[0] <= point[0] <= rect_top_right[0] and rect_bottom_left[1] <= point[1] <= rect_top_right[1]

def do_lines_intersect(line1, line2):
    """Check if two line segments intersect. This function can be expanded based on line segment intersection logic."""
    # Simplified version: check if endpoints of one line are on opposite sides of the other line
    # Full implementation would require checking the actual intersection
    return False  # Placeholder for actual intersection test

def check_overlap(vertices, labels, offsets, label_size):
    """Check if any label overlaps with the shape lines."""
    safe_zones = []
    for vertex, offset in zip(vertices, offsets):
        label_pos = vertex + offset
        bottom_left = label_pos - label_size / 2
        top_right = label_pos + label_size / 2
        safe_zones.append((bottom_left, top_right))

    for i, vertex in enumerate(vertices):
        next_vertex = vertices[(i + 1) % len(vertices)]
        line_segment = (vertex, next_vertex)

        for bottom_left, top_right in safe_zones:
            if is_point_in_rect(line_segment[0], bottom_left, top_right) or is_point_in_rect(line_segment[1], bottom_left, top_right):
                print(f"Overlap detected with label at {bottom_left} - {top_right}")
                return True

            # Check if the line segment intersects any edge of the safe zone
            # This is a simplified approach; a full implementation would require detailed intersection logic
            if do_lines_intersect(line_segment, (bottom_left, (bottom_left[0], top_right[1]))):
                print(f"Overlap detected with label at {bottom_left} - {top_right}")
                return True

    return False


def draw_rectangle(labels, coordinate_0, length_0, length_1, angle_0, fig, ax):
    # Convert angle from degrees to radians for numpy calculations
    angle_rad = np.deg2rad(angle_0)

    # Calculate the coordinates of the rectangle's vertices
    point_0 = np.array(coordinate_0)
    point_1 = point_0 + np.array([length_0 * np.cos(angle_rad), length_0 * np.sin(angle_rad)])
    point_2 = point_0 + np.array([length_1 * np.sin(angle_rad), -length_1 * np.cos(angle_rad)])
    point_3 = point_2 + (point_1 - point_0)

    # Setup the plot

    ax.set_aspect('equal', 'box')
    ax.plot(*zip(*[point_0, point_1, point_3, point_2, point_0]), '-r')

    # Label offset for clarity
    label_offset = 0.2

    # Label the vertices with an offset to avoid overlap
    label_points = [point_0, point_1, point_3, point_2]
    label_offsets = [np.array([-label_offset, -label_offset]),
                     np.array([label_offset, -label_offset]),
                     np.array([label_offset, label_offset]),
                     np.array([-label_offset, label_offset])]
    for label, point, offset in zip(labels, label_points, label_offsets):
        ax.text(point[0] + offset[0], point[1] + offset[1], label, fontsize=12, ha='right')

    # Denote the lengths of the lines
    # Randomly choose a side to label lengths
    sides = [(point_0, point_1, length_0), (point_0, point_2, length_1)]
    side = sides[np.random.randint(len(sides))]
    mid_point = (side[0] + side[1]) / 2
    ax.text(mid_point[0], mid_point[1], str(side[2]), fontsize=10, va='bottom')

    # Add square notations to show 90 degree angles
    square_size = min(length_0, length_1) * 0.1  # Size of the square notation
    square_points = [point_0, point_0 + np.array([square_size * np.cos(angle_rad), square_size * np.sin(angle_rad)]),
                     point_0 + np.array([square_size * np.sin(angle_rad), -square_size * np.cos(angle_rad)])]
    ax.plot(*zip(*[square_points[0], square_points[1], square_points[1] + square_points[2] - square_points[0], square_points[2], square_points[0]]), '-k')

    plt.axis('off')  # Hide the axes
    plt.show()

# Example usage
fig, ax = plt.subplots()
# ax.set_xlim(0, 1000)
# ax.set_ylim(0, 1000)

draw_rectangle(['A', 'B', 'C', 'D'], (1, 1), 3, 2, 30, fig=fig, ax=ax)



