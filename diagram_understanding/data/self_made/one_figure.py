import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import json

def append_to_json(i, points, sides, file_path='1/rectangles.json'):
    new_data = {
        "index": i,
        "labelled": False,
        "points": points,
        "annotated sides": sides
    }

    # Path to the rectangles.json file


    try:
        # Read the existing data
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):  # Ensure the top-level structure is a list
                data = [data]
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Initialize as an empty list if the file doesn't exist or is empty

    # Append the new data
    data.append(new_data)

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def draw_rectangle(labels, coordinate_0, length_0, length_1, angle_0, index):



    # Convert angle from degrees to radians for numpy calculations
    angle_rad = np.deg2rad(angle_0)

    # Calculate the coordinates of the rectangle's vertices
    point_0 = np.array(coordinate_0)
    point_1 = point_0 + np.array([length_0 * np.cos(angle_rad), length_0 * np.sin(angle_rad)])
    point_2 = point_0 + np.array([-length_1 * np.sin(angle_rad), +length_1 * np.cos(angle_rad)])
    point_3 = point_2 + (point_1 - point_0)

    # print(f"point_0: {point_0}, point_1: {point_1}, point_2: {point_2}, point_3: {point_3}")

    #assert that the rectangle is not out of the image
    assert point_0[0] >= 0 and point_0[1] >= 0 and point_1[0] >= 0 and point_1[1] >= 0 and point_2[0] >= 0 and point_2[
        1] >= 0 and point_3[0] >= 0 and point_3[1] >= 0, f"Rectangle {index} is out of the image"
    assert point_0[0] <= 1000 and point_0[1] <= 1000 and point_1[0] <= 1000 and point_1[1] <= 1000 and point_2[
        0] <= 1000 and point_2[1] <= 1000 and point_3[0] <= 1000 and point_3[
               1] <= 1000, f"Rectangle {index} is out of the image"
    # print(f"\nRectangle {i} has coordinates of {point_0}, {point_1}, {point_2}, {point_3}")
    # Setup the plot

    fig, ax = plt.subplots()
    # Start a new figure for each rectangle
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_aspect('equal', 'box')
    plt.axis('off')  # Hide the axes




    ax.plot(*zip(*[point_0, point_1, point_3, point_2, point_0]), '-k')

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
    sides = [(point_0, point_1, length_0), (point_0, point_2, length_1), (point_2, point_3, length_0), (point_1, point_3, length_1)]
    annotated_sides = random.sample(sides, random.randint(1, 4))
    for side in annotated_sides:
        if random.choice([True, False]):
            mid_point = (side[0] + side[1]) / 2
            ax.text(mid_point[0], mid_point[1], str(side[2]), fontsize=10, va='bottom')



    # Add square notations to show 90 degree angles
    square_size = min(length_0, length_1) * random.randint(8,15)/100  # Size of the square notation

    # for each vertex, randomly choose to add a square
    add_square = [ random.choice([True, False]), random.choice([True, False]), random.choice([True, False]), random.choice([True, False])]

    if add_square[0]:
        square_0 = [point_0, point_0  +np.array([square_size * np.cos(angle_rad), square_size * np.sin(angle_rad)]),
                    point_0 + np.array([-square_size * np.sin(angle_rad), + square_size * np.cos(angle_rad)])]
        ax.plot(*zip(*[square_0[0], square_0[1], square_0[1] + square_0[2] - square_0[0], square_0[2], square_0[0]]), '-k')


    if add_square[1]:
        square_1 =  [point_1, point_1 + np.array([-square_size * np.cos(angle_rad), -square_size * np.sin(angle_rad)]),
                    point_1 + np.array([-square_size * np.sin(angle_rad), square_size * np.cos(angle_rad)])]
        ax.plot(*zip(*[square_1[0], square_1[1], square_1[1] + square_1[2] - square_1[0], square_1[2], square_1[0]]), '-k')


    if add_square[2]:
        square_2 = [point_2, point_2 + np.array([square_size * np.cos(angle_rad), square_size * np.sin(angle_rad)]),
                    point_2 + np.array([square_size * np.sin(angle_rad), -square_size * np.cos(angle_rad)])]
        ax.plot(*zip(*[square_2[0], square_2[1], square_2[1] + square_2[2] - square_2[0], square_2[2], square_2[0]]), '-k')

    if add_square[3]:
        square_3 = [point_3, point_3 + np.array([-square_size * np.cos(angle_rad), -square_size * np.sin(angle_rad)]),
                    point_3 + np.array([square_size * np.sin(angle_rad), -square_size * np.cos(angle_rad)])]
        ax.plot(*zip(*[square_3[0], square_3[1], square_3[1] + square_3[2] - square_3[0], square_3[2], square_3[0]]), '-k')

    plt.savefig(f'1/unlabelled_rectangle_{i}.png', dpi=300, bbox_inches='tight')  # Adjust filename and dpi as needed
    # plt.show()

    return [point_0, point_1, point_2, point_3], annotated_sides


