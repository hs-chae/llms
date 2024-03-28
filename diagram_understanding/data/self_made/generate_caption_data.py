import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import json
from rules import *
from create_tree import *
from plot import *
import os

plt.ioff()  # Turn off interactive mode
num_entities = 10
num_images = 20000
balance_limit = 0.2 * num_images

type_path = "caption"
#create the directory if it doesn't exist
os.makedirs(f'./GOVU_data/{type_path}', exist_ok=True)


# Load the caption.json file
with open('captions.json') as file:
    caption_data = json.load(file)

# Access the dictionary from the loaded JSON data
caption_dict = caption_data
entity_count = {key: 0 for key in caption_dict.keys()}

# Load the questions.json file
with open('questions.json') as file:
    question_data = json.load(file)
    caption_question = question_data['caption']


def count_files(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
    return count

def complete_sentence(entity):
        key = entity[0]
        # print(f"Current step : entity, key = {entity}, {key}")
        sentence = random.choice(caption_dict[key])
        inputs = entity[1]
        for i in range(len(inputs)):
            # print(inputs[i])
            sentence = sentence.replace(f'<{i+1}>', inputs[i])
        return sentence
    # except :
    #     print(f"Error with entity : {entity}")

def generate_caption(diagram):
    entities = diagram.entities
    caption = ""
    if len(entities) == 0:
        for line in diagram.lines:
            sentence = "There is a line " + f"{line.point1.label}{line.point2.label}."
            caption += sentence + " "
        for circle in diagram.circles:
            sentence = "There is a circle " + circle.label + "."
            caption += sentence + " "
        for point in diagram.points:
            sentence = "There is a point " + point.label + "."
            caption += sentence + " "
    else:
        for entity in entities:
            sentence = complete_sentence(entity)
            caption += sentence + " "
    if len(caption) == 0:
        caption = "I see nothing."
    return caption[:-1]



def create_diagram(num_entities):
    diagram = Diagram(points=[], lines=[], circles=[], triangles=[], squares=[], steps=[])
    # print(f"length of diagram.points : {len(diagram.points)}")

    indx = 0
    num_points = 0
    while True:
        diagram = no_free_points(diagram)
        if len(diagram.entities) >= num_entities or indx > len(diagram.entities)*1.5 or len(diagram.points)>15:
            break
        else:
            indx += 1

        # print(f"Current points count : {num_points}" )
        # print(f"Current Step : {diagram.steps[-1] if len(diagram.steps) > 0 else 'None'}")
        # print(f"Points added count : {len(diagram.points) - num_points}")
        # print("index : ", indx)
        num_points = len(diagram.points)
    return diagram

def diagram_data(diagram, i,j, directory):
    caption = generate_caption(diagram)
    entity_list = [entity[0] for entity in diagram.entities]
    steps = diagram.steps
    points = [point.label for point in diagram.points]
    lines = [line.label for line in diagram.lines]
    circles = [circle.label for circle in diagram.circles]
    id_name = f'{i}_{j}_' + str(random.randint(100,999)) + str(random.choice(['a','b','c','d','e','f','g','h']))
    img_path = f"{directory}/{id_name}.png"
    question = random.choice(caption_question)
    if random.random() > 0.5:
        question = question + "\n<image>"
    else :
        question = "<image>\n" + question
    final_data = {
        "id": id_name,
        "image" : img_path,
        "conversations": [
            {
                "from": "human",
                "value": question
            },
            {
                "from": "assistant",
                "value": caption
            },
        ],
        "caption": caption,
        "entity_list": entity_list,
        "steps": steps,
        "points": points,
        "lines": lines,
        "circles": circles
    }
    return final_data, id_name, img_path


for i in range(20):
    # Create the directory path
    directory_path = f'./GOVU_data/{type_path}/{i}'

    # Create the directory if it doesn't exist
    os.makedirs(directory_path, exist_ok=True)

    # Create the file path
    file_path = f'{directory_path}/qa.json'

    # Create the file if it doesn't exist
    with open(file_path, 'a'):
        pass

# print("Directories and files created successfully.")

i,j = 0, 3

#Count the number of each entity



while i < num_images:
    try :
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)

        diagram = create_diagram(j)
        plot_diagram(ax, diagram)

        diagram_entitiy_count = len(diagram.entities)
        directory = f"./GOVU_data/{type_path}/{diagram_entitiy_count}"

        image_count = count_files(directory)
        # print(f"image_count : {image_count}")
        if diagram_entitiy_count == 0 and image_count >10:
            continue
        os.makedirs(directory, exist_ok=True)
        if image_count < balance_limit:
            data, unique_id, image_path = diagram_data(diagram, image_count, diagram_entitiy_count, directory)
            plt.savefig(image_path)

            with open(f"./GOVU_data/{type_path}/qa.json", "a") as file:
                json.dump(data, file)
                file.write("\n")
            # print(f"Saved image {diagram_entitiy_count}/{unique_id}.png")
            i += 1
        if image_count > 0.9 * balance_limit and j < num_entities:
            j += 1
        plt.close(fig)

        # print(f"diagram_entitiy_count : {diagram_entitiy_count}, image_count : {image_count}")
        for entity in diagram.entities:
            entity_count[entity[0]] += 1
    except:
        print("Error")
        pass
    print(f"i : {i}")



print("Data generation complete.")
total_img_num = 0
for c in range(20):
    current_count = count_files(f'./GOVU_data/{type_path}/{c}')
    print(f"Total images in {c} entities directory : {current_count}")
    total_img_num += current_count
print(f"Total images : {total_img_num}")
print("Entity Used-----------------")
for key in entity_count.keys():
    print(f"{key} : {entity_count[key]}")
print("-----------------")
print(f"List of not used keys : {[key for key in entity_count.keys() if entity_count[key] == 0]}")
print(f"Count of most used key : {max(entity_count, key=entity_count.get)}")

