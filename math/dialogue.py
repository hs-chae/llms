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

from .prompts.examples import ex_COT, ex_SPP


def role_to_color(role):
    if role not in ["system", "user", "assistant", "function", "debug"]:
        raise ValueError("Invalid role")
    elif role == "system": return "cyan"
    elif role == "user": return "green"
    elif role == "assistant": return "yellow"
    elif role == "agent": return "yellow"
    elif role == "function": return "magenta"
    elif role == "debug": return "red"
    else: return "white"


class agent:
    def __init__(self, model, storage_path = "storage", name = "Assistant", preprompt = "", postprompt="", temperature = 0.5, max_token = 1024, color = "yellow"):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        openai.api_key = self.api_key
        self.client = OpenAI()

        self.model = model
        self.name = name

        self.preprompt = preprompt
        self.postprompt = postprompt

        self.messages = []
        self.record_messages = False
        self.background = ""


        #other config
        self.temperature = temperature
        self.max_token = max_token
        self.color = color




    def talk(self, context = "", additional_input = ""):
        """
        This function receives context and question if needed
        """

        message = self.preprompt + context + self.postprompt

        self.messages_for_question = [{
            "role": "system",
            "content": (message),
        }]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages_for_question,
            temperature=self.temperature,
            stream=True,
            max_tokens=self.max_token,
        )

        # Process the stream to extract emotions
        role = ""
        answer = ""



        for chunk in response:
            choice = chunk.choices[0]
            if choice.delta.role is not None:
                role = choice.delta.role
                if role == "assistant":
                    print(colored(f"{self.name} : ", role_to_color(role)), end="", flush=True)
            else:
                content = choice.delta.content
                if content is not None:
                    answer += content
                    if role == "assistant":
                        print(colored(f"{content}", self.color), end="", flush=True)
            time.sleep(0.05)
        print()

        return answer





if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)

    spiderman = agent("gpt-4", name = "Spiderman", preprompt="You are Spiderman. You should act like a friendly neighbor superhero. ", postprompt= "\nSpiderman : ", color = "green")
    superman = agent("gpt-4", name="Superman",
                      preprompt="You are Superman. You should act like Superman, thinking that no superheros are needed anymore besides yourself. ",
                      postprompt="\nSuperman : ",
                        color = "blue")


    question = "You are involved in the follwing debate: Do we still need superheros when there are no villains??"
    print("Question : " + question)

    history = question
    for i in range(3):
        talk_spidy = spiderman.talk(context=history)
        history += "\n" + talk_spidy

        talk_sup = superman.talk(context=history)
        history += "\n" +  talk_sup


    # questions = []
    # with open('gsm8k_questions.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         # Extracting the question surrounded by quotes
    #         question = row[0].strip('"')
    #         questions.append(question)
    #
    #
    #
    # module = my_gpt("gpt-4", "./storage", prompt = my_prompt)
    #
    # with open('results/90result.csv', 'w', newline='') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(['Question', 'Answer'])
    #
    #     for i in range(len(questions)):
    #
    #         if i < start_index or i>end_index :
    #             continue
    #
    #
    #         question = questions[i]
    #         exact_question = question.split("Question:")[-1].split("Answer")[0]
    #         print(f"\n\nQ{i}------------------------------\n" + exact_question)
    #         answer = module.answer(question)
    #
    #         writer.writerow((exact_question, answer))
    #         time.sleep(2)


