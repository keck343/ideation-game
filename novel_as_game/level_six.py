from chapter_structure import LevelofStory
from constants import end_state_mappings, max_round
from text_graphics import growing_symbol_transition, gamer, coffee, play_loop, watch_fence_void, moving_truck
from world_sectors_camps import BeitSector, GimelSector
import random
import time


class ChapterSix(LevelofStory):

    def events(self):
        # from last level saw_news is bool
        # round number is number of times played Chapter 6
        chapter_sector, chapter_camp, saw_news, fame = self.starting_point
        print(saw_news, self.number)
        if self.number == 0:
            print("""What do you want the outcome of this crisis to be?""")
            for key, value in end_state_mappings.items():
                print(f"""{key}. {value}""")
            desired_outcome = self.player_multi_choice()
            self.main_character.chose_desired_end_state(desired_outcome)

        # TO DO:
        # loop
        print(chapter_sector, chapter_camp, saw_news, fame)
        return self.main_character, chapter_sector, chapter_camp, saw_news, fame

        if round_number == max_round:
            if chapter_camp.end_state_key == 'd':
                world_survives: bool = True
                player_wins: bool = True
                print("""
                In the end, your camp stopped the death of the embodied and Beings.
                While the world could never be the same again,
                Attention flows through out all the camps.""")
                growing_symbol_transition("√♥-√v--√♥-√v–", num_lines=3)
                if self.main_character.desired_end_state_key in ['a', 'b']:
                    print("""Your new found camp survived and allowed other camps to survive.
                    This came voice grew but did not dominate.""")
                    print("""Do you consider that acceptable? (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if not yes:
                        player_wins = False
                elif self.main_character.desired_end_state_key in ['e', 'f']:
                    print("""Your fame however was fleeting.  
                    Your fellow camp members were feed up with your ego, and no one will talk to you.""")
                    print("""Do you consider that acceptable? (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if not yes:
                        player_wins = False
                else:
                    # player desired state is c or d
                    print("""You sigh in relief.""")
                    print("""You achieved your goals and the worlds.""")

                return chapter_sector, chapter_camp, world_survives, player_wins

            else:
                world_survives: bool = False
                if chapter_camp.end_state_key == self.main_character.desired_end_state_key:
                    player_wins: bool = True
                    print("""You achieved your goal, but you did not survive much longer to enjoy your victory
                    because no one did.""")
                else:
                    player_wins: bool = False
                    print("""You did not achieved your goal, 
                    and did not survive much longer,
                    neither did anyone else.""")

                growing_symbol_transition(symbol="+=={:::::::::::::::::>", num_lines=3)
                print("""How the world works will remain a mystery,
                but unlike real life,
                you can choose to play this game again.""")
                return self.main_character, chapter_sector, chapter_camp, world_survives, player_wins




                # To Do: Add fame bool -- chapter 6.5 is with fame

        return chapter_sector, chapter_camp, saw_news, fame