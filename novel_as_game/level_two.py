from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition
from world_sectors_camps import BeitSector, GimelSector
import time


class ChapterTwo(LevelofStory):
    number = 2
    next_chapter = 3

    def events(self):
        print("""
──────────────▄▀█▀█▀▄
─────────────▀▀▀▀▀▀▀▀▀ 
─────────────▄─░░░░░▄
───█──▄─▄───▐▌▌░░░░░▌▌
▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌
        """)
        print(f"""You are at the dinner party.
        The characters that brought you here have long abandoned you for their friends.
        You are overwhelmed with social anxiety and questions about where you are and who you are.
        What course of action will you take?""")
        time.sleep(1)
        print("""Do you want approach a dinner party guest? (Y/N)""")
        yes: bool = self.player_yn_to_bool()

        if yes:
            first_speaker = BeitSector
            second_speaker = GimelSector
            print("""You walk over to the nearest dinner party guest and ask what they are discussing.
            They smile at you and say, why""")
        else:
            first_speaker = GimelSector
            second_speaker = BeitSector
            print("""You stare off into space a little while longer.  
            A party guest approaches you and asks if you are new here. 
            You say yes, and they invite you to join the conversation saying,
            """)

        first_talking_points = first_speaker.dinner_talking_points
        second_talking_points = second_speaker.dinner_talking_points

        print(f"""we are discussing how {first_talking_points["sector"]}...""")
        print(f"""The other guest interjects, which is of course preposterous
        {second_talking_points["sector"]}""")

        print("""Would you like to:
        a) smile and nod 
        b) inquire what Beings are
        c) inquire how to leave the party

        Type 'a' 'b' or 'c' to make your choice.""")
        choice: str = self.player_multi_choice(['a', 'b', 'c'])

        # get explanation of Beings with choice b
        if choice == 'b':
            print(f"""You ask what Beings are.  The first guest says:

            {first_talking_points["Beings"]}""")
            growing_symbol_transition(symbol="｡ •̀ _ •́ ｡", num_lines=3)
            time.sleep(1)
            print(f"""The second guest looks furious and interjects:

             {second_talking_points["Beings"]}""")
            growing_symbol_transition(symbol="｡ •̀ _ •́ ｡", num_lines=3)

            print("""You inquire to what fate Beings might control.  
            The first guests clears their throat and says, """)
            growing_symbol_transition(symbol="( ｡ •̀ _ •́ ｡ )", num_lines=1)
            time.sleep(1)

        # no explanation of Beings, skip to disappearance
        if choice == 'c':
            print("""You inquire how to leave the party.  
            Both guests look at you alarmed.  
            The first exclaims, it's not safe out there! Haven't you heard?""")
            growing_symbol_transition(symbol="( ｡ •̀ _ •́ ｡ )", num_lines=1)
            print("""Do you admit you have not heard what they are talking about? (Y/N)""")
            yes: bool = self.player_yn_to_bool()
            if yes:
                print("""You confess to being new here.  
                Both express sympathy and remark they miss being young, and fear for your survival because""")

            else:
                print(f"""The second guest asks you what you your take on the situation. 
                You stumble, and start to mumble ...
                The first guest roles their eyes and butts in, saying obviously,""")

        if choice == 'a':
            print("""You smile and nod, zoning out on the conversation until you hear the first being say,""")

        print("""We have been disappearing across all camps and sectors at alarming rates.""")

        print(f"""{first_talking_points["disappearance"]}

        The second being jumps in.  This is ludicrous.  
        Clearly {second_talking_points["disappearance"]}""")

        time.sleep(1)

        print(f"""You sense the anger rising up in both guests.""")
        growing_symbol_transition(symbol="( ｡ •̀ ᴖ •́ ｡)", num_lines=3)
        print(f"""The second guest continues, 
        {second_talking_points["Beings counter point"]}""")
        growing_symbol_transition(symbol="( ｡ •̀ ᴖ •́ ｡)", num_lines=2)
        print(f"""The first guest interjects, 
        {first_talking_points["Beings counter point"]}""")
        growing_symbol_transition(symbol="୧(๑•̀ᗝ•́)૭", num_lines=1)

        print(f"""You find yourself faced with a choice. 
        Do you believe in Beings? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print(GimelSector.dinner_talking_points["camp invitation"])
            self.main_character.add_sector(GimelSector)
        else:
            print(BeitSector.dinner_talking_points["camp invitation"])
            self.main_character.add_sector(BeitSector)

        print("""Do you accept the guest's invitation? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print("""You accept the invitation and thank both guests for the conversation.
            The other guest's frustrations soften a little and they wish you a good next cycle. 
            After a pause they add, """)
            self.main_character.add_camp(self.main_character.sectors[0].camps[0])
        else:
            print(f"""The other guest says, you must be having second thoughts on your stance on Beings.
            Come with me to my camp instead, I'm not an ideologue and will not force you to agree with me! 
            """)
            print("""Do you accept the guest's invitation? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print("""You accept the invitation and thank both guests for the conversation.
                The other guest nods saying, of course only you can choose what camp you visit,""")
                # at this point there is only BeitSector or GimelSector
                if BeitSector not in self.main_character.sectors[0]:
                    self.main_character.add_sector(BeitSector)
                    self.main_character.add_camp(BeitSector.camps[0])
                else:
                    self.main_character.add_sector(GimelSector)
                    self.main_character.add_camp(GimelSector.camps[0])
            else:
                print("""You say, while I appreciate this dialogue, I am firm in my stance on Beings.
                Therefore I must accept the other invitation for the next cycle.
                The other guest nods saying, of course only you can choose what camp you visit,""")
                self.main_character.add_camp(self.main_character.sectors[0].camps[0])

        print("""but before you go, can you declare your take on this situation? """)
        growing_symbol_transition(symbol="( ｡ •̀ ``-`` •́ ｡ )", num_lines=1)
        worldview = self.player_long_answer()
        self.main_character.expand_idea(worldview)

        print("""The other player thanks you for your response and takes their leave.""")
        growing_symbol_transition(symbol="ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧", num_lines=2)

        print("""You leave the party grateful to have some place to go and 
        wondering what just happened and what mysteries await you next cycle.""")
        print("""
────██──────▀▀▀██
──▄▀█▄▄▄─────▄▀█▄▄▄
▄▀──█▄▄──────█─█▄▄
─▄▄▄▀──▀▄───▄▄▄▀──▀▄
─▀───────▀▀─▀───────▀▀
        """)

