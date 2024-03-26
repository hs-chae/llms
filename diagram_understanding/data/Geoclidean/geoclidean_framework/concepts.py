# Two lines are intersecting
intersecting_lines =  [
    'l1* = line(p1(), p2())',
'c1* = circle(p1(), p3(l1))',
'c2* = circle(p3(l1), p1())',
'c3* = circle(p2(), p3(l1))',
'l2 = line(p4(c1, c2), p5(c1, c2))',
'l3 = line(p6(c2), p7(c2))',
]


# Three circles are meeting at a point
three_circles_common_intersection = [
'c1 = circle(p1(), p2())',
'c2 = circle(p3(c1), p4(c1))',
'c3 = circle(p5(c1), p6(c1, c2))',
]

# There are three circles without common intersection
three_circles_no_common_intersection = [
'c1 = circle(p1(), p2())',
'c2 = circle(p3(c1), p4())',
'c3 = circle(p5(), p6())']

# Two lines are ending in a point, generating a horn, or a angle-like shape
horn = [
'l1 = line(p1(), p2())',
'l2 = line(p2(), p3())',
]

# Two lines are not parallel.
nonparallel_lines = [
'l1 = line(p1(), p2())',
'l2 = line(p3(), p4())',
]

# It is a triangle with a right angle.
right_angle_triangle = [
'l1* = line(p1(), p2())',
'c1* = circle(p1(), p2())',
'c2* = circle(p2(), p1())',
'l2* = line(p3(c1, c2), p4(c1, c2))',
'l3 = line(p5(l1, l2), p6(l2))',
'l4 = line(p5(l1, l2), p7(l1))',
'l5 = line(p6(l2), p7(l1))',
]

# This is a triangle, not necessarily with any unique properties.
triangle = [
'l1* = line(p1(), p2())',
'c1* = circle(p1(), p2())',
'c2* = circle(p2(), p1())',
'l2* = line(p3(c1, c2), p4(c1, c2))',
'l3 = line(p5(l1, l2), p6())',
'l4 = line(p5(l1, l2), p7())',
'l5 = line(p6(), p7())',
]


# There are two circles intersecting at two points. There is a line whose one end lies on one circle and the other end is by itself.
two_circles_one_line_ending_on_one_circle = [
'c1 = circle(p1(), p2())',
'c2 = circle(p3(c1), p4())',
'l3 = line(p5(), p6(c1))'
]

# There are two circles intersecting at two points. There is a line whose one end lies on one of their intersection points and the other end is by itself.
two_circles_one_line_ending_on_one_intersection = [
'c1 = circle(p1(), p2())',
'c2 = circle(p3(c1), p4())',
'l3 = line(p5(), p6(c1, c2))'
]

# There are two circles intersecting at two points. There is a line whose one end lies on one of their intersection points and the other end lies on one of the circles.
two_circles_one_line_ending_on_one_intersection_and_one_circle = [
'c1 = circle(p1(), p2())',
'c2 = circle(p3(c1), p4())',
'l3 = line(p5(c1), p6(c1, c2))'
]

