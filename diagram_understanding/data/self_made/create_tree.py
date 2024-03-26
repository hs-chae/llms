import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import json

import torch
import torch.nn.functional as F

from rules import *
import rules
import inspect

def write_rules_json(rules_list, output_file):
    rules_dict = {str(rule[1]): [] for rule in rules_list}

    with open(output_file, 'w') as file:
        json.dump(rules_dict, file, indent=4)

    print(f"JSON file '{output_file}' created successfully.")


functions_list = [o for o in inspect.getmembers(rules) if inspect.isfunction(o[1])]
function_names = [name for name, func in functions_list]

empty_diagram = Diagram()
rules_list = [(eval(name),name) for name in function_names]
#remoeve random_angle, random_coord, line_already_in, label_point
rules_list = [rule for rule in rules_list if rule[1] not in ['random_angle', 'random_coord', 'line_already_in', 'label_point','random_length', 'normalize', 'add_radius']]
no_circle_rules = [rule for rule in rules_list if rule[1] not in ['add_free_circle', 'add_circle', 'circle_with_radius',]]

test_rules = [
    (c_tangent,'c_tangent'),
    #(cc_tangent,'cc_tangent'), (cc_tangent_one, 'cc_tangent_one'),
    (add_free_circle, 'add_free_circle')

    # (init_square, 'init_square')
              ]
# (add_free_point,'add_free_point')
def one_step_uniform(diagram : Diagram):
    rule, rule_name = random.choice(test_rules)
    print(rule_name)
    if len(diagram.entities) < 2 :
        diagram =  add_free_point(diagram)
        diagram.steps.append('add_free_point')
    elif random.random() < 2/(len(diagram.entities)+1):
        diagram = add_free_point(diagram)
        diagram.steps.append('add_free_point')
        return diagram
    else:
        try:
            diagram = rule(diagram)
            diagram.steps.append(rule_name)
        except: pass
    return diagram


def no_free_points(diagram : Diagram):
    rule, rule_name = random.choice(rules_list)
    print(rule_name)
    if random.random() < 1 / (len(diagram.entities) + 4):
        r = random.choice([add_free_line, add_free_circle, circle_with_radius])
        diagram = r(diagram)
        diagram.steps.append('r')
        return diagram
    else:
        try:
            diagram = rule(diagram)
            diagram.steps.append(rule_name)
        except:
            print("step failed with rule: ", rule_name)
    return diagram

def test_generation(diagram : Diagram):
    rule, rule_name = random.choice(test_rules)
    print(rule_name)
    if random.random() < 1 / (len(diagram.entities) + 4):
        r = random.choice([add_free_line, add_free_circle])
        diagram = r(diagram)
        diagram.steps.append('r')
        return diagram
    else:
        try:
            diagram = rule(diagram)
            diagram.steps.append(rule_name)
        except:
            print("step failed with rule: ", rule_name)
    return diagram

def no_circle(diagram : Diagram):
    rule, rule_name = random.choice(no_circle_rules)
    print(rule_name)
    if random.random() < 1 / (len(diagram.entities) + 4):
        r = random.choice([add_free_line])
        diagram = r(diagram)
        diagram.steps.append('r')
        return diagram
    else:
        try:
            diagram = rule(diagram)
            diagram.steps.append(rule_name)
        except:
            print("step failed with rule: ", rule_name)
    return diagram



print(len(rules_list))

#
#
# ###example
# diagram = Diagram()
# for i in range(10):
#     diagram = one_step_uniform(diagram)
#     print(diagram.steps)
#
# print(f'diagram points : {[point.label for point in diagram.points]}')
# print(f'diagram lines : {[line.label for line in diagram.lines]}')
# print(f'diagram circles : {[circle.label for circle in diagram.circles]}')
# print(f'diagram triangles : {[triangle.label for triangle in diagram.triangles]}')
# print(f'diagram squares : {[square.label for square in diagram.squares]}')
# print(f'steps : {diagram.steps}')

lst = ("A","B","C")
print(lst)
lst = [input for input in lst]
lst.append(random.choice(capitals.candidates))
sent = "<1> then <2> and <3>"

for i in range(len(lst)):
    sent = sent.replace(f"<{i+1}>", lst[i])
print(lst)
