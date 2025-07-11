from typing import List


class IdeaObjectified:
    def __init__(self, name, description, creator):
        self.name: str = name
        self.description: str = description
        self.creator: str = creator
        self.emotions: List[str] = []
        self.other_ideas_interacted_with: List[IdeaObjectified] = []
        self.status: str = "Essential"

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

    def summarize_self(self):
        pass


"""
These are the incumbents of the current iteration of the collective unconscious.
"Generic" can be seen as an insult, I simply mean to denote ideas whose content does not effect the plot.
Ideas whose status is generic can be interchanged for user generated ideas automatically.
Most ideas feel more essential and urgent when they are first thought. 
"""

# TO DO: Create Earth Person classin world_narrators.py, currently using string names

BFFIdea = IdeaObjectified(name="BFF",
                          description="When life gives you lemons, make lemonade!",
                          creator="Zeitgeist")
BFFIdea.status = "Generic"


Hope_001 = IdeaObjectified(name="Hope 365.25",
                           description="Each cycle we spiral outwards into new growth.",
                           creator="Earth person 365")

Hope_001.status = "Number Structure Needed"

Fear_001 = IdeaObjectified(name="Fear 365.25",
                           description="Each cycle is the same horrible history repeated.",
                           creator="Earth person 365")

Fear_001.status = "Number Structure Needed"

MarxismStickerIdeas = IdeaObjectified(name="Cheery Marxist Sticker",
                                      description="When life gives you lemons, destroy capitalism!",
                                      creator="SeizeThePrints Etsy Shop")

DefaultIdea = IdeaObjectified(name="Origin Idea",
                              description="Make the Idea Novel into a Game!",
                              creator="Quinn Ray Keck")

DefaultIdea.status = "Debugging"
