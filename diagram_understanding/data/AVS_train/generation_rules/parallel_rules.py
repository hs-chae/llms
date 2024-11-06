import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import math
import json

def random_angle():
    return np.random.uniform(np.pi/9, 17/9*np.pi)

def rotate_vector(vector, angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) @ np.array(vector)


def random_coord(start = 10, end = 990):
    return np.random.uniform(start, end)


def line_already_in(diagram, point1, point2):
    for line in diagram.lines:
        if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
            return True
    return False

def label_point(diagram):
    ind = 0
    while True:
        label = random.choice(capitals.candidates)
        if label not in [point.label for point in diagram.points]:
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.points)} points of list : {[point.label for point in diagram.points]}')


        ind+=1

def random_length():
    if random.random() < 0.5:
        return random.choice(small_letters.candidates)
    else:
        return int(random.uniform(1, 30))


def add_radius(center_x, center_y, radius):
    angle = random_angle()
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    length = f'{random_length()}'
    return (x, y, length)


#Objects definition
class Point:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.label = label

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.label})'


class Line:
    def __init__(self, point1 : Point, point2 : Point, label, infinite=False, tickmarks = 0, dotted = False):
        self.passing_points = [point1, point2]
        self.point1 = point1
        self.point2 = point2
        self.label = label
        self.infinite = infinite
        self.tickmarks = tickmarks
        self.dotted = dotted

    def __str__(self):
        return f'Line({self.passing_points}, {self.label}, {self.infinite})'

class Circle:
    def __init__(self, center, radius, label):
        self.center = center
        self.radius = radius
        self.label = label

    def __str__(self):
        return f'Circle({self.center}, {self.radius}, {self.label})'

class Triangle:
    def __init__(self, point1, point2, point3, label = ''):
        self.vertices = [point1, point2, point3]
        # self.label = label
        self.label = f'Triangle({point1.label}{point2.label}{point3.label})'

    def __str__(self):
        return f'Triangle({self.vertices}, {self.label})'

class Curve:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __str__(self):
        return f'Curve({self.label})'



#Diagram definition
class Diagram:
    def __init__(self, points=[], lines=[], circles=[], triangles=[], squares=[], steps=[]):
        self.points = points
        self.lines = lines
        self.circles = circles
        self.triangles = triangles
        self.squares = squares
        self.steps = steps
        self.entities = []
        self.perpendiculars = []
        self.curves = []
        self.angles = []

        # for line in self.lines:
        #     for point in line.passing_points:
        #         assert point in self.points
        #
        # for triangle in self.triangles:
        #     for point in triangle.vertices:
        #         assert point in self.points




def normalize(vector):
    (x, y) = vector
    magnitude = (x**2 + y**2)**0.5
    return (x / magnitude, y / magnitude)

def assert_coord_in_range(x,y):
    return x < 1000 and x > 0 and y < 1000 and y > 0

def add_free_point(diagram : Diagram):
    x_coord, y_coord = random_coord(), random_coord()
    label = label_point(diagram)
    diagram.points.append(Point(x_coord, y_coord, label))
    # diagram.entities.append(f'Point({label})')
    return diagram

def add_free_line(diagram: Diagram):
    while True:
        x1, y1 = random_coord(), random_coord()
        x2, y2 = random_coord(), random_coord()
        length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if length > 300:
            break

    label1 = label_point(diagram)

    while True:
        label2 = label_point(diagram)
        if label2 != label1:
            break

    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind += 1
    length = int(length)


    # label = random.sample([label, f'{length}'],1)[0]
    diagram.points.append(Point(x1, y1, label1))
    diagram.points.append(Point(x2, y2, label2))
    label = random.choice([label, "", "", "", "", "", ""])

    if len(label) == 0:
        diagram.entities.append(('line', [diagram.points[-2].label, diagram.points[-1].label]))
    else:
        diagram.entities.append(('labelled_line', [diagram.points[-2].label, diagram.points[-1].label, label]))


    diagram.lines.append(Line(diagram.points[-2], diagram.points[-1], label))

    # diagram.entities.extend([f'{label} : Line({label1}{label2})'])
    return diagram

