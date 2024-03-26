import os
import sys
sys.path.append("..")
import numpy as np
import shutil
import json

path_c = 'constraints'
path_e = 'elements'

#get lists of subdirectories of the path

subdirs_c =  [d for d in os.listdir(path_c) if os.path.isdir(os.path.join(path_c, d))]
subdirs_e = [d for d in os.listdir(path_e) if os.path.isdir(os.path.join(path_e, d))]

concepts = []

for PATH, subdir in  [(path_c, subdirs_c), (path_e, subdirs_e)]:
    for path in subdir:
        concept_data = {}

        path = PATH + '/' +  path

        # Construct file paths
        concept_path = os.path.join(path, 'concept.txt')
        close_concept_path = os.path.join(path, 'close_concept.txt')
        far_concept_path = os.path.join(path, 'far_concept.txt')

        # Read the content of concept.txt
        with open(concept_path, 'r') as file:
            concept_data['exact'] = file.read()

        # Read the content of close_concept.txt
        with open(close_concept_path, 'r') as file:
            concept_data['close'] = file.read()

        # Read the content of far_concept.txt
        with open(far_concept_path, 'r') as file:
            concept_data['far'] = file.read()

        # Add the path to the concept data
        concept_data['name'] = path.replace('constraints/', '').replace('elements/', '').replace('concept_','')

        # Append the collected data to the concepts list
        concepts.append(concept_data)

# Save the concepts data to a JSON file
with open('concepts.json', 'w') as json_file:
    json.dump(concepts, json_file, indent=4)