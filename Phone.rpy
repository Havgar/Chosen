default Stacyhookupcall = False
define persistent.School = False
define persistent.Home = False
default dildo = False
define julyfirsttext = False




label Profile:

    menu:

        "Change your title":
            $ povtitle = renpy.input("{size=+1}{font=Charm-Bold.ttf}You can pick a title to be called, or just retype your name. What'll it be?{/font}{/size}", length = 32)

            $ persistent.povtitle = povtitle

            hide screen Phone
            if persistent.School:
                jump school
            elif persistent.Home:
                jump home




        "Change the relations to characters":

            $ Jenniferrelation = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your relation with Jennifer?{/font}{/size} (Default is Sister/Roommate)", length = 32)

            $ persistent.Jenniferrelation = Jenniferrelation

            $ Carolinerelation = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your relation with Caroline?{/font}{/size} (Default is Mom/Landlord)", length = 32)

            $ persistent.Carolinerelation = Carolinerelation

            $ Hannahrelation = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your relation with Hannah?{/font}{/size} (Default is Aunt/Roommate)", length = 32)

            $ persistent.Hannahrelation = Hannahrelation

            hide screen Phone
            if persistent.School:
                jump school
            elif persistent.Home:
                jump home

        "Change your name":
            $ povname = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your name mortal?{/font}{/size}", length = 32)

            $ persistent.povname = povname

            hide screen Phone
            if persistent.School:
                jump school
            elif persistent.Home:
                jump home


        "Display your statistics":

            "You have [dollars] dollars and [favor] favor"
            "You are level [level]"
            if level == 1:
                "You have [exp] points of experience,
                For the next level you need to have 250 exp."
            if level == 2:
                "You have [exp] points of experience,
                For the next level you need to have 500 exp."
            if level == 3:
                "You have [exp] points of experience,
                For the next level you need to have 1000 exp."
            if level == 4:
                "You have [exp] points of experience,
                For the next level you need to have 2000 exp."
            hide screen Phone
            if persistent.School:
                jump school
            elif persistent.Home:
                jump home









label Message:
    menu:
        "Message Stacy":
            if clock.weekday == "Monday" or clock.weekday == "Tuesday" or clock.weekday == "Wednesday" or clock.weekday == "Thursday" or clock.weekday == "Friday":
                if stacyintro == True:
                    if clock.time == "Morning" or clock.time == "Noon":
                        jump Stacyintro
                    else:
                        jump Stacylateintro
                elif stacyintro == False:
                    if clock.time == "Morning" or clock.time == "Noon":
                        jump Stacyhookup
                    else:
                        jump Stacylate
            else:
                jump Stacyweekend
        "Message July" if julyfirsttext == True:
            jump Julyfirsttext
        #"Message July" if meetjuly == True:
            #elif clock.weekday == "Monday" or clock.weekday == "Tuesday" or clock.weekday == "Wednesday" or clock.weekday == "Thursday" or clock.weekday == "Friday":
            #    if julyintro == True:
            #        if clock.time == "Morning" or clock.time == "Noon":
            #            call Julyintro
            #        else:
            #            jump Julylateintro
            #    else:
            #        if clock.time == "Morning" or clock.time == "Noon":
            #            jump Julyhookup
            #        else:
            #            jump Julylate

            #else:
            #    jump Julyweekend
        "Return":
            if persistent.School:
                hide screen Phone
                jump school
            elif persistent.Home:
                hide screen Phone
                jump home

    if persistent.School:
        hide screen Phone
        jump school
    elif persistent.Home:
        hide screen Phone
        jump home










label Navigation:
    menu:
        "Go to school":
            hide screen Phone
            jump school
        "Go to your home":
            hide screen Phone
            jump home
        "Return":
            if persistent.School:
                jump school
            elif persistent.Home:
                jump home





label Stacylate:

    hide screen Phone

    povname "Hey, wanna meet up again?"

    "Stacy" "No sorry, its too late. Hit me up tommorrow."

    if persistent.School:
        jump school
    elif persistent.Home:
        jump home


