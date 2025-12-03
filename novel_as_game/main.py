import time
import atexit
from world_ideas import IdeaObjectified
from level_one import ChapterOne
from level_two import ChapterTwo
from level_three import ChapterThree
from level_four import ChapterFour
from level_five import ChapterFive
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
    print("""All you need to know for now is:""")
    time.sleep(1)
    print("Press enter to submit answers.")
    growing_symbol_transition(sleep_seconds=0.5)


def start_next_level(narrative_dictionary, chapter: LevelofStory):
    if chapter.next_chapter in narrative_dictionary.keys():
        narrative_dictionary[chapter.next_chapter].run_level()
    else:
        print("This story is over and now you must write your own.")


def exit_handler():
    print("""Welcome back to Level 0.
            You have now left this world, but has it left you?""")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    atexit.register(exit_handler)
    game_step_up()

    if debugging:
        PlayerIdea: IdeaObjectified = IdeaObjectified(name="unknown",
                                                      description="This is all made up",
                                                      creator="unknown")
        chapter_camp = GimelSector
        next_move = "attend" # "skip", "attend" or "volunteer"

    else:
        PlayerIdea: IdeaObjectified = IdeaObjectified(name="unknown",
                                                      description="unknown",
                                                      creator="unknown")

        chapter_01 = ChapterOne(number=1, main_character=PlayerIdea,
                                supporting_characters=[Inspiration001, Overwhelm001])

        chapter_01.run_level()

        chapter_02 = ChapterTwo(number=2, main_character=PlayerIdea)
        PlayerIdea, next_sector = chapter_02.run_level()

        chapter_03 = ChapterThree(number=3, main_character=PlayerIdea, starting_point=next_sector)
        next_sector, friend_type, desired_product = chapter_03.run_level()

        chapter_04 = ChapterFour(number=4, main_character=PlayerIdea,
                                 starting_point=(next_sector, friend_type, desired_product))
        PlayerIdea, chapter_camp, next_move = chapter_04.run_level()

    chapter_05 = ChapterFive(number=5, main_character=PlayerIdea,
                             starting_point=(chapter_camp, next_move))
    PlayerIdea, chapter_sector, next_camp, saw_news = chapter_05.run_level()

    print(next_move)
    print(PlayerIdea.description)









