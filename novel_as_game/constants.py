yes_responses = ["yes", "Yes", "Y", "y"]
no_responses = ["no", "No", "N", "n"]

# must be greater than 6 for loop to run
max_round = 10

end_state_mappings = {
    # player may be unaware that no camp can survive past max round unless they stop beings + ideas disappearance
    'a': 'your camp survives',
    # no camp survives if they are only looking out for themselves
    'b': 'your camp is the dominate voice in your sector',
    # if c is camp's outcome then no one survives because beings are needed for ideas
    'c': 'all camps survive',
    # player may be unaware that for all camps to survive, beings must survive
    'd': 'all camps survive and if beings exist they survive',
    # camp outcomes can not be e or f
    # if player achieves fame they are exiled from their camp
    'e': 'you achieve fame, all other outcomes irrelevant',
    'f': 'you achieve fame & your camp survives - why do these need to be contradictory?',
}
