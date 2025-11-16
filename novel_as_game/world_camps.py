from novel_as_game.world_sectors import (
    SectorObjectified,
    BeitSector,
    GimelSector)
from typing import List
# in levels 3 & 4 you are interacting with a representative of a camp
# only once crisis occurs do you interact with individual ideas


class CampObjectified:

    def __int__(self, sector: SectorObjectified, summary_statement: str,
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


