from chapter_structure import LevelofStory
from text_graphics import growing_symbol_transition, penguins_and_skull, fence_void, lock_and_key
from world_sectors_camps import BeitSector, GimelSector
import time


class ChapterThree(LevelofStory):
    number = 3

    def events(self):
        # return next camp name and either "contrarian" or "believer" to indicate the type of friend you've made
        if self.starting_point == "Beit":
            chapter_sector = BeitSector
            alt_sector = GimelSector
        else:
            chapter_sector = GimelSector
            alt_sector = BeitSector

        chapter_camp = chapter_sector.camps[0]
        alt_camp = alt_sector.camps[0]

        print("""
        You wake up for a fresh day in your new camp, relieved to have escaped nonexistence even for just a night.
        """)
        print(penguins_and_skull)

        print("""Not totally sure what to make of this new day, you set out to find caffeine. 
        
        Which form of caffeine do you crave today?
        
        a. Coffee
        b. Tea
        c. Caffeinated Gum
        d. No need for stimulants - Refreshing Sparkling Water
        
        Type 'a' 'b' 'c' or 'd' to make your choice.
        """)

        choice: str = self.player_multi_choice(['a', 'b', 'c', 'd'])
        if choice == 'a':
            desired_product = "coffee"
        elif choice == 'b':
            desired_product = "tea"
        elif choice == 'c':
            desired_product = "caffeinated gum"
        elif choice == 'd':
            desired_product = "sparkling water"
        else:
            desired_product = "XL dunkin donuts iced coffee"

        print(f"""You see the embodiment form the party. 
        Hoping they will continue to be a good host, you walk over and inquire, 
        Do you know where I could find a {desired_product}?""")
        print("(｡ᵕ ◞ _◟)")
        print(f"""They look up at you with a grim face.
        You really haven't been around much have you?
        There hasn't been {desired_product} in many cycles.
        I guess you did conclude quote: '{self.main_character.description}' """)

        print(f"""They scoff. 
        Come, let's meet with the others to figure out what do about the lack of {desired_product} these days.""")

        print("""
        Do you follow them to meet with the others? (Y/N)
        """)
        yes = self.player_yn_to_bool()
        if not yes:
            print("""Annoyed by their arrogance, you wonder in the opposite direction.  
            You begin to see the edge of the camp emerge, with a fence unlike any you've ever seen.
            """)
            time.sleep(1)
            print(fence_void)

            print("""It feels impenetrable, yet you can see 
            the other party guest on the other side and wave at them.""")
            print("""(っᵔ◡ᵔ)っ""")
            print(f"""They wave back and ask, 
            how is '{self.main_character.description}' going for you?""")

            print("""In response do you:
            a. tear up silently
            b. express your frustration
            c. lash out at them for mocking you
            
            Type 'a' 'b' or 'c' to make your choice.
            """)

            alt_mock_choice: str = self.player_multi_choice(['a', 'b', 'c'])
            if alt_mock_choice == 'a':
                print("""They say, I totally understand, 
                everyone is feeling it these days and no one is what they seem.
                Would you like to come to my camp?""")
                print(fence_void)
                print("""Would you like to go with them? (Y/N)""")
                yes = self.player_yn_to_bool()
                if yes:
                    print("""You wipe the tears from your face and nod.  
                    You both smile, and without even knowing how you cross the threshold.""")
                    return alt_camp.known_name, "believer"
                else:
                    print("""You wipe the tears from your face and say:
                    Thank you for your offer, but there's been too much change lately 
                    and I'm going to try to stick it out here.""")
                    growing_symbol_transition("^")
                    print("""They wish you luck and take their leave.""")
                    # TO DO: add choice here
                    print("""Resigned to make things work, you turn back towards the others.""")

            if alt_mock_choice == 'b':
                print("""You turn to them and say exasperatedly:
                How do you know what you're talking about?!? 
                How do any of us know what we are talking about?!""")
                print(f"""They retort: 
                {alt_camp.counter_sector_statement}""")
                print("""Do you apologize? (Y/N)""")
                yes = self.player_yn_to_bool()
                if yes:
                    print(f"""You say, I'm sorry, it's been a confusing morning, 
                    and I really just needed a {desired_product}.""")
                    print("""They nod, I totally understand.  Would you like a break from all this?  
                    Do you want to come to my camp?""")
                    print(fence_void)
                    print("""Would you like to go with them? (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if yes:
                        print("""Without even knowing how you cross the threshold.""")
                        return alt_camp.known_name, "believer"
                    else:
                        print("""You say:
                        Thank you for your offer, but there's been too much change lately 
                        and I'm going to try to stick it out here.""")
                        growing_symbol_transition("^")
                        print("""They wish you luck and take their leave.""")
                        # TO DO: add choice here
                        print("""Resigned to make things work, you turn back towards the others.""")

            if alt_mock_choice == 'c':
                print("""You turn to them and say exasperatedly:
                How do you know what you're talking about?!? 
                You're such an arrogant prick!""")
                print(f"""They look at you exacerbated.  
                Do you really want to condemn yourself to a camp without {desired_product}?""")
                print(f"""How do you know I like {desired_product}?""")
                print("""Walls are thin, they laugh.  
                Maybe when you've come to your senses you'll want to pass through them.""")
                print("""Determined to prove them wrong, you say nothing and turn back towards the others.""")

            # unless level is already exited, one way or another you turn towards the others in the camp
            print("""As you walk towards the others, you see many people fluttering around 
            with different diagrams, charts, and statistics.""")
            growing_symbol_transition(symbol="(╯ ͠° ͟ʖ ͡°)╯┻━┻", num_lines=3)
            print("""Someone turns to you, clutching their diagrams close to their chest.  They implore you,
            What is to be done? 
            """)
            if self.starting_point == "Gimel":
                lenin_opinion = "no "
            else:
                lenin_opinion = ""
            print(f"""Another person turns to them whispering,
            Don't be like that Komunisto! Died at 53 in a coma and for {lenin_opinion}good reason.""")
            print("""They clutch their diagrams closer to their chest, fear in their eyes.""")
            growing_symbol_transition(symbol="┻━┻(╯ ͠° ͟ʖ ͡°)╯", num_lines=3)
            print("""Emerging out of the chaos, one person climbs on a chairs and clears their throat.
            The stirring begins to die down as people turn towards them.""")
            print("""They begin to address the crowd.
            
            Fellow camp members, these are unprecedented times.
            We can not even eat breakfast as we used to.
            Where has all the coffee, tea, and sparkling water gone?
            What will become of our way of life?
            """)
            growing_symbol_transition(symbol="ᕙ(  •̀ ᗜ •́  )ᕗ", num_lines=3)
            print(f"""
            But fear not, we know that {chapter_camp.summary_statement}
            """)
            print("""The crowd cheers.""")
            print(lock_and_key)
            print("""Do you cheer with the crowd? (Y/N)""")
            yes = self.player_yn_to_bool()
            if yes:
                print("""Unsure if you believe the speaker or this is just the wisest thing to do,
                you join the crowd cheering.""")
                print("""The speaker clears his throat.  
                Fellow comrades, let's get to work!""")
                print("""Unsure of what to do, you look around anxiously.  
                As your eyes complete their dart around the room, someone gestures at you to come over.""")
                print("""Do you go over to them? (Y/N)""")
                yes = self.player_yn_to_bool()
                if yes:
                    print("""You walk over to the person gesturing you.
                    They smile and invite you to help them cut up pamphlets.""")
                    print("""You inquire what the pamphlets are for.
                    They respond, 
                    Excellent Question!""")
                    print("(´｡• ◡ •｡`) ♡")
                    time.sleep(0.5)
                    print(f"""{chapter_camp.pamphlet_slogans[0]}""")
                    print(f"""Do you ask why the group must 
                    '{chapter_camp.pamphlet_slogans[0]}'?
                    (Y/N)""")
                    yes = self.player_yn_to_bool()
                    if yes:
                        print(f"""They seem less excited at your second question, and continue:
                        Well of course, {chapter_camp.pamphlet_slogans[1]} """)
                        print("""You smile uneasily and point out that they are just reading what the pamphlet says.""")
                        print("∘ ∘ ∘ ( °ヮ° )")
                        print("""Another person interjects:
                        Some people can only just read the propaganda.  
                        Why don't we have an actual discussion over here?
                        """)
                        print(".·°՞(ᗒ□ᗕ)՞°·.")
                        print("""You smile and follow them to their workbench.""")
                        return chapter_camp.known_name, "contrarian"

                    else:
                        print("""You smile and begin helping them cut pamphlets.""")
                        print("""ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ""")
                        print("""As you settle into a rhythm with cutting, 
                        you began to feel more at ease with your surroundings and companion.""")
                        print("""ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ""")
                        print("""Pleasant conversation ensues and you feel less alone with a new friend.""")
                        print("""ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ""")
                        return chapter_camp.known_name, "believer"

            else:
                print("""You do not join in and feel uneasy surrounded by so many people 
                who would just go along with generic statements.""")
                growing_symbol_transition("(๑•́ -•̀)", num_lines=3)
                print("""As you are about to despair, you turn around to see someone else who is also not clapping.""")
                growing_symbol_transition("(๑•́ -•̀)", num_lines=2)
                print("""They spot you and you relief wash over their face. They walk over towards you.
                You smile as they approach.
                (๑•́(੭˃ᴗ˂)੭•̀)""")
                print("""ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ""")
                print("""They invite you to get out of here and find a better part of camp.
                You smile and follow them.""")
                print("""ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ""")
                return chapter_camp.known_name, "contrarian"
































