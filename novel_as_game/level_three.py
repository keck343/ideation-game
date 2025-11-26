from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition
import time


class ChapterThree(LevelofStory):
    number = 3

    def events(self):
        return self.starting_point
