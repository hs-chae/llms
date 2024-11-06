import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import math
import json

def random_angle():
    return np.random.uniform(np.pi/9, 17/9*np.pi)

def random_acute():
    return np.random.uniform(np.pi/9, 4/9*np.pi)

def random_obtuse():
    return np.random.uniform(5/9*np.pi, 8/9*np.pi)

def rotate_vector(vector, angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) @ np.array(vector)


def random_coord(start = 10, end = 990):
    return np.random.uniform(start, end)


def line_already_in(diagram, point1, point2):
    for line in diagram.lines:
        if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
            return True
    return False

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

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


def angle1(d):
    # generate two lines with an acute angle
    new_labels = []
    p1 = Point(random_coord(),random_coord(),label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(),random_coord(),label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_acute()
        vector2 = rotate_vector(vector, angle)
        scale = random.uniform(0.5, 1.5)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale*vector2[0], p1.y + scale*vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('angle1', [p1.label, p2.label, p3.label]))

    return d

def angle2(d):
    # generate two lines with an obtuse angle
    # generate two lines with an acute angle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_obtuse()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale* vector2[0], p1.y + scale* vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('angle2', [p1.label, p2.label, p3.label]))

    return d


def angle3(d):
    # generate a right angle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    ind=0
    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    while True:
        angle = np.pi/2
        vector2 = rotate_vector(vector, angle)
        scale = random.uniform(0.5, 1.5)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('angle3', [p1.label, p2.label, p3.label]))
    return d


def angle4(d):
    # generate an acute triangle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_acute()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        V_23 = np.array([p3.x - p2.x, p3.y - p2.y])
        cs_1 = cos_sim((-1) * vector, V_23) #v21 and v23
        cs_2 = cos_sim((-1) * V_23, (-1)*vector2) #v32 and v31

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels and cs_1 > 0 and cs_2 > 0:
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1


    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))
    l3 = Line(p2, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('angle4', [p1.label, p2.label, p3.label]))

    return d

def angle5(d):
    # generate an obtuse triangle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_obtuse()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))
    l3 = Line(p2, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('angle4', [p1.label, p2.label, p3.label]))
    return d

def angle6(d):
    # generate a right triangle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = np.pi/2
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))
    l3 = Line(p2, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('angle4', [p1.label, p2.label, p3.label]))
    return d

def angle7(d):
    # Make  one obtuse angles and one acute angle
    new_labels = []
    O = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(O.label)


    while True:
        label_A = label_point(d)
        if label_A != O.label:
            new_labels.append(label_A)
            break
    A_x, A_y = random_coord(), random_coord()
    A = Point(A_x, A_y, label_A)

    while True:
        label_B = label_point(d)
        if label_B not in new_labels:
            break

    while True:
        label_C = label_point(d)
        if label_C not in new_labels:
            break

    #Choos a clockwise angle
    #If random > 0.5, then angle_1 is acute and else obtuse
    ent = "angle7"
    if random.random() > 0.5:
        angle_1 = random_acute()
        angle_2 = random_obtuse()
    else:
        angle_1 = random_obtuse()
        angle_2 = random_acute()
        ent = "angle7-2"

    ind=0
    #Choose a random scale
    while True:
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(np.array([A_x - O.x, A_y - O.y]), angle_1)
        x, y = O.x + scale1 * vector_B[0], O.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B = Point(O.x + scale1 * vector_B[0], O.y + scale1 * vector_B[1], label_B)
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(np.array([A_x - O.x, A_y - O.y]), -angle_2)
        x, y = O.x + scale2 * vector_C[0], O.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            C = Point(O.x + scale2 * vector_C[0], O.y + scale2 * vector_C[1], label_C)
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O, A, label_line(d))
    l2 = Line(O, B, label_line(d))
    l3 = Line(O, C, label_line(d))

    d.points.extend([O, A, B, C])
    d.lines.extend([l1, l2, l3])

    # if ent = "angle7", then AOB is acute. if ent= angle7-2 AOB is obtuse
    d.entities.append((ent, [O.label, A.label, B.label, C.label]))

    return d

def angle8(d):
    # Make  one acute angle and one obtuse angle and one right angle
    new_labels = []
    while True:
        label1, label2, label3 = label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3:
            new_labels.extend([label1, label2, label3])
            break


    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_3 = np.pi/2
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")

    d.points.extend([O_1, O_2, O_3])
    d.lines.extend([l1, l2, l3, l4, l5, l6])

    tmp = [[O_1, "acute"], [O_2, "obtuse"], [O_3, "right"]]
    random.shuffle(tmp)
    d.entities.append(('angle8', [tmp[0][0].label, tmp[0][1], tmp[1][0].label, tmp[1][1], tmp[2][0].label, tmp[2][1]]))

    return d


def angle9(d):
    # Make different pairs of lines with one acute, and three obtuse angles
    new_labels = []
    while True:
            label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
            if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
                new_labels.extend([label1, label2, label3, label4])
                break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind = 0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1


    ind = 0
    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    ind=0
    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    ind=0
    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle9', [O_1.label, O_2.label, O_3.label, O_4.label])) #O_1 : ocute, O_2~4 : obtuse

    return d

