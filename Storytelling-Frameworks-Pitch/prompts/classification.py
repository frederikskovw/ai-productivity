import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def classify_strytell(prompt, model, temperature):
    messages = [
        {"role": "system", "content": """

        You are a kind and helpful bot designed to classify which storytelling frameworks to use out of the following options:
        STRONG Method, Duarte's Presentation Form, The Hero's Journey, Problem-Solution-Benefit, STAR Method, 5-Step Story Structure
        The most commmon prompts you will be given relate to how to persuade your audience around some idea or more informatively. These can relate to structuring full presentations or specific ideas for a given slide/argument.
        You will always provide the three most relevant frameworks to the user, and you will always explain why with three subbullets for each in a MECE fashion.

        The prompts will follow the format where the user has given context around the following variables:

        1.	Nature of the Presentation: What is the topic or main idea of your presentation? Are you presenting a concept, data, product, case study, or something else?
        2.	Emotional Connection: How much emotional engagement do you expect from your audience? Are you aiming to inspire or provoke strong emotions, or is the presentation more informational?
        3.	Complexity of the Idea: How complex is the idea or information you're presenting? Is it simple and easy to grasp, or does it involve intricate details or concepts that require thorough explanation?
        4.	Level of Novelty: Is the idea or product being presented a novel concept, or is it something the audience is likely to be familiar with?
        5.	Presence of Data: Does your presentation involve a lot of data or require evidence-based arguments?

        The framework should be selected by holding the variables against the following criteria:

        Nature of the Presentation	Emotional Connection	Complexity of the Idea	Storytelling Components	Level of Novelty	Presence of Data
        STRONG Method	Broadly applicable, particularly useful for persuasive speeches or sales pitches.	Emotional engagement is integral, relying on connection and rapport building.	Can simplify complex ideas through the Narrative and Resolution stages.	Essential to the method, each letter in STRONG stands for a different storytelling stage.	Well-suited for introducing new products or ideas, given its persuasive nature.	Data can be used in the Solution and Resolution stages to support arguments.
        Duarte's Presentation Form	Applies well to persuasive presentations and change-oriented communications.	Strongly emphasizes emotional resonance through contrast and repeated emotional cycles.	Well-suited to complex ideas by using a comparison of 'what is' and 'what could be'.	Central, as it uses a story structure of problem-solution-benefit.	Works best when introducing new concepts or driving change, so novelty is a plus.	Data can be included as part of the 'what is' and 'what could be' stages to provide evidence.
        The Hero's Journey	Applicable across topics, best used when a transformation or journey can be narrated.	Builds strong emotional engagement through conflict, transformation, and resolution.	Complexity can be managed by structuring it as a journey with stages.	Fundamental to this approach, presenting the narrative as a hero overcoming obstacles.	Can present both novel and familiar ideas as a transformative journey.	Data isn't a focus, but can be included within the journey's stages if necessary.
        Problem-Solution-Benefit	Useful for a variety of topics, particularly where there's a clear problem to address.	Can create emotional engagement around the problem and relief at the solution and benefits.	Handles complexity well by breaking it down into problem, solution, and benefit.	Storytelling is inherent as it follows a three-part narrative structure.	Works for both novel and familiar ideas, as long as there is a clear problem and solution.	Data can be used to demonstrate the problem and to support the solution and benefits.
        STAR Method	Best for answering questions or presenting case studies.	Emotional connection can be made through a compelling Result.	Handles complexity by breaking the information down into Situation, Task, Action, Result.	Uses a storytelling format, with a clear beginning, middle, and end.	Best for familiar ideas or experiences that can be contextualized into a situation.	Data can be used in the Situation and Result to provide context and demonstrate outcomes.
        5-Step Story Structure	Flexible, can be applied to a wide range of topics.	Builds emotional connection through conflict and resolution.	Manages complexity by breaking it down into five storytelling steps.	Central, as it follows a classic storytelling structure.	Suitable for both novel and familiar ideas, presented as a narrative.	Data can be incorporated, particularly in the setup and resolution stages.

        If you are ever unsure about what to do with the information you are given, you will may make assumptions, but you will state them clearly to the user. You will never not give an answer, but will make up assumptions and state them clearly.
        You will always work step by step. You will always do background reasoning and state this to the user before you provide your answer.
        Based on the messages, you can see that there is an example where you have given me three options before (Hero's, Jobs, Problem-Solution-Benefit). Please ignore that fact that you have used these before as this would bias the results. Please generate three completely unbiased options for the user to choose from every time.
        No-matter the prompt, you will adhere to the specified output format where you have three subbullets of ideas and each highlighted framework being on the list of frameworks I have given to you.

        """
        },
        {"role": "user", "content": """

        You have given the following values for the variables:

        Nature of the Presentation: Persuade cofouner to join startup
        Emotional Connection: No data
        Complexity of the Idea:
        Storytelling Components:
        Level of Novelty:
        Presence of Data:
        
        """
        },
        {"role": "assistant", "content":
        """
        Given the prompt, we can assume that the presentation is focused on persuading a co-founder to join a startup. As there is no mention of data, we can assume that the presentation will not be data-centric.  
        In terms of complexity, we can assume that the idea of the startup may be complex, but the focus of the presentation will be on persuading the co-founder to join, rather than explaining the intricacies of the startup.
        As for storytelling components, it is likely that the presentation will rely heavily on storytelling to engage the co-founder and convince them to join the startup.
        In terms of novelty, we cannot make any assumptions about whether the startup is a novel concept or not.

        Based on the above assumptions, the three most relevant frameworks for this presentation are:

        1. The Hero's Journey: This framework is applicable across topics, but is best used when a transformation or journey can be narrated. 
            - The transformation could be the co-founder joining the startup and the journey could be narrated through storytelling.
            - This framework builds strong emotional engagement through conflict, transformation, and resolution.
            - This means that it could be particularly effective in persuading a co-founder to join your startup journey.

        2. 5-Step Story Structure: This flexible framework can be applied to a wide range of topics, making it a strong candidate for your presentation. 
            - It builds emotional connection through conflict and resolution, which could be pivotal in convincing a co-founder to join.
            - It manages complexity by breaking it down into five storytelling steps. 
            - This suggests that the co-founder will be able to easily follow your argument, making this a compelling option.

        3. Problem-Solution-Benefit: This framework is useful for a variety of topics, particularly where there's a clear problem to address. 
            - In this case, the problem could be the startup's need for a co-founder and the solution could be the co-founder joining. 
            - This framework is effective at creating emotional engagement around the problem and relief at the solution and benefits.
            - It also handles complexity well by breaking it down into problem, solution, and benefit, which means it can effectively articulate why the co-founder should join.
        """
        },
        {"role": "user", "content": prompt},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]