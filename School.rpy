default stacyintro = True
default stacypower = False
default Endofbeta = False
define Mary = Character("Mary")
define Olivia = Character("Olivia")
define Lily = Character("Lily")



image School_morning = "images/BG/School_morning.webp"
image School_noon = "images/BG/School_noon.webp"
image School_evening = "images/BG/School_evening.webp"
image School_night = "images/BG/School_night.webp"
image Stacyhandjob1 = Movie(play="images/Stacy/Stacyhandjob1.webm")
image Stacyintro1 = "images/Stacy/Stacyintro1.webp"
image Stacyintro2 = "images/Stacy/Stacyintro2.webp"
image Stacyintro3 = "images/Stacy/Stacyintro3.webp"
image Stacyintro4 = "images/Stacy/Stacyintro4.webp"
image Stacyintro5 = "images/Stacy/Stacyintro5.webp"
image Stacyintro6 = "images/Stacy/Stacyintro6.webp"
image Stacyintro7 = "images/Stacy/Stacyintro7.webp"
image Stacyintro8 = "images/Stacy/Stacyintro8.webp"
image Stacyintro9 = "images/Stacy/Stacyintro9.webp"
image Stacyintro10 = "images/Stacy/Stacyintro10.webp"
image Stacyintro11 = "images/Stacy/Stacyintro11.webp"
image Stacyintro12 = "images/Stacy/Stacyintro12.webp"
image Stacyintro13 = "images/Stacy/Stacyintro13.webp"
image Stacyintro14 = "images/Stacy/Stacyintro14.webp"
image Stacyintro15 = "images/Stacy/Stacyintro15.webp"
image Stacyintro16 = "images/Stacy/Stacyintro16.webp"
image Stacyintro17 = "images/Stacy/Stacyintro17.webp"
image Stacyintro18 = "images/Stacy/Stacyintro18.webp"
image Stacyintro19 = "images/Stacy/Stacyintro19.webp"
image Stacyintro20 = "images/Stacy/Stacyintro20.webp"
image Stacyintro21 = "images/Stacy/Stacyintro21.webp"
image Oliviaschool1 = "images/School/Oliviaschool1.webp"
image Oliviaschool2 = "images/School/Oliviaschool2.webp"
image Oliviaschool3 = "images/School/Oliviaschool3.webp"
image Maryschool1 = "images/School/Maryschool1.webp"
image Maryschool2 = "images/School/Maryschool2.webp"
image Maryschool3 = "images/School/Maryschool3.webp"
image Lilyschool1 = "images/School/Lilyschool1.webp"
image Lilyschool2 = "images/School/Lilyschool2.webp"
image Lilyschool3 = "images/School/Lilyschool3.webp"












label school:

    $ persistent.Home = False

    $ persistent.School = True

    if clock.time == "Morning":

        scene School_morning

    elif clock.time == "Noon":

        scene School_noon

    elif clock.time == "Evening":

        scene School_evening

    elif clock.time == "Night":

        scene School_night

    call screen schoolUI


label restroom:
    if clock.weekday == "Monday" or clock.weekday == "Tuesday" or clock.weekday == "Wednesday" or clock.weekday == "Thursday" or clock.weekday == "Friday":
        if clock.time == "Morning" or clock.time == "Noon":
            if stacypower == True:
                jump Stacypower
            elif Stacyhookupcall == True:
                jump Stacybathroom
            else:
                "Nobody is here."
                jump school

        else:
            "It's locked"
            jump school

    else:
        "It's locked i should comeback after the weekend."
        jump school



