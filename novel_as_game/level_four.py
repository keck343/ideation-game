from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition, play_loop, play_button, \
    chains_line, fence_void, floating_heart_ghost
from world_sectors_camps import BeitSector, GimelSector
import time


class ChapterFour(LevelofStory):
    number = 4

    def events(self):
        # from level three friend type can be "alt-believer", "believer", or "contrarian"
        starting_camp, friend_type, desired_product = self.starting_point

        if starting_camp == "Beit":
            chapter_sector = BeitSector
            alt_sector = GimelSector
        else:
            chapter_sector = GimelSector
            alt_sector = BeitSector

        chapter_camp = chapter_sector.camps[0]
        alt_camp = alt_sector.camps[0]

        if friend_type == "alt-believer":
            bonding: str = """your mutual distrust in the first camp you visited.
            You feel so relieved you escaped there and can't imagine having stayed."""
        elif friend_type == "believer":
            bonding: str = """your shared work towards a common goal.
            It feels comforting to be doing something concrete amid the chaos.
            """
        else:
            bonding: str = """your numerous late night debates.
            It feels comforting to have real discussions and gain a better understanding of this world.
            """

        print(f"""A few weeks have passed and you have enjoyed getting to know your friend.
                You have bonded over {bonding}""")
        print(play_loop*4)
        print("""Just when you had settled into a routine,
        one morning you awake to blaring siren.""")
        growing_symbol_transition(symbol=chains_line, num_lines=3)
        print("""You are bombarded with the news. 
        Do you read the headline? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print(f"""You are surrounded by the headline:
        {chapter_camp.initial_crisis_headline}""")

        print("""You rush to find your friend.""")
        if friend_type != "alt-believer":
            print(f"""Your friend rushes over to you and hands you a {desired_product}, saying
            Here have the last {desired_product}, it may be a long time before we get more.""")
        else:
            print("""Your friend rushes over to you, looking scared.""")
        growing_symbol_transition(symbol=f"( //>///<//)", num_lines=3)

        print("""Do you ask your friend what is going on? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print("""You ask your friend what's going on.  Surely they must know.""")
            print(f"""Your friend shakes their head and explains:
            {chapter_camp.initial_crisis_explanation}""")
            print("""Another person chimes in, Attention is all you need.""")

            growing_symbol_transition(symbol=f"( //>///<//)", num_lines=2)
            print("""You ask, surely there must be a way to survive without Attention?
            Your friend shakes their head like you are insane.""")
            growing_symbol_transition(symbol=f"( //>///<//)", num_lines=1)

        print("""Do you want to stay with your friend to figure out what to do? (Y/N)""")
        yes = self.player_yn_to_bool()
        if not yes:
            print("""
            You turn away from your friend, doubting the person you have formed a bond with.
            Unsure what to do, you walk to the edge of the camp.
            """)
            # meet up with other dinner party guest
            # they offer you your desired_product
            print("""You did not realize how far you've wondered when you see the fence at the edge of camp.""")
            print(fence_void)
            if friend_type == "alt-believer":
                print(f"""You see the person from your old camp.  You feel embarrassed, 
                 but before you turn away they call out:
                Sorry about earlier, I was having an off day! I found you a {desired_product}.""")
                growing_symbol_transition(symbol="(๑'ᵕ'๑)⸝*", num_lines=2)
                print(f"""You smile and thank them for finding a {desired_product}.""")
                growing_symbol_transition(symbol="(๑'ᵕ'๑)⸝*", num_lines=2)
                say_next: str = " next"
            else:
                print("""You see the other guest from the dinner party that feels so long ago.""")
                say_next: str = ""

            print(f"""Feeling a little unsure what to say{say_next}, you ask them if they've heard the news.
            
            """)
            print("""They nod, saying
            I can't believe we are living through these times.  All our camps survive on Attention.

            """)
            print("""You nod saying, I wish I knew what to do about it.""")
            growing_symbol_transition(symbol="｡°(°¯᷄◠¯᷅°)°｡", num_lines=2)
            print("""They say, 
            Our camp is working to figure out what to do.  
            Would you like to come back and we can figure it out together?""")
            print("""Do you accept their invitation? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print(fence_void)
                print("""You cross over the fence, relieved to be elsewhere.""")
                alt_sector, chapter_sector = chapter_sector, alt_sector
                alt_camp, chapter_camp = chapter_camp, alt_camp
            else:
                print("""You thank them for the offer, but decline.""")
                print("""They wish you luck because you'll both need it.""")
                print(fence_void)
                print("""You turn back towards the center of camp, determined to figure this out.
                You see your friend and they smile at you.
                You ask simply, What do we do? 
                """)

        else:
            print("""You apologize for asking a silly question.
            You ask simply, What do we do? 
            """)

        print("""
        Come, they say, let's find the others and brainstorm what to do.
        """)
        print("""As you approach the meeting place, you see everyone is holding a brochure.""")
        print(floating_heart_ghost)
        # TO DO: maybe use a different word than comrade?
        print(f"""A comrade is handing out brochures and calling everyone from this sector to come together
         {chapter_camp.brochure_summary}""")
        print("""
        They offer your friend and you a brochure.  You both take one to not be rude.""")
        print("""Do you read the brochure? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print(f"""You pick up the brochure, and notice the headline.
            Turning to your friend, you ask:
            But the headline is '{chapter_sector.brochure_tagline}'""")
            growing_symbol_transition(symbol=play_button, num_lines=2)
            print("""Your friend shrugs saying,
            It's basically the same thing.""")
            print("""Do you agree that they basically say the same thing? (Y/N)""")
            yes = self.player_yn_to_bool()
            if not yes:
                print("""Why? Type your answer below.""")
                response = input()
                self.main_character.expand_idea(response)
                print("""Before you have a chance to question the differences,""")

        print("""Your friend asks when the conference is. The comrade replies, 
        Tomorrow! There's a call for volunteers, but they have to wake up at dawn.""")
        print("""Do you ask if they are going to volunteer? (Y/N)""")
        yes = self.player_yn_to_bool()
        if yes:
            print("""You ask if they are going to volunteer.
            They say they will be leaving a dawn to volunteer and ask if you'd like to join them.""")
            print("""Do you wish to volunteer with them? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print("""Your friend agrees to volunteer as well.  
                You all decide to retire for the night so you will be awake at dawn.""")
                return self.main_character, chapter_sector.name, "volunteer"
            else:
                print("""You decline.  The other person excuses themselves 
                as they will have a very busy day tomorrow.""")
                print("""As soon as they leave you friend turns to you and says,
                What a nerd! But still do you think we should go to this conference?""")
                print("""Do you agree to go to the conference? (Y/N)""")
                yes = self.player_yn_to_bool()
                if yes:
                    print("""You are relieved your friend does not think less of you.
                    Yes, you say, let's go to the conference at a reasonable hour.""")
                    print("""Relieved to be doing something, you and your friend retire for the evening.""")
                    return self.main_character, chapter_sector.name, "attend"
                else:
                    print("""Why do you not want to attend the conference? 
                     Type your answer below.""")
                    response = input()
                    self.main_character.expand_idea(response)
                    print(f"""No thank-you, you reply, I think
                    {response}""")
                    print("""Too bad, your friend replies, I guess we will see what tomorrow brings.""")
                    return self.main_character, chapter_sector.name, "skip"
        else:
            print("""The other person excuses themselves 
                            as they will have a very busy day tomorrow.""")
            print("""As soon as they leave you friend turns to you and says,
                            Do you think we should go to this conference?""")
            print("""Do you agree to go to the conference? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print("""Yes, you say, let's go to the conference at a reasonable hour.""")
                print("""Relieved to be doing something, you and your friend retire for the evening.""")
                return self.main_character, chapter_sector.name, "attend"
            else:
                print("""Why do you not want to attend the conference? 
                                     Type your answer below.""")
                response = input()
                self.main_character.expand_idea(response)
                print(f"""No thank-you, you reply, I think
                                    {response}""")
                print("""Too bad, your friend replies, I guess we will see what tomorrow brings.""")
                return self.main_character, chapter_sector.name, "skip"
