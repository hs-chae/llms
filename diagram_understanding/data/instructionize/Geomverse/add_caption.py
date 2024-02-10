import os
import ast
import time
import json
import uuid
import base64
import openai
import logging
import pandas as pd
import numpy as np
from openai import OpenAI
from PIL import Image
from termcolor import colored
from textwrap import wrap
import base64
import requests
import csv

from diagram_understanding.dialogue import *
from  ..prompt import *
from ..instruction_prompts import *


def list_subdirectories(directory_path):
    subdirectories = [d for d in os.listdir(directory_path)
                      if os.path.isdir(os.path.join(directory_path, d))]
    return subdirectories


def json_to_string(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Convert the entire JSON content into a single string
    string_representation = json.dumps(data)

    return string_representation


def write_to_json(input_string, file_name="natural_form.json"):
    import json

    # Writing to a file
    with open(file_name, 'w') as json_file:
        json_file.write(input_string)


def extract_questions(file_path):
    questions = []
    image_paths = []
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        for line in file:

            # Parse the JSON object from the line
            data = json.loads(line)

            qstn = data['question']
            questions.append(qstn)
            try : image_paths.append(data["image_path"])
            except : pass
            # print('Question : ' + qstn)
            # Extract the questions from the JSON file

            # except KeyError as e:
            #     print(f"Missing key {e} in the data: {line}")
            #     # Optionally, log the error or handle it as needed
            #     continue  # Skip this line and move to the next

    return questions, image_paths


def add_to_json(image_path, caption, file_name):
    # Add the caption to the JSON object
    data_to_add = {"image_path": image_path, "caption": answer}

    with open(file_name, 'r+') as file:
        try :
            existing_data = json.load(file)
            # Ensure the existing data is a list
            if not isinstance(existing_data, list):
                existing_data = []
        except json.JSONDecodeError:
    # If the file is empty or contains invalid JSON, initialize as an empty list
            existing_data = []
        existing_data.append(data_to_add)
        file.seek(0)

        # Write the updated JSON object back to the file
        json.dump(existing_data, file, indent=4)






if __name__ == '__main__':
    translator = agent("gpt-3.5-turbo", name= "Translation 3.5",
                      preprompt="",
                      postprompt="", color="green")

    translator2 = agent("gpt-4", name= "Translation 4",
                      preprompt="",
                      postprompt="", color="blue")

    no_image_path = 'diagram_understanding/data/GeomVerse/NO_IMG_TEST/D2_STD_NO_IMG/data.jsonl'
    yes_image_path = 'diagram_understanding/data/GeomVerse/TEST/D2_STD/data.jsonl'
    output_path = 'diagram_understanding/data/instructionize/Geomverse/D2/D2_STD_caption.json'

    # Initialize an empty list to hold the questions
    no_image_questions, _ = extract_questions(no_image_path)
    yes_image_questions, image_paths = extract_questions(yes_image_path)
    assert len(no_image_questions) == len(yes_image_questions), "The number of questions in the two files should be the same"


    print(f'How Many Questions :  {len(no_image_questions)}')

    # subdirectories = list_subdirectories(json_paths)


    i = 0
    for j in range(len(yes_image_questions)):

        #
        #
        # if j<200:
        #     continue

        subd = f'{j}'
        print("Current problem number : " + subd)

        # logic_form = json_to_string(json_paths + '/'+ subd + '/logic_form.json')
        prompt = geomverse_no_image.replace("<Q_1>", yes_image_questions[j]).replace("<Q_2>", no_image_questions[j])
        # print(prompt)
        try:
            answer  = translator.talk(context=prompt)
        except :
            try:
                print(f"Prompt length : {len(prompt)}")
                answer  = translator2.talk(context=prompt)

            except :
                answer = translator2.talk(context=prompt[-12000:-1])


        #Preprocessing the answer
        try: answer = answer.split('[')[1].split(']')[0]
        except :
            try: answer = answer.split("Caption : ")[1]
            except : pass



        add_to_json(image_paths[j], answer, output_path)



        # natural_form = natural_form.replace("\n","").replace("\\", "")
        print("---\n\n")
        # write_to_json(natural_form, file_name= json_paths + '/' + subd  +"/natural_form.json")




