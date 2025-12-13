from chapter_structure import LevelofStory
from constants import end_state_mappings, max_round
from text_graphics import growing_symbol_transition, watch_fence_void, fence_void, \
    line_of_fish, moon_star_line, chains_line, floating_heart_ghost, speedy_snail
from world_sectors_camps import BeitSector, GimelSector, CampObjectified, SkalismoCamp, AnarkioCamp
import random
import time


class ChapterSix(LevelofStory):

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

    def round_one(self, chapter_camp, last_round: bool = False):
        """
        returns the chapter_camp for the next round

        free market for tokens introduced
        in all camps but Skalismo, free market is adopted
        in Anarkio camp, 1/2 adopt free market, 1/2 reject tokens and player can choose which to go down
        if reject free market in Anarkio self.main_character.no_tokens = True
        """
        self.main_character.add_camp(chapter_camp)

        print(f"""You find your fellow camp members who are gathering to figure out what to do.
    
        The latest headlines report even more dead and disappeared.
        The death toll is up to {min(self.number-1, 9)*10}% of all the embodiments everywhere.""")
        growing_symbol_transition(symbol="_|⚠|_︎", num_lines=3)
        print("""They all seem gathered around someone who is lecturing about innovation.""")
        print("""The lecturer says: """)
        print(chapter_camp.round_one_dict["lecturer"])

        if chapter_camp == AnarkioCamp:
            print("""Your friend seems excited, but others look concerend.""")
            print("""Do you want to challenge the lecturer's doctrine? (Y/N) """)
            doctrine_yes = self.player_yn_to_bool()
            if doctrine_yes:
                self.main_character.no_tokens = True
                self.main_character.fame = True
                print("""You look around at your camp and realize you must say something.""")
                growing_symbol_transition("(╥﹏╥)", num_lines=2)
                print(f"""You address the crowd saying: 
                                {chapter_camp.round_one_dict["counter_lecture"]}
                                """)
            else:
                print("""Someone in the crowd shouts: Why would we care if we reject authority?

                The lecturer replied:

                Their big banks are popping up everywhere, we must provide an alternative to tokens!
                """)

            print("""You turn to look at your friend, and see their excitement turn to disgust.""")
            print(f"""They address the crowd saying: 
                {chapter_camp.round_one_dict["counter_lecture"]}""")
            print("""A few people murmur in agreement.
            """)
            self.transition_as_typewriter("""The lecturer looks around as if to see if they still have supporters.  

                Come my friends, they implore, these are unprecedented times that call for unprecedented measures.
                We must leave those who would hold us back behind.

                """)
            print("""Another person makes a motion to split the camp.  
                Your friend tells you this is uncommon but not unheard of.
                """)
            print("""What do you do?

                a. Join the lecturer's side of the camp
                b. Reject the lecturer and stay
                c. Leave the entire camp behind.

                Type 'a', 'b', or 'c' """)
            choice = self.player_multi_choice(['a', 'b', 'c'])
            if choice == 'a':
                self.main_character.no_tokens = False
                print("""You decide to join the side of innovation and follow the lecturer.""")
                return chapter_camp
            elif choice == 'b':
                self.main_character.no_tokens = True
                print("""You join your friend and urge others to reject the lecturer.""")
                growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=3)
                print("""More people than you expect join the lecturer.""")
                growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=2)
                print("""Those who remain decide to each pursue their own path to find a way to stop the loss of Attention 
                    and connection with beings and reconvene tomorrow.""")
                return chapter_camp
            else:
                self.main_character.no_tokens = False
                print(
                    """You decide that neither of these splits are for you and get as far away from the crowd as you can.""")
                next_chapter_camp = self.switch_choice(chapter_camp)
                return next_chapter_camp

        elif chapter_camp == SkalismoCamp:
            print(f"""People look uncomfortable and start to murmur.""")
            print("""Do you wish to counter the lecturer's points? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                self.main_character.fame = True
                print(f"""Seeing the unease in the camp and feel confident you say:
                
                {SkalismoCamp.round_one_dict["counter_lecture"]}
                """)
                growing_symbol_transition(num_lines=2)
                print("""Another person is inspired by your point and says:
                """)
            else:
                self.main_character.fame = False
                print(f"""Someone stands up and addresses the crowd: 
                
                {SkalismoCamp.round_one_dict["counter_lecture"]}
                """)
                growing_symbol_transition(num_lines=2)
                print("""Another person stands up and adds: 
                """)

            print(f"""{SkalismoCamp.round_one_dict["counter_lecture_2"]}
            """)
            growing_symbol_transition(symbol="₍₍⚞(˶>ᗜ<˶)⚟⁾⁾", num_lines=3)
            print(f"""The crowd begins to chant:
            
            {SkalismoCamp.round_one_dict["chant"]}
            """)
            print(f"""The lecturer's frustration is palpable.  They shout at the crowd:
            
            {SkalismoCamp.round_one_dict["lecturer_counter"]}
            
            """)
            self.transition_as_typewriter("""But the crows does not back down.""")

            if yes:
                print(f"""The other person grabs your hand and addresses to the crowd:
                """)
            else:
                print("""The two people who spoke up address the crowd:
                """)

            print("""Tomorrow we begin to create our democratically managed economy!
            """)

            print("""Do you want to stay and be part of the democratically managed economy? (Y/N)""")
            stay_yes = self.player_yn_to_bool()
            if not stay_yes:
                next_chapter_camp = self.switch_choice(chapter_camp)
                return next_chapter_camp
            else:
                return chapter_camp

        else:
            print("""Someone in the crowd shouts:
            How would we do that?
            """)
            print("""The lecture replies:

            We can achieve that if we implement tokens as a reward.  
            These tokens will give those who work the hardest the ability to buy the remaining resources and Attention.""")
            print("""You can see excitement rising in your friend and camp members.
                """)
            print("""Do you want to challenge the lecturer's doctrine? (Y/N) """)
            doctrine_yes = self.player_yn_to_bool()
            if doctrine_yes:
                self.main_character.no_tokens = True
                self.main_character.fame = True
                print("""You look around at your camp and realize you must say something.""")
                growing_symbol_transition("(╥﹏╥)", num_lines=2)
                print(f"""You address the crowd saying: 
                {chapter_camp.round_one_dict["counter_lecture"]}
                """)
                print(f"""While some people seem to consider what you are saying, most start chanting:

                                        {chapter_camp.round_one_dict["chant"]}""")
            else:
                print(f"""The crowd starts chanting: {chapter_camp.round_one_dict["chant"]}""")

            growing_symbol_transition("☚⍢⃝☚", num_lines=3)
            print("""Soon everyone has joined in.""")
            print("""Do you cheer with the crowd? (Y/N)""")
            cheer_yes = self.player_yn_to_bool()
            if cheer_yes:
                print("""You join the cheering, the energy feels electric.""")
                growing_symbol_transition(symbol="❇", num_lines=3)
                print("""The lecturer praises everyone for accepting what's needed in unprecedented times.

                    Tomorrow, they say, we began a new era.  I'll see you all here in the morning.
                    """)
                print("""The crowd disperses.  Your friend is bubbling with excitement.
                    You wonder what tomorrow brings and about your next move.
                    """)
            else:
                print("""A strong feeling of dread creeps into your bones.  You walk away from the crowd.""")

            print("""Do you want to remain at this camp? (Y/N)""")
            stay_yes = self.player_yn_to_bool()
            if stay_yes:
                print("""You retire for the night in the safety of a familiar bed.""")
                return chapter_camp
            else:
                print("""You realize it is time to leave this place behind and journey to the edge of camp.""")
                if last_round:
                    print("""There were so few of the embodied left.
                    No matter how many times you ran to the edge, no fence appeared.""")
                    return chapter_camp
                else:
                    next_chapter_camp = self.switch_choice(chapter_camp)
                    return next_chapter_camp

    def round_two(self, chapter_camp, last_round: bool = False):
        """
        fall of free market and death of camp unless:
        Skalismo --> democratically managed economy
        Anarkio and no_tokens --> chaos + disorder + invasion?
        """
        remaining_percent = min(11 - self.number, 1) * 10

        if chapter_camp == SkalismoCamp:
            camp_lives: bool = True
            print("""Your camp begins to form committees and elect leaders to shape a new economic system.
            
            They reach out to other camps, offer to help provide for their needs, and invite them to be part of the new system.""")
            growing_symbol_transition(symbol="≽ ^⎚ ˕ ⎚^ ≼", num_lines=3)
            print("""As scientific minds collaborate across camps, new understandings of the attention equations emerge.
            """)
            if self.main_character.fame: # will exit function
                print("""As one of the people who spoke out against the lecturer, you are often invited to consult with the scientists.
                
                One scientist makes a break through.  They realize that beings and the emodied are dependant on each other.
                There is no way to ensure Attention flows without the beings survival.
                """)
                print("""Understanding the importance of this breakthrough, you make plans to share the findings with the public.
                You are nominated to address the public.
                """)
                print("""The scientist is someone who recently came from another camp and no one knows them.
                """)
                print("""You realize that as the only other person in the room, 
                you could take credit for the breakthrough - could it be better if the breakthrough came from an original member of the camp?""")
                print("""Do you give the new scientist credit for the discovery? (Y/N)""")
                credit_yes = self.player_yn_to_bool()
                if not credit_yes:
                    print("""You were only able to keep up the lie for a couple cycles. 
                    
                    Eventually the truth came out, you were disgraced and no one will work with you.""")

                    self.transition_as_typewriter("""The lie also caused fractures in the movement, 
                    but with you out of the picture, the camp recovers.
                    """)
                    print("""Fame is fickle.""")
                    print(floating_heart_ghost)

                    return camp_lives, chapter_camp
                else:
                    self.main_character.fame = False
                    print("""The new scientist's breakthrough allows for the camp to set up a system 
                    where beings and embodied make it through the crisis and thrive.""")

                    self.transition_as_typewriter("""Attention flows freely.""")
                    growing_symbol_transition(symbol="༄.° ≽ ^⎚ ˕ ⎚^ ≼ ༄.°", num_lines=3)

                    if self.main_character.desired_end_state_key in ['e', 'f']:
                        print("""You think of the fame you once desired and conclude it would require leaving your camp.
                        
                        Do you want to stay with your camp? (Y/N)""")
                        yes = self.player_yn_to_bool()
                        if yes:
                            next_chapter_camp = self.switch_choice(chapter_camp)
                            return camp_lives, next_chapter_camp
                        else:
                            print("""Even if your name is not in the history textbooks,""")
                    else:
                        print("""Looking around at the this camp, """)
                    print("""
                    you are proud of the role you played and the community you are part of.""")
                    print(floating_heart_ghost)
                    return camp_lives, chapter_camp

            print("""One scientist who recently came from another camp makes a break through.  
            They realize that beings and the embodied are dependant on each other.
             """)
            self.transition_as_typewriter("""There is no way to ensure Attention flows without the beings survival.""")

            print("""The new scientist's breakthrough allows for the camp to set up a system 
                                where beings and embodied make it through the crisis and thrive.""")

            self.transition_as_typewriter("""Attention flows freely.""")
            growing_symbol_transition(symbol="༄.° ≽ ^⎚ ˕ ⎚^ ≼ ༄.°", num_lines=3)
            return camp_lives, chapter_camp

        elif chapter_camp == AnarkioCamp and self.main_character.no_tokens:
            camp_lives: bool = False
            print("""You wake up to a new day with half your camp.  You try to figure out what to do.
            """)
            print("""Without a leadership structure, it's hard to work together, 
            so you all decide to go off on your own to try to figure out the attention equations and what to do about resources.
            """)
            growing_symbol_transition(symbol=line_of_fish, num_lines=3)
            print("""You all agree you hope things will be clearer in the morning.""")
            growing_symbol_transition(symbol=line_of_fish, num_lines=3)
            print("""Many days pass and the tokens side of the camp invaded.  
            The days of dreaming of anti-hierarchical idea sharing are over and everyone that does not adopt tokens are forced to flee.""")
            growing_symbol_transition(symbol=chains_line, num_lines=3)
            print("""You are able to make it out alive before everything collapses.""")
            if last_round:
                return camp_lives, chapter_camp
            else:
                next_chapter_camp = self.switch_choice(chapter_camp)
                return camp_lives, next_chapter_camp

        else:
            camp_lives: bool = False
            print(f"""The lecturer convenes everyone the next morning to begin the implementation of tokens.
            They explain the goal of accumulating wealth will provide the incentives needed for
            {chapter_camp.round_two_dict["innovation"]}
            
            They are ready to begin operation of the stores where people can exchange tokens for resources.
            """)
            print("""Do you ask how the members of the camp get tokens? (Y/N)""")
            question_yes = self.player_yn_to_bool()
            if question_yes:
                print(f"""The crowd murmurs in agreement, you raise your hand and ask:
                
                How do the members of our camp get tokens?
                """)

                print("""The lecturer responds that they already have the tokens,
                and people only need to be hired for a role in their store or provide an innovation worthy of reward.
                """)
            elif {chapter_camp.round_two_dict["crowd_asks"]}:
                print(f"""The crowd murmurs in agreement, someone raises their hand and asks:
                
                {chapter_camp.round_two_dict["counter_question"]}
            """)

                print("""The lecturer responds that they already have the tokens,
                and will generously set up the store for only a modest fee.
                """)

            if chapter_camp.round_two_dict["crowd_asks"] or question_yes:
                print("""Some unease spreads through the camp, but people begin to get to work with the lecturer's instructions.""")
            else:
                print("""The crowd cheers, ready to get to work with the lecturer's instructions.""")

            growing_symbol_transition(symbol=chains_line, num_lines=3)
            print("""The store does not go as planned.
            """)
            print("""The lecturer did not have enough jobs for everyone, and many in the camp went hungry.
            
            Whenever anyone asked what they were to do, the lecturer said they needed to innovate and try harder.
            """)
            print("""Do you want to stay in the camp (Y/N)?""")
            stay_yes = self.player_yn_to_bool()
            if stay_yes:
                growing_symbol_transition(symbol=chains_line, num_lines=3)
                print(f"""Soon people in the camp starved.  Some left to other camps,
            some tried to rise up against the lecturer,
            but he paid informants handsomely.
            
            No real {chapter_camp.round_two_dict["innovation"]} ever came.
            """)
                growing_symbol_transition(symbol=chains_line, num_lines=3)

            print("""Soon you too were forced to starve or flee.""")
            print("""With what little strength you have left, you make it to the edge of camp.""")
            if last_round:
                print("""There were so few of the embodied left.
                No matter how many times you ran to the edge, no fence appeared.""")
                return camp_lives, chapter_camp
            else:
                next_chapter_camp = self.switch_choice(chapter_camp)
                return camp_lives, next_chapter_camp

    def switch_choice(self, chapter_camp):
        self.main_character.add_camp(chapter_camp)
        if chapter_camp.sector.name == "Beit":
            chapter_sector = BeitSector
            alt_sector = GimelSector
        else:
            chapter_sector = GimelSector
            alt_sector = BeitSector

        camp_index = chapter_sector.camps.index(chapter_camp)
        visited_chapter_sector_camps = list(set([camp for camp in self.main_character.camps if camp.sector == chapter_sector]))
        visited_alt_sector_camps = list(set([camp for camp in self.main_character.camps if camp.sector != chapter_sector]))

        if camp_index == len(chapter_sector.camps) - 1:
            next_camp_index = 0
        else:
            next_camp_index = camp_index + 1

        next_chapter_camp = chapter_sector.camps[next_camp_index]
        next_alt_chapter_camp = alt_sector.camps[next_camp_index]

        if next_chapter_camp in visited_chapter_sector_camps:
            unvisited_chapter_camps = set(chapter_sector.camps) - set(visited_chapter_sector_camps)
            if len(unvisited_chapter_camps) == 0:
                next_chapter_camp = visited_chapter_sector_camps[0]
            else:
                next_chapter_camp = random.choice(unvisited_chapter_camps)

        if next_alt_chapter_camp in visited_alt_sector_camps:
            unvisited_alt_camps = set(alt_sector.camps) - set(visited_alt_sector_camps)
            if len(unvisited_alt_camps) == 0:
                next_alt_chapter_camp = visited_alt_sector_camps[0]
            else:
                next_alt_chapter_camp = random.choice(unvisited_alt_camps)

        self.transition_as_typewriter("""You escape to the edge of camp.  
        As you approach you see a fence and someone waving at you from behind it.""")

        sector_or_camp: str = random.choice('SC')
        if sector_or_camp == 'S':
            print(watch_fence_void)
            print(f"""The person asks you if seen that {alt_sector.dinner_talking_points["sector"]}""")
            print(f"""Do you agree that '{alt_sector.dinner_talking_points["sector"]}'? (Y/N)""")
            sector_yes = self.player_yn_to_bool()
            if sector_yes:
                print(f"""You respond,
                Yes! I've seen the error in my ways and want to go where people think '{alt_sector.dinner_talking_points["sector"]}'""")
                print("""Without thinking, you cross over the fence,
                leaving what you knew behind.""")
                return next_alt_chapter_camp
            else:
                print(f"""You respond, 
                Sorry, I'm looking for another path but that is not it.""")
                print("""""")
                print(fence_void)
                print("""You turn and are confronted with another fence. 
                A new person calls out to you: """)
                print(f"""You are right about beings.
                Why don't you come to my camp, where we believe that
                {next_chapter_camp.summary_statement}?""")
                print("""You briefly consider going back to the safety of your camp,
                but the anger in their eyes reminds you this is the time to leave.""")
                self.transition_as_typewriter("""For better or worse, you cross over the fence.""")
                return next_chapter_camp
        else:
            print(fence_void)
            print(f"""The person behind the fence looks concerned.  They invite you to their camp.
            """)
            print(f"""Do you ask what their camp believes? (Y/N)""")
            beliefs_yes = self.player_yn_to_bool()
            if beliefs_yes:
                print(f"""They say that their camp believes: {next_chapter_camp.summary_statement}""")
            print("""Do you want to join their camp? (Y/N)""")
            camp_yes = self.player_yn_to_bool()
            if camp_yes:
                print("""You accept the invitation to their camp, wondering what awaits you next.""")
                return next_chapter_camp
            elif beliefs_yes:
                print(f"""You say that you can not go somewhere where people believe that
                {next_chapter_camp.summary_statement}
                """)
            else:
                print("""You decline, this feels wrong in your gut.""")

            self.transition_as_typewriter("""Just as you are about to give up leaving, a different fence appears.""")
            print(watch_fence_void)
            print("""A different person waves at you.""")
            self.transition_as_typewriter(f"""They ask you if seen that {alt_sector.dinner_talking_points["sector"]}""")
            print(f"""Do you agree that '{alt_sector.dinner_talking_points["sector"]}'? (Y/N)""")
            sector_yes = self.player_yn_to_bool()
            if sector_yes:
                print(f"""Sighing in relief, you nod yes.""")
                print("""Without thinking, you cross over the fence,
                                leaving what you knew behind.""")
                return next_alt_chapter_camp
            else:
                if chapter_camp == GimelSector.camps[-1] or next_alt_chapter_camp == SkalismoCamp:
                    print("""Realizing that neither of these are great options, you turn back towards your camp.""")
                    return chapter_camp

                else:
                    print("""You say you don't agree with them about beings.""")
                    print(f"""A new person appears.  
                    They tell you that their camp believes {SkalismoCamp.stated_camp_core_belief}
                    and even if you are not sure you agree, you could come to their camp and for now.""")
                    print("""Do you want to go to their camp? (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if yes:
                        print("""You accept the invitation to their camp, wondering what awaits you next.""")
                        return SkalismoCamp
                    else:
                        print("""You decline.  
                        Feed up with the lack of other options, you turn back towards your camp.""")
                        return chapter_camp

    def events(self):
        # round number is number of times played Chapter 6
        # last_round effects how chapter is played.
        # end_loop exits in main.py and stays False until max rounds
        chapter_camp, num_rounds_in_camp, end_loop = self.starting_point

        if self.number == 6:
            print("""What do you think the most important goal is?""")
            for key, value in end_state_mappings.items():
                print(f"""{key}. {value}""")
            print(f"""Type '{"', '".join(list(end_state_mappings.keys())[:-1])}' or '{list(end_state_mappings.keys())[-1]}'""")
            desired_outcome = self.player_multi_choice(list(end_state_mappings.keys()))

            self.main_character.chose_desired_end_state(desired_outcome)

        participate = self.participation_choice()
        if not participate:
            if self.number == max_round:
                end_loop = True
            return self.main_character, chapter_camp, num_rounds_in_camp, end_loop

        if self.number == max_round:
            end_loop = True
            if num_rounds_in_camp < 1:
                chapter_camp = self.round_one(chapter_camp, last_round=True)
            else:
                camp_lives, chapter_camp = self.round_two(chapter_camp, last_round=True)
            return self.main_character, chapter_camp, num_rounds_in_camp, end_loop

        # run, self.number is incremented in main.py
        if num_rounds_in_camp == 0:
            self.main_character.add_camp(chapter_camp)
            next_chapter_camp = self.round_one(chapter_camp, last_round=False)
            print(f"""chapter_camp = {chapter_camp.known_name}""")
            print(f"""next_chapter_camp = {next_chapter_camp.known_name}""")
            if next_chapter_camp != chapter_camp:
                num_rounds_in_camp = 0
                return self.main_character, next_chapter_camp, num_rounds_in_camp, end_loop
            else:
                num_rounds_in_camp = 1
                return self.main_character, next_chapter_camp, num_rounds_in_camp, end_loop
        elif num_rounds_in_camp == 1:
            camp_lives, next_chapter_camp = self.round_two(chapter_camp, last_round=False)
            print(f"""chapter_camp = {chapter_camp.known_name}""")
            print(f"""next_chapter_camp = {next_chapter_camp.known_name}""")
            if chapter_camp == SkalismoCamp and next_chapter_camp == SkalismoCamp:
                end_loop = True
            else:
                num_rounds_in_camp = 0
            return self.main_character, next_chapter_camp, num_rounds_in_camp, end_loop
        else: # this shouldn't happen, just a backup
            next_chapter_camp = self.switch_choice(chapter_camp)
            return self.main_character, next_chapter_camp, 0, end_loop

