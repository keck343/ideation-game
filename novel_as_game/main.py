import time
import atexit
from world_ideas import IdeaObjectified
from constants import quotes, new_idea_01, new_idea_02
from level_one import ChapterOne
from level_two import ChapterTwo
from level_three import ChapterThree
from level_four import ChapterFour
from level_five import ChapterFive
from level_six import ChapterSix
from constants import max_round
from typing import Dict
from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition, welcome_art, transition_as_typewriter, heart_of_zeros
from world_sectors_camps import BeitSector, GimelSector, CampObjectified, SkalismoCamp

""" 
Disambiguation
by Quinn Ray Keck
An existential crisis in the form of a python script. Enjoy!
"""

# for debugging
debugging: bool = True


def game_step_up():
    print(welcome_art)
    print("""Welcome to Disambiguation.""")

    print(f"""The blank canvas of creation is heaven or hell depending on your perspective. 
    """)

    print("Pick the quote that most resonates with you:")
    for letter, quote_dict in quotes.items():
        print(f"""{letter}. From {quote_dict["author"]}:
        '{quote_dict["quote"]}'
        """)

    choices = list(quotes.keys())
    print(f"""Type '{"', '".join(choices[:-1])}' or '{choices[-1]}'
    Press enter to submit your choice.""")
    player_quote_key: str = input().lower().strip()
    while not any(x in player_quote_key.lower().strip() for x in choices):
        print(f"""Please try again! Type one of these selections '{", ".join(choices)}'""")
        player_quote_key: str = input().lower().strip()

    growing_symbol_transition(sleep_seconds=0.5)
    return player_quote_key


def exit_handler():
    print("""Welcome back to Level 0.
            You have now left this world, but has it left you?""")


def ending(end_camp: CampObjectified, PlayerIdea: IdeaObjectified, final_num_rounds_in_camp: int):

    if final_num_rounds_in_camp > 0 and end_camp == SkalismoCamp:
        world_survived = True
    else:
        world_survived = False

    passcode_instructions: str = """Give the passcode 'all caffeine'
    to the bartender to get the diagram"""

    player_wins: bool = False

    if not world_survived:
        # chose to read novel
        if PlayerIdea.desired_end_state_key == 'a':
            print("""You did get to finish your novel.""")
            player_wins: bool = True
            transition_as_typewriter("""
            As you relish in the prose,
            the last being perished and 
            like the rest of the embodied, you disappeared into the void.
            """)
            growing_symbol_transition(symbol="+=={:::::::::::::::::>", num_lines=3)
            print("""You achieved your goal, but you did not survive much longer to enjoy your victory
                            because no one did.""")

        if end_camp.end_state_key == PlayerIdea.desired_end_state_key and final_num_rounds_in_camp > 0:
            if PlayerIdea.desired_end_state_key not in ['d', 'c']:
                player_wins: bool = True

        if player_wins:
            growing_symbol_transition(symbol="+=={:::::::::::::::::>", num_lines=3)
            print(f"""Unlike the real world, there is a diagram for how this world works.
                Sense you did achieve your goal,
                {passcode_instructions}
                """)
            print(""" 
            Maybe you will want to play again with this new knowledge.""")
        else:
            growing_symbol_transition(symbol="+=={:::::::::::::::::>", num_lines=3)
            print("""How the world works will remain a mystery,
                but unlike real life,
                you can choose to play this game again.""")

    if world_survived:
        if PlayerIdea.desired_end_state_key in ['d', 'c']:
            player_wins: bool = True
        print("""
        In the end, your camp stopped the death of the embodied and Beings.
        While the world could never be the same again,
        Attention flows through out all the camps.""")
        growing_symbol_transition("√♥-√v--√♥-√v–", num_lines=3)

        if PlayerIdea.desired_end_state_key in ['b']:
            print("""Your new found camp survived and allowed other camps to survive.
            This came voice grew but did not dominate.""")

        elif PlayerIdea.desired_end_state_key in ['e', 'f']:
            print("""Your attempts at fame however were fleeting.  
            Your fellow camp members were feed up with your ego, and no one will talk to you.""")

        elif player_wins:
            print("""You sigh in relief.""")
            print("""You achieved your goal and the world goes on.""")

        print(heart_of_zeros)
        print(f"""Unlike the real world, there is a diagram for how this world works.
        Sense the world survived,
        {passcode_instructions}
        """)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    atexit.register(exit_handler)

    if debugging:
        PlayerIdea: IdeaObjectified = IdeaObjectified(name="unknown",
                                                      description="This is all made up",
                                                      creator="unknown")
        chapter_sector = GimelSector
        # debugging level 5
        # next_move = "volunteer"  # "skip", "attend" or "volunteer"
        # next_camp = chapter_sector.camps[1]
        # participated = False
        next_camp = chapter_sector.camps[2]
        participated = True

    else:
        player_quote_key = game_step_up()
        PlayerIdea: IdeaObjectified = IdeaObjectified(name="unknown",
                                                      description="unknown",
                                                      creator="unknown",
                                                      player_quote_key=player_quote_key)
        # TO DO: NEW CHAPTER 1
        chapter_01 = ChapterOne(number=1, main_character=PlayerIdea,
                                supporting_characters=[new_idea_01, new_idea_02])

        chapter_01.run_level()

        chapter_02 = ChapterTwo(number=2, main_character=PlayerIdea)
        PlayerIdea, next_sector = chapter_02.run_level()

        chapter_03 = ChapterThree(number=3, main_character=PlayerIdea, starting_point=next_sector)
        next_sector, friend_type, desired_product = chapter_03.run_level()

        chapter_04 = ChapterFour(number=4, main_character=PlayerIdea,
                                 starting_point=(next_sector, friend_type, desired_product))
        PlayerIdea, chapter_sector, next_move = chapter_04.run_level()

        chapter_05 = ChapterFive(number=5, main_character=PlayerIdea,
                                 starting_point=(chapter_sector, next_move))
        PlayerIdea, chapter_sector, next_camp, participated = chapter_05.run_level()

    rounds: int = 6
    num_rounds_in_camp: int = 0
    end_loop: bool = False

    while not end_loop:
        chapter = ChapterSix(number=rounds, main_character=PlayerIdea,
                             starting_point=(next_camp, num_rounds_in_camp, end_loop))
        PlayerIdea, next_camp, num_rounds_in_camp, end_loop = chapter.run_level()
        rounds += 1

    ending(end_camp=next_camp, PlayerIdea=PlayerIdea, final_num_rounds_in_camp=num_rounds_in_camp)









