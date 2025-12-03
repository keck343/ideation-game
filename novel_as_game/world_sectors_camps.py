from typing import List


class SectorObjectified:
    def __init__(self, known_name: str, core_belief: str, beings_exist: bool,
                 dinner_talking_points: dict, brochure_tagline: str):
        self.name: str = known_name
        self.core_belief: str = core_belief
        self.beings_exists: bool = beings_exist
        self.camps = []
        self.dinner_talking_points = dinner_talking_points
        self.brochure_tagline = brochure_tagline

    def add_camp(self, camp):
        self.camps.append(camp)

    def tell_camps_beliefs(self, speaker_title: str, stated_and_unstated: bool):
        stated_camps = 0
        for camp in self.camps:
            if stated_camps == 0:
                speaker_prefix = f"The first {speaker_title}"
            elif stated_camps % 2 == 0:
                speaker_prefix = f"Another {speaker_title}"
            else:
                speaker_prefix = f"A different {speaker_title}"
            print(f"""{speaker_prefix} says that the camp often referred to as {camp.known_name}
            believes that {camp.stated_camp_core_belief}""")
            if stated_and_unstated:
                print(f"""And other {speaker_title}s add that {camp.unstated_camp_core_belief} """)
            print("\n")
            stated_camps += 1


class CampObjectified:
    def __init__(self, known_name: str, sector: SectorObjectified, summary_statement: str,
                 counter_sector_statement: str, tenants: List[str],
                 stated_camp_core_belief: str, unstated_camp_core_belief: str,
                 pamphlet_slogans: List[str] = [], initial_crisis_headline: str = "",
                 initial_crisis_explanation: str = "", brochure_summary: str = "",
                 second_crisis_explanation: str = "",):
        self.known_name = known_name
        self.sector = sector
        self.sector_core_belief = sector.core_belief
        self.beings_exist = sector.beings_exists
        self.summary_statement = summary_statement
        self.counter_sector_statement = counter_sector_statement
        self.tenants = tenants
        self.stated_camp_core_belief = stated_camp_core_belief
        self.unstated_camp_core_belief = unstated_camp_core_belief
        self.pamphlet_slogans = pamphlet_slogans
        self.initial_crisis_headline = initial_crisis_headline
        self.initial_crisis_explanation = initial_crisis_explanation
        self.brochure_summary = brochure_summary
        self.second_crisis_explanation = second_crisis_explanation

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
                                   Would you like to join me at my camp for the next cycle?"""},
                               brochure_tagline="""Come together to in times of low-attention.
                               Together we can figure this out."""
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
                                    """},
                                brochure_tagline="""Come together to share Attention-Beings hypothesis's.
                                With the latest research, we can figure this out."""
                                )

KonspiroCamp = CampObjectified(known_name="Konspiro",
                               sector=BeitSector,
                               summary_statement="""There is a secret circle running all of our existences.""",
                               counter_sector_statement="""
                               there are too many coincidences are happening for this all to be random""",
                               tenants=[
                                   "Everything that happens is result of someone’s plan",
                                   "The world is a battle between good and evil",
                                   "We are approaching a new world order",
                                   "When things go wrong, it demonstrates the planning of whoever is in charge",
                               ],
                               stated_camp_core_belief="""finding out whose in charge
                               is the key to knowing how the world works""",
                               unstated_camp_core_belief="""there is someone to blame, and it's not us.""",
                               pamphlet_slogans=["""Through rigorous self discipline and doing your own research,
                               you can find truth.""", """Everything you once knew is false"""],
                               initial_crisis_headline="""The new world order may be upon us.
                               Unprecedented Drop in Attention Rates""",
                               initial_crisis_explanation="""the Eksterteranoj's rulers are bringing 
                               their plan to fruition, nothing else could explain this scale.
                               We cannot survive without sufficient Attention.""",
                               brochure_summary="""to figure out what whoever is responsible for the drop in Attention wants.""",
                               second_crisis_explanation="""We have failed to please Eksterteranoj's rulers
                               or outsmart them.  Attention drops even further, 10 more reported disappeared or dead."""
                               )

BeitSector.add_camp(KonspiroCamp)

KristanaCamp = CampObjectified(known_name="Kristana",
                               sector=GimelSector,
                               summary_statement="""through my personal relationship with the One of Beings,
                               we know our paths in all things""",
                               counter_sector_statement="""some people have not felt the love or might of the One""",
                               tenants=[
                                 "Ultimately we can find truth through our personal experiences",
                                 "The beings are our masters, and the One of Beings is the highest power",
                                 "It is our highest duty to convert others to the love of the One",
                                 "Beings are the angels of the One, they carry of the One's will"
                                ],
                               stated_camp_core_belief="""the love of the One of Beings is salvation""",
                               unstated_camp_core_belief="""some are unworthy of the One's love.
                                The non-believers are the cause of all crises, 
                                and so must be eliminated so the rest of may be spared.""",
                               pamphlet_slogans=["""You too are loved by the One""",
                                                 """Beings perform the miracles of the One's will."""],
                               initial_crisis_headline="""Unprecedented Drop in Attention Rates,
                               Search for Beings Connection Continues""",
                               initial_crisis_explanation="""We are sinners, 
                               and the One is punishing us by taking away the Beings.
                               Beings bless us with Attention when we obey the One so we may live a good life.""",
                               brochure_summary="""so we can figure out how we can right our relation with beings.""",
                               second_crisis_explanation="""We have failed to please Eksterteranoj's rulers
                               or outsmart them.  Attention drops even further, 10 more reported disappeared or dead."""
                               )

