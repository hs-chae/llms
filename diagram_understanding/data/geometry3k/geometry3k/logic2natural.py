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

from ....dialogue import *
from ...prompt import prompt_geometry3k


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








if __name__ == '__main__':
    translator = agent("gpt-3.5-turbo", name= "Translation 3.5",
                      preprompt="",
                      postprompt="", color="green")

    translator2 = agent("gpt-4", name= "Translation 4",
                      preprompt="",
                      postprompt="", color="blue")
    json_paths= 'diagram_understanding/data/geometry3k/geometry3k/test'
    subdirectories = list_subdirectories(json_paths)


    i = 0
    for j in range(len(subdirectories)):
        j = j +2401
        if j<2710:
            continue

        subd = f'{j}'
        print("Current problem number : " + subd)

        logic_form = json_to_string(json_paths + '/'+ subd + '/logic_form.json')
        prompt = prompt_geometry3k.replace('<INPUT>',logic_form)
        try: natural_form  = translator.talk(context=prompt).replace('"""','')
        except :
            try:
                print(f"Prompt length : {len(prompt)}")
                natural_form  = translator2.talk(context=prompt).replace('"""','')
            except :  natural_form = translator2.talk(context=prompt[-12000:-1])

        natural_form = natural_form.replace("\n","").replace("\\", "")
        print(natural_form)
        write_to_json(natural_form, file_name= json_paths + '/' + subd  +"/natural_form.json")