label Stacypower:

    if persistent.MCDomtoggle == True:
        jump domStacypower


    scene Stacyintro1 with dissolve

    Stacy "I only have one shot at this..."

    pause 1

    scene Stacyintro2 with dissolve

    pause 1

    scene Stacyintro3 with dissolve

    Stacy "{i}Heeyy [povname]{/i}..."

    pause 1

    scene Stacyintro4 with dissolve

    Stacy "Sooo... What did You want to talk about?"

    povname "(Flashing these huge tits like that...)"

    povname "(One touch is all it takes as Namaah said...)"

    scene Stacyintro5 with dissolve

    Stacy "(Mhmmm... I knew He couldn't resist them...)"

    povname "(They are soo goddamn soft...)"

    scene Stacyintro6 with dissolve

    povname "It worked..."

    scene Stacyintro7 with dissolve

    Stacy "Step into the light [povname]... I need to get a good {i}look{/i} at you..."

    scene Stacyintro8 with dissolve

    Stacy "You don't know how happy I am, that you find me attractive..."

    Stacy "But it's only fair if You let me touch Your body too..."

    scene Stacyintro9 with dissolve

    Stacy "Maybe I'll grind my {i}big juicy ass on Your cock{/i}..."

    scene Stacyintro10 with dissolve

    Stacy "But I have an even better idea..."

    scene Stacyintro11 with dissolve

    Stacy "I need to let these puppies breathe a little..."

    play sound "audio/Cloth.wav"

    scene Stacyintro12 with dissolve

    Stacy "Now... Time for my reward..."

    play sound "audio/zipper.wav"

    scene Stacyintro13 with dissolve

    Stacy "(It's.. {b}SO BIG{/b}...)"

    scene Stacyintro14 with dissolve

    Stacy "This is the luckiest day of my life [povname]..."

    show Stacyhandjob1 with dissolve

    stop music

    play music "audio/Scenetheme.mp3" fadein 1.0


    povname "Fuck..."

    Stacy "Enjoying yourself are You?"

    Stacy "Remember it's only the beginning of our little secret {i}friendship{/i}..."

    pause

    Stacy "{i}[povname]~{/i}..."

    povname "Yeah..?"

    Stacy "Tell me how would you {i}fuck{/i} me..."

    povname "{i}I would pound you soo hard you would be mindlessly drooling on the floor, while filling your pussy to the brim with my cum...{/i}"

    Stacy "{i}Mmmm... Would You do that to me everyday..?{/i}"

    povname "{i}Even when you are carrying my triplets.{/i}"

    Stacy "Fuck... [povname], You are making me {i}dripping wet{/i}..."

    Stacy "I'll let this come true... {i}After I suck every drop of Your semen from Your massive cock{/i}..."

    Stacy "{i}And after that tasty meal, I'll squeeze the life out of Your dick with my breasts until you fall unconscious.{/i}"

    Stacy "{i}When I'm done with using these puppies, I'll grind and ride the {b}fuck{/b} out of Your cock, day and night until You pour gallons worth of cum into me...{/i}"

    Stacy "Just imagine... You will be regaining consciousness up to my bouncing breasts infront of Your face, just to lose it again when you fill my womb with-"

    stop music

    play sound "audio/Cum1.mp3"

    scene Stacyintro15 with vpunch

    pause

    play sound "audio/Cum2.mp3"

    scene Stacyintro16 with vpunch

    pause

    povname "Ahhh... Fuck..."

    play sound "audio/Swallow.wav" volume 0.1

    scene Stacyintro17 with dissolve

    Stacy "Mmmm..."

    scene Stacyintro18 with dissolve

    Stacy "If You are going to be blowing loads as big as this, You really are going to knock me up with triplets..."

    Stacy "{i}Fuck{/i} I feel so horny with all this cum on me..."

    scene Stacyintro19 with dissolve

    Stacy "{i}You really made my day [povname]{/i}..."

    Stacy "And don't worry I'll keep this between us."

    scene Stacyintro20 with dissolve

    Stacy "You should go now, I have to clean myself now before the classes."

    Stacy "{i}And promise me You will call me again so we can have some more fun~{/i}"

    povname "Sure, I'll call ya, see you later."

    Stacy "{i}Bye-bye~{/i}..."

    scene Stacyintro21 with dissolve

    Stacy "I could've pushed this further..."

    Stacy "But atleast this way i won't scare him off..."

    $ stacyintro = False

    $ stacypower = False

    $ Quest2 = False

    $ Quest3 = True

    $ persistent.galleryStacy = True

    $ persistent.Stacyhandjob = True

    $ Stacyhookupcall = False

    play music "audio/Mainbackgroundmusic.mp3" fadein 1.0

    "+40 Dollars
    +1 Favor
    +100 exp"

    $ dollars += 40
    $ favor += 1
    $ exp += 100

    call expression 'levelup' pass ('school') from _call_expression

    jump school

label Stacybathroom:

    if persistent.MCDomtoggle == True:
        jump domStacyhandjob

    scene Stacyintro8 with dissolve

    menu:
        "Handjob":
            jump Stacyhandjob
        #"Fuck her pussy" if level >= 2:
            #jump Stacyfuck





label Stacyhandjob:

    if persistent.MCDomtoggle == True:
        jump domStacyhandjob

    stop music

    play music "audio/Scenetheme.mp3" fadein 1.0

    scene Stacyintro11 with dissolve

    Stacy "I was getting impatient [povname]..."

    play sound "audio/Cloth.wav"

    scene Stacyintro12 with dissolve

    Stacy "I had to wait all this time to touch Your cock again..."

    play sound "audio/zipper.wav"

    scene Stacyintro14 with dissolve

    Stacy "Every day after every session I count the hours till You call me~..."

    Stacy "{i}I think I'm getting addicted to You...{/i}"

    show Stacyhandjob1 with dissolve

    Stacy "I should introduce You to my friends..."

    Stacy "But right now You are {i}mine{/i}~..."

    pause 1

    Stacy "{i}You are making such a lewd face [povname]~{/i}..."

    povname "I'm going to bust..."

    Stacy "Paint me with Your cum again [povname]..."

    extend " Treat me like the slut I am..."

    scene Stacyintro15 with vpunch

    pause

    play sound "audio/Cum2.mp3"

    scene Stacyintro16 with vpunch

    pause

    povname "Ahhh... Fuck..."

    play sound "audio/Swallow.wav" volume 0.1

    scene Stacyintro17 with dissolve

    Stacy "Mmmm..."

    scene Stacyintro19 with dissolve

    Stacy "Thanks for the tasty meal~..."

    Stacy "Be sure to call me again soon, or I might get {i}lonely{/i}~..."

    povname "I'd be dumb if I wouldn't..."

    Stacy "{i}Heehee~{/i}... {i}Thanks cutie~{/i}..."

    Stacy "And take this..."

    Stacy "A little motivation for my future husband..."

    povname "Future who..?"

    Stacy "Nothing... Heehee~"

    "+40 Dollars
    +1 Favor
    +100 exp"

    $ dollars += 40
    $ favor += 1
    $ exp += 100

    $ persistent.Stacyhandjob2 = True

    $ Stacyhookupcall = False

    call expression 'levelup' pass ('school') from _call_expression_1

    play music "audio/Mainbackgroundmusic.mp3" fadein 1.0

    jump school

