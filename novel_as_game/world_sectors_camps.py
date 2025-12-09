from typing import List


class SectorObjectified:
    def __init__(self, name: str, core_belief: str, beings_exist: bool,
                 dinner_talking_points: dict, brochure_tagline: str):
        self.name: str = name
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
                print(f"""And other {speaker_title}s add that {camp.known_name} also believes {camp.unstated_camp_core_belief} """)
            print("\n")
            stated_camps += 1


class CampObjectified:
    def __init__(self, known_name: str, sector: SectorObjectified, summary_statement: str,
                 counter_sector_statement: str, tenants: List[str],
                 stated_camp_core_belief: str, unstated_camp_core_belief: str,
                 end_state_key: str, round_one_dict,
                 pamphlet_slogans: List[str] = [], initial_crisis_headline: str = "",
                 initial_crisis_explanation: str = "", brochure_summary: str = "",
                 second_crisis_explanation: str = ""):
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
        self.end_state_key = end_state_key
        self.round_one_dict = round_one_dict

    def revise_summary(self, revision: str, append: bool = True):
        """
        if append = False summary statement is overwritten
        """
        if append:
            self.summary_statement += " & " + revision
        else:
            self.summary_statement = f"""We no longer believe: {self.summary_statement}
            We now believe: {revision}"""


BeitSector = SectorObjectified(name="Beit",
                               core_belief="There are no beings. Only optimizing the here and now.",
                               beings_exist=False,
                               dinner_talking_points={
                                   "sector": "Beings do not exist.",
                                   "Beings": """"Fools claim that Beings exist in a physical realm connected to ours.
                                    Some even claim that we come out of their thoughts, 
                                    as if we are not enough in and of ourselves. 
                                    As if something as foolish as attention could control our fate.""",
                                   "disappearance": """The elite's plans must be advancing quickly.""",
                                   "Beings counter point": """No one has ever seen a being.
                                    I believe in things I have done my own research on.""",
                                   "camp invitation": """You are correct to reject the nonsense of Beings.
                                   The party is almost over and we can't stay here.
                                   Would you like to join me at my camp for the next cycle?"""},
                               brochure_tagline="""Come together to in times of low-attention.
                               Together we can figure this out."""
                               )

