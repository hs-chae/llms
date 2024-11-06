from rules import *
# from generation_rules.parallel_rules import *
from generation_rules import parallel_rules
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

circle_rules = ['add_free_circle', 'add_circle', 'circle_with_radius']


test_rules = [
    (add_free_circle, 'add_free_circle'),(add_circle, 'add_circle'),(circle_with_radius, 'circle_with_radius'),
    # (init_square, 'init_square')
              ]

# angle_rules = [rule for rule in rules_list if rule[1] not in ['random_angle', 'random_coord', 'line_already_in', 'label_point','random_length', 'normalize', 'add_radius']]



parallel_list = [o for o in inspect.getmembers(parallel_rules) if inspect.isfunction(o[1])]
parallel_names = [name for name, func in parallel_list]
parallel_rules_list = [name for name, func in parallel_list]
# parallel_rules = [rule for rule in parallel_rules_list if rule[1] not in ['add_free_line', 'add_line', 'add_infinite_line']]#[(parallel_1,"parallel_1")] #[(parallel_1,"parallel_1")] #[(add_free_line,"add_free_line"),(add_free_circle, 'add_free_circle'),(add_circle, 'add_circle'),(circle_with_radius, 'circle_with_radius'),(parallel_1,"parallel_1")]
parallel_rules = ['parallel_1','parallel_2','parallel_3','parallel_4','add_free_point','add_free_point','add_circle','add_free_circle',"circle_with_radius"]
length_rules = ['add_free_point','add_circle','add_free_circle',"circle_with_radius",'length_1','length_2','length_3','length_4','length_5','length_6','length_7','length_8']
angle_rules = ['add_free_point','add_circle','add_free_circle',"circle_with_radius","angle1", "angle2", "angle3", "angle4", "angle5", "angle6", "angle7", "angle8", "angle9", "angle10", "angle11", "angle12", "angle13", "angle14", "angle15", "angle16", "angle17"]
