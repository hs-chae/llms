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


def extract_questions(caption_path):
    with open(caption_path, 'r') as file:
        # Read the entire file content and parse it as JSON
        data = json.load(file)

    yes_image_questions = []
    image_paths = []

    # Iterate through the list of data
    for item in data:
        image_path = item.get("image_path")
        caption = item.get("caption")

        # Process your data here
        # For example, appending paths and questions to lists
        image_paths.append(image_path)
        yes_image_questions.append(caption)  # Assuming you process captions into questions

    return yes_image_questions, image_paths


def add_to_json(image_path, caption, file_name):
    # Add the caption to the JSON object
    data_to_add = {"image_path": image_path, "conversation": caption}

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


    caption_path = 'diagram_understanding/data/instructionize/Geomverse/D3/D3_caption.json'
    output_path = 'diagram_understanding/data/instructionize/Geomverse/D3/D3_conv_tmp.json'

    # Initialize an empty list to hold the questions

    yes_image_questions, image_paths = extract_questions(caption_path)



    print(f'How Many Questions :  {len(yes_image_questions)}')

    # subdirectories = list_subdirectories(json_paths)


    i = 0
    for j in range(len(yes_image_questions)):

        #
        #
        if j>=862:
            continue

        subd = f'{j}'
        print("Current problem number : " + subd)

        # logic_form = json_to_string(json_paths + '/'+ subd + '/logic_form.json')
        prompt = geomverse_conversation.replace("<CAPTION>", yes_image_questions[j])
        print("\nCaption : ", yes_image_questions[j])
        try:
            answer  = translator.talk(context=prompt)
        except :
            try:
                print(f"Prompt length : {len(prompt)}")
                answer  = translator2.talk(context=prompt)

            except :
                answer = translator2.talk(context=prompt[-12000:-1])


        #Preprocessing the answer
        try:
            answer = answer.split('[')[1].split(']')[0]
            answer = '[' + answer + ']'
        except : pass



        add_to_json(image_paths[j], eval(answer), output_path)




        print("---\n\n")





