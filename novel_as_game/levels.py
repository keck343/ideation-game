from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition
import time


class ChapterOne(LevelofStory):
    number = 1
    next_chapter = 2

    def events(self):
        print("""
───────────────▄▄───▐█
───▄▄▄───▄██▄──█▀───█─▄
─▄██▀█▌─██▄▄──▐█▀▄─▐█▀
▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌
▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄
        """)
        print("""You wake up in an unfamiliar town with no recollection of how you got here.""")
        print("Do you want to walk around? (Y/N)")
        yes: bool = self.player_yn_to_bool()
        # anything that isn't a yes counts a no
        if yes:
            print("""You walk around, noting how this world has elements of the world you know, 
            but also feels fantastical in a jarring way but awe inspiring way.""")
            time.sleep(1)
            print("""There are so many combinations of seemingly disparate things.""")
            time.sleep(1)
            print("""You find yourself synthesizing new meanings that make sense to you.
            The world you came from feels bigger than you ever could have imagined back on Earth.""")
            print("")

        # nothing about trajectory changes if you don't walk around this time, you just have less information
        print("""You run into a stranger.""")
        time.sleep(1)
        print("""As a new comer in a strange land, you override any social anxiety and walk towards them.""")
        time.sleep(1)
        print("")
        print("""As you approach, the stranger asks you your name.  Do you give your name? (Y/N)""")
        yes: bool = self.player_yn_to_bool()
        print("")
        if yes:
            if len(self.main_character.creator) < 3:
                partial_name = self.main_character.creator
            else:
                partial_name: str = self.main_character.creator[0:round(len(self.main_character.creator)/2)]
            print(f"""You begin to say, 'I am {partial_name}...' but something feels off.""")
            print("""In this new world with everything out of place, 
            it feels as if you are mistaken about your own name.""")
            known_player_name: str = partial_name
        else:
            print("""You pause, and in ambiguity say nothing at all.""")
            known_player_name: str = "unknown"

        print("")
        time.sleep(1)
        print("""Would you like to ask the stranger their name? (Y/N)""")
        yes: bool = self.player_yn_to_bool()
        if yes:
            known_idea_name: str = self.supporting_characters[0].name
            print(f"""You ask the stranger their name.  
            They tell you that they are {known_idea_name}.""")
        else:
            known_idea_name: str = "The stranger"

        print("")
        print(f"""{known_idea_name} says,
        'Hello {known_player_name}! Where do you come from?' """)
        print("")
        print("""You suddenly realize you have no recollection of where you come from.
        Stunned by your lack of origin you simply reply:""")
        print("""
        'I have no idea.' 
        """)
        time.sleep(3)

        print(f"""{known_idea_name} replies,
        'I woke up here just like you with no memory of who I was or how I got here.  
        Well come to think of it, amnesia is a pretty common experience here.  
        You’re always halfway somewhere, aren’t you?
        I believe firmly, {self.supporting_characters[0].describe_self()}'""")
        print("")
        time.sleep(1)

        print(f"""Would you like to respond to {known_idea_name}'s statement that 
        '{self.supporting_characters[0].describe_self()}'? (Y/N)""")
        yes: str = self.player_yn_to_bool()
        if yes:
            print(f"What do you say to {known_idea_name}?")
            response = input()
            print("")
            print(f"""{known_idea_name} thinks over your statement carefully.""")
            time.sleep(1)
            print("")
            print(f"""Do you {known_idea_name} think has taken in your point? (Y/N)""")
            new_yes: bool = self.player_yn_to_bool()
            print("")
            if new_yes:
                print(f"""{known_idea_name} thanks you for the dialogue, they had not thought of that before.
                They feel this may expand their perspective.""")
                self.supporting_characters[0].expand_idea(expansion=response)

        print(f"""{known_idea_name} says, 'It was lovely to meet you, {known_player_name}, but I must be going,'
        and exit stage left.
        """)
        print("")
        time.sleep(1)

        print("""Do you want to wonder around? (Y/N)""")
        yes: bool = self.player_yn_to_bool()
        print("")
        if yes:
            print("""Just as you are stumped on where to go next, a new being appears.""")
        else:
            print("""Just as you are being to feel lost and trapped, a new being appears.""")

        # TO DO: consider assigning ideas numbers
        if known_idea_name != "The stranger":
            numberless_concept: str = known_idea_name.rsplit(' ', 1)[0]
        else:
            numberless_concept: str = known_idea_name

        print(f"""The new being walks over to you and introduces themselves as 
             {numberless_concept} 6.28.""")
        print(f"""You be begin to wonder how many {numberless_concept}s there are out there.
        
             """)
        time.sleep(1)
        print(f"""Just as soon as they appear, a new being calls for {numberless_concept} 6.28.""")
        self.transition_as_typewriter(f"""
              They scamper off saying, 'Yes {self.supporting_characters[1].name}, I'm coming! 
              Sorry to  be so brief {known_player_name} -  you should come to our dinner party!'
              """)

        print("""Do you wish to go to the dinner party? (Y/N)""")
        yes: bool = self.player_yn_to_bool()
        if yes:
            print(f"""
            {numberless_concept} 6.28 says, 'Delightful, it starts at 7! See you there!'
            """)

        else:
            print("""
            You reply, 'It's been a long day, and I don't know where I am. I should.....'
            """)
            time.sleep(1)
            print(f"""
            Before you can think of where you should be or what you should be doing,
            {numberless_concept} 6.28 butts in,""")
            print("""

            'You look so lost, this will be the thing to lift your spirits! 
            Regardless, I really must insist.
            
            """)


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

        conspiracism_talking_points = {
            "sector": "Beings do not exist.",
            "beings": """"Fools claim that beings exist in a physical realm connected to ours.
            Some even claim that we come out of their thoughts, 
            as if we are not enough in and of ourselves. 
            As if something as foolish as attention could control our fate.""",
            "disappearance": """
            The Eksterteranoj's plans must be advancing quickly.
            """,
            "beings counter point": """No one has ever seen a being.
            I believe in things I have done my own research on.""",
            "camp invitation": """You are correct to reject the nonsense of beings.
            The party is almost over and we can't stay here.  
            Would you like to join me at my camp for the next cycle?
            """
        }
        systems_talking_points = {
            "sector":  "The fact that beings exist is widely accepted by most camps.",
            "beings": """Through careful research into the disappearance of our kind,
            most scientists beings exist in a physical realm that we are connected to.
            Our origin story is still a matter of debate, but most agree there is an 
            attention mechanism that can explains 98% of our disappearance rates.""",
            "disappearance": """
            Our top scientific camps are struggling to find a pattern or cause, much less a solution.
            """,
            "beings counter point": """How could so many camps, and even ones outside my sector
            come to conclude that we exist in a system with beings?""",
            "camp invitation": """You are correct to accept the existence of beings.
            The party is almost over and I'm afraid you might disappear without a camp,
            Top scientists say connection is key to existence.  
            Would you like to join me at my camp for the next cycle?
            """
        }

        if yes:
            first_talking_points = conspiracism_talking_points
            second_talking_points = systems_talking_points
            print("""You walk over to the nearest dinner party guest and ask what they are discussing.
            They smile at you and say,""")
        else:
            first_talking_points = systems_talking_points
            second_talking_points = conspiracism_talking_points
            print("""You stare off into space a little while longer.  
            A party guest approaches you and asks if you are new here. 
            You say yes, and they invite you to join the conversation and say,
            """)

        print(f"""why we are discussing how {first_talking_points["sector"]}...""")
        print(f"""The other guest interjects, which is of course preposterous
        {second_talking_points["sector"]}""")

        print("""Would you like to:
        a) smile and nod 
        b) inquire what beings are
        c) inquire how to leave the party
        
        Type 'a' 'b' or 'c' to make your choice.""")
        choice: str = self.player_multi_choice(['a', 'b', 'c'])

        # get explanation of beings with choice b
        if choice == 'b':
            print(f"""You ask what beings are.  The first guest says:
        
            {first_talking_points["beings"]}""")
            time.sleep(1)
            print(f"""The second guest looks furious and interjects:
            
             {second_talking_points["beings"]}""")
            print("""You inquire to what fate beings might control.  
            The first guests clears their throat and says, """)
            time.sleep(1)

        # no explanation of beings, skip to disappearance
        if choice == 'c':
            print("""You inquire how to leave the party.  
            Both guests look at you alarmed.  
            The first exclaims, it's not safe out there! Haven't you heard?""")
            print("""Do you admit you have not heard what they are talking about? (Y/N)""")
            yes: bool = self.player_yn_to_bool()
            if yes:
                print("""You confess to being new here.  
                Both express sympathy and remark they miss being young, and fear for your survival because""")

            else:
                print(f"""The second guest asks you what you your take on the situation. 
                You stumble, and start to mumble {self.main_character.describe_self()[0:3]}...
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
        {second_talking_points["beings counter point"]}""")
        growing_symbol_transition(symbol="( ｡ •̀ ᴖ •́ ｡)", num_lines=2)
        print(f"""The first guest interjects, 
        {first_talking_points["beings counter point"]}""")
        growing_symbol_transition(symbol="୧(๑•̀ᗝ•́)૭", num_lines=1)

        print(f"""You find yourself faced with a choice. 
        Do you believe in beings? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print(systems_talking_points["camp invitation"])
        else:
            print(conspiracism_talking_points["camp invitation"])

        print("""Do you accept the guest's invitation? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print("""You accept the invitation and thank both guests for the conversation.
            The other guest's frustrations soften a little and they wish you a good next cycle.""")
            # to do: add sector to player's idea?
        else:
            print(f"""The other guest says, you must be having second thoughts on your stance on beings.
            Come with me to my camp instead, I'm not an ideologue and will not force you to agree with me! 
            """)
            print("""Do you accept the guest's invitation? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print("""You accept the invitation and thank both guests for the conversation.""")
            else:
                print("""You say, while I appreciate this dialogue, I am firm in my stance on beings.
                Therefore I must accept the other invitation for the next cycle.
                The other guest nods saying, of course only you can choose what camp you visit.""")

        print("""You leave the party grateful to have some place to go and 
        wondering what just happened and what mysteries await you next cycle.""")
        print("""
────██──────▀▀▀██
──▄▀█▄▄▄─────▄▀█▄▄▄
▄▀──█▄▄──────█─█▄▄
─▄▄▄▀──▀▄───▄▄▄▀──▀▄
─▀───────▀▀─▀───────▀▀
        """)


class ChapterThree(LevelofStory):
    number = 3
