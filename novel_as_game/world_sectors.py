from typing import List


class SectorObjectified:
    def __init__(self, known_name: str, core_belief: str, beings_exist: bool, camps: List = []):
        self.name: str = known_name
        self.core_belief: str = core_belief
        self.beings_exists: bool = beings_exist
        self.camps: List = camps


BeitSector = SectorObjectified(known_name="Beit",
                               core_belief="There are no beings. Only the here and now.",
                               beings_exist=False)

GimelSector = SectorObjectified(known_name="Gimel",
                                core_belief="Beings are probable to exist. There is a synthesis we do not yet know.",
                                beings_exist=True)
