from typing import List
from world_camps import (
    KonspiroCamp, KristanaCamp)

class SectorObjectified:
    def __init__(self, known_name: str, core_belief: str, beings_exist: bool,
                 dinner_talking_points: dict, camps: List = []):
        self.name: str = known_name
        self.core_belief: str = core_belief
        self.beings_exists: bool = beings_exist
        self.camps = camps
        self.dinner_talking_points = dinner_talking_points


BeitSector = SectorObjectified(known_name="Beit",
                               core_belief="There are no beings. Only optimizing the here and now.",
                               beings_exist=False,
                               camps=[KonspiroCamp],
                               dinner_talking_points={
                                   "sector": "Beings do not exist.",
                                   "Beings": """"Fools claim that Beings exist in a physical realm connected to ours.
                                    Some even claim that we come out of their thoughts, 
                                    as if we are not enough in and of ourselves. 
                                    As if something as foolish as attention could control our fate.""",
                                   "disappearance": """The Eksterteranoj's plans must be advancing quickly.""",
                                   "Beings counter point": """No one has ever seen a being.
                                    I believe in things I have done my own research on.""",
                                   "camp invitation": """You are correct to reject the nonsense of Beings.
                                   The party is almost over and we can't stay here.
                                   Would you like to join me at my camp for the next cycle?"""}
                               )

GimelSector = SectorObjectified(known_name="Gimel",
                                core_belief="Beings are probable to exist. There is a synthesis we do not yet know.",
                                beings_exist=True,
                                camps=[KristanaCamp],
                                dinner_talking_points={
                                    "sector": "The fact that Beings exist is widely accepted by most camps.",
                                    "Beings": """Through careful research into the disappearance of our kind,
                                    most scientists Beings exist in a physical realm that we are connected to.
                                    Our origin story is still a matter of debate, but most agree there is an 
                                    attention mechanism that can explains 98% of our disappearance rates.""",
                                    "disappearance": """Our top scientific camps are struggling 
                                    to find a pattern or cause, much less a solution.
                                    """,
                                    "Beings counter point": """How could so many camps, and even ones outside my sector
                                    come to conclude that we exist in a system with Beings?""",
                                    "camp invitation": """You are correct to accept the existence of Beings.
                                    The party is almost over and I'm afraid you might disappear without a camp,
                                    Top scientists say connection is key to existence.  
                                    Would you like to join me at my camp for the next cycle?
                                    """}
                                )
