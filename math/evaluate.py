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

def role_to_color(role):
    if role not in ["system", "user", "assistant", "function", "debug"]:
        raise ValueError("Invalid role")
    elif role == "system": return "cyan"
    elif role == "user": return "green"
    elif role == "assistant": return "yellow"
    elif role == "function": return "magenta"
    elif role == "debug": return "red"
    else: return "white"


class my_gpt:
    def __init__(self, model, storage_path, prompt = ""):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        openai.api_key = self.api_key
        self.client = OpenAI()

        self.model = model
        self.prompt = prompt

        # self.messages_for_imgprompt = []
        # self.user_preferences = user_preferences

        self.storage_path = storage_path
        assert (os.path.exists(self.storage_path))
        # self.diary_df_path = os.path.join(self.storage_path, "diary.csv")
        # self.diary_df = pd.read_csv(self.diary_df_path)

        # self.image = None
        # self.image_path = os.path.join(self.storage_path, "images")
        # assert (os.path.exists(self.image_path))
        # self.image_file = None
        #
        # self.use_refiner = use_refiner
        # self.max_refine_tries = 2
        #
        # self.logger = logging.getLogger()
        # self.user_bg = user_preferences

    def answer(self, question):
        """
        This function extracts emotions from the diary entry.
        """
        self.messages_for_question = [{
            "role": "system",
            "content": (self.prompt + question),
        }]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages_for_question,
            temperature=0.5,
            stream=True,
            max_tokens=1024,
        )

        # Process the stream to extract emotions
        role = ""
        answer = ""



        for chunk in response:
            choice = chunk.choices[0]
            if choice.delta.role is not None:
                role = choice.delta.role
                if role == "assistant":
                    print(colored(f"Assistant Answer: ", role_to_color(role)), end="", flush=True)
            else:
                content = choice.delta.content
                if content is not None:
                    answer += content
                    if role == "assistant":
                        print(colored(f"{content}", role_to_color(role)), end="", flush=True)
            time.sleep(0.05)
        print()

        return answer


    def extract_emotions(self, diary_entry):
        """
        This function extracts emotions from the diary entry.
        """
        self.messages_for_emotion_extraction = [{
            "role": "system",
            "content": EMOTION_EXTRACT_PROMPT.format(diary_entry),
        }]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages_for_emotion_extraction,
            temperature=0.9,
            stream=True,
            max_tokens=1024,
        )

        # Process the stream to extract emotions
        role = ""
        extracted_emotions = ""
        for chunk in response:
            choice = chunk.choices[0]
            if choice.delta.role is not None:
                role = choice.delta.role
                if role == "assistant":
                    print(colored(f"Extracted emotions: ", role_to_color(role)), end="", flush=True)
            else:
                content = choice.delta.content
                if content is not None:
                    extracted_emotions += content
                    if role == "assistant":
                        print(colored(f"{content}", role_to_color(role)), end="", flush=True)
            time.sleep(0.05)
        print()

        return extracted_emotions



my_prompt = ""
start_index = 0
end_index = 100

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    questions = []
    with open('gsm8k_questions.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Extracting the question surrounded by quotes
            question = row[0].strip('"')
            questions.append(question)



    module = my_gpt("gpt-4", "./storage", prompt = my_prompt)

    with open('results/90result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Question', 'Answer'])

        for i in range(len(questions)):

            if i < start_index or i>end_index :
                continue


            question = questions[i]
            exact_question = question.split("Question:")[-1].split("Answer")[0]
            print(f"\n\nQ{i}------------------------------\n" + exact_question)
            answer = module.answer(question)

            writer.writerow((exact_question, answer))
            time.sleep(2)




    #
    # imagen_module = DiaryImageGeneration("gpt-4", "./storage", question= ,prompt = "")
    # input_date = input("Enter date: ")
    # diary_date = int(input_date)
    #
    # generated_image = imagen_module.generate_image(diary_date)
    # Image.open(generated_image).show()
