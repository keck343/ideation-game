from typing import List
from world_sectors_camps import BeitSector, GimelSector, SectorObjectified

class IdeaObjectified:
    def __init__(self, name, description, creator, sectors: List = [], camps: List = []):
        self.name: str = name
        self.description: str = description
        self.creator: str = creator
        self.emotions: List[str] = []
        self.other_ideas_interacted_with: List[IdeaObjectified] = []
        self.status: str = "Essential"
        self.sectors: List[SectorObjectified] = sectors
        self.camps: List = camps
        self.rejected_sectors: List[SectorObjectified] = []
        self.rejected_camps: List = []

    def print_name(self):
        print(self.name)

    def describe_self(self):
        return self.description.capitalize()

    def expand_idea(self, expansion):
        if self.description.strip().lower() == "unknown":
            self.description = f"{expansion}"
        else:
            self.description += f" and {expansion}"

    def rewrite_idea(self, rewrite):
        self.description = rewrite

    def record_interaction(self, other_text: str):
        self.other_ideas_interacted_with.append(other_text)

    def expansive_interaction(self, other_idea):
        self.description += f" and {other_idea.describe_self()}"

    def add_emotion(self, emotion):
        self.emotions.append(emotion)

    def summarize_self(self):
        pass

    def add_sector(self, sector):
        self.sectors.append(sector)

    def remove_sector(self, sector):
        self.rejected_sectors.append(sector)
        if sector in self.sectors:
            self.sectors.remove(sector)
            return f"You left {sector} behind."
        else:
            return f"You had already left {sector}."

    def add_camp(self, camp):
        self.sectors.append(camp)

    def remove_camp(self, camp):
        self.rejected_camps.append(camp)
        if camp in self.camps:
            self.remove_camp()
            return f"You rejected {camp}."
        else:
            return f"You had already rejected {camp}."



"""
These are the incumbents of the current iteration of the collective unconscious.
"Generic" can be seen as an insult, I simply mean to denote ideas whose content does not effect the plot.
Ideas whose status is generic can be interchanged for user generated ideas automatically.
Most ideas feel more essential and urgent when they are first thought. 
"""

# TO DO: Create Earth Person class in world_beings.py, currently using string names

Inspiration001 = IdeaObjectified(name="Rakonto 365.1",
                                 description="I want to write a tale about how my cat in unknowable.",
                                 creator="Terpersono 365")

Inspiration001.status = "Number Structure Needed"

Overwhelm001 = IdeaObjectified(name="Nihilismo 365.15",
                               description="""We are at the end of history.
                                            Each cycle is the same horrible history repeated.
                                            Nothing matters anyways.""",
                               creator="Terpersono 365")

Overwhelm001.status = "Number Structure Needed"

DefaultIdea = IdeaObjectified(name="Origina Ideo",
                              description="Make the Idea Novel into a Game!",
                              creator="Quinn Ray Keck")

DefaultIdea.status = "Debugging"

Conspiracism001 = IdeaObjectified(name="Intentionalism",
                                  description="""The world is a battle between good and evil.
                                   Everything has a deeper meaning behind it.
                                   Study will reveal the plans of those in power.""",
                                  creator="Beit",
                                  camps=["Affirmation Salvation"],
                                  sectors=[BeitSector])

Systems001 = IdeaObjectified(name="Complication",
                             description="""
                              Knowledge is a collective pursuit.
                              Nothing is certain, but some things have more compelling evidence.""",
                             creator="Gimel",
                             camps=["Attention Optimization"],
                             sectors=[GimelSector])

