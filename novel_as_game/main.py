import time
import atexit
from world_ideas import DefaultIdea, IdeaObjectified
from levels import ChapterOne, ChapterTwo, ChapterThree
from typing import Dict
from chapter_structure import LevelofStory
from world_ideas import Inspiration_001, Overwhelm_001, Conspiracism_001, Systems_001
from text_graphics import growing_symbol_transition

""" 
Ideation Lores
by Quinn Ray Keck
An existential crisis in the form of a python script. Enjoy!
"""

# for debugging
use_default_idea: bool = False


def game_step_up():
    print(f"""Welcome to this story.  
        Before we begin, can you share an idea? 
        
        """)
    time.sleep(1)
    print("""It can be one you've been mulling over a long time,
        or an idea behind the last piece of content you consumed,
        or simply the next idea that pops into your head.
        If you feel stuck, just look up at the space your in and contemplate an object that catches your eye.
        
        Type your idea below:
        """)
    player_idea = input()
    if len(player_idea) < 5:
        print(f"""You entered: {player_idea} - that idea doesn’t seem very fleshed out, would you please add more?""")
        player_idea = input()

    print("""Thank you! We are in desperate need of new realities.""")
    print("If you could give your idea a name, what you it be?")
    print("Don't stress too much about it, what's in a name anyways!")
    player_idea_name = input()
    print("Thank you! What emotion(s) did you feel when submitting this idea?")
    player_emotions = input()
    if len(player_emotions) < 3:
        print(
            f"""You entered: {player_emotions} - that idea doesn’t seem very fleshed out, would you please add more?""")
        player_emotions = input()
    time.sleep(1)
    print("Vulnerability is hard, so have no fear that's over with!")
    time.sleep(1)
    print("""
        ________00000000000___________000000000000_________
    ______00000000_____00000___000000_____0000000______
    ____0000000_____________000______________00000_____
    ___0000000_______________0_________________0000____
    __000000____________________________________0000___
    __00000_____________________________________ 0000__
    _00000______________________________________00000__
    _00000_____________________________________000000__
    __000000_________________________________0000000___
    ___0000000______________________________0000000____
    _____000000____________________________000000______
    _______000000________________________000000________
    __________00000_____________________0000___________
    _____________0000_________________0000_____________
    _______________0000_____________000________________
    _________________000_________000___________________
    _________________ __000_____00_____________________
    ______________________00__00_______________________
    ________________________00_________________________
        """)

    print("As the creator of this idea, what would you like to be called?")
    player_name = input()

    player_idea = IdeaObjectified(name=player_idea_name, description=player_idea, creator=player_name)
    player_idea.emotions.append(player_emotions)
    time.sleep(1)
    print("Now we may begin!")
    growing_symbol_transition()

    return player_idea


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

    if use_default_idea:
        PlayerIdea = DefaultIdea
    else:
        PlayerIdea = game_step_up()

    narrative_mappings: Dict = {
        1: ChapterOne(number=1, main_character=PlayerIdea,
                      supporting_characters=[Inspiration_001, Overwhelm_001],
                      next_chapter=2),
        2: ChapterTwo(number=2, main_character=PlayerIdea,
                      supporting_characters=[Conspiracism_001, Systems_001],
                      next_chapter=3),
        3: ChapterThree(number=3, main_character=PlayerIdea,
                        supporting_characters=[],
                        next_chapter=0)
    }

    next_key: int = 1

    while next_key != 0:
        next_key: int = narrative_mappings[next_key].run_level()

    print(next_key)






