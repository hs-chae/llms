import torch

from rules import *
import rules
import inspect
import rule_list
from generation_rules.parallel_rules import *
from generation_rules.length_rules import *
from generation_rules.angle_rules import *

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

circle_rules = ['add_free_circle', 'add_circle', 'circle_with_radius']

#
# test_rules = [
#     (add_free_circle, 'add_free_circle'),(add_circle, 'add_circle'),(circle_with_radius, 'circle_with_radius'),
#     # (init_square, 'init_square')
#               ]
# (add_free_point,'add_free_point')
def one_step_uniform(diagram : Diagram):
    rule, rule_name = random.choice(rule_list.test_rules)
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

def parallel_tree(diagram : Diagram):
    rule_name = random.choice(rule_list.parallel_rules)
    print("Rule : " + rule_name)
    if random.random() < 1 / (len(diagram.entities) + 4):
        r = random.choice([add_free_circle])
        diagram = r(diagram)
        diagram.steps.append('r')
        return diagram
    else:
        # try:
            diagram = eval(rule_name)(diagram)
            diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram

def length_tree(diagram : Diagram):
    rule_name = random.choice(rule_list.length_rules)
    print("Rule : " + rule_name)
    if random.random() < 1 / (len(diagram.entities) + 4):
        r = random.choice([add_free_circle])
        diagram = r(diagram)
        diagram.steps.append('r')
        return diagram
    else:
        # try:
            diagram = eval(rule_name)(diagram)
            diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram

def angle_tree(diagram : Diagram):
    rule_name = random.choice(rule_list.angle_rules)
    print("Rule : " + rule_name)
    # if random.random() < 1 / (len(diagram.entities) + 4):
    #     r = random.choice([add_free_circle])
    #     diagram = r(diagram)
    #     diagram.steps.append('r')
    #     return diagram
    # else:
        # try:
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram

def test_generation(diagram : Diagram):
    rule, rule_name = random.choice(rule_list.test_rules)
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

#
# tensor = torch.tensor([[-1.0, 0.0, 1.0],
#                        [-0.5, 2.0, -2.0]])
# relu_tensor = F.relu(tensor)
#
# print("Original tensor:")
# print(tensor)
# print("\nTensor after ReLU:")
# print(relu_tensor)

# print(torch.nn.Parameter(torch.ones(4) ** -0.5))

class SimplifiedRMSNorm(torch.nn.Module):
    def __init__(self, hidden_size: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.learnable_scale = torch.nn.Parameter(torch.ones(hidden_size) ** -0.5)

    def _norm(self, x):
        # Compute the root mean square value and apply reciprocal square root normalization
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

# Example usage
hidden_size = 3  # For a 2x3 tensor
norm_layer = SimplifiedRMSNorm(hidden_size)

# Create a 2x3 tensor with arbitrary values
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Apply the _norm method
normalized_x = norm_layer._norm(x)

print("Original Tensor:")
print(x)
print("\nNormalized Tensor:")
print(normalized_x)