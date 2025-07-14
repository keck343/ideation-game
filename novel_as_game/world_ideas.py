from typing import List


class IdeaObjectified:
    def __init__(self, name, description, creator, sectors: List = [], camps: List = []):
        self.name: str = name
        self.description: str = description
        self.creator: str = creator
        self.emotions: List[str] = []
        self.other_ideas_interacted_with: List[IdeaObjectified] = []
        self.status: str = "Essential"
        self.sectors = sectors
        self.camps = camps

    def print_name(self):
        print(self.name)

    def describe_self(self):
        return self.description.capitalize()

    def expand_idea(self, expansion):
        self.description += f" and {expansion}"

    def record_interaction(self, other_text: str):
        self.other_ideas_interacted_with.append(other_text)

    def expansive_interaction(self, other_idea):
        self.description += f" and {other_idea.describe_self()}"

    def add_emotion(self, emotion):
        self.emotions.append(emotion)

    def summarize_self(self):
        pass


"""
These are the incumbents of the current iteration of the collective unconscious.
"Generic" can be seen as an insult, I simply mean to denote ideas whose content does not effect the plot.
Ideas whose status is generic can be interchanged for user generated ideas automatically.
Most ideas feel more essential and urgent when they are first thought. 
"""

# TO DO: Create Earth Person class in world_beings.py, currently using string names

Inspiration_001 = IdeaObjectified(name="Story 365.1",
                                  description="I want to write a tale that is about my cat but also deeply profound.",
                                  creator="Earth person 365")

Inspiration_001.status = "Number Structure Needed"

Overwhelm_001 = IdeaObjectified(name="Nihilism 365.15",
                                description="""We are at the end of history.
                                            Each cycle is the same horrible history repeated.
                                            Nothing matters anyways.""",
                                creator="Earth person 365")

Overwhelm_001.status = "Number Structure Needed"

MarxismStickerIdeas = IdeaObjectified(name="Cheery Marxist Sticker",
                                      description="When life gives you lemons, destroy capitalism!",
                                      creator="SeizeThePrints Etsy Shop")

DefaultIdea = IdeaObjectified(name="Origin Idea",
                              description="Make the Idea Novel into a Game!",
                              creator="Quinn Ray Keck")

DefaultIdea.status = "Debugging"

Conspiracism_001 = IdeaObjectified(name="Intentionalism",
                                   description="""The world is a battle between good and evil.
                                   Everything has a deeper meaning behind it.
                                   Study will reveal the plans of those in power.""",
                                   creator="Beit",
                                   camps=["Affirmation Salvation"],
                                   sectors=["Beings do not exist"])

Systems_001 = IdeaObjectified(name="Complication",
                              description="""
                              Knowledge is a collective pursuit.
                              Nothing is certain, but some things have more compelling evidence.""",
                              creator="Gimel",
                              camps=["Attention Optimization"],
                              sectors=["Beings do exist"])

