from world_ideas import IdeaObjectified
from typing import List, Dict
import time


class LevelofStory:
    def __init__(self, number: int, main_character: IdeaObjectified, supporting_characters: List[IdeaObjectified],
                 next_chapter: int):
        self.number = number
        self.main_character = main_character
        self.supporting_characters = supporting_characters
        self.next_chapter = next_chapter
        self.transition_str = "*" * 13

    def title(self):
        return f"Level {self.number}"

    def greeting(self):
        print(f"Welcome to Level {self.number}")

    def parting(self):
        print(f"End of Level {self.number}")

    def events(self):
        print("This level has an empty skeleton.")
        print("""The future is not yet written, and neither is this chapter""")


    def run_level(self):
        time.sleep(2)
        self.greeting()
        self.events()
        self.parting()
        self.transition_as_typewriter(self.transition_str)
        return self.next_chapter

    @staticmethod
    def player_yn_to_bool():
        answer: str = input()
        while not any(x in answer.lower() for x in ['y', 'n']):
            print("Please try again! Type 'Y' or 'N'")
            answer: str = input()

        if answer.strip()[0].lower() == "y":
            return True
        else:
            return False

    @staticmethod
    def transition_as_typewriter(transition_str, time_between: float = 0.01):
        for transition in transition_str:
            print(transition, end='', flush=True)
            time.sleep(time_between)
        print("\n")