GimelSector.add_camp(KristanaCamp)


NovaEpokoCamp = CampObjectified(known_name="Nova Epoko",
                                sector=BeitSector,
                                summary_statement="""by our bettering ourselves we can save ourselves""",
                                counter_sector_statement="""
                                Those who have already disappeared were not trying hard enough""",
                                tenants=["Preservation is through self-improvement and wellness",
                                         "Repeat affirmations to build mental fortitude",
                                         "Repeat exercises to build resilience",
                                         "Renounce attachments to anything that stands in the way of improvement",
                                         "My life is a reflection of my effort"],
                                stated_camp_core_belief="""Through strict self-discipline 
                                we will become imprivable to disappearance""",
                                unstated_camp_core_belief="""Those who disappeared lacked discipline, 
                                real dedication to self-improvement could have saved them"""
                                )

BeitSector.add_camp(NovaEpokoCamp)


LongperspektivaCamp = CampObjectified(known_name="Longperspektiva",
                                      sector=GimelSector,
                                      summary_statement="""we must generate the most value 
                                      for those now and those to come""",
                                      counter_sector_statement="""by creating the most Attention for ourselves,
                                      it trickles down to you""",
                                      tenants=["We must optimize the Attention Equations",
                                               "We are the innovators this world needs",
                                               "We killed false gods and we are our own gods",
                                               "Beings are a resource to optimize"],
                                      stated_camp_core_belief="""optimization of the Attention equations
                                      will create prosperity for all of us now and in the future""",
                                      unstated_camp_core_belief="""as the innovator class,
                                      we deserve first crack at any remaining Attention and resources"""
                                      )
GimelSector.add_camp(LongperspektivaCamp)


NaciismoCamp = CampObjectified(known_name="Naciismo",
                               sector=BeitSector,
                               summary_statement="""in the face of the failures of the global Attention elites, 
                               we must hold on to what we have""",
                               counter_sector_statement="""we are the victims, each camp must save themselves""",
                               tenants=["we can only be responsible for saving those in our camp",
                                        "other camps have attacked us in the past and it will never stop",
                                        "if others perish, it is unfortunate but that is not on us",
                                        "we have a long and proud history that must continue"],
                               stated_camp_core_belief="""as victims, we must preserve our way of life""",
                               unstated_camp_core_belief="""we have suffered the most"""
                               )

BeitSector.add_camp(NaciismoCamp)


CionismoCamp = CampObjectified(known_name="Cionismo",
                               sector=GimelSector,
                               summary_statement="""we must create a camp where we are safe from others and Beings""",
                               counter_sector_statement="""Beings and the others will always persecute us.
                               this is the only way""",
                               tenants=["given historical legacies, we must annex a new place",
                                        "this new place is the only way we will survive",
                                        "people will always turn against us",
                                        "we have a long and proud history that must continue",
                                        "it is our destiny and birthright to live in a new camp"],
                               stated_camp_core_belief="""a new camp is the only way""",
                               unstated_camp_core_belief="""the people who are already living 
                               in the new camp are destined to their fate"""
                               )
GimelSector.add_camp(CionismoCamp)


BlankaSavismoCamp = CampObjectified(known_name="Blanka Savismo",
                                    sector=BeitSector,
                                    summary_statement="""we can determine the best way to spend everyone's resources,
                                    we have to save everyone from themselves""",
                                    counter_sector_statement="""other camps lack the instituions and resources to shape culture""",
                                    tenants=["nothing is true unless it is written down",
                                             "we can establish alliances with other proud camps",
                                             "we must use Attention most effectively and put all resources in that"],
                                    stated_camp_core_belief="""we, as the camp with the most well-funded research,
                                     must determine the best way to spend everyone's resources""",
                                    unstated_camp_core_belief="we alone can save everyone from themselves"
                                    )
BeitSector.add_camp(BlankaSavismoCamp)


KomunistoCamp = CampObjectified(known_name="Komunisto",
                                sector=GimelSector,
                                summary_statement="""through understanding the material conditions,
                                We can create a system where resources are produced and distributed in a way 
                                so we can all survive.""",
                                counter_sector_statement="""
                                Only through understanding the real struggle can we make real change.""",
                                tenants=[
                                    "History is ultimately the tale of class struggle",
                                    "Power is who controls the means of production",
                                    "Only a democratically managed economy can get us out of this mess."
                                ],
                                stated_camp_core_belief="""We must create a system of resources production and
                                distribution so we can all survive""",
                                unstated_camp_core_belief="""We must convert the masses."""
                                )

GimelSector.add_camp(KomunistoCamp)