label Stacylateintro:

    hide screen Phone

    povname "Hey Stacy, i have something important to tell you, can we meet in the boys restroom?"

    "Stacy" "No sorry, its too late. Hit me up tommorrow."


    if persistent.School:
        jump school
    elif persistent.Home:
        jump home




label Stacyintro:

    hide screen Phone

    povname "Hey Stacy, i have something important to tell you, can we meet in the boys restroom?"

    "Stacy" "Yeah, sure [povname] I'll be there in 5 minutes."

    povname "(Okay, now all i have to do is use the mark.)"

    $ stacypower = True

    $ Quest1 = False

    $ Quest2 = True

    if persistent.School:
        jump school
    elif persistent.Home:
        jump home


label Stacyhookup:

    hide screen Phone

    povname "Hey, wanna meet up again?"

    "Stacy" "Of course [povname], You always text me at the right time."

    "Stacy" "Ughhh, i can't wait, hurry up [povname]!"

    $ Stacyhookupcall = True


    if persistent.School:
        jump school
    elif persistent.Home:
        jump home

label Stacyweekend:

    hide screen Phone

    povname "Hey, wanna meet up again?"

    "Stacy" "No I can't, sorry [povname]."

    "Stacy" "Buuut, we can have some fun after the weekend."

    povname "Sure!"

    "Stacy" "Text me after saturday whenever You're ready."


    if persistent.School:
        jump school
    elif persistent.Home:
        jump home

screen Shop:
    image "gui/store.png"



    if kitsuneears == False:
        imagebutton:
            xalign 0.402
            yalign 0.295
            auto "gui/kitsuneears_%s.png"
            if dollars >= 120:
               action Jump("Boughtkitsuneears")
            else:
               action Jump("NoMoney")

    elif kitsuneears == True:
        image "gui/kitsuneears_bought.png"

    if dildo == 0:
         imagebutton:
            xalign 0.209
            yalign 0.3
            auto "gui/dildo_%s.png"
            if dollars >= 80:
                action Jump("Boughtdildo")
            else:
                action Jump("NoMoney")



    elif dildo >= 0:
        image "gui/dildo_bought.png"
    imagebutton:
        yalign 0.87
        xalign 0.5

        auto "gui/return.shop_%s.png"
        if persistent.Home:
            action Hide("Shop"), Jump ("home")
        elif persistent.School:
            action Hide("Shop"), Jump ("school")
    text "{color=#000000}{size=+10}{font=CarroisGothic-Regular.ttf}[dollars]${/font}{/size}{/color}":
        yalign 0.132
        xalign 0.78

label Boughtdildo:

    "You bought a dildo for 80 dollars!"


    $ dildo += 1

    $ dollars -= 80

    hide screen Shop

    if persistent.School:
        jump school
    elif persistent.Home:
        jump home

label Boughtkitsuneears:

    "You bought kitsune ears for 120 dollars!"

    hide screen Shop

    $ kitsuneears = True

    $ dollars -= 120

    if persistent.School:
        jump school
    elif persistent.Home:
        jump home


label NoMoney:

    hide screen Shop

    "You don't have enough money"

    if persistent.School:
        jump school
    elif persistent.Home:
        jump home

label Julyfirsttext:

    povname "Hey July."

    July "Oh, hi [povname]!"

    July "Good job on making up with Jenny, I honestly don't know how you did that but I'm happy for you!"

    povname "Uhh, yeah thanks."

    July "Imagine if both of you started dating, Haha!"

    July "Just kidding..! It would be cute tho ^.^"

    povname "I don't think it would come to that, lol."

    July "Yeah, I don't think she even has enough money to do that."

    July "Do you need anything..? You texted me first for a reason."

    povname "Nahh, just wanted to say hi."

    July "Oh, okay. I wouldn't mind if we would hangout at my place when you have time ;)."

    povname "Yeah, I'll text you whenever im free."

    hide screen Phone

    povname "Huh, maybe Namaah's idea worked even better than i thought."

    povname "I might take up July on her offer, but first I should talk to Jennifer."

    $ Quest8 = False

    $ Quest9 = True

    $ julyfirsttext = False

    if persistent.School:
        jump school
    elif persistent.Home:
        jump home
