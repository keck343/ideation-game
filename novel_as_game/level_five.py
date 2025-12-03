from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition, gamer, coffee, play_loop, watch_fence_void, moving_truck
from world_sectors_camps import BeitSector, GimelSector
import random
import time


class ChapterFive(LevelofStory):
    number = 5

    def events(self):
        # from level four attendance can be "skip", "attend" or "volunteer"
        starting_camp, attendance = self.starting_point

        if starting_camp == "Beit":
            chapter_sector = BeitSector
            alt_sector = GimelSector
        else:
            chapter_sector = GimelSector
            alt_sector = BeitSector

        chapter_camp = chapter_sector.camps[0]
        alt_camp = alt_sector.camps[0]
        change_sectors: bool = False

        if attendance == "volunteer":
            print("""You arise bright and early at the crack of dawn.  
            Ready to volunteer you get dressed, brush your teeth and grab your bag.""")
            print(gamer)
            print("""But your friend is no where to be found.  You go looking for them,
            only to find them asleep in their bed.""")
            print("""Do you wake them? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print("""You shake your friend gentle for a few minutes,
                but then gradually increase the vigor of your shakes until they awake dazed and confused.""")
                print("""You tell them that if we are going to make it in time to volunteer they have to get up.""")
                print("""They tell you to go ahead and they'll try to catch up.""")
                print("""Do you still go early to volunteer? (Y/N)""")
                attend_yes = self.player_yn_to_bool()
            else:
                print("""You decide to let your friend sleep and catch the bus to the conference.""")
                attend_yes = True
            if attend_yes:
                print(coffee)
                print("""You make it to the conference early and are assigned to set up chairs.""")
                print("""While setting out chairs you chat with the other volunteers 
                and learn that there are at least four other major camps in your sector.""")
                print(play_loop)
                print(f"""The others call your camp {chapter_camp.known_name},
                though the people in your camp don't like that name. 
                """)
                print(f"""One of the other volunteers explains that your camps does believe that
                {chapter_camp.stated_camp_core_belief},
                but not so hidden underneath that is the belief that
                {chapter_camp.unstated_camp_core_belief}
                """)
                print("""Do you think this is an accurate assessment of your camps beliefs? (Y/N)""")
                yes_assessment = self.player_yn_to_bool()
                if yes_assessment:
                    print("""You feel relieved that someone said out loud what you suspected all along.""")
                    print("""Do you ask the other volunteers about their camps beliefs? (Y/N)""")
                    yes_other_camps = self.player_yn_to_bool()
                else:
                    print("""What do you think? Complete the sentence:
                    My camp believes... """)
                    response = input()
                    print(f"""You tell them that your camp believes {response}""")
                    print("""Another volunteer asks if that's your belief. 
                    Is your camp's beliefs your beliefs? (Y/N)""")
                    yes_beliefs = self.player_yn_to_bool()
                    if yes_beliefs:
                        self.main_character.expand_idea(response)
                        print("""You say proudly that it is.  
                        Everyone returns to setting up chairs.""")
                        yes_other_camps = False
                    else:
                        print("""You say it's not what you believe, but what you've observed.
                        Another volunteer says there's often a lot of confusion about what their camp believes.""")
                        print("""Do you ask the other volunteers about their camps beliefs? (Y/N)""")
                        yes_other_camps = self.player_yn_to_bool()
                if yes_other_camps:
                    chapter_sector.tell_camps_beliefs(speaker_title="volunteer", stated_and_unstated=True)
                    print("""Overwhelmed with information you say you need to go to the bathroom,
                    but really just want an excuse to wonder outside.""")
                    print("""As you wonder, you see a different kind of fence and a flurry of activity behind it.""")
                    print(watch_fence_void)
                    print("Do you go up to the fence? (Y/N)")
                    yes = self.player_yn_to_bool()
                    if yes:
                        print("""Someone from the other fence waves at you.  
                        It's rare to catch glimpses of people from other sectors, they say.
                        Would you like to join our conference?""")
                        print(""" How do you respond?
                        
                        a. Say yes
                        b. Politely decline
                        c. Decline denouncing their sector
                        d. Ask what the difference between their conference and your conference is
                        e. Run away
                        
                        Type 'a' 'b' 'c' 'd' or 'e' to make your choice.
                        """)
                        choice: str = self.player_multi_choice(['a', 'b', 'c', 'd', 'e'])

                        if choice == 'a':
                            change_sectors: bool = True
                        elif choice == 'e':
                            print("""You run back to the conference just in time to hear the first speakers.""")
                        elif choice == 'b':
                            print("""You thank them for their offer, but must go back to setting up chairs.
                            They wish you luck at your conference and you wish them luck at theirs.
                            You return to the conference just as it's getting started.""")
                        elif choice == 'c':
                            print(f"""You tell them that it {chapter_sector.core_belief}
                            They scoff and call you a bigot.
                            Having said your piece, you return to the conference just as it's getting started.""")
                        else:
                            print("""You ask what the difference between the conferences is.""")
                            print(f"""They respond, while there's some controversy essentially 
                            _your_ conference believes {chapter_sector.core_belief}
                            But _our_ conference believes {alt_sector.core_belief}.""")
                            print("""They ask you what you think and which conference you want to be at.
                            """)
                            print("""How do you respond?
                            
                            a. My conference's belief resonates with me, so I will stay
                            b. Your conference's belief resonates with me, so I will switch conferences
                            c. I must fulfil my volunteer duties and meet my friend, so I will stay
                            
                            Type 'a' 'b' or 'c' to make your choice.
                            """)
                            next_choice = self.player_multi_choice(['a', 'b', 'c'])
                            if next_choice == 'b':
                                change_sectors: bool = True
                            elif next_choice == 'c':
                                print("""You thank them for their offer, but must go back to setting up chairs.""")

                            if next_choice != 'b':
                                print("""They wish you luck at your conference and you wish them luck at theirs.
                                       You return to the conference just as it's getting started.""")

                        if change_sectors:
                            print("""You cross over the fence, wondering what this new conference will be like.""")
                            alt_sector, chapter_sector = chapter_sector, alt_sector
                            alt_camp, chapter_camp = chapter_camp, alt_camp

        if attendance != "skip":
            print("""You feel mildly overwhelmed at the number of people, but take your seat to hear the speakers.""")
            print("""Each camp at the conference gets a session, do you want to stay for all sessions? (Y/N)""")
            all_sessions_yes = self.player_yn_to_bool()
            if all_sessions_yes:
                chapter_sector.tell_camps_beliefs(speaker_title="speaker", stated_and_unstated=False)
                conference_camps = chapter_sector.camps[1:]
                print("""You feel full of knowledge and mildly overwhelemed.""")
            else:
                print("""You skip in and out of the conference and catch a couple speakers.""")
                conference_camps = random.sample(chapter_sector.camps[1:], 2)
                print(f"""You heard one speaker from the co-called {conference_camps[0].known_name} camp
                say that their camp believes {conference_camps[0].stated_camp_core_belief}""")
                print(f"""You heard one speaker from the co-called {conference_camps[1].known_name} camp
                say that their camp believes {conference_camps[1].stated_camp_core_belief}""")

            if not change_sectors:
                print(f"""Do you want to find your friend and discuss the sessions you heard? (Y/N)""")
                find_yes = self.player_yn_to_bool()
                if find_yes:
                    print("""You find your friend and they apologize for oversleeping 
                    and ask you if made it in time to volunteer.""")
                    if attendance == "volunteer":
                        print("""You say you made it and helped with the chairs, 
                        and ask what they thought of the conference.""")
                    else:
                        print("""You shrug and admit you went back to sleep, 
                        and ask what they thought of the conference.""")
            else:
                print("""You have the urge to find your friend, but realize they wouldn't be at this sectors conference.
                Do you want to search for the person who invited you? (Y/N)""")
                find_yes = self.player_yn_to_bool()

                if find_yes:
                    print("""You find them in the tabling area and ask what they thought of the speakers.""")

            if find_yes:
                if change_sectors:
                    person_camp = chapter_sector.camps[-1]
                else:
                    person_camp = chapter_camp

                print(f"""They say that they thought while everyone's heart was in a good place,
                the only one that made any sense was the one who talked about
                {person_camp.stated_camp_core_belief}.""")

                print("""You smile and nod, but find yourself wondering about what the other speakers said.
                
                """)
            growing_symbol_transition("√♥-√v--√♥-√v–", num_lines=3)

        if attendance == "skip":
            print("""You wake up to another day in the new low-Attention normal. 
            
            What do you want to with your day?
            
            a. Your own research at the camp's Library
            b. Read a novel
            c. Find a way of being in service
            
            Type 'a', 'b' or 'c'
            """)
            choice = self.player_multi_choice(['a', 'b', 'c'])
            if choice == 'a':
                print(f"""After hours of pouring over old newspaper archives, 
                you feel that between all the lines the articles are saying:
                {chapter_camp.stated_camp_core_belief} and
                {chapter_camp.counter_sector_statement}""")
                print(watch_fence_void)
            elif choice == "b":
                print("""You find a novel and quite enjoy reading it.""")
            else:
                print("""You find a group of people cutting up more pamphlets and handing out supplies.
                It feels satisfying to be doing some concrete.""")

            growing_symbol_transition(num_lines=5)
            print("""Just as you are about to take a lunch break, more headlines come in.""")
            print("""Do you look at the headlines? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print(f"""The headlines read:
                {chapter_camp.second_crisis_explanation}""")
                print(coffee)
                print("""You are about to eat your lunch when you see your friend depart for the conference. 
                
                Do you chase after them? (Y/N)""")
                yes = self.player_yn_to_bool()
                if not yes:
                    print("""You turn away to return to your lunch.""")
                    saw_news: bool = True
                    return self.main_character, chapter_sector, chapter_camp, saw_news
                else:
                    print("""You chase after them and just catch the last bus before it departs.
                    You arrive at the conference after the speakers have finished.""")
                    conference_camps = []
            else:
                print("""You turn away to return to your lunch.""")
                saw_news: bool = False
                return self.main_character, chapter_sector, chapter_camp, saw_news

        print("""You wonder through the tabling area and wonder how this Attention 
        is an important as everyone says and about where you've been sleeping this whole time.""")

        print("""Headlines come raining in saying: 
        Attention drops even further, 10 more reported dead.""")
        saw_news: bool = True
        growing_symbol_transition(num_lines=4)

        print("""The people tabling look frightened and begin packing up. 
        Contemplating your next move, you realize there there are buses headed back to all the camps.""")
        if not change_sectors:
            print("""Where do you want to take a bus to? 
            
            a. back to your camp
            b. go to a new camp
            
            Type 'a' or 'b'.""")
            choice = self.player_multi_choice(['a', 'b'])
            if choice == 'a':
                print("""You take the bus back to your camp.""")
                return self.main_character, chapter_sector, chapter_camp, saw_news
        # else:
        if len(conference_camps) > 0:
            print("""Which camp do you want to take the bus back to?
            
            """)
            count = 0
            for camp in conference_camps:
                count += 1
                print(f"""{count}. Camp known as {camp.known_name}""")

            if len(conference_camps) + 1 != len(chapter_sector.camps):
                count += 1
                print(f"""{count}. A camp you've never heard of.""")

            print(f"""Type '{"', '".join([str(x) for x in range(1, count)])}' or '{count}'""")
            camp_choice = self.player_multi_choice([str(x) for x in range(1, count+1)])

            print("""You catch the bus and wonder what awaits you in this new camp.""")
            print(moving_truck)

            next_camp = chapter_sector.camps[int(camp_choice)]

            return self.main_character, chapter_sector, next_camp, saw_news
        else:
            print("""Not knowing what any of the camps are, you pick a bus at random.""")
            print(moving_truck)
            next_camp = random.choice(chapter_sector.camps[1:])
            return self.main_character, chapter_sector, next_camp, saw_news


    ## if skip, hear next level of news and chance to catch last speaker (from last added camp)
    ## if still skip go to next level in same camp


    ## if hear statements of camp then get to choose which camp you depart with from all camps (and possibly to switch sector?)
    ## otherwise get choice between staying with your current camp or a random other camp

