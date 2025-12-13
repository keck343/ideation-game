from chapter_structure import LevelofStory
from constants import quotes
from text_graphics import growing_symbol_transition
import time


class ChapterOne(LevelofStory):
    number = 1

    def events(self):
        print("""
───────────────▄▄───▐█
───▄▄▄───▄██▄──█▀───█─▄
─▄██▀█▌─██▄▄──▐█▀▄─▐█▀
▐█▀▀▌───▄▀▌─▌─█─▌──▌─▌
▌▀▄─▐──▀▄─▐▄─▐▄▐▄─▐▄─▐▄
        """)
        print("""You wake up in an unfamiliar town with no recollection of how you got here.""")
        print("""This world is so many combinations of seemingly disparate things.
        """)
        time.sleep(1)
        print("""You find yourself synthesizing new meanings that make sense to you.
            The world feels bigger than you ever could have imagined back home.
            """)
        print("")
        print("""A stranger appears.""")
        time.sleep(1)
        print("""As a new comer in a strange land, you override any social anxiety and walk towards them.""")
        time.sleep(1)
        print("")
        print(f"""The stranger turns toward you smiling.  
        I'm {self.supporting_characters[0]}.  What's your name?""")
        print(f"""
        Do you want to give {self.supporting_characters[0]} your name? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print("""You freeze, realizing that suddenly you can not recall your name.""")
        else:
            print("""You shake your head no.""")

        print(f"""Not to worry, {self.supporting_characters[0]} says, a lot of new folks here do not yet have names.
        """)

        print(f"""A new person runs up to {self.supporting_characters[0]} saying,
        I'm running late to worldview club and can not think of a quote to bring.
        """)

        print(f"""{self.supporting_characters[0]} introduces the other person as {self.supporting_characters[1]} to you.
        They pause, and turn to you and ask you if you have a quote.""")
        print("""Do you have a quote to give them? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print(f"""You smile and say, a quote that resonates with me was once said by {quotes[self.main_character.player_quote_key]['author']}:
            
            '{quotes[self.main_character.player_quote_key]['quote']}'
            """)

            print(f"""{self.supporting_characters[1]}'s face lights up. 
            I love that quote! They exclaim.
            Worldview club's membership is currently closed, but we have a dinner party tonight. You should come!""")
        else:
            print(f"""{self.supporting_characters[0]} apologies for putting you on the spot.  
            They turn to {self.supporting_characters[1]} and say:
            My favorite quote is by {quotes[self.main_character.player_quote_key]['author']}:
            
            '{quotes[self.main_character.player_quote_key]['quote']}'""")

            print("""""")
            print("""A smile creeps on your face without you realizing it.""")
            print(f"""{self.supporting_characters[1]} says:
            It must be a good quote if the new person likes it! I'll use it. 
            Are you going to the after worldview-club dinner party tonight?  Everyone is invited!""")

        print("""Do you wish to go to the dinner party? (Y/N)""")
        yes: bool = self.player_yn_to_bool()
        if yes:
            print(f"""
            {self.supporting_characters[1]} says, 'Delightful, it starts at 7! See you there!'
            """)

        else:
            print("""
            You reply, 'It's been a long day, and I don't know where I am. I should.....'
            """)
            time.sleep(1)
            print(f"""
            Before you can think of where you should be or what you should be doing,
            {self.supporting_characters[0]} butts in,""")
            self.transition_as_typewriter(f"""
            'You look so lost, this will be the thing to lift your spirits! 
            When I first came here, it was important to listen to new ideas and make friends.
            Plus there will be plenty of people who want to talk about {quotes[self.main_character.player_quote_key]["author"]}!
            """)
            print(f"""Unable to come up with another excuse and thinking of {quotes[self.main_character.player_quote_key]["author"]},
            you agree to go for only an hour.
            """)
