
default Quest2 = False
default Quest3 = False
default Quest4 = False
default Quest5 = False
default Quest6 = False
default Quest7 = False
default Quest8 = False
default Quest9 = False
default Quest10 = False
default Quest11 = False
default Quest12 = False
default Quest13 = False
default Quest14 = False
default Namaahfirstevercall = False
default Namaahtalk = False
default Jentalk = False


screen homeUI:

    image "gui.png"

    imagebutton:
        xalign 0.92
        yalign 0
        yoffset 22
        auto "Questbook_%s.png"


        if Quest1 == True:
            action Notify("Message Stacy")
        elif Quest2 == True:
            action Notify("Meet with Stacy in the school bathroom at noon/morning")
        elif Quest3 == True:
            action Notify("Talk to Namaah")
        elif Quest4 == True:
            action Notify("Talk to Jennifer in the evening")
        elif Quest5 == True:
            action Notify("Talk to Namaah")
        elif Quest6 == True:
            action Notify("Buy and give a dildo to Jennifer in the evening")
        elif Quest7 == True:
            action Notify("Talk to Namaah")
        elif Quest8 == True:
            action Notify("Message July")
        elif Quest9 == True:
            action Notify("Talk to Jennifer in the morning/noon during the weekend")
        elif Quest10 == True:
            action Notify("This is the end of the main content, be sure to explore all the optional though!")

    imagebutton:
        xalign 0.9845
        yalign 0
        yoffset 8
        auto "UI/Phonebutton_%s.png"
        action Show("Phone"), Hide("homeUI")

    imagebutton:
        xalign 0.005
        yalign -0.005
        yoffset 8
        auto "UI/Nav_%s.png"
        action Jump("Navigation")


    imagebutton:

        xalign 0.65
        yalign 0.7

        auto "gui/Rest_%s.png"




        action Function(clock.advance, 1), Jump("home")

    imagebutton:

        xalign 0.8
        yalign 0.7

        auto "gui/Sleep_%s.png"




        if clock.time == "Night":
            action Function(clock.advance, 1), Jump("home")
        if clock.time == "Evening":
            action Function(clock.advance, 2), Jump("home")
        if clock.time == "Noon":
            action Function(clock.advance, 3), Jump("home")
        if clock.time == "Morning":
            action Function(clock.advance, 4), Jump("home")









    if Namaahfirstevercall == True:
        imagebutton:
            auto "images/UI/Namaahbutton_%s.png"

            yalign 0.99


            if clock.time == "Noon" or clock.time == "Morning":
                action Jump("Namaahcall")
            else:
                action Jump("Namaahcallfail")
    hbox:

        yalign 0.09
        xalign 0.1
        if Jentalk == True:
            imagebutton:

                auto "images/UI/Jenroombutton_%s.png"


                action Jump("Jenroom")



    if Quest3 == True:
        imagebutton:
            auto "images/UI/Namaahbutton_%s.png"
            yalign 0.99
            action Jump("Namaahfirstcall")

    hbox:



        xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
        yalign .01 #change this value if you want to move it to a different part of the screen vertically

        text "{alpha=0.85}{size=+5}{font=Charm-Bold.ttf}[clock.weekday]{/font}{/size}{/alpha}":
            xoffset 240
            yoffset -8
            if clock.weekday == "Saturday":
                xoffset 230
            elif clock.weekday == "Wednesday":
                xoffset 210
            elif clock.weekday == "Thursday":
                xoffset 225
            elif clock.weekday == "Friday":
                xoffset 250
            elif clock.weekday == "Sunday":
                xoffset 245
            elif clock.weekday == "Tuesday":
                xoffset 235
    hbox:
        text "{alpha=0.85}{size=+5}{font=Charm-Bold.ttf}[clock.time]{/font}{/size}{/alpha}":
            xoffset 900
            yoffset 1

            if clock.time == "Noon":
                xoffset 555
            elif clock.time == "Night":
                xoffset 550
            elif clock.time == "Evening":
                xoffset 535
            elif clock.time == "Morning":
                xoffset 530

    hbox:

        text "{alpha=0.85}{size=-10}{font=Charm-Bold.ttf}Dollars = [dollars]{/font}{/size}{/alpha}":
            xoffset 750
            yoffset 0

    hbox:

        text "{alpha=0.85}{size=-10}{font=Charm-Bold.ttf}Favor = [favor]{/font}{/size}{/alpha}":
            xoffset 750
            yoffset 30

    hbox:

        text "{alpha=0.85}{size=+5}{font=Charm-Bold.ttf}Level = [level]{/font}{/size}{/alpha}":
            xoffset 1070
            yoffset 0




