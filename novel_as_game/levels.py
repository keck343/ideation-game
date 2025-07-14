from chapter_structure import LevelofStory
from world_ideas import IdeaObjectified
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

        conspiracism_talking_points = [
            "Beings do not exist.",
        ]
        systems_talking_points = [
            "The fact that beings exist is widely accepted by most camps.",
        ]

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
            We are discussing how ...
            """)

        print(f"""why we are discussing how {first_talking_points[0]}""")




class ChapterThree(LevelofStory):
    number = 3
