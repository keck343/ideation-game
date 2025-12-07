from world_ideas import IdeaObjectified
from text_graphics import growing_symbol_transition
from typing import List, Dict
import time


class LevelofStory:
    def __init__(self, number: int, main_character: IdeaObjectified,
                 supporting_characters: List[str] = [],
                 starting_point: str = ""):
        self.number = number
        self.main_character = main_character
        self.supporting_characters = supporting_characters
        self.transition_str = "*" * 13
        self.starting_point = starting_point

    def title(self):
        return f"Level {self.number}"

    def greeting(self):
        print(f"Welcome to Level {self.number}")

    def parting(self):
        print(f"End of Level {self.number}")
        time.sleep(1)

    def events(self):
        print("This level has an empty skeleton.")
        print("""The future is not yet written, and neither is this chapter""")
        next_parameters: dict = {}
        return next_parameters

    def run_level(self):
        time.sleep(1)
        self.greeting()
        next_parameters = self.events()
        time.sleep(1)
        self.parting()
        growing_symbol_transition(sleep_seconds=0.5)
        return next_parameters

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
    def player_multi_choice(possible_answers: List):
        answer: str = input()
        while not any(x in answer.lower().strip() for x in possible_answers):
            print(f"""Please try again! Type one of these selections '{", ".join(possible_answers)}'""")
            answer: str = input()

        return answer

    @staticmethod
    def player_long_answer():
        print("Please type your response:")
        answer: str = input()
        return answer

    @staticmethod
    def transition_as_typewriter(transition_str, time_between: float = 0.1):
        for transition in transition_str:
            print(transition, end='', flush=True)
            time.sleep(time_between)
        print("\n")
