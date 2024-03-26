
import os
import sys
sys.path.append("..")
from geoclidean_env_euclid import *
from concepts import *
import numpy as np
import shutil
import json

eg_concept = three_circles_common_intersection


# Load the list of concepts from 'concepts.json'
with open('concepts.json', 'r') as json_file:
    concept_list = json.load(json_file)

# Iterate over each concept in the list
for j, concept in enumerate(concept_list):
    if not concept['name'] in ['oblong', 'parallel_l']:
        continue
    # Directories for exact, close, and far concepts
    exact_dir = os.path.join('my_data', concept['name'])
    close_dir = os.path.join('my_data', concept['name'] + '_close')
    far_dir = os.path.join('my_data', concept['name'] + '_far')

    # Ensure directories exist
    os.makedirs(exact_dir, exist_ok=True)
    os.makedirs(close_dir, exist_ok=True)
    os.makedirs(far_dir, exist_ok=True)

    rule = [line.strip().replace("'","") for line in concept['exact'].split('\n') if line.strip()]

    print(f'exact_dir : {exact_dir}')
    print(f'exact rule :  {rule}')

    # Generate images based on the 'exact' rule
    for i in range(300):

        generate_concept(rule, mark_points=False, show_plots=True, path=os.path.join(exact_dir, f'{i}.png'))


    print(f'generated exact images for {concept["name"]}')


    close_rule = rule = [line.strip().replace("'","") for line in concept['close'].split('\n') if line.strip()]
    # Generate images based on the 'close' rule
    for i in range(300):
        generate_concept(close_rule, mark_points=False, show_plots=False, path=os.path.join(close_dir, f'{i}.png'))

    print(f'generated close images for {concept["name"]}')

    far_rule = rule = [line.strip().replace("'","") for line in concept['far'].split('\n') if line.strip()]
    # Generate images based on the 'far' rule
    for i in range(300):
        generate_concept(far_rule, mark_points=False, show_plots=False, path=os.path.join(far_dir, f'{i}.png'))

    print(f'generated far images for {concept["name"]}')



# output_dir = 'my_data/three_circles_common_intersection_steps/'
#
# concept = three_circles_common_intersection
#
# #check if the directory exists, and if not create one
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
#
#
# for i in range(100):
#     generate_concept(concept,steps_path= True, mark_points=True, show_plots=True, path=output_dir + f'{i}.png')
#

