geomverse_no_image = """
Your task is to write a caption for an image that is not present. You will be given two questions.
Question_1 is a question assuming the presence of an image. Question_2 is a same question as Question_1 but without providing the image.

Comparing these two questions carefully, check what's  in the image. Then write a precise and detailed caption for the image that is not present.
Give the caption in the following format: " `Caption` : `[description of the image]`. " For example, you can answer like this: "Caption : [There is a rectangle ADBC, sharing with its edge AB with another rectangle ABEF. On the left side of the rectangle ABEF, the edge AF is also a diameter of a semicircle drawn outside the rectangle ABEF. On the right side of ABEF, the edge BF is a part of a figure BEHI, which looks like a rectangle with some semicircle part, having line BI as its diameter inside, removed from the rectangle.]"
Remember to put your caption inside []. Note that the caption should be detailed and precise, and should not be a generic caption that could be used for any image.
Also remember that caption should not talk about solving the problem, it should only describe the image. Don't add any other pharses, like "The image is not present" or "This is the end of the caption". Just describe the image as if you are seeing it.


Be careful! Don't add any information that is not present in the question. Don't make up any facts about the image!
Be careful! Don't add any information that is not present in the question. Don't make up any facts about the image!
Be careful! Don't add any information that is not present in the question. Don't make up any facts about the image!

Question_1 : <Q_1>
Question_2 : <Q_2>

"""

geomverse_conversation = """
Your task is to write a conversation between a human and an assistant, about an image of geometric figures. You will be given a caption for the image, and the human will ask a question about the image, and the assistant will answer the question based on the caption.
Write the conversation in the following json format:
[
      {
        "from": "human",
        "value": "What do you see in the image?"
      },
      {
        "from": "gpt",
        "value": "The image shows a triangle ABC. The angle CAB is labeled as 40 degrees and the angle BCA is labeled as 45 degrees."
      },
      {
        "from": "human",
        "value": "Do you see a circle in the image?"
      },
      {
        "from": "gpt",
        "value": "No, there is no circle in the image."
      },
      {
        "from": "human",
        "value": "What is the perimeter of the triangle?"
      },
        {
            "from": "gpt",
            "value": "The information about the lengths of the sides of the triangle is not provided in the image. So, the perimeter of the triangle cannot be calculated."
        }    
]

The conversation SHOULD END IN ONE TO THREE ROUNDS. The human will ask information about the image, and the assistant will answer based only on the caption. 
The human may ask about something that is on the image, or not on the image, or ask for some measurements, or ask for some properties of the figures. 
The assistant should answer as if it is seeing the image, and should not make up any information that is not present in the caption.

Always remember the following rules:
1. Don't add any information that is not present in the caption!
2. Don't ask questions unrelated to describing the image! Don't ask about hidden values, just ask direct information only.
3. Don't ask to calculate or solve a problem! Don't ask for any measurements or calculations! Just ask : 'do you see some' or 'what do you see' or 'is there'
4.End the conversation in less than three rounds!


Caption : <CAPTION>
"""


geomverse_ferret = """
Your task is to 

"""