def angle10(d):
    # Make different pairs of lines with one obtuse, and three acute angles
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_obtuse()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle10', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle11(d):
    # Make different pairs of lines with one right, and three acute angles
    new_labels = []

    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = np.pi/2
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle11', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse
    return d

def angle12(d):
    # Make different pairs of lines with one right, and three obtuse angles
    new_labels = []
    while True:
      label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
      if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
          new_labels.extend([label1, label2, label3, label4])
          break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
      angle_1 = np.pi/2
      scale1 = random.uniform(0.5, 1.5)
      vector_B = rotate_vector(vector_1, angle_1)
      x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
      if assert_coord_in_range(x, y):
          B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
          break
      if ind > 30:
          raise ValueError('No possible point found in angle9')
      ind += 1

    while True:
      angle_2 = random_obtuse()
      scale2 = random.uniform(0.5, 1.5)
      vector_C = rotate_vector(vector_2, angle_2)
      x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
      if assert_coord_in_range(x, y):
          B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
          break
      if ind > 60:
          raise ValueError('No possible point found in angle9')
      ind += 1

    while True:
      angle_3 = random_obtuse()
      scale3 = random.uniform(0.5, 1.5)
      vector_D = rotate_vector(vector_3, angle_3)
      x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
      if assert_coord_in_range(x, y):
          B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
          break
      if ind > 90:
          raise ValueError('No possible point found in angle9')
      ind += 1

    while True:
      angle_4 = random_obtuse()
      scale4 = random.uniform(0.5, 1.5)
      vector_E = rotate_vector(vector_4, angle_4)
      x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
      if assert_coord_in_range(x, y):
          B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
          break
      if ind > 120:
          raise ValueError('No possible point found in angle9')
      ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle12', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle13(d):
    # Make different pairs of lines with two acute, and two obtuse angles
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle13')
        ind += 1

    ind=0
    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle13')
        ind += 1

    ind = 0
    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle13')
        ind += 1

    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 60:
            raise ValueError('No possible point found in angle13')
        ind += 1


    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle13', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d



def angle14(d):
    # Make AOB + COD acute
    new_labels = [ ]
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2:
            new_labels.extend([label1, label2])
            break

    O1 = Point(random_coord(), random_coord(), label1)
    O2 = Point(random_coord(), random_coord(), label2)
    A1 = Point(random_coord(), random_coord(), "")
    A2 = Point(random_coord(), random_coord(), "")

    vector1 = np.array([A1.x - O1.x, A1.y - O1.y])
    vector2 = np.array([A2.x - O2.x, A2.y - O2.y])

    ind = 0
    while True:
        total_angle = random.uniform(np.pi/4, np.pi/2)
        angle1 = random.uniform(np.pi/8, total_angle-np.pi/8)
        angle2 = total_angle - angle1

        scale1 = random.uniform(0.5, 1.5)
        vector_A = rotate_vector(vector1, angle1)
        x1, y1 = O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1]

        scale2 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector2, angle2)
        x2, y2 = O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1]

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            B1 = Point(O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1], "")
            B2 = Point(O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1], "")
            break

        if ind > 100:
            raise ValueError("Cannot find a valid point")
        ind += 1

    l1 = Line(O1, A1, "")
    l2 = Line(O1, B1, "")
    l3 = Line(O2, A2, "")
    l4 = Line(O2, B2, "")

    d.points.extend([O1, O2])
    d.lines.extend([l1, l2, l3, l4])
    d.entities.append(('angle14', [O1.label, O2.label]))

    return d

def angle15(d):
    # Make AOB + BOC obtuse
    new_labels = []
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2:
            new_labels.extend([label1, label2])
            break

    O1 = Point(random_coord(), random_coord(), label1)
    O2 = Point(random_coord(), random_coord(), label2)
    A1 = Point(random_coord(), random_coord(), "")
    A2 = Point(random_coord(), random_coord(), "")

    vector1 = np.array([A1.x - O1.x, A1.y - O1.y])
    vector2 = np.array([A2.x - O2.x, A2.y - O2.y])

    ind = 0
    while True:
        total_angle = random.uniform(np.pi / 2, np.pi * 0.9 )
        angle1 = random.uniform(np.pi / 6, total_angle - np.pi / 6)
        angle2 = total_angle - angle1

        scale1 = random.uniform(0.5, 1.5)
        vector_A = rotate_vector(vector1, angle1)
        x1, y1 = O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1]

        scale2 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector2, angle2)
        x2, y2 = O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1]

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            B1 = Point(O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1], "")
            B2 = Point(O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1], "")
            break

        if ind > 100:
            raise ValueError("Cannot find a valid point")
        ind += 1

    l1 = Line(O1, A1, "")
    l2 = Line(O1, B1, "")
    l3 = Line(O2, A2, "")
    l4 = Line(O2, B2, "")

    d.points.extend([O1, O2])
    d.lines.extend([l1, l2, l3, l4])
    d.entities.append(('angle15', [O1.label, O2.label]))

    return d

def angle16(d):
    # Make different pairs of lines with all acute.
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 110:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle16', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle17(d):
    # Make different pairs of lines with all acute.
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_obtuse()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            raise ValueError('No possible point found in angle9')
        ind += 1

    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            raise ValueError('No possible point found in angle9')
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle17', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d







