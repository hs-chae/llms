import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
from labels import *
import random
import json
from rules import *
from create_tree import *
import math


fixed_color = 'black'
fix_color= False

def plot_point(ax, label = '', coord = (random.randint(0, 1000),random.randint(0, 1000)), color = random.choice(colors.candidates)):
    if fix_color:
        color = fixed_color

    # Coordinates for the free point X
    x_coord, y_coord = coord

    # Possible vertical alignments and colors
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Basic color abbreviations
    # random_color = random.choice(colors)

    # Plotting point X with a random color
    ax.plot(x_coord, y_coord, marker='o', color=color, markersize=3)  # 'o' stands for circle marker

    # Adding a label "X" next to the point with random vertical alignment and color
    ax.text(x_coord + 20, y_coord, label, fontsize=12, verticalalignment=random_vertical_alignment, color='black')

def plot_line(ax, label, point1 : Point, point2 : Point, color = random.choice(colors.candidates), infinite = False, tickmarks = 0, dotted = False):
    if fix_color:
        color = fixed_color

    # Coordinates for the free point X
    x1, y1 = point1.coord
    x2, y2 = point2.coord

    # Possible vertical alignments and colors
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Basic color abbreviations
    # random_color = random.choice(colors)

    if not infinite:
        # Plotting the line between the two points with a random color
        if dotted:
            ax.plot([x1, x2], [y1, y2], color=color, linestyle='dashed')
        else : ax.plot([x1, x2], [y1, y2], color=color)  # 'o' stands for circle marker
        ax.text((x1 + x2)/2 + 20, (y1 + y2)/2, label, fontsize=12, verticalalignment=random_vertical_alignment, color='black')
    else:
        direction = np.array([x2 - x1, y2 - y1])
        norm_direction = direction / np.linalg.norm(direction)

        # Extend the line by a large factor (e.g., 10000) beyond the plot limits
        factor = 10000
        new_x1, new_y1 = np.array([x1, y1]) - factor * norm_direction
        new_x2, new_y2 = np.array([x2, y2]) + factor * norm_direction

        ax.plot([new_x1, new_x2], [new_y1, new_y2], color=color)  # Dashed line for visual distinction
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, label, fontsize=12, verticalalignment=random_vertical_alignment,
                color='black')

    if tickmarks > 0:
        # Draw tick marks
        tick_length = 10  # Length of the tick marks
        for i in range(tickmarks):
            offset = 10 * (i - tickmarks / 2 + 0.5)  # Offset each tick mark for visibility

            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2
            unit_vec = np.array([x2 - x1, y2 - y1]) / np.linalg.norm(np.array([x2 - x1, y2 - y1]))
            perp_unit_vector = np.array([y2 - y1, x1 - x2]) / np.linalg.norm(np.array([y2 - y1, x1 - x2]))

            tick_start_x = midpoint_x + offset * unit_vec[0] - tick_length * perp_unit_vector[0]
            tick_start_y = midpoint_y + offset * unit_vec[1] - tick_length * perp_unit_vector[1]
            tick_end_x = tick_start_x + 2* tick_length * perp_unit_vector[0]
            tick_end_y = tick_start_y + 2* tick_length * perp_unit_vector[1]
            ax.plot([tick_start_x, tick_end_x], [tick_start_y, tick_end_y], 'k-')  # 'k-' for black line


def plot_circle(ax, label, center, radius, color = random.choice(diverse_colors.candidates)):
    if fix_color:
        color = fixed_color
    # Coordinates for the free point X
    x, y = center.coord


    # Possible vertical alignments and colors
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Basic color abbreviations
    # random_color = random.choice(colors)

    # Plotting point X with a random color
    circle = plt.Circle((x, y), radius, color=color, fill=False)  # 'o' stands for circle marker
    ax.add_artist(circle)

    # Adding a label "X" next to the point with random vertical alignment and color
    ax.text(x + 20, y, label, fontsize=12, verticalalignment=random_vertical_alignment, color='black')

def plot_triangle(ax, point1, point2, point3, diagram=Diagram(), mark_points = False, color = random.choice(diverse_colors.candidates)):
    if fix_color:
        color = fixed_color
    # Coordinates for the points
    x1, y1 = point1.coord
    x2, y2 = point2.coord
    x3, y3 = point3.coord

    # Define lines of the triangle
    lines = [(point1,point2), (point2, point3), (point3, point1)]
    #check if the lines are already in the diagram
    for line in lines:
        if line not in diagram.lines and (line[1],line[0]) not in diagram.lines:
            plot_line(ax, label='', point1=line[0], point2=line[1], color=color)

    if mark_points:
        plot_point(ax, label=point1.label, coord=point1.coord)
        plot_point(ax, label=point2.label, coord=point2.coord)
        plot_point(ax, label=point3.label, coord=point3.coord)


