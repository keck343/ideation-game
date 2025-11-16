import time
import atexit
from world_ideas import IdeaObjectified
from level_one import ChapterOne
from level_two import ChapterTwo
from level_three import ChapterThree
from typing import Dict
from chapter_structure import LevelofStory
from world_ideas import Inspiration001, Overwhelm001, Conspiracism001, Systems001
from text_graphics import growing_symbol_transition, heart_of_zeros

""" 
Disambiguation
by Quinn Ray Keck
An existential crisis in the form of a python script. Enjoy!
"""

# for debugging
use_default_idea: bool = False


def game_step_up():
    print(f"""Weclome to Ideation.""")

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

    PlayerIdea: IdeaObjectified = IdeaObjectified(name="unknown",
                                                  description="unknown",
                                                  creator="unknown")

    narrative_mappings: Dict = {
        1: ChapterOne(number=1, main_character=PlayerIdea,
                      supporting_characters=[Inspiration001, Overwhelm001],
                      next_chapter=2),
        2: ChapterTwo(number=2, main_character=PlayerIdea,
                      supporting_characters=[Conspiracism001, Systems001],
                      next_chapter=3),
        3: ChapterThree(number=3, main_character=PlayerIdea,
                        supporting_characters=[],
                        next_chapter=0)
    }

    next_key: int = 1

    while next_key != 0:
        next_key: int = narrative_mappings[next_key].run_level()

    print(next_key)






