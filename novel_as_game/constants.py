yes_responses = ["yes", "Yes", "Y", "y"]
no_responses = ["no", "No", "N", "n"]

# must be greater than 6 for loop to run
max_round = 10

# for new game set up and level 1
quotes: dict = {
    "a": {
        "author": "William S. Burroughs",
        "quote": """Cut ups are for everyone. Anybody can make cut ups. All Writing is cut-ups.""",
    },
    "b": {
        "author": "Jose Ortega",
        "quote": """I am I and my circumstance; and, if I do not save it, I do not save myself.""",
    },
    "c": {
        "author": "Anne Bogart",
        "quote": """We create truths by describing, or by re-describing , our beliefs and observations. 
        Our task, and the task of every artist and scientist, is to re-describe our inherited assumptions 
        and invented fictions in order to create new paradigms for the future""",
    },
    "d": {
        "author": "Rosemarie Garland-Thompson",
        "quote": """The task of a misfit is not to try and fail endlessly to somehow fit, but to develop alternative methods.""",
    },
    "e": {
        "author": "the Shoe of Shoes, created by Julio Torres",
        "quote": """I am difficult to explain and hard to draw. I am alive.""",
    },
    # "f": {
    #     "author": "",
    #     "quote": """""",
    # },
}

# for level 1
new_idea_01 = "(๑'ᵕ'๑)⸝*"
new_idea_02 = "₍^ >⩊< ^₎Ⳋ"
new_idea_04 = "｡°(°¯᷄◠¯᷅°)°｡"
new_idea_03 = "( ദ്ദി ˙ᗜ˙ )"

end_state_mappings = {
    # player may be unaware that no camp can survive past max round unless they stop beings + ideas disappearance
    'a': 'your camp survives',
    # no camp survives if they are only looking out for themselves
    'b': 'your camp is the dominate voice in your sector',
    # if c is camp's outcome then no one survives because beings are needed for ideas
    'c': 'all camps survive',
    # player may be unaware that for all camps to survive, beings must survive
    'd': 'all camps survive & if beings exist they survive',
    # camp outcomes can not be e or f
    # if player achieves fame they are exiled from their camp
    'e': 'you achieve fame, all other outcomes irrelevant',
    'f': 'you achieve fame & your camp survives - why do these need to be contradictory?',
}