def plot_perpendicularity(ax, line1, line2, intersection):
    if fix_color:
        color = fixed_color
    # Coordinates for the points
    x1, y1 = line1.point1.x, line1.point1.y
    x2, y2 = line1.point2.x, line1.point2.y
    x3, y3 = line2.point1.x, line2.point1.y
    x4, y4 = line2.point2.x, line2.point2.y
    x5, y5 = intersection.x, intersection.y

    ind = 0
    while True:
        # Choosing a random point from line1:

        x_rand, y_rand = random.choice([(x1, y1), (x2, y2)])
        if not (-1 < x_rand - x5 < 1 and  -1 < y_rand - y5 < 1):
            break
        elif ind > 5 :
            print(f"x1,y1 : {x1, y1}")
            print(f"x2,y2 : {x2, y2}")
            print(f"x_rand,y_rand : {x_rand, y_rand}")
            raise ValueError("Random point is too close to the intersection point")
        ind += 1


    ind = 0
    while True:
        # Choosing a random point from line2:
        x_rand2, y_rand2 = random.choice([(x3, y3), (x4, y4)])
        if not ( -1 < x_rand2 - x5 < 1 and -1 < y_rand2 - y5 < 1):
            break
        elif ind > 5 :
            print(f"x3,y3 : {x3, y3}")
            print(f"x4,y4 : {x4, y4}")
            print(f"x_rand2,y_rand2 : {x_rand2, y_rand2}")
            raise ValueError("Random point is too close to the intersection point")
        ind += 1

    direction1 = np.array([x_rand - x5, y_rand - y5])
    direction2 = np.array([x_rand2 - x5, y_rand2 - y5])
    length1 = np.linalg.norm(direction1)
    length2 = np.linalg.norm(direction2)
    length = (length1 + length2)/20

    norm_direction1 = direction1 * length / length1
    norm_direction2 = direction2 * length / length2

    #draw the square mark
    ax.plot([x5+ norm_direction2[0], x5 + norm_direction1[0] +  norm_direction2[0]], [y5+ norm_direction2[1], y5+ norm_direction1[1]+ norm_direction2[1] ], color='black')
    ax.plot([x5 + norm_direction1[0] , x5+ norm_direction2[0] + norm_direction1[0] ], [y5+ norm_direction1[1], y5+ norm_direction1[1] + norm_direction2[1]], color='black')

def plot_curve(ax,x,y, t_start=0,t_end=1000 ,color = random.choice(diverse_colors.candidates)):
    if fix_color:
        color = fixed_color
    parameter= np.linspace(t_start, t_end, 1000)
    ax.plot(x, y, color=color)




def plot_angle(ax, line1, line2, intersection, color='black', label = ''):
    if fix_color:
        color = fixed_color
        # Coordinates for the points
    x1, y1 = line1.point1.coord
    x2, y2 = line1.point2.coord
    x3, y3 = line2.point1.coord
    x4, y4 = line2.point2.coord
    x_inter, y_inter = intersection.coord

    directions = []
    for (xi, yi) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
        if not (-1 < xi - x_inter < 1 and -1 < yi - y_inter < 1):
            directions.append((xi - x_inter, yi - y_inter))

    # Sort the directions clockwise
    directions.sort(key=lambda p: math.atan2(p[1], p[0]))
    ind = random.choice(range(len(directions) - 1))
    xi, yi = directions[ind]
    xj, yj = directions[ind + 1]

    direction1 = np.array([xi, yi])
    direction2 = np.array([xj, yj])
    norm1 = np.linalg.norm(direction1)
    norm2 = np.linalg.norm(direction2)

    # Normalize the direction vectors
    norm_direction1 = direction1 / norm1
    norm_direction2 = direction2 / norm2

    radius = max(50, min(norm1, norm2) / 5)

    # Calculate the angles relative to the positive x-axis
    angle1 = math.atan2(norm_direction1[1], norm_direction1[0])
    angle2 = math.atan2(norm_direction2[1], norm_direction2[0])

    # Calculate the angle between the lines
    ang = abs(angle2 - angle1)
    if ang > math.pi:
        ang = 2 * math.pi - ang

    # Determine the start and end angles for the arc
    start_angle = min(angle1, angle2)
    end_angle = max(angle1, angle2)

    # Plot the arc
    arc = Arc((x_inter, y_inter), 2 * radius, 2 * radius, angle=0, theta1=math.degrees(start_angle),
              theta2=math.degrees(end_angle), color=color)

    ax.add_artist(arc)

    # Add the angle label at the midpoint of the arc
    mid_angle = (start_angle + end_angle) / 2
    label_angle = math.degrees(ang)

    # Adjust the label position based on the angle value
    if label_angle < 10 or label_angle > 170:
        label_x = x_inter + radius * math.cos(mid_angle) * 1.2
        label_y = y_inter + radius * math.sin(mid_angle) * 1.2
    else:
        label_x = x_inter + radius * math.cos(mid_angle)
        label_y = y_inter + radius * math.sin(mid_angle)

    ax.text(label_x, label_y, f"{int(label_angle)}°", fontsize=10, color='black')



def plot_diagram(ax, diagram):
    # fig, ax = plt.subplots()
    # ax.set_xlim(0, 1000)
    # ax.set_ylim(0, 1000)

    for point in diagram.points:
        plot_point(ax, label=point.label, coord=point.coord)

    for line in diagram.lines:
        plot_line(ax, label=line.label, point1=line.point1, point2=line.point2, infinite=line.infinite, tickmarks=line.tickmarks, dotted=line.dotted)

    for tup in diagram.perpendiculars:
        line1, line2, intersection = tup
        plot_perpendicularity(ax, line1, line2, intersection)

    for circle in diagram.circles:
        # print(f"BEFORE PLOTTING CIRCLE {circle.label}")
        plot_circle(ax, label='', center=circle.center, radius=circle.radius)
        # print(f"AFTER PLOTTING CIRCLE {circle.label}")
    for triangle in diagram.triangles:
        plot_triangle(ax, point1=triangle.vertices[0], point2=triangle.vertices[1], point3=triangle.vertices[2])

    for curve in diagram.curves:
        plot_curve(ax,curve.x,curve.y)

    for ang in diagram.angles:
        line1, line2, intersection, ang_label = ang
        plot_angle(ax, line1, line2, intersection, label = ang_label)

    # for square in diagram.squares:
    #     plot_square(ax, label='', point1=square.point1, point2=square.point2, point3=square.point3, point4=square.point4)

    plt.show()
