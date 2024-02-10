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