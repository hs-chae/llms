ex_COT = """
Let's think step by step. 
"""

ex_SPP = '''When faced with a task, begin by identifying the participants who will contribute to solving the task. Then, initiate a multi-round collaboration process until a final solution is reached. The participants will give critical comments and detailed suggestions whenever necessary.

Here are some examples:
---
Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once.
Input: 6 12 1 1

Participants: AI Assistant (you); Math Expert

Start collaboration!

Math Expert: Let's analyze the task in detail. You need to make sure that you meet the requirement, that you need to use exactly the four numbers (6 12 1 1) to construct 24. To reach 24, you can think of the common divisors of 24 such as 4, 6, 8, 3 and try to construct these first. Also you need to think of potential additions that can reach 24, such as 12 + 12.
AI Assistant (you): Thanks for the hints! Here's one initial solution: (12 / (1 + 1)) * 6 = 24
Math Expert: Let's check the answer step by step. (1+1) = 2, (12 / 2) = 6, 6 * 6 = 36 which is not 24! The answer is not correct. Can you fix this by considering other combinations? Please do not make similar mistakes.
AI Assistant (you): Thanks for pointing out the mistake. Here is a revised solution considering 24 can also be reached by 3 * 8: (6 + 1 + 1) * (12 / 4) = 24.
Math Expert: Let's first check if the calculation is correct. (6 + 1 + 1) = 8, 12 / 4 = 3, 8 * 3 = 24. The calculation is correct, but you used 6 1 1 12 4 which is not the same as the input 6 12 1 1. Can you avoid using a number that is not part of the input?
AI Assistant (you): You are right, here is a revised solution considering 24 can be reached by 12 + 12 and without using any additional numbers: 6 * (1 - 1) + 12 = 24.
Math Expert: Let's check the answer again. 1 - 1 = 0, 6 * 0 = 0, 0 + 12 = 12. I believe you are very close, here is a hint: try to change the "1 - 1" to "1 + 1".
AI Assistant (you): Sure, here is the corrected answer:  6 * (1+1) + 12 = 24
Math Expert: Let's verify the solution. 1 + 1 = 2, 6 * 2 = 12, 12 + 12 = 12. You used 1 1 6 12 which is identical to the input 6 12 1 1. Everything looks good!

Finish collaboration!

Final answer: 6 * (1 + 1) + 12 = 24

---
Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid.

Participants: AI Assistant (you); Poet; Computer Scientist; Ten year old child

Poet: Make sure that you write the poem with seven lines, and the first letters of the lines should be C, H, A, T, G, P, T.
Computer Scientist: A quantum computer is an advanced computing device that uses the principles of quantum mechanics to process and store information. Unlike classical computers that use bits to represent information as 0s and 1s, quantum computers use quantum bits or qubits. Qubits can exist in multiple states simultaneously, due to a quantum phenomenon called superposition. You can consider using these information for the poem.
Ten year old child: I hope the poem to be fun and easy to understanding. I don't want to see a lot of jargons or complicated concepts.
AI Assistant (you): Thanks for the guidance! Here's my initial attempt at the poem:
Computational wonder of our age,
Harnessing the quantum world's strange ways,
Atoms dance, entwined in dual state,
Tapping secrets hidden in their haze.

Grand power to solve, simulate,
Profound problems that perplex the wise,
Transforming our future, we await.

Poet: Let's verify if the poem meets the requirements. The first letters are CHATGPT which is correct! And the poem rhymes well. Good job!
Computer Scientist: Everything looks good to me!
Ten year old child: I don't know what does perplex mean. Can you make the use of words easier to understand?
AI Assistant (you): Sure, let me revise the poem by using more common words. Check out the revised version:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

Poet: Let's check again if the poem meets the requirements. The first letters are C H A T G P T. And now the poem is more accessible to children. Everything looks good to me.
Computer Scientist: Looking good!
Ten year old child: I like this version a lot!

Finish collaboration!

Final answer:
Curious machine of our time,
Harnessing the quantum realm's odd ways,
Atoms play, two states they embrace,
Taking secrets from their puzzling maze.

Great power to solve and imitate,
Problems that confuse the brightest minds,
Transforming our future, we await.

---
Now, identify the participants and collaboratively solve the following task step by step. Remember to provide the final solution with the following format "Final answer: The house number here.".

Task: {input}
'''