def draw_triangle(labels, coordinate_0, length_0, length_1, angle_0, index):
    # Convert angle from degrees to radians for numpy calculations
    angle_rad = np.deg2rad(angle_0)

    # Calculate the coordinates of the first two vertices
    point_0 = np.array(coordinate_0)
    point_1 = point_0 + np.array([length_0, 0])  # First side is along the x-axis

    # Rotate the second side by the specified angle to find the third vertex
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)], [np.sin(angle_rad), np.cos(angle_rad)]])
    point_2 = point_0 + np.dot(rotation_matrix, np.array([length_1, 0]))

    # Ensure the triangle is within bounds
    assert all(0 <= p[0] <= 1000 and 0 <= p[1] <= 1000 for p in [point_0, point_1, point_2]), f"Triangle {index} is out of the image"

    # Setup the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_aspect('equal', 'box')
    plt.axis('off')

    # Draw the triangle
    ax.plot(*zip(*[point_0, point_1, point_2, point_0]), '-k')

    # Label the vertices
    label_offset = 0.2
    label_points = [point_0, point_1, point_2]
    label_offsets = [np.array([-label_offset, -label_offset]),
                     np.array([label_offset, -label_offset]),
                     np.array([-label_offset, label_offset])]
    for label, point, offset in zip(labels, label_points, label_offsets):
        ax.text(point[0] + offset[0], point[1] + offset[1], label, fontsize=12, ha='right')

    # Annotate the sides with lengths
    sides = [(point_0, point_1, length_0), (point_1, point_2, np.linalg.norm(point_2 - point_1)), (point_0, point_2, length_1)]
    for side in sides:
        mid_point = (side[0] + side[1]) / 2
        ax.text(mid_point[0], mid_point[1], f"{side[2]:.2f}", fontsize=10, va='bottom')

    # plt.savefig(f'triangle_{index}.png', dpi=300, bbox_inches='tight')
    plt.show()  # Uncomment to display the figure

    return [point_0, point_1, point_2], sides




# # Rectangle Example
#
# labels = random.sample(empty_label.candidates, 4)
#
# i = 0
# j = 0
# while i<100:
#
#     x_0 = random.randint(100, 900)
#     y_0 = random.randint(100, 900)
#     length_0 = random.randint(150, 900)
#     length_1 = random.randint(150, 900)
#     angle_0 = random.randint(0, 359)
#
#
#     try:
#
#         points, sides = draw_rectangle(labels, (x_0, y_0), length_0, length_1, angle_0, index=i)
#         print(f"test: {i}")
#         points_list = [point.tolist() for point in points]
#         sides  = [sides[0][2], sides[1][2], sides[2][2], sides[3][2]]
#         print(f"i: {i}")
#         append_to_json(i, points_list, sides)
#         i += 1
#     except :
#         j+=1
#         print(f"j: {j}")








# except:
#     print(j)
#     j+=1



# draw_rectangle(labels, (500, 500), 100, 200, 45, fig=fig, ax=ax)


labels = ['A', 'B', 'C']
coordinate_0 = [500, 500]
length_0 = 300
length_1 = 300
angle_0 = 45
index = 1

draw_triangle(labels, coordinate_0, length_0, length_1, angle_0, index)