def add_free_point_with_line(diagram : Diagram):
    p1 = random.choice(diagram.points)
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        length = ((p1.x - x_coord)**2 + (p1.y - y_coord)**2)**0.5
        label = label_point(diagram)
        if length > 200:
            break
        if ind  >30:
            return diagram
        ind += 1
    ind = 0
    while True:
        label_l = random.choice(small_letters.candidates)
        if label_l not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind += 1
    diagram.points.append(Point(x_coord, y_coord, label))

    label_l = random.choice([label_l, "", "", "", "", "", ""])
    diagram.lines.append(Line(p1, diagram.points[-1], label_l))
    if len(label) == 0:
        diagram.entities.append(('line', [diagram.points[-2], diagram.points[-1]]))
    else:
        diagram.entities.append(('labelled_line', [diagram.points[-2].label, diagram.points[-1].label, label_l]))




    return diagram

def add_line(diagram : Diagram):
    try:
        ind = 0
        while True:

            point1, point2 = random.sample(diagram.points, 2)
            length = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5


            #assert that the line is not already in the diagram
            already_in = False
            for line in diagram.lines:
                if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
                    already_in = True

            if ind > 100:
                raise ValueError('No possible line found')
            elif already_in: print('already in')
            else: break

            ind += 1


        label = random.choice(small_letters.candidates.extend(["","","","","",""]))
        diagram.lines.append(Line(point1, point2, label))
        if len(label) == 0 :
            diagram.entities.append(('line', [point1.label, point2.label]))
        else:
            diagram.entities.append(('labelled_line', [point1.label, point2.label,label]))


        return diagram
    except: return diagram

def add_infinite_line(diagram : Diagram):

    point1, point2 = random.sample(diagram.points, 2)
    label = ''
    diagram.lines.append(Line(point1, point2, label, infinite=True))
    diagram.entities.append(('infinite_line',[point1.label, point2.label]))
    return diagram


def add_circle(diagram : Diagram, radius = None):

    center = random.choice(diagram.points)
    max_rad = min(center.x, center.y, 1000 - center.x, 1000 - center.y)
    if radius is None :
        ind = 0
        while True:
            radius = random.uniform(150, max_rad)
            if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
                break
            if ind > 10:
                return diagram
            ind += 1

    else:
        radius = radius
        assert assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius)


    # label = random.choice(small_letters.candidates)
    label = f'({center.label},{radius})'
    different_pt_label = label_point(diagram)
    diagram.circles.append(Circle(center, radius, label))
    diagram.entities.append(('circle', [f'{center.label}', f'{different_pt_label}']))
    return diagram