GimelSector = SectorObjectified(name="Gimel",
                                core_belief="Beings are probable to exist. There is a synthesis we do not yet know.",
                                beings_exist=True,
                                dinner_talking_points={
                                    "sector": "the fact that Beings exist is widely accepted by most camps.",
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
                               summary_statement="""there is a secret circle running all of our existences.""",
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
                               end_state_key="b",
                               round_one_dict={
                                    "lecturer": """We must ·in·cen·tiv·ize· people are in our camp to find the powerful
                                    elites who are behind a loss of Attention at this scale.""",
                                    "counter_lecture": """But what happens to those who fall down the wrong research rabbit-hole? 
                                If tokens alone determine resource allocation, won't those without tokens starve?""",
                                    "chant": """Tokens will find the truth! Nothing else matters!"""
                                },
                               pamphlet_slogans=["""Through rigorous self discipline and doing your own research,
                               you can find truth.""", """Everything you once knew is false"""],
                               initial_crisis_headline="""The new world order may be upon us.
                               Unprecedented Drop in Attention Rates""",
                               initial_crisis_explanation="""the rulers are bringing 
                               their plan to fruition, nothing else could explain this scale.
                               We cannot survive without sufficient Attention.""",
                               brochure_summary="""to figure out what whoever is responsible for the drop in Attention wants.""",
                               second_crisis_explanation="""We have failed to please the rulers or outsmart them.
                               Attention drops even further,
                               10 more reported disappeared.""",
                               )

BeitSector.add_camp(KonspiroCamp)

KristanaCamp = CampObjectified(known_name="Kristana",
                               sector=GimelSector,
                               summary_statement="""through personal relationships with the One of Beings,
                               we know our paths in all things""",
                               counter_sector_statement="""some people have not felt the love or might of the One""",
                               tenants=[
                                 "Ultimately we can find truth through our personal experiences",
                                 "The beings are our masters, and the One of Beings is the highest power",
                                 "It is our highest duty to convert others to the love of the One",
                                 "Beings are the angels of the One, they carry of the One's will",
                                 """The non-believers are the cause of all crises 
                                and so must be eliminated so the rest of may be spared."""
                                ],
                               stated_camp_core_belief="""the love of the One of Beings is salvation""",
                               unstated_camp_core_belief="""some are unworthy of the One's love and so crises result.""",
                               end_state_key="b",
                               round_one_dict={
                                    "lecturer": """We must ·in·cen·tiv·ize· everyone to find a personal relationships with the One of Beings.
                                    Only when everyone is in right relationship with the One can this end.
                                    We will can best decide amongst all the camps how to distribute what little is left in the name of the One.""",
                                    "counter_lecture": """Can we really force our faith on everyone through making everyone's 
                                    token allocation based on their professed alignment with us?
                                    Do people who believe differently really deserve to starve?""",
                                    "chant": """Tokens for the faithful! We do it in the name of the One of Beings!"""
                                },
                               pamphlet_slogans=["""You too are loved by the One""",
                                                 """Beings perform the miracles of the One's will."""],
                               initial_crisis_headline="""Unprecedented Drop in Attention Rates,
                               Search for Beings Connection Continues""",
                               initial_crisis_explanation="""We are sinners, 
                               and the One is punishing us by taking away the Beings.
                               Beings bless us with Attention when we obey the One so we may live a good life.""",
                               brochure_summary="""so we can figure out how we can right our relation with beings.""",
                               second_crisis_explanation="""We have failed to please the One, more Beings gone. 
                               Attention drops even further, 
                               10 more reported disappeared."""
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
                                stated_camp_core_belief="""through strict self-discipline we will become imprivable to disappearance""",
                                unstated_camp_core_belief="""Those who disappeared lacked discipline, 
                                real dedication to self-improvement could have saved them""",
                                end_state_key="c",
                                round_one_dict={
                                    "lecturer": """We must ·in·cen·tiv·ize· everyone to find their highest self.
                                    Only through each person's rigorous self-discipline can this crisis stop.""",
                                    "counter_lecture": """Who are we to judge someone's highest self?
                                    Even if we could, how could our highest selves let people who still haven't reach their full potential starve? """,
                                    "chant": """Tokens belong to the best of us!"""
                                },
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
                                      stated_camp_core_belief="""optimization of the Attention equations will create prosperity for all of us now and in the future""",
                                      unstated_camp_core_belief="""as the innovator class,
                                      we deserve first crack at any remaining Attention and resources""",
                                      end_state_key="b",
                                      round_one_dict={
                                        "lecturer": """We must ·in·cen·tiv·ize· everyone to invent the technology that will optimize the Attention equations.
                                        In times like these, we must make the hard choices to maximize value for our camp and those yet to be born.""",
                                        "counter_lecture": """Who defines value? 
                                        Who wins and who looses if this technology optimizes the Attention equations at all costs?""",
                                        "chant": """Tokens for the innovators! Innovators will save us!"""
                                      },
                                      )
GimelSector.add_camp(LongperspektivaCamp)


NaciismoCamp = CampObjectified(known_name="Naciismo",
                               sector=BeitSector,
                               summary_statement="""in the face of the failures of the global Attention elites, 
                               we must create a world where we are safe""",
                               counter_sector_statement="""we are the victims, each camp must save themselves""",
                               tenants=["we can only be responsible for saving those in our camp",
                                        "other camps have attacked us in the past and it will never stop",
                                        "if others perish, it is unfortunate but that is not on us",
                                        "we have a long and proud history that must continue",
                                        "given historical legacies, we must annex a new place",
                                        "it is our destiny and birthright to live in a new camp",
                                        "this new place is the only way we will survive",
                                        "people will always turn against us",
                                        ],
                               stated_camp_core_belief="""as victims, we must preserve our way of life""",
                               unstated_camp_core_belief="""we have suffered the most and 
                               everyone else is destined to their fate""",
                               end_state_key='b',
                               round_one_dict={
                                    "lecturer": """We must ·in·cen·tiv·ize· the people in this camp to save this camp 
                                    and seize the remaining resources for ourselves. We are the victims!""",
                                    "counter_lecture": """Why does our camp get to plunder and invade everywhere else?
                                    """,
                                    "chant": """We will not be weak! Tokens for the victors!"""
                                },
                               )

BeitSector.add_camp(NaciismoCamp)


AnarkioCamp = CampObjectified(known_name="Anarkio",
                              sector=GimelSector,
                              summary_statement="""all hierarchy has caused the Attention imbalance,
                              so we must abolish all hierarchies""",
                              counter_sector_statement="""we are free thinkers""",
                              tenants=["everyone must do what they think is right",
                                       "all leaders are not to be trusted",
                                       "ignorance is a personal failing",
                                       "people's individual choices can right all wrongs"],
                              stated_camp_core_belief="""each individual must chose their own path""",
                              unstated_camp_core_belief="""no organization that can represent real collective action""",
                              end_state_key='c',
                              round_one_dict={
                                    "lecturer": """We need a decentralized way to manage resources and alternative currency is the answer!
                                    We can not trust any centralized authority and their tokens.
                                     """,  # anracho-capitalism
                                    "counter_lecture": """What is the use case for our currency?
                                    Why should those without currency starve?""",
                                    "chant": """Decentralize currency!"""
                                },
                               )

GimelSector.add_camp(AnarkioCamp)


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
                                    unstated_camp_core_belief="we alone can save everyone from themselves",
                                    end_state_key='b',
                                    round_one_dict={
                                        "lecturer": """We are the inheritors of knowledge and civility! 
                                        We must ·in·cen·tiv·ize· those who will follow in our footsteps.""",
                                        "counter_lecture": """Why must people starve if they do not follow in our footsteps
                                        or worship the written word above all else?""",
                                        "chant": """Tokens for civility and learning!"""
                                    },
                                    )
