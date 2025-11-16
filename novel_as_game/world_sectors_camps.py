from typing import List


class SectorObjectified:
    def __init__(self, known_name: str, core_belief: str, beings_exist: bool,
                 dinner_talking_points: dict):
        self.name: str = known_name
        self.core_belief: str = core_belief
        self.beings_exists: bool = beings_exist
        self.camps = []
        self.dinner_talking_points = dinner_talking_points

    def add_camp(self, camp):
        self.camps.append(camp)


class CampObjectified:
    def __init__(self, sector: SectorObjectified, summary_statement: str,
                 counter_sector_statement: str, tenants: List[str],
                 stated_camp_core_belief: str, unstated_camp_core_belief: str):
        self.sector = sector
        self.sector_core_belief = sector.core_belief
        self.beings_exist = sector.beings_exists
        self.summary_statement = summary_statement
        self.counter_sector_statement = counter_sector_statement
        self.tenants = tenants
        self.stated_camp_core_belief = stated_camp_core_belief
        self.unstated_camp_core_belief = unstated_camp_core_belief

    def revise_summary(self, revision: str, append: bool = True):
        """
        if append = False summary statement is overwritten
        """
        if append:
            self.summary_statement += " & " + revision
        else:
            self.summary_statement = f"""We no longer believe: {self.summary_statement}
            We now believe: {revision}"""


BeitSector = SectorObjectified(known_name="Beit",
                               core_belief="There are no beings. Only optimizing the here and now.",
                               beings_exist=False,
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

KonspiroCamp = CampObjectified(sector=BeitSector,
                               summary_statement="""There is a secret circle running all of our existences.""",
                               counter_sector_statement="""
                               There are too many coincidences are happening for this all to be random""",
                               tenants=[
                                   "Everything that happens is result of someone’s plan",
                                   "The world is a battle between good and evil",
                                   "We are approaching a new world order",
                                   "When things go wrong, it demonstrates the planning of whoever is in charge",
                               ],
                               stated_camp_core_belief="""If we can find out whose in charge, 
                                                       "we can know how the world works""",
                               unstated_camp_core_belief="""There is someone to blame, and it's not us."""
                               )

BeitSector.add_camp(KonspiroCamp)

KristanaCamp = CampObjectified(sector=GimelSector,
                               summary_statement="""Through my personal relationship with the One of Beings,
                               I know my path in all things""",
                               counter_sector_statement="""You have not felt the love or might of the One""",
                               tenants=[
                                 "The beings are our masters, and the One of Beings is the highest power",
                                 "Ultimately we can only find truth through our experiences and our faith",
                                 "It is our highest duty to convert others to the love of the One",
                                 "Beings are the angels of the One, they carry of the One's will"
                                ],
                               stated_camp_core_belief="""The love of the One of Beings is our salvation""",
                               unstated_camp_core_belief=""" Some are unworthy of the One's love.
                                The non-believers are the cause of all crises, 
                                and so must be eliminated so the rest of may be spared."""
                               )

GimelSector.add_camp(KristanaCamp)