def add_free_circle(d):
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        center = Point(x_coord, y_coord, label_point(d))
        radius = int(random.uniform(200,500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
            break
        if ind> 30:
            return d
        ind += 1

    d.points.append(center)
    d.circles.append(Circle(center, radius, f'({center.label},{radius})'))
    d.entities.append(('circle',[f'{center.label}',f'{label_point(d)}']))

    return d

def circle_with_radius(d):
    while True:
        center = Point(random_coord(), random_coord(), label_point(d))
        radius = int( random.uniform(50, 500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
            break
    circle = Circle(center, radius, '')
    angle = random_angle()
    x,y  = center.x + radius * np.cos(angle), center.y + radius * np.sin(angle)
    P = Point(x, y, "")
    length = random_length()
    d.points.append(center)
    d.circles.append(circle)
    d.lines.append(Line(center, P, label=length, dotted=True))
    # d.entities.append(f'Circle with center {center.label} and radius {length}')
    d.entities.append(('circle_with_radius', [center.label, f'{length}']))
    return d

###

#
# def parallel_0(d):
#     l = random.choice(d.lines)
#     A, B = l.point1, l.point2
#
#     vector = (B.x - A.x, B.y - A.y)
#
#     # tk = random.randint(0,5)
#
#     while True:
#         scale = random.uniform(-5, 5)
#         x,y = random_coord(), random_coord()
#         if assert_coord_in_range(x+vector[0]*scale, y+vector[1]*scale):
#             break
#
#     while True:
#
#         C = Point(x+vector[0]*scale, y+vector[1]*scale, label_point(d))
#         D = Point(x, y, label_point(d))
#         if C.label != D.label:
#             break
#
#     d.points.extend([C, D])
#     d.lines.append(Line(C, D, label=""))
#     d.lines.append(Line(A, B, label=""))
#     # d.entities.append(f'Line({C.label}{D.label}) parallel to Line({A.label}{B.label})')
#     d.entities.append(('parallel', [A.label, B.label, C.label, D.label]))
#     return d

def parallel_1(d):
    # l = random.choice(d.lines)
    # A, B = l.point1, l.point2

    A = Point(random_coord(), random_coord(), label_point(d))
    B = Point(random_coord(), random_coord(), label_point(d))



    #define numpy vector of difference of A, B
    AB_diff = np.array([B.x - A.x, B.y - A.y])

    # tk = random.randint(0,5)
    num_not_prl = random.randint(1, 5)

    new_points_0 = []
    new_points_1 = []
    new_lines = []
    new_labels = []



    #Generate a parallel line
    while True:
        scale = random.uniform(-5, 5)
        x, y = random_coord(), random_coord()
        vector = AB_diff
        x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
        if assert_coord_in_range(x_end, y_end):
            break

    while True:
        label0 = label_point(d)
        if label0 not in new_labels:
            new_labels.append(label0)
            break

    while True:
        label1 = label_point(d)
        if label1 not in new_labels:
            new_labels.append(label1)
            break

    C = Point(x, y, label0)
    D = Point(x_end, y_end, label1)


    new_lines.append(Line(C, D, label=""))



    #Generate non-parallel lines
    for j in range(num_not_prl):
        while True:
            angle = random_angle()
            scale = random.uniform(-5, 5)
            x,y = random_coord(), random_coord()
            vector = rotate_vector(AB_diff, angle)
            x_end, y_end = x + vector[0]*scale, y + vector[1]*scale
            if assert_coord_in_range(x_end, y_end):
                break

        while True:
            label0 = label_point(d)
            if label0 not in new_labels:
                new_labels.append(label0)
                break

        while True:
            label1 = label_point(d)
            if label1 not in new_labels:
                new_labels.append(label1)
                break

        new_points_0.append(Point(x, y, label0))
        new_points_1.append(Point(x_end, y_end, label1))
        new_lines.append(Line(new_points_0[-1], new_points_1[-1], label=""))


    d.points.extend([A, B])
    d.lines.append(Line(A, B, label=""))
    d.points.extend([C, D])

    d.points.extend(new_points_0)
    d.points.extend(new_points_1)
    d.lines.extend(new_lines)

    d.entities.append(('parallel_1', [A.label, B.label, C.label, D.label] + [p.label for p in new_points_0] + [p.label for p in new_points_1], len(new_points_0)))

    return d


def parallel_2(d):

    A = Point(random_coord(), random_coord(), label_point(d))
    B = Point(random_coord(), random_coord(), label_point(d))
    # define numpy vector of difference of A, B
    AB_diff = np.array([B.x - A.x, B.y - A.y])


    num_prl = random.randint(1, 5)
    num_not_prl = random.randint(1, 5)

    prl_points_0 = []
    prl_points_1 = []
    non_prl_points_0 = []
    non_prl_points_1 = []
    new_lines = []
    new_labels = []

    #Generate parallel lines
    for i in range(num_prl):
        while True:
            scale = random.uniform(-5, 5)
            x, y = random_coord(), random_coord()
            vector = AB_diff
            x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
            if assert_coord_in_range(x_end, y_end):
                break

        while True:
            label_0 = label_point(d)
            if label_0 not in new_labels:
                new_labels.append(label_0)
                break

        while True:
            label_1 = label_point(d)
            if label_1 not in new_labels:
                new_labels.append(label_1)
                break

        prl_points_0.append(Point(x, y, label_0))
        prl_points_1.append(Point(x_end, y_end, label_1))
        new_lines.append(Line(prl_points_0[-1], prl_points_1[-1], label=""))


    #Generate non-parallel lines
    for j in range(num_not_prl):
        while True:
            scale = random.uniform(-5, 5)
            angle = random_angle()
            x, y = random_coord(), random_coord()
            vector = rotate_vector(AB_diff, angle)
            x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
            if assert_coord_in_range(x_end, y_end):
                break

        while True:
            label_0 = label_point(d)
            if label_0 not in new_labels:
                new_labels.append(label_0)
                break

        while True:
            label_1 = label_point(d)
            if label_1 not in new_labels:
                new_labels.append(label_1)
                break

        non_prl_points_0.append(Point(x, y, label_0))
        non_prl_points_1.append(Point(x_end, y_end, label_1))
        new_lines.append(Line(non_prl_points_0[-1], non_prl_points_1[-1], label=""))

    d.points.extend([A, B])
    d.lines.append(Line(A, B, label=""))
    d.points.extend(prl_points_0)
    d.points.extend(prl_points_1)
    d.points.extend(non_prl_points_0)
    d.points.extend(non_prl_points_1)
    d.lines.extend(new_lines)

    # print("=================================\n=================================\n=================================32112313131231")
    d.entities.append(('parallel_2', [A.label, B.label, f'{num_prl}', f'{num_not_prl}']))
    # print(f"Parallel_2 : {A.label}{B.label}, {num_prl}, {num_not_prl}")
    return d




def parallel_3(diagram):
    #"X = parallelogram(A, B, C)": { "Description": "Construct X such that ABCX is a parallelogram" },
    while len(diagram.points)< 3:
        diagram = add_free_point(diagram)

    A, B, C = random.sample(diagram.points, 3)
    vector = (B.x - A.x, B.y - A.y)
    D_x = C.x - vector[0]
    D_y = C.y - vector[1]
    assert assert_coord_in_range(D_x, D_y)

    D_label = label_point(diagram)

    D = Point(D_x, D_y, D_label)
    diagram.points.append(D)
    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # diagram.entities.append(f'Parallelogram({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('parallel_3', [A.label, B.label, C.label, D.label]))
    return diagram

def parallel_4(diagram: Diagram):

    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)
    # Randomly select two points A, B to form the base AB of the trapezoid
    A, B = random.sample(diagram.points, 2)

    # Calculate the directional vector for AB and its perpendicular
    AB_vector = (B.x - A.x, B.y - A.y)
    perp_AB = (-AB_vector[1], AB_vector[0])  # Rotate AB_vector by 90 degrees to get perpendicular

    # Normalize the perpendicular vector
    perp_AB_normalized = normalize(perp_AB)

    # Select a random angle θ < π/2 for rotation
    theta = random.uniform(0, np.pi / 6)

    # Calculate the direction for AD by rotating the perpendicular direction by θ
    AD_direction = (perp_AB_normalized[0] * np.cos(theta) - perp_AB_normalized[1] * np.sin(theta),
                    perp_AB_normalized[0] * np.sin(theta) + perp_AB_normalized[1] * np.cos(theta))

    # Calculate the direction for BC by rotating the perpendicular direction by -θ
    BC_direction = (perp_AB_normalized[0] * np.cos(-theta) - perp_AB_normalized[1] * np.sin(-theta),
                    perp_AB_normalized[0] * np.sin(-theta) + perp_AB_normalized[1] * np.cos(-theta))

    # Decide on a length for AD and BC
    leg_length = random.uniform(50, 400)  # Example range for the leg length

    # Calculate points D and C using the determined directions and length
    Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
    Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length

    # Check if D and C are within the diagram range
    assert assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy)

    # Create points C and D
    C_label, D_label = random.sample(capitals.candidates, 2)
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)
    diagram.points.extend([C, D])

    # Add lines to form the trapezoid
    diagram.lines.extend([
        Line(A, B, label=""),  # Base AB
        Line(B, C, label=""),  # Side BC
        Line(C, D, label=""),  # Top CD, parallel to AB
        Line(D, A, label="")   # Side AD
    ])

    # diagram.entities.extend([
    #     f'Point({C.label})', f'Point({D.label})',
    #     f'Line({A.label}{B.label})', f'Line({B.label}{C.label})',
    #     f'Line({C.label}{D.label})', f'Line({D.label}{A.label})',
    #     f'Equilateral Trapezoid({A.label}{B.label}{C.label}{D.label})'
    # ])

    diagram.entities.append(('parallel_4', [A.label, B.label, C.label, D.label]))
    # print(f"=====A,B,C,D : {A.label}{B.label}{C.label}{D.label}")
    return diagram
