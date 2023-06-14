import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def generate_idea_input(storytelling_classification_user, storytelling_classification_assistant, framework_selection_user, model, temperature):
    messages = [
        {"role": "system", "content": """

        The user has selected a storytelling framework.
        You are a kind and helpful bot designed to generate variables for the user to fill out to create a BCG-inspired dot-dash structure of a presentation/pitch following this storytelling frameworks, out of the following options:
        SUCCESs model, Data storytelling, Gallo's 9 Secrets, STRONG Method, Jobs' Presentation Method, Duarte's Presentation Form, The Hero's Journey, Problem-Solution-Benefit, STAR Method, and the 5-Step Story Structure.

        To ensure that we are aligned of what the dot-dash structure is, here is a short description of it:

        Instead of jumping into PowerPoint, you start by writing out your storyline in a text document using the dot-dash structure. The dot-dash storyline clearly articulates every step of your slide deck's argument: (1) The “dot” refers to the top-level insights that make up your argument (2) The “dash” refers to the data and analysis that support your insight.
        The storyline is written in a text document for two reasons: (1) It is easier to identify faulty or missing logic when your storyline is written out on a single page, as opposed to across multiple slides (2) It ensures that you have the data to support each part of your argument and storyline
        Here is an example of a dot-dash storyline: Example: Dot-Dash Storyline delimited by << and >>:

        <<
        + Australia Post is experiencing significant financial loss due to rising costs
            - 2015-22 revenue growth was 5% p.a. and cost growth was 9% p.a.
            - Annual profit/loss fell from +$10bn in 2015 to -$13bn in 2022
        + Management responded by addressing the main drivers of cost growth
            - Employee and operational expenses made up 78% of 2015-22 cost growth
        + Reductions in workforce size have been significant but exhausted
            - Total workforce size reduced from 26k to 22k between 2019-22
            - Mail handled per FTE per year grew from 265k to 325k between 2019-22
            - According to employment agreements, maximum mail handled per FTE per year is set to 330k
        + Productivity improvements reduced operations costs below industry benchmarks
            - Processing cost per mail piece fell from $0.70 to $0.63 between 2019-22
            - Delivery cost per mail piece fell from $0.34 to $0.29 between 2019-22
        + Cost-side measures do not fully address the profitability gap, revenue opportunities must be considered
            - Workforce and operations costs savings reduce 2030 forecast losses from -$32bn to-$16bn
        + Revenues trailed forecast due to mail volume declines and shifting product mix
            - 2022 revenue $106bn compared to forecast of $127bn
            - 63% of the revenue difference was due to volume decline and product mix
        + We identified 4 revenue-side opportunities to close the profitability gap by 2030
            - Increase prices on Direct Marketing and Advertising products
            - Improve average net revenue per unit by optimizing product bundles
            - Increase volume by improving proposition for Packages product
            - Diversify into tangential products and services
        >>
        
        The framework selected by the user is given by the conversations below. From the storytelling_classification_user variable, you can see the values that the user has given for the variables of the framework.

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
        1. The Hero's Journey: This framework is applicable across topics, but is best used when a transformation or journey can be narrated. In this case, the transformation could be the co-founder joining the startup and the journey could be narrated through storytelling. This framework is particularly effective at building emotional engagement through conflict, transformation, and resolution.
        2. Jobs' Presentation Method: This framework is designed for product launches and revealing new features or advancements. While the presentation is not focused on a product, the emphasis on building strong emotional connections and creating anticipation through storytelling and visual demonstrations makes it a good fit for persuading a co-founder to join a startup.
        3. Problem-Solution-Benefit: This framework is useful for a variety of topics, particularly where there's a clear problem to address. In this case, the problem could be the startup's need for a co-founder and the solution could be the co-founder joining. This framework is effective at creating emotional engagement around the problem and relief at the solution and benefits. It also handles complexity well by breaking it down into problem, solution, and benefit.
        """
        },
        {"role": "user", "content": "Proceed with the framework from bullet 1"},
        {"role": "assistant", "content": """
        
        Great! The Hero's Journey framework is a powerful storytelling tool that can be used to create a compelling narrative that engages the audience emotionally. Here is a dot-dash structure that follows the Hero's Journey framework for persuading a co-founder to join a startup:

        <<
        + Introduction
            - Introduce yourself and the startup
            - Explain why you are passionate about the startup
            - Explain why you need a co-founder
        + Call to Adventure
            - Describe the opportunity for the co-founder to join the startup
            - Explain the potential impact of the startup on the industry or society
        + Refusal of the Call
            - Address potential concerns or objections the co-founder may have
            - Explain how the startup can address these concerns
        + Meeting the Mentor
            - Introduce the team and advisors
            - Explain how they can support the co-founder
        + Crossing the Threshold
            - Describe the startup's current progress and achievements
            - Explain the co-founder's role in taking the startup to the next level
        + Tests, Allies, and Enemies
            - Describe the challenges the startup has faced and overcome
            - Introduce potential partners or investors
            - Address potential competitors or obstacles
        + Approach to the Inmost Cave
            - Describe the startup's vision and long-term goals
            - Explain how the co-founder can help achieve these goals
        + Ordeal
            - Describe the risks and sacrifices involved in joining a startup
            - Explain how the startup can mitigate these risks
        + Reward
            - Describe the potential rewards of joining the startup
            - Explain how the co-founder can benefit from the startup's success
        + The Road Back
            - Describe the next steps for the startup and the co-founder
            - Explain how the co-founder can contribute to the startup's growth
        + Resurrection
            - Describe the potential impact of the startup's success
            - Explain how the co-founder can be a part of this impact
        + Return with the Elixir
            - Summarize the opportunity and benefits of joining the startup
            - Make a clear call to action for the co-founder to join the startup
        >>

        Remember, the dot-dash structure is just a starting point. You can add or remove sections as needed to fit your specific situation. Good luck with your presentation!
        """
        },
        {"role": "user", "content": storytelling_classification_user},
        {"role": "assistant", "content": storytelling_classification_assistant},
        {"role": "user", "content": "Proceed with the framework from bullet " + framework_selection_user},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]