BeitSector.add_camp(BlankaSavismoCamp)


SkalismoCamp = CampObjectified(known_name="Skalismo",
                               sector=GimelSector,
                               summary_statement="""through understanding the material conditions,
                               We can create a system where resources are produced and distributed in a way so we can all survive.""",
                               counter_sector_statement="""Only through understanding the real struggle can we make real change.""",
                               tenants=[
                                    "History is ultimately the tale of class struggle",
                                    "Power is who controls the means of production",
                                    "Only a democratically managed economy can get us out of this mess."
                                ],
                               stated_camp_core_belief="""creation of a new system of resources production and distribution is how we can survive""",
                               unstated_camp_core_belief="""We must unite the masses against their real enemy""",
                               end_state_key='d',
                               round_one_dict={
                                    "lecturer": """A system where people are forced to innovate or starve will bring Attention back to us all!
                                    Ideas will thrive in a market place!  It's the only way someone will solve the Attention equations!
                                    """,
                                    "counter_lecture": """No one person should unilaterally control all our wealth -
                                    A market place the incentivizes the accumulation of tokens above all else 
                                    will ultimately lead to single entities controlling everything.
                                    """,
                                   "counter_lecture_2": """Who has these tokens to begin with?
                                   Who wins and who looses in this system?""",
                                   # in this camp tokens are rejected, chant is against lecturer
                                    "chant": """Democratically managed economy!
                                    Everyone deserves to have their needs met and contribute according to their ability!""",
                                   "lecturer_counter": """Utopian fools!"""
                                },
                               )

GimelSector.add_camp(SkalismoCamp)
