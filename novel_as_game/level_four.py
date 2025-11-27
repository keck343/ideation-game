from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition, play_loop, chains_line
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
        growing_symbol_transition(symbol=play_loop, num_lines=3)
        print("""Just when you had settled into a routine,
        one morning you awake to blaring siren.""")
        growing_symbol_transition(symbol=chains_line, num_lines=3)
        print(f"""You are surrounded by the headline:
        {chapter_camp.initial_crisis_headline}""")
        print("""You rush to find your friend.""")
        if friend_type == "alt-believer":
            print(f"""Your friend rushes over to you and hands you a {desired_product}, saying
            Here have the last {desired_product}, it may be a long time before we get more.""")
        else:
            print("""Your friend rushes over to you, looking scared.""")
        growing_symbol_transition(symbol=f"( //>///<//)", num_lines=3)

        print("""You ask your friend what's going on.  Surely they must know.""")
        print(f"""Your friend shakes their head and explains:
        {chapter_camp.initial_crisis_explanation}""")
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

            # you have another choice to switch camps
            # alt_camp and chapter_camp switch
        else:
            print("""You apologize for asking a silly question.
            You ask simply, What do we do? 
            """)

        print("""
        Come, they say, let's find the others and brainstorm what to do.
        """)

        ## join others in your camp and get invitation to conference
        # next round there will be even more beings gone -- crisis continued as conference was organized

