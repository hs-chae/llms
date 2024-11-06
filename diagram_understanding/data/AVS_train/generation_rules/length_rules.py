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


def label_line(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label not in [line.label for line in diagram.lines]:
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.lines)} lines of list : {[line.label for line in diagram.lines]}')
        ind += 1
def random_length():
        return int(random.uniform(200, 700))


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
    diagram = add_free_point(diagram)
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


def length_1(d):

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label2 != label1:
            break
    new_labels.extend([label1, label2])

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    #Generate longer line
    ind = 0
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break
    while True:
        label4 = label_point(d)
        if label4 not in new_labels:
            new_labels.append(label4)
            break

    C = Point(X0, Y0, label3)
    D = Point(X1, Y1, label4)

    d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, ''), Line(C, D, '')])
    d.entities.append(('length_1', [A.label, B.label, C.label, D.label]))
    return d

def length_2(d):

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_line(d)
    new_labels.append(label1)

    A = Point(x0, y0, "")
    B = Point(x1, y1, "")

    #Generate longer line
    ind = 0
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break


    C = Point(X0, Y0, "")
    D = Point(X1, Y1, "")

    # d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, label1), Line(C, D, label3)])
    d.entities.append(('length_2', [label1, label3]))
    return d


def length_3(d):
    #Generate a longer line and other shorter lines
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_line(d)
    new_labels.append(label1)

    A = Point(x0, y0, "")
    B = Point(x1, y1, "")

    ind = 0
    #Generate longer line
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    C = Point(X0, Y0, "")
    D = Point(X1, Y1, "")

    #Generate shorter lines
    short_count = random.randint(3, 5)
    short_lines = []
    for i in range(short_count):
        while True:
            x0, y0 = random_coord(), random_coord()
            length = random_length()
            angle = random_angle()
            x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
            if assert_coord_in_range(x1, y1):
                break

        while True:
            label = label_line(d)
            if label not in new_labels:
                new_labels.append(label)
                break

        short_lines.append(Line(Point(x0, y0, ""), Point(x1, y1, ""), label))

    d.lines.extend([Line(A, B, label1), Line(C, D, label2)])
    d.lines.extend(short_lines)
    d.entities.append(('length_3', [label1, label2] + [line.label for line in short_lines]))
    return d


def length_4(d):
    #Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    #Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if radius < length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius, y0 - radius):
            break
        elif ind > 30:
            print(f"breakout of loop with radius {radius} and length {length}")
            return d
        else:
            # print("too large radius")
            ind+=1


    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_4', [A.label, B.label, C.label]))
    return d

def length_5(d):
    # Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if radius > length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        elif ind > 30:
            print(f"breakout of loop with radius {radius} and length {length}")
            return d
        else:
            # print("too large radius")
            ind+=1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_5', [A.label, B.label, C.label]))
    return d

def length_6(d):
    # Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    # Generate a circle
    ind=0
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = length
        if assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius, y0 - radius):
            break
        elif ind > 30:
            print(f"breakout of loop with lnegth {length}")
            return d
        else:
            # print("too large radius")
            ind+=1


    ind=0
    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break



    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_6', [A.label, B.label, C.label]))
    return d


def length_7(d):
    # Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if 2*radius < length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_7', [A.label, B.label, C.label]))

    return d

def length_8(d):
    #Generate a anchor point
    anchor = Point(random_coord(), random_coord(), label_point(d))
    new_label = [anchor.label]

    #Generate the furthest point.
    while True:
        x0, y0 = random_coord(), random_coord()
        if ((x0 - anchor.x)**2 + (y0 - anchor.y)**2)**0.5 > 300:
            break
    while True:
        label = label_point(d)
        if label not in new_label:
            new_label.append(label)
            break

    furthest = Point(x0, y0, label)
    new_points = [anchor, furthest]
    #Generate closer points
    num = random.randint(1, 2)
    for i in range(num):
        while True:
            scale = random.uniform(0.1, 0.9)
            angle = random_angle()
            x1, y1 = anchor.x + scale * ((x0 - anchor.x) * np.cos(angle) - (y0 - anchor.y) * np.sin(angle)), anchor.y + scale * ((x0 - anchor.x) * np.sin(angle) + (y0 - anchor.y) * np.cos(angle))
            if assert_coord_in_range(x1, y1):
                    break
        while True:
            label = label_point(d)
            if label not in new_label:
                new_label.append(label)
                break
        new_points.append(Point(x1, y1, label))

    d.points.extend(new_points)
    d.entities.append(('length_8', new_label))
    return d