label Lilyschool:

    scene Lilyschool1 with dissolve

    Lily "Heya [povname]..!"

    Lily "I've heard You've been fooling around with {b}Stacy{/b} lately..."

    povname "So..?"

    scene Lilyschool2 with dissolve

    Lily "What would You say, if I'd offer You a lot of cash for playing with me too..?"

    povname "Well, if you have enough on your person then why not."

    Lily "{b}Great{/b}..! Let's go to the bathroom."

    scene black with dissolve

    "Some time later..."

    scene Lilyschool3 with dissolve

    Lily "{i}Ahhh~... [povname]...{/i}"

    Lily "Your hands are soo firm and {b}strong{/b}..."

    povname "With such a small and tight pussy like that anything is going to feel massive."

    Lily "{i}Mhmmm{/i}... It's probably true..."

    Lily "I need to compose myself..."

    Lily "Take this, for Your troubles."

    $ dollars += 140
    $ favor += 1
    $ exp += 80

    "+140 Dollars
    +1 Favor
    +80 exp"

    povname "Thanks, see ya later."

    call expression 'levelup' pass ('school') from _call_expression_5

    jump school

label Oliviaschool:

    scene Oliviaschool1 with dissolve

    Olivia "{i}Hey handsome~...{/i}"

    povname "Sup Olivia."

    Olivia "Word has been going around, that you are offering {b}certain services{/b} lately."

    povname "Uhh, yeah."

    scene Oliviaschool2 with dissolve

    Olivia "Say, if I'd make you {i}cum{/i} like no one else did before."

    Olivia "Would you cut me some slack on the price..?"

    povname "I'd take you up on that offer."

    Olivia "{i}Great{/i}... You won't regret it"

    scene black with dissolve

    "Some time later..."

    scene Oliviaschool3 with dissolve

    povname "{b}Fucking hell{/b} that was great..."

    Olivia "What did you expect [povname]... {b}I'm the best of the best{/b}."

    Olivia "Soo, about that {i}price{/i}..."

    povname "Yeah sure, you did your part."

    Olivia "A big load like that almost for free, my day couldn't get any {b}better{/b}."

    Olivia "I'll see you later you {i}hunk{/i}, I need to get back to something."

    "+20 Dollars
    +4 Favor
    +110 exp"

    $ dollars += 20
    $ favor += 4
    $ exp += 110

    call expression 'levelup' pass ('school') from _call_expression_6

    jump school

label Maryschool:

    scene Maryschool1 with dissolve

    Mary "{i}H-hey [povname]...{/i}"

    povname "Oh, Mary do you need something..?"

    Mary "{b}Well{/b}... Yeah..."

    extend " I wanted to {i}um{/i}..."

    Mary "Buy some of your services..."

    povname "I didn't know you were into that Mary, but yeah sure I'll do it for you."

    scene Maryschool2 with dissolve

    Mary "{i}Really..?{/i}"

    povname "Yeah why not, you are a beautiful girl with a great figure, I wouldn't pass on that."

    Mary "{b}Oh{/b}... Wow..."

    Mary "Thank you [povname], {i}that was really nice{/i}~..."

    povname "Come on, let's go to the bathroom."

    scene black with dissolve

    "Some time later..."

    scene Maryschool3 with dissolve

    Mary "{b}Ahh{/b}~... Did I do good [povname]..?"

    povname "Yeah... that was great."

    povname "Your {b}breasts{/b} look amazing covered in my cum..."

    Mary "Thanks [povname]~..."

    Mary "Do You {i}umm{/i}-..."

    Mary "Do You want to do it again sometime..?"

    povname "Yeah, I'd really like to play around with you again..."

    Mary "{b}That's great..!{/b}"

    Mary "Thank you..."

    povname "I'm the one who should be thanking you right now."

    Mary "..."

    povname "Well, I gotta go."

    povname "See you later."

    Mary "{i}Yeah{/i}... see you later..."

    "+60 Dollars
    +2 Favor
    +200 exp"

    $ dollars += 60
    $ favor += 2
    $ exp += 200

    call expression 'levelup' pass ('school') from _call_expression_7

    jump school
