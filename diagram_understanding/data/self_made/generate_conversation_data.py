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
from labels import *

plt.ioff()  # Turn off interactive mode
num_entities = 10
num_images = 50000
balance_limit = 0.2 * num_images


type_path = "simple_conversation"
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
    positive_mining = question_data['positive_mining']
    negative_mining = question_data['negative_mining']
    conversation_general = question_data['conversation_general']
    not_existing = question_data['not_existing']



def count_files(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
    return count

def complete_sentence(entity):
        key = entity[0]
        print(f"Current step : entity, key = {entity}, {key}")
        sentence = random.choice(caption_dict[key])
        inputs = entity[1]
        try :
            inputs.append(random.choice(capitals.candidates))
            for i in range(len(inputs)):
                # print(inputs[i])
                sentence = sentence.replace(f'<{i+1}>', inputs[i])
            return sentence
        except: print(f"Error with entity : {entity} and type: caption")
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
    print(f"length of diagram.points : {len(diagram.points)}")

    indx = 0
    num_points = 0
    while True:
        diagram = no_free_points(diagram)
        if len(diagram.entities) >= num_entities or indx > len(diagram.entities)*1.5 or len(diagram.points)>12:
            break
        else:
            indx += 1
        #
        # print(f"Current points count : {num_points}" )
        # print(f"Current Step : {diagram.steps[-1] if len(diagram.steps) > 0 else 'None'}")
        # print(f"Points added count : {len(diagram.points) - num_points}")
        # print("index : ", indx)
        num_points = len(diagram.points)
    return diagram

def diagram_data(diagram, i,j, directory, conversation):
    entity_list = [entity[0] for entity in diagram.entities]
    steps = diagram.steps
    points = [point.label for point in diagram.points]
    lines = [f"({line.point1.label}{line.point2.label},{line.label})" for line in diagram.lines]
    circles = [circle.label for circle in diagram.circles]
    id_name = f'{i}_{j}_' + str(random.randint(100,999)) + str(random.choice(['a','b','c','d','e','f','g','h']))
    img_path = f"{directory}/{id_name}.png"

    if random.random() < 0.01:
        print(f"<Conversation {id_name}>\n{conversation}")

    final_data = {
        "id": id_name,
        "image" : img_path,
        "conversations": conversation,
        "entity_list": entity_list,
        "steps": steps,
        "points": points,
        "lines": lines,
        "circles": circles
    }
    return final_data, id_name, img_path

def generate_question_general(diagram):
    question_type = random.choice(["count_p", "count_l", "count_c"])
    question = random.choice(conversation_general[question_type])
    if question_type == "count_p":
        num_p = len(diagram.points)
        if random.choice([True, False]):
            answer = random.choice(["There are " + str(num_p) + " points.","I see " + str(num_p) + " points.","There are " + str(num_p) + " points in the diagram.", str(num_p)])
        else:
            answer = random.choice([f"The points described in the diagram are ", f"The points in the diagram are "])
            for point in diagram.points:
                answer += point.label + ", "
            answer = answer[:-2] + random.choice([". We have " + str(num_p) + " points.", ". There are " + str(num_p) + " points."])
        if num_p == 0:
            answer = random.choice([ "There are no points in the diagram.", "0.", "There are no points.", "I see no points."])
        elif num_p == 1:
            answer = random.choice([ "There is only one point in the diagram.", "1.", "There is one point.", "I see one point."])
    elif question_type == "count_l":
        num_l = len(diagram.lines)
        if random.random() < 0.8:
            answer = random.choice(["There are " + str(num_l) + " lines.","I see " + str(num_l) + " lines.","There are " + str(num_l) + " lines in the diagram.", str(num_l)])
        else:
            answer = random.choice([f"The lines described in the diagram are ", f"The lines in the diagram are "])
            for line in diagram.lines:
                answer += f"{line.point1.label}{line.point2.label}, "
            answer = answer[:-2] + random.choice([". We have " + str(num_l) + " lines.", ". There are " + str(num_l) + " lines."])
        if num_l == 0:
            answer = random.choice([ "There are no lines in the diagram.", "0.", "There are no lines.", "I see no lines."])
        elif num_l == 1:
            answer = random.choice([ "There is only one line in the diagram.", "1.", "There is one line.", "I see one line."])

    elif question_type == "count_c":
        assert len(diagram.circles) > 0
        num_c = len(diagram.circles)
        if random.choice([True, False]):
            answer = random.choice(["There are " + str(num_c) + " circles.","I see " + str(num_c) + " circles.","There are " + str(num_c) + " circles in the diagram.", str(num_c)])
        else:
            answer = random.choice([f"The circles described in the diagram are ", f"The circles in the diagram are ", f"There are circles with centers "])
            for circle in diagram.circles:
                answer += circle.center.label + ", "
            answer = answer[:-2] + random.choice([". We have " + str(num_c) + " circles.", ". There are " + str(num_c) + " circles."])
        if num_c == 0:
            answer = random.choice([ "There are no circles in the diagram.", "0.", "There are no circles.", "I see no circles."])
        elif num_c == 1:
            answer = random.choice([ "There is only one circle in the diagram.", "1.", "There is one circle.", "I see one circle."])
    else: answer = "I don't know."

    return question, answer

def generate_question_positive_mining(entity):
    key = entity[0]
    question, answer = random.choice(positive_mining[key])
    inputs = entity[1]
    try:
        inputs.append(random.choice(capitals.candidates))
        for i in range(len(inputs)):
            question = question.replace(f'<{i+1}>', inputs[i])
            answer = answer.replace(f'<{i+1}>', inputs[i])
        return question, answer
    except: print(f"Error with entity : {entity} and type: positive_mining")

def generate_question_negative_mining(entity):
    key = entity[0]
    question, answer = random.choice(negative_mining[key])
    inputs = entity[1]
    try:
        inputs.append(random.choice(capitals.candidates))

        for i in range(len(inputs)):
            question = question.replace(f'<{i+1}>', inputs[i])
            answer = answer.replace(f'<{i+1}>', inputs[i])
        return question, answer
    except: print(f"Error with entity : {entity} and type: negative_mining")

def generate_not_existing(diagram):

    ind = 0
    entity_list = [entity[0] for entity in diagram.entities]
    while True:
        key = random.choice(list(entity_count.keys()))

        if key not in entity_list:
            break
        if ind > 10:
            raise ValueError("No non-existing entity found")
        ind += 1

    question, answer = random.choice(not_existing[key])
    return question, answer


def generate_full_conversation(diagram):
    conversation = []
    added_caption = False
    max_num_rounds = random.randint(2, 5)
    num_round = 0
    while num_round < max_num_rounds:
        try:
            conv_type = random.choice(["general", "positive_mining", "negative_mining", "not_existing","caption","positive_mining", "negative_mining"])
            if conv_type == "caption" and not added_caption:
                added_caption = True
                if random.random() < 0.1:
                    answer = generate_caption(diagram)
                    question = random.choice(caption_question)
            elif conv_type == "general":
                question, answer = generate_question_general(diagram)
            elif conv_type == "positive_mining":
                entity = random.choice(diagram.entities)
                question, answer = generate_question_positive_mining(entity)
            elif conv_type == "negative_mining":
                entity = random.choice(diagram.entities)
                question, answer = generate_question_negative_mining(entity)
            elif conv_type == "not_existing":
                question, answer = generate_not_existing(diagram)
            else:
                raise ValueError("Invalid conversation type")

            if num_round == 0:
                if random.random() > 0.5:
                    question += "\n<image>"
                else:
                    question = "<image>\n" + question

            conversation.extend([{
                    "from": "human",
                    "value": question
                },
                {
                    "from": "assistant",
                    "value": answer
                }]
            )
            num_round += 1
        except : pass


    return conversation




# Create the directories and files
for i in range(20):
    # Create the directory path
    directory_path = f'./GOVU_data/{type_path}/{i}'
    # Create the directory if it doesn't exist
    os.makedirs(directory_path, exist_ok=True)
    # Create the file path
    # file_path = f'{directory_path}/qa.json'
    # # Create the file if it doesn't exist
    # with open(file_path, 'a'):
    #     pass

print("Directories and files created successfully.")

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
        if diagram_entitiy_count == 0 and image_count >10:
            continue
        # print(f"image_count : {image_count}")
        os.makedirs(directory, exist_ok=True)
        if image_count < balance_limit:
            data, unique_id, image_path = diagram_data(diagram, image_count, diagram_entitiy_count, directory, generate_full_conversation(diagram))
            plt.savefig(image_path)

            with open(f"./GOVU_data/{type_path}/qa.json", "a") as file:
                json.dump(data, file)
                file.write("\n")
            # print(f"Saved image {diagram_entitiy_count}/{unique_id}.png")
            i += 1
        if image_count > 0.9 * balance_limit and j < num_entities:
            j += 1
        plt.close(fig)

        # print(f"diagram_entitiy_count : {diagram_entitiy_count}, image_count : {image_count}, num_rounds = {len(data['conversations'])}")
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