screen schoolUI:

    image "gui.png"


    if clock.time == "Morning" or clock.time == "Noon":
        if stacyintro == False:
            if clock.weekday == "Monday" or clock.weekday == "Thursday" or clock.weekday == "Sunday":
                imagebutton:
                    yalign 0.75
                    xalign 0.3
                    auto "UI/Lily_%s.png"
                    action Function(clock.advance, 1), Jump("Lilyschool")

            elif clock.weekday == "Wednesday" or clock.weekday == "Saturday":
                imagebutton:
                    yalign 0.7
                    xalign 0.35
                    auto "UI/Olivia_%s.png"
                    action Function(clock.advance, 1), Jump("Oliviaschool")

            elif clock.weekday == "Friday" or clock.weekday == "Tuesday":
                imagebutton:
                    yalign 0.7
                    xalign 0.3
                    auto "UI/Mary_%s.png"
                    action Function(clock.advance, 1), Jump("Maryschool")





    imagebutton:
        xalign 0.9845
        yalign 0
        yoffset 8
        auto "UI/Phonebutton_%s.png"
        action Show("Phone"), Hide("schoolUI")

    imagebutton:

        yalign 0.09
        xalign 0.1

        auto "UI/Bathroombutton_%s.webp"

        action Jump("restroom")

    imagebutton:
        xalign 0.005
        yalign -0.005
        yoffset 8
        auto "UI/Nav_%s.png"
        action Jump("Navigation")





    imagebutton:
        xalign 0.92
        yalign 0
        yoffset 22
        auto "Questbook_%s.png"


        if Quest1 == True:
            action Notify("Message Stacy")
        elif Quest2 == True:
            action Notify("Meet with Stacy in the school bathroom at noon/morning")
        elif Quest3 == True:
            action Notify("Talk to Namaah")
        elif Quest4 == True:
            action Notify("Talk to Jennifer in the evening")
        elif Quest5 == True:
            action Notify("Talk to Namaah")
        elif Quest6 == True:
            action Notify("Buy and give a dildo to Jennifer in the evening")
        elif Quest7 == True:
            action Notify("Talk to Namaah")
        elif Quest8 == True:
            action Notify("Message July")
        elif Quest9 == True:
            action Notify("Talk to Jennifer in the morning/noon during the weekend")
        elif Quest10 == True:
            action Notify("This is the end of the main content, be sure to explore all the optional though!")


    hbox:



        xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
        yalign .01 #change this value if you want to move it to a different part of the screen vertically

        text "{alpha=0.85}{size=+5}{font=Charm-Bold.ttf}[clock.weekday]{/font}{/size}{/alpha}":
            xoffset 240
            yoffset -8
            if clock.weekday == "Saturday":
                xoffset 230
            elif clock.weekday == "Wednesday":
                xoffset 210
            elif clock.weekday == "Thursday":
                xoffset 225
            elif clock.weekday == "Friday":
                xoffset 250
            elif clock.weekday == "Sunday":
                xoffset 245
            elif clock.weekday == "Tuesday":
                xoffset 235
    hbox:
        text "{alpha=0.85}{size=+5}{font=Charm-Bold.ttf}[clock.time]{/font}{/size}{/alpha}":
            xoffset 900
            yoffset 1

            if clock.time == "Noon":
                xoffset 555
            elif clock.time == "Night":
                xoffset 550
            elif clock.time == "Evening":
                xoffset 535
            elif clock.time == "Morning":
                xoffset 530

    hbox:

        text "{alpha=0.85}{size=-10}{font=Charm-Bold.ttf}Dollars = [dollars]{/font}{/size}{/alpha}":
            xoffset 750
            yoffset 0

    hbox:

        text "{alpha=0.85}{size=-10}{font=Charm-Bold.ttf}Favor = [favor]{/font}{/size}{/alpha}":
            xoffset 750
            yoffset 30

    hbox:

        text "{alpha=0.85}{size=+5}{font=Charm-Bold.ttf}Level = [level]{/font}{/size}{/alpha}":
            xoffset 1070
            yoffset 0



screen Phone:

    image ("images/UI/Phone.png"):
        xalign 0.5
        yalign 0.9999
        yoffset -45
    imagebutton:
        xalign 0.5029
        yalign 0.99
        yoffset -45
        auto "UI/Phonereturn_%s.png"
        if persistent.Home:
            action Hide("Phone"), Jump ("home")
        elif persistent.School:
            action Hide("Phone"), Show("schoolUI")


    imagebutton:
        xalign 0.4
        yalign 0.9
        yoffset -45
        auto "UI/Textapp_%s.png"
        action Call ("Message")

    imagebutton:
        xalign 0.53
        yalign 0.904
        yoffset -45
        auto "UI/Shopapp_%s.png"
        action Show ("Shop"), Hide("Phone")

    imagebutton:
        xalign 0.465
        yalign 0.9
        yoffset -45
        auto "UI/Profileapp_%s.png"
        action Jump ("Profile")


    image "gui/timebox.png"


    vbox:



        xalign .01 #change this value between 0 and 1 if you want to move it to a different part of the screen horizontally
        yalign .01 #change this value if you want to move it to a different part of the screen vertically

        text "{alpha=0.85}{size=+10}{font=Charm-Bold.ttf}[clock.weekday]{/font}{/size}{/alpha}":
            xoffset 40
            yoffset 3
            if clock.weekday == "Saturday":
                xoffset 35
            elif clock.weekday == "Wednesday":
                xoffset 15
            elif clock.weekday == "Thursday":
                xoffset 30
            elif clock.weekday == "Friday":
                xoffset 55
            elif clock.weekday == "Sunday":
                xoffset 50

        text "{alpha=0.85}{size=+10}{font=Charm-Bold.ttf}[clock.time]{/font}{/size}{/alpha}":
            xoffset 320
            yoffset -75
            if clock.time == "Noon":
                xoffset 345
            elif clock.time == "Night":
                xoffset 340

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
