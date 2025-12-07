from chapter_structure import LevelofStory
from constants import end_state_mappings, max_round
from text_graphics import growing_symbol_transition, watch_fence_void, fence_void, line_of_fish, moon_star_line
from world_sectors_camps import BeitSector, GimelSector, CampObjectified, SkalismoCamp
import random
import time


class ChapterSix(LevelofStory):

    def ending(self, chapter_camp: CampObjectified, participate: bool):
        if not participate:
            # chose to read novel
            if self.main_character.desired_end_state_key == 'a':
                print("""You did get to finish your novel.""")
                player_wins: bool = True
            else:
                print("""You are reading your novel.""")
                player_wins: bool = False
            self.transition_as_typewriter("""
            As you relish in the prose,
            the last being perished and 
            like the rest of the embodied, you disappeared into the void.
            """)
            world_survives: bool = False
            growing_symbol_transition(symbol="+=={:::::::::::::::::>", num_lines=3)

            return world_survives, player_wins

        if chapter_camp.end_state_key == 'd':
            world_survives: bool = True
            player_wins: bool = True
            print("""
            In the end, your camp stopped the death of the embodied and Beings.
            While the world could never be the same again,
            Attention flows through out all the camps.""")
            growing_symbol_transition("√♥-√v--√♥-√v–", num_lines=3)
            if self.main_character.desired_end_state_key in ['b']:
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
                print("""You achieved your goal and the world goes on.""")

            return world_survives, player_wins

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
            return world_survives, player_wins

    def participation_choice(self):
        print("""You wake up to another day in the new low-Attention normal. 
            
            What do you want to with your day?
            
            a. Join your camp in strategizing
            b. Read a novel
            
            Type 'a' or 'b' """)
        choice = self.player_multi_choice(['a', 'b'])
        if choice == 'b':
            print("""You enjoy your novel.""")
            growing_symbol_transition(line_of_fish, num_lines=3)
            return False
        else:
            print("""You treat yourself to a poem,
             but then go to find the others in your camp.""")
            growing_symbol_transition(moon_star_line, num_lines=3)
            return True


    def round_one(self, chapter_camp):
        """
        free market for tokens introduced
        in all camps but Skalismo, free market is adopted
        in Anarkio camp, 1/2 adopt free market, 1/2 reject tokens and player can choose which to go down
        if reject free market in Anarkio no_tokens = True

        returns fame, no_tokens: bool
        """
        print("""round 1 is to be written""")
        fame: bool = False
        no_tokens: bool = False
        next_chapter_camp = self.switch_choice(chapter_camp)
        return fame, no_tokens, next_chapter_camp

    def round_two(self, chapter_camp, fame, no_tokens):
        """
        fall of free market and death of camp unless:
        Skalismo --> democratically managed economy
        Anarkio and no_tokens --> chaos + disorder + invasion?
        """
        print("""round 2 is to be written""")
        if chapter_camp == SkalismoCamp:
            camp_lives: bool = True
            return camp_lives, chapter_camp
        else:
            camp_lives: bool = False
            next_chapter_camp = self.switch_choice(chapter_camp)
            return camp_lives, next_chapter_camp

    def switch_choice(self, chapter_camp):
        if chapter_camp.sector.name == "Beit":
            chapter_sector = BeitSector
            alt_sector = GimelSector
        else:
            chapter_sector = GimelSector
            alt_sector = BeitSector

        camp_index = chapter_sector.camps.index(chapter_camp)
        if camp_index == len(chapter_sector.camps) - 1:
            next_camp_index = random.choice([2, 3])
        else:
            next_camp_index = camp_index + 1

        self.transition_as_typewriter("""You escape to the edge of camp.  
        As you approach you see a fence and someone waving at you from behind it.""")

        sector_or_camp: str = random.choice('SC')
        if sector_or_camp == 'S':
            print(watch_fence_void)
            self.transition_as_typewriter(f"""The person asks you if seen that {alt_sector.dinner_talking_points["sector"]}""")
            print(f"""Do you agree that '{alt_sector.dinner_talking_points["sector"]}'? (Y/N)""")
            sector_yes = self.player_yn_to_bool()
            if sector_yes:
                print(f"""You respond,
                Yes! I've seen the error in my ways and want to go where people think '{alt_sector.dinner_talking_points["sector"]}'""")
                print("""Without thinking, you cross over the fence,
                leaving what you knew behind.""")
                return True, alt_sector.camps[camp_index]
            else:
                print(f"""You respond, 
                Sorry, I'm looking for another path but that is not it.""")
                print("""""")
                print(fence_void)
                print("""You turn and are confronted with another fence. 
                A new person calls out to you: """)
                self.transition_as_typewriter(f"""You are right about beings.
                Why don't you come to my camp, where we believe that
                {chapter_sector.camps[next_camp_index].summary_statement}?""")
                print("""You briefly consider going back to the safety of your camp,
                but the anger in their eyes reminds you this is the time to leave.""")
                print("""For better or worse, you cross over the fence.""")
                return True, chapter_sector.camps[next_camp_index]
        else:
            print(fence_void)
            print(f"""The person behind the fence looks concerned.  They invite you to their camp.
            """)
            print(f"""Do you ask what their camp believes? (Y/N)""")
            beliefs_yes = self.player_yn_to_bool()
            if beliefs_yes:
                print(f"""They say that their camp believes: {chapter_sector.camps[next_camp_index].summary_statement}""")
            print("""Do you want to join their camp? (Y/N)""")
            camp_yes = self.player_yn_to_bool()
            if camp_yes:
                print("""You accept the invitation to their camp, wondering what awaits you next.""")
                return True, chapter_sector.camps[next_camp_index]
            elif beliefs_yes:
                print(f"""You say that you can not go somewhere where people believe that
                {chapter_sector.camps[next_camp_index].summary_statement}
                """)
            else:
                print("""You decline, this feels wrong in your gut.""")

            self.transition_as_typewriter("""Just as you are about to give up leaving, a different fence appears.""")
            print(watch_fence_void)
            print("""A different person waves at you.""")
            self.transition_as_typewriter(f"""They ask you if seen that {chapter_sector.dinner_talking_points["sector"]}""")
            print(f"""Do you agree that '{chapter_sector.dinner_talking_points["sector"]}'? (Y/N)""")
            sector_yes = self.player_yn_to_bool()
            if sector_yes:
                print(f"""Sighing in relief, you nod yes.""")
                print("""Without thinking, you cross over the fence,
                                leaving what you knew behind.""")
                return True, alt_sector[next_camp_index]
            else:
                if chapter_camp == GimelSector.camps[-1] or alt_sector[next_camp_index] == SkalismoCamp:
                    print("""Realizing that neither of these are great options, you turn back towards your camp.""")
                    return False, chapter_camp

                else:
                    print("""You say you don't agree with them about beings.""")
                    print(f"""A new person appears.  
                    They tell you that their camp believes {SkalismoCamp.stated_camp_core_belief}
                    and even if you are not sure you agree, you could come to their camp and for now.""")
                    print("""Do you want to go to their camp? (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if yes:
                        print("""You accept the invitation to their camp, wondering what awaits you next.""")
                        return True, SkalismoCamp
                    else:
                        print("""You decline.  
                        Feed up with the lack of other options, you turn back towards your camp.""")
                        return False, chapter_sector



    def events(self):
        # from last level saw_news is bool
        # round number is number of times played Chapter 6
        chapter_sector, chapter_camp, num_rounds_in_camp, participate, fame, no_tokens = self.starting_point
        print(participate, self.number, num_rounds_in_camp)
        print(f"last round participate {participate} -- run round {self.number} -- camp round {num_rounds_in_camp}")
        if self.number == 6:
            print("""What do you think the most important goal is?""")
            for key, value in end_state_mappings.items():
                print(f"""{key}. {value}""")
            print(f"""Type '{"', '".join(list(end_state_mappings.keys())[:-1])}' or '{list(end_state_mappings.keys())[-1]}'""")
            desired_outcome = self.player_multi_choice(list(end_state_mappings.keys()))

            self.main_character.chose_desired_end_state(desired_outcome)

        # extra round if in the socialist camp
        if self.number == max_round or num_rounds_in_camp >= 3:
            if num_rounds_in_camp < 1 and participate:
                fame, no_tokens = self.round_one(chapter_camp)
            world_survives, player_wins = self.ending(chapter_camp, participate)
            return self.main_character, chapter_sector, chapter_camp, world_survives, player_wins

        participate = self.participation_choice()
        if not participate:
            return self.main_character, chapter_sector, chapter_camp, num_rounds_in_camp, participate, fame, no_tokens
        else:
            num_rounds_in_camp += 1

        print(f"run round {self.number} -- camp round {num_rounds_in_camp}")
        if num_rounds_in_camp == 1:
            fame, no_tokens, next_chapter_camp = self.round_one(chapter_camp)
        elif num_rounds_in_camp == 2:
            camp_lives, next_chapter_camp = self.round_two(chapter_camp)

        if next_chapter_camp != chapter_camp:
            num_rounds_in_camp = 0

        print(chapter_sector, chapter_camp, num_rounds_in_camp, participate, num_rounds_in_camp,fame, no_tokens)
        return self.main_character, chapter_sector, chapter_camp, num_rounds_in_camp, participate, fame, no_tokens


