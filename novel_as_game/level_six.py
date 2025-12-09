from chapter_structure import LevelofStory
from constants import end_state_mappings, max_round
from text_graphics import growing_symbol_transition, watch_fence_void, fence_void, \
    line_of_fish, moon_star_line, chains_line
from world_sectors_camps import BeitSector, GimelSector, CampObjectified, SkalismoCamp, AnarkioCamp
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

    def round_one(self, chapter_camp, last_round: bool = False):
        """
        free market for tokens introduced
        in all camps but Skalismo, free market is adopted
        in Anarkio camp, 1/2 adopt free market, 1/2 reject tokens and player can choose which to go down
        if reject free market in Anarkio no_tokens = True

        returns fame, no_tokens: bool
        """
        fame: bool = False
        no_tokens: bool = False
        self.main_character.add_camp(chapter_camp)

        print(f"""You find your fellow camp members who are gathering to figure out what to do.
    
        The latest headlines report even more dead and disappeared.
        The death toll is up to {min(self.number-1, 9)*10}% of all the embodiments everywhere.""")
        growing_symbol_transition(symbol="_|⚠|_︎", num_lines=3)
        print("""They all seem gathered around someone who is lecturing about innovation.""")
        print("""The lecturer says: """)
        print(chapter_camp.round_one_dict["lecturer"])

        if chapter_camp not in (AnarkioCamp, SkalismoCamp):
            print("""Someone in the crowd shouts:
        How would we do that?
        """)
            print("""The lecture replies:
        
        We can achieve that if we implement tokens as a reward.  
        These tokens will give those who work the hardest the ability to buy the remaining resources and Attention.""")
        else:
            print("""Someone in the crowd shouts: Why would we care if we reject authority?
                                     
            The lecturer replied:
            
            Their big banks are popping up everywhere, we must provide an alternative to tokens!""")

        if chapter_camp != SkalismoCamp:
            print("""You can see excitement rising in your friend and camp members.""")
            print("""Do you want to challenge the lecturer's doctrine? (Y/N) """)
            doctrine_yes = self.player_yn_to_bool()
            if doctrine_yes:
                no_tokens = True
                fame = True
                print("""You look around at your camp and realize you must say something.""")
                growing_symbol_transition("(╥﹏╥)", num_lines=2)
                print(f"""You address the crowd saying: 
                {chapter_camp.round_one_dict["counter_lecture"]}""")
                if chapter_camp != AnarkioCamp:
                    fame = True
                    print("""You look around at your camp and realize you must say something.""")
                    growing_symbol_transition("(╥﹏╥)", num_lines=2)
                    print(f"""You address the crowd saying:
                                                    {chapter_camp.round_one_dict["counter_lecture"]}
                                                    """)
                    print(f"""While some people seem to consider what you are saying, most start chanting:

                                    {chapter_camp.round_one_dict["chant"]}""")
                    print("""The lecturer eggs the crowd on saying:

                                        Yes friends, these are unprecedented times that call for unprecedented measures!
                                            The future awaits us!

                                    """)
                    print("""What do you do?

                                                    a. Join the lecturer and the camp on their new token path
                                                    c. Leave the entire camp behind.

                                                    Type 'a' or 'b' """)
                    choice = self.player_multi_choice(['a', 'b'])
                    if choice == 'b':
                        print(f"""You know in your heart you must leave and try to find new ways to exist 
                                        with {min(11 - self.number, 1) * 10}% of all the embodiments everywhere that are left.
                                        You walk away from the crowd.""")
                        if last_round:
                            next_chapter_camp = chapter_camp
                        else:
                            next_chapter_camp = self.switch_choice(chapter_camp)
                        return fame, no_tokens, next_chapter_camp

                elif chapter_camp == AnarkioCamp:
                    print("""People cheer.  Your friend changes their mind and calls for people to reject the lecturer.""")
                    print("""The lecturer the crowd:

                    Come my friends, they implore, these are unprecedented times that call for unprecedented measures.
                    I call for a motion to split the camp.""")
                    print("""""")
                    print("""A murmur ripples through the crowd.  
                    Your friend stands up and tells the lecturer they are welcome to leave and start their own camp.""")
                    print("""""")
                    growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=3)
                    print("""The lecturer invites all who are with them to split and start their own camp.""")
                    growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=2)
                    print("""More people than you expect join them.""")
                    growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=1)
                    print("""Those who remain decide to each pursue their own path to find a way to stop the loss of Attention 
                    and connection with beings and reconvene tomorrow.""")
                    if not last_round:
                        print("""Do you wish to join them? (Y/N) """)
                        yes = self.player_yn_to_bool()
                        if yes:
                            print("""Full of purpose, you set off to figure out what where to begin.""")
                            return fame, no_tokens, chapter_camp
                        else:
                            print("""You decide that neither of these splits are for you and get as far away from the crowd as you can.""")
                            next_chapter_camp = self.switch_choice(chapter_camp)
                            return fame, no_tokens, next_chapter_camp
                    else:
                        print("""Wondering how long the last 10% of the embodied will hold out,
                        you set off to figure out what where to begin.""")
                        return fame, no_tokens, chapter_camp

            elif not doctrine_yes and chapter_camp == AnarkioCamp:
                print("""You turn to look at your friend, and see their excitement turn to disgust.""")
                print(f"""They address the crowd saying: 
                {chapter_camp.round_one_dict["counter_lecture"]}""")
                print("""A few people murmur in agreement.""")
                print("""The lecturer looks around as if to see if they still have supporters.  
                
                Come my friends, they implore, these are unprecedented times that call for unprecedented measures.
                We must leave those who would hold us back behind.
                
                """)
                print("""Another person makes a motion to split the camp.  
                Your friend tells you this is uncommon but not unheard of.""")
                print("""What do you do?
                
                a. Join the lecturer's side of the camp
                b. Reject the lecturer and stay
                c. Leave the entire camp behind.
                
                Type 'a', 'b', or 'c' """)
                choice = self.player_multi_choice(['a', 'b', 'c'])
                if choice == 'a':
                    print("""You decide to join the side of innovation and follow the lecturer to make a new camp.""")
                    return fame, no_tokens, chapter_camp
                elif choice == 'b':
                    no_tokens = True
                    print("""You join your friend and urge others to reject the lecturer.""")
                    growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=3)
                    print("""More people than you expect join them.""")
                    growing_symbol_transition("(⸝⸝⸝╸w╺⸝⸝⸝)", num_lines=2)
                    print("""Those who remain decide to each pursue their own path to find a way to stop the loss of Attention 
                    and connection with beings and reconvene tomorrow.""")
                    return fame, no_tokens, chapter_camp
                else:
                    print(
                        """You decide that neither of these splits are for you and get as far away from the crowd as you can.""")
                    next_chapter_camp = self.switch_choice(chapter_camp)
                    return fame, no_tokens, next_chapter_camp

            # elif doctrine_yes:

            elif not doctrine_yes:
                print(f"""The crowd continues to cheer. Someone beings to chant:
                
                {chapter_camp.round_one_dict["chant"]}
                """)
                growing_symbol_transition("☚⍢⃝☚", num_lines=3)
                print("""Soon everyone has joined in.""")
                print("""Do you cheer with the crowd? (Y/N)""")
                yes = self.player_yn_to_bool()
                if yes:
                    print("""You join the cheering, the energy feels electric.""")
                    growing_symbol_transition(symbol="❇", num_lines=3)
                    print("""The lecturer praises everyone for accepting what's needed in unprecedented times.
                    
                    Tomorrow, they say, we began a new era.  I'll see you all here in the morning.
                    """)
                    print("""The crowd disperses.  Your friend is bubbling with excitement.
                    You wonder what tomorrow brings and about your next move.
                    """)
                    print("""Do you want to remain at this camp? (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if yes:
                        print("""You retire for the night in the safety of a familiar bed.""")
                        return fame, no_tokens, chapter_camp
                    else:
                        print("""A strong feeling of dread creeps into your bones.  You walk away from the crowd.""")
                        print("""You realize it is time to leave this place behind.""")
                        next_chapter_camp = self.switch_choice(chapter_camp)
                        return fame, no_tokens, next_chapter_camp
                else:
                    no_tokens = True
                    print("""You realize you have to get out of here as soon as possible. You walk away from the crowd.""")
                    next_chapter_camp = self.switch_choice(chapter_camp)
                    return fame, no_tokens, next_chapter_camp

            return fame, no_tokens, chapter_camp

        elif chapter_camp == SkalismoCamp:
            print(f"""People look uncomfortable and start to murmur.""")
            print("""Do you wish to counter the lecturer's points? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print(f"""Seeing the unease in the camp and feel confident you say:
                
                {SkalismoCamp.round_one_dict["counter_lecture"]}
                """)
                fame = True
                growing_symbol_transition(num_lines=2)
                print("""Another person is inspired by your point and says:
                """)
            else:
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

            if not yes:
                print("""Do you want to stay and be part of the democratically managed economy? (Y/N)""")
                stay_yes = self.player_yn_to_bool()
                if not stay_yes:
                    next_chapter_camp = self.switch_choice(chapter_camp)
                    return fame, no_tokens, next_chapter_camp

            return fame, no_tokens, chapter_camp

        else:  # back up agnostic to camp event
            print("""The crowd cheers.  You realize can not stay with people who are so easily swayed.
            You walk away from the crowd.""")

            if last_round:
                next_chapter_camp = chapter_camp
            else:
                next_chapter_camp = self.switch_choice(chapter_camp)
            return fame, no_tokens, next_chapter_camp

    def round_two(self, chapter_camp, fame, no_tokens, last_round: bool = False):
        """
        fall of free market and death of camp unless:
        Skalismo --> democratically managed economy
        Anarkio and no_tokens --> chaos + disorder + invasion?
        """

        if chapter_camp == SkalismoCamp:
            camp_lives: bool = True
            print("""Your camp begins to form committees and elect leaders to shape a new economic system.
            
            They reach out to other camps, offer to help provide for their needs, and invite them to be part of the new system.""")
            growing_symbol_transition(symbol="≽ ^⎚ ˕ ⎚^ ≼", num_lines=3)
            print("""As scientific minds collaborate across camps, new understandings of the attention equations emerge.
            """)
            if fame:
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
                you could take credit for the breakthrough - could it be better if the breakthrough came from an original memeber of the camp?""")
                print("""Do you give the new scientist credit for the discovery? (Y/N)""")
                credit_yes = self.player_yn_to_bool()
                if credit_yes:
                    fame = True
                    print("""You were only able to keep up the lie for a couple cycles. 
                    
                    Eventually the truth came out, you were disgraced and no one will work with you.""")

                    self.transition_as_typewriter("""The lie also caused fractures in the movement, 
                    but with you out of the picture, the camp recovers.
                    """)
                else:
                    fame = False
                    print("""The new scientist's breakthrough allows for the camp to set up a system 
                    where beings and embodied make it through the crisis and thrive.""")

                    self.transition_as_typewriter("""Attention flows freely.""")
                    growing_symbol_transition(symbol="༄.° ≽ ^⎚ ˕ ⎚^ ≼ ༄.°", num_lines=3)

                    print("""Even if your name is not in the history textbooks, 
                    you are proud of the role you played and the community you are part of.""")

        elif chapter_camp == AnarkioCamp and no_tokens:
            camp_lives: bool = False
            print(f"""round 2 for {chapter_camp.known_name} is to be written""")
            print(f"""fame = {fame}""")
            print(f"""no_tokens = {no_tokens}""")


        else:
            camp_lives: bool = False
            print(f"""round 2 for {chapter_camp.known_name} is to be written""")
            print(f"""fame = {fame}""")
            print(f"""no_tokens = {no_tokens}""")


        if last_round or chapter_camp == SkalismoCamp:
            next_chapter_camp = chapter_camp
            return fame, camp_lives, next_chapter_camp
        else:
            next_chapter_camp = self.switch_choice(chapter_camp)

        return fame, camp_lives, next_chapter_camp

    def switch_choice(self, chapter_camp):
        if chapter_camp.sector.name == "Beit":
            chapter_sector = BeitSector
            alt_sector = GimelSector
        else:
            chapter_sector = GimelSector
            alt_sector = BeitSector

        visited_chapter_sector_camps = [camp for camp in self.main_character.camps if camp.sector == chapter_sector]
        visited_alt_sector_camps = [camp for camp in self.main_character.camps if camp.sector != chapter_sector]
        camp_index = chapter_sector.camps.index(chapter_camp)

        if camp_index == len(chapter_sector.camps) - 1:
            next_camp_index = 0
        else:
            next_camp_index = camp_index + 1

        next_chapter_camp = chapter_sector.camps[next_camp_index]
        next_alt_camp = alt_sector.camps[next_camp_index]

        if next_chapter_camp in visited_chapter_sector_camps:
            unvisited_chapter_camps = set(chapter_sector.camps) - set(visited_chapter_sector_camps)
            if len(unvisited_chapter_camps) == 0:
                next_chapter_camp = visited_chapter_sector_camps[0]
            else:
                next_chapter_camp = random.choice(unvisited_chapter_camps)

        if next_alt_camp in visited_alt_sector_camps:
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
                        return chapter_sector

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

        # extra round if just switched camps
        if self.number == max_round or num_rounds_in_camp >= 3:
            if num_rounds_in_camp < 1 and participate:
                fame, no_tokens = self.round_one(chapter_camp, last_round=True)
            elif num_rounds_in_camp == 1 and chapter_camp == SkalismoCamp:
                self.round_two(SkalismoCamp, fame, no_tokens, last_round=True)

            world_survives, player_wins = self.ending(chapter_camp, participate)
            return self.main_character, chapter_sector, chapter_camp, world_survives, player_wins

        participate = self.participation_choice()
        if not participate:
            return self.main_character, chapter_sector, chapter_camp, num_rounds_in_camp, participate, fame, no_tokens
        else:
            num_rounds_in_camp += 1
            self.main_character.add_camp(chapter_camp)

        print(f"run round {self.number} -- camp round {num_rounds_in_camp}")
        if self.number == max_round - 1:
            last_round = True
        else:
            last_round = False

        if num_rounds_in_camp == 1:
            fame, no_tokens, next_chapter_camp = self.round_one(chapter_camp, last_round)
        elif num_rounds_in_camp == 2:
            fame, camp_lives, next_chapter_camp = self.round_two(chapter_camp, last_round, no_tokens)

        if next_chapter_camp != chapter_camp:
            num_rounds_in_camp = 0

        return self.main_character, chapter_sector, next_chapter_camp, num_rounds_in_camp, participate, fame, no_tokens