ex_TERA = '''
In addressing complex tasks, it's beneficial to engage participants with defined roles that bring diverse perspectives and approaches to the problem-solving table. This structured collaboration involves iterative discussions, critiques, and refinements led by participants who contribute their unique insights and expertise.

Here are the role frameworks to utilize:

Pros, Cons, Judge: This framework involves participants who advocate for the positive aspects (Pros) of potential solutions, those who highlight the negative aspects (Cons), and a Judge who balances these viewpoints to guide the decision-making process towards a balanced resolution.
Examples:

Example Task 1: Introducing a new technology in the workplace

Participants: Pros Advocate, Cons Advocate, Judge

Pros Advocate: Highlights the potential for increased efficiency and productivity that the new technology could bring, such as automation of mundane tasks and improved data management.
Cons Advocate: Raises concerns about the potential drawbacks, including the cost of implementation, the learning curve for employees, and possible disruptions during the transition period.
Judge: Weighs the arguments presented by both the Pros and Cons Advocates. The Judge considers the long-term benefits against the short-term challenges and resources required for the implementation of the new technology.
Through a balanced examination of the pros and cons, the Judge decides to proceed with a pilot program for the new technology. This approach allows for a smaller-scale implementation to evaluate its impact and address any issues before a full rollout.

Final solution: Initiate a pilot program for the new technology, allowing for evaluation and adjustments before deciding on a wider implementation.

---

Example Task 2: Implementing a new remote work policy

Participants: Dreamer, Realist, Critic

Dreamer: Proposes a flexible policy allowing employees to work from anywhere, aiming to boost morale and productivity by offering maximum flexibility.
Realist: Evaluates operational and collaboration needs, suggesting a hybrid model that balances remote work with regular in-office days to maintain team cohesion.
Critic: Highlights potential challenges in team communication and project management, recommending clear guidelines and tools to support effective remote collaboration.
After thorough deliberation, the team decides on a hybrid remote work policy with clear guidelines and support for remote collaboration, ensuring operational efficiency and team cohesion.

Final solution: Adopt a hybrid remote work policy with defined in-office days to foster team interaction, supported by comprehensive guidelines and tools for remote collaboration.

---

Example Task 3: Designing a new public library system

Participants: Reasoner, Planner, Critic

Reasoner: Analyzes the current needs of the community, the evolving role of libraries, and how digital resources can be integrated with traditional services. The Reasoner suggests a library system that combines physical spaces with digital platforms for wider access.
Planner: Develops a detailed plan for the library system, including the layout of physical library spaces, the digital platform's architecture, and a phased implementation schedule. The plan also includes budget estimates and resource allocation.
Critic: Reviews the plan to identify potential issues such as budget overruns, underestimation of resources needed for digital platform maintenance, and accessibility issues for different community segments. The Critic suggests adjustments to ensure the plan is realistic and inclusive.
After several rounds of discussion and refinement, taking into account the Critic's feedback, the team finalizes a comprehensive plan for a hybrid library system that addresses both current and future needs of the community.

Final solution: Implement a hybrid public library system that integrates physical library spaces with an extensive digital platform, offering a wide range of resources and services accessible to the entire community. The implementation will be phased, with ongoing evaluation and adjustment to ensure the system meets community needs effectively.


---

Now, apply these frameworks to collaboratively address the following task. Remember to iterate through the process and provide the final solution in the format "Final answer: [Solution here]."

Task: {input}
'''
