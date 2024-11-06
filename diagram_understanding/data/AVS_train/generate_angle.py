import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from generation_rules.length_rules import *
from plot import *
import os
from labels import *

plt.ioff()  # Turn off interactive mode
num_entities = 3
num_images = 100
balance_limit = 0.2 * num_images



# Load the questions.json file
with open('jsons/conversation.json') as file:
    question_data = json.load(file)




def count_files(directory):
    count = 0
    for _, _, files in os.walk(directory):
        count += len(files)
    return count


def create_diagram(num_entities):
    diagram = Diagram(points=[], lines=[], circles=[], triangles=[], squares=[], steps=[])
    # print(f"length of diagram.points : {len(diagram.points)}")

    indx = 0
    num_points = 0
    while True:
        diagram = angle_tree(diagram)
        if len(diagram.entities) >= num_entities or indx > len(diagram.entities)*1.5 or len(diagram.points)>12:
            break
        if len(diagram.entities) > 0:
            if 'angle' in diagram.entities[-1][0]:
        #
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

    # if random.random() < 0.01:
        # print(f"<Conversation {id_name}>\n{conversation}")

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

# def generate_question_general(diagram):
#
#     question = question_data
#     # if question_type == "count_p":
#     #     num_p = len(diagram.points)
#     #     if random.choice([True, False]):
#     #         answer = random.choice(["There are " + str(num_p) + " points.","I see " + str(num_p) + " points.","There are " + str(num_p) + " points in the diagram.", str(num_p)])
#     #     else:
#     #         answer = random.choice([f"The points described in the diagram are ", f"The points in the diagram are "])
#     #         for point in diagram.points:
#     #             answer += point.label + ", "
#     #         answer = answer[:-2] + random.choice([". We have " + str(num_p) + " points.", ". There are " + str(num_p) + " points."])
#     #     if num_p == 0:
#     #         answer = random.choice([ "There are no points in the diagram.", "0.", "There are no points.", "I see no points."])
#     #     elif num_p == 1:
#     #         answer = random.choice([ "There is only one point in the diagram.", "1.", "There is one point.", "I see one point."])
#
#     except: answer = "I don't know."
#
#     return question, answer

def generate_question_positive_mining(entity):
    key = entity[0]
    question, answer = random.choice(question_data[key])
    inputs = entity[1]
    # print(f"starting with {entity}")

    try:
        # print(inputs)
        inputs.append(random.choice(capitals.candidates))
        # print(f"11111")
        for i in range(len(inputs)):
            question = question.replace(f'<{i+1}>', inputs[i])

            answer = answer.replace(f'<{i+1}>', inputs[i])
            # print(f"Succeeded with {inputs[i]}")


        return question, answer
    except: print(f"Error with entity : {entity} ")

# def generate_question_negative_mining(entity):
#     key = entity[0]
#     question, answer = random.choice(negative_mining[key])
#     inputs = entity[1]
#     try:
#         inputs.append(random.choice(capitals.candidates))
#
#         for i in range(len(inputs)):
#             question = question.replace(f'<{i+1}>', inputs[i])
#             answer = answer.replace(f'<{i+1}>', inputs[i])
#         return question, answer
#     except: print(f"Error with entity : {entity} and type: negative_mining")

# def generate_not_existing(diagram):
#
#     ind = 0
#     entity_list = [entity[0] for entity in diagram.entities]
#     while True:
#         key = random.choice(list(entity_count.keys()))
#
#         if key not in entity_list:
#             break
#         if ind > 10:
#             raise ValueError("No non-existing entity found")
#         ind += 1
#
#     question, answer = random.choice(not_existing[key])
#     return question, answer


def generate_full_conversation(diagram):
    conversation = []
    added_caption = False
    max_num_rounds = 1 #random.randint(1, 2)
    num_round = 0
    while num_round < max_num_rounds:
        # try:
            if len(diagram.entities) == 0:
                raise ValueError("No entities in the diagram")
            entity = random.choice(diagram.entities)
            # print(f"==================entitiy : {entity}")
            question, answer = generate_question_positive_mining(entity)

            # if num_round == 0:
            #     question = "<image>\n" + question

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
        # except : pass


    return conversation



#
# # Create the directories and files
# for i in range(20):
#     # Create the directory path
#     directory_path = f'./GOVU_data/{type_path}/{i}'
#     # Create the directory if it doesn't exist
#     os.makedirs(directory_path, exist_ok=True)
#     # Create the file path
#     # file_path = f'{directory_path}/qa.json'
#     # # Create the file if it doesn't exist
#     # with open(file_path, 'a'):
#     #     pass
#
# print("Directories and files created successfully.")

i,j = 0, 3

#Count the number of each entity


while i < num_images:
    try:
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(0, 1000)
        ax.set_ylim(0, 1000)



        diagram = create_diagram(j)
        plot_diagram(ax, diagram)

        diagram_entitiy_count = len(diagram.entities)
        directory = f"./data/angle"

        image_count = count_files(directory)
        # if diagram_entitiy_count == 0 and image_count >10:
        #     continue
        # print(f"image_count : {image_count}")
        os.makedirs(directory, exist_ok=True)
        # if image_count < balance_limit:
        data, unique_id, image_path = diagram_data(diagram, image_count, diagram_entitiy_count, directory, generate_full_conversation(diagram))
        plt.savefig(image_path)

        with open(f"./data/angle.json", "a") as file:
            json.dump(data, file)
            file.write("\n")
        # print(f"Saved image {diagram_entitiy_count}/{unique_id}.png")

        i += 1
        # if image_count > 0.9 * balance_limit and j < num_entities:
        #     j += 1
        plt.close(fig)

    # print(f"diagram_entitiy_count : {diagram_entitiy_count}, image_count : {image_count}, num_rounds = {len(data['conversations'])}")
    # for entity in diagram.entities:
    #     entity_count[entity[0]] += 1
    except:
        print("Error in generating images")
        pass
    finally:
        plt.close(fig)
    # print(f"i : {i}")



print("Data generation complete.")
total_img_num = 0

current_count = count_files(f'./data/angle')
print(f"Total images of Angle : {current_count}")
# print(f"Total images : {total_img_num}")
print("-----------------")


