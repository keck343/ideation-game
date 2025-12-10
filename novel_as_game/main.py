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
from world_ideas import Inspiration001, Overwhelm001, Conspiracism001, Systems001
from text_graphics import growing_symbol_transition, welcome_art
from world_sectors_camps import BeitSector, GimelSector

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
        next_camp = chapter_sector.camps[-1]
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
    fame: bool = False
    no_tokens: bool = False
    num_rounds_in_camp: int = 0
    last_round: bool = False

    while (rounds < max_round or num_rounds_in_camp < 3) and not last_round:
        chapter = ChapterSix(number=rounds, main_character=PlayerIdea,
                             starting_point=(chapter_sector, next_camp, num_rounds_in_camp, participated, fame, no_tokens, last_round))
        PlayerIdea, chapter_sector, next_camp, num_rounds_in_camp, participated, fame, no_tokens, last_round = chapter.run_level()
        rounds += 1

    final_chapter = ChapterSix(number=rounds, main_character=PlayerIdea,
                               starting_point=(chapter_sector, next_camp, num_rounds_in_camp, participated, fame, no_tokens, last_round))

    PlayerIdea, chapter_sector, chapter_camp, world_survives, player_wins, fame, no_tokens = final_chapter.run_level()









