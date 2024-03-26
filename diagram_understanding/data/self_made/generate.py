import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import json
from rules import *
from create_tree import *
from plot import *

# Load the caption.json file
with open('captions.json') as file:
    caption_data = json.load(file)

#Generate a list of pairs of a key in caption_data and one sentence
pair_list = []
for key in caption_data:
    pair_list.append((key, random.choice(caption_data[key])))
print(pair_list)



# Access the dictionary from the loaded JSON data
caption_dict = caption_data

def complete_sentence(entity):
        key = entity[0]
        sentence = random.choice(caption_dict[key])
        inputs = entity[1]
        print("key : ", key)
        for i in range(len(inputs)):
            print(inputs[i])
            sentence = sentence.replace(f'<{i+1}>', inputs[i])
        return sentence
    # except :
    #     print(f"Error with entity : {entity}")

def generate_caption(entities):
    caption = ""
    for entity in entities:
        sentence = complete_sentence(entity)
        caption += sentence + " "
    return caption[:-1]

fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)


#Plotting diagrams
diagram = Diagram()
# add_free_point(diagram)
# add_free_circle(diagram)
# add_free_circle(diagram)

n = random.randint(2, 5)
indx = 0
while True:
    diagram = test_generation(diagram)
    if len(diagram.entities) >= n or indx > 10:
        break
    indx+=1
    # print(diagram.steps)
print( f"n : {n}")
print(f'diagram points : {[point.label for point in diagram.points]}')
print(f'diagram lines : {[line.label for line in diagram.lines]}')
print(f'diagram perps : {[X[2].label for X in diagram.perpendiculars]}')
print(f'diagram circles : {[circle.label for circle in diagram.circles]}')
print(f'diagram triangles : {[triangle.label for triangle in diagram.triangles]}')
print(f'diagram squares : {[square.label for square in diagram.squares]}')
print(f'steps : {diagram.steps}')
print(f'entities : {[entity[0] for entity in diagram.entities]}')
caption = generate_caption(diagram.entities)
print("<Caption>\n" + caption)
plot_diagram(ax, diagram)

plt.show()