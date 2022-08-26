image Stacydom1 = "images/Stacy/Stacydom1.webp"
image Stacydom2 = "images/Stacy/Stacydom2.webp"
image Stacydom3 = "images/Stacy/Stacydom3.webp"
image Stacydom4 = "images/Stacy/Stacydom4.webp"
image Stacydom5 = "images/Stacy/Stacydom5.webp"

label domStacyBathroomStripping:

    Stacy "What did you want to see me take off, [povtitle]?"

    menu domStacyBathroomStrip1:
        "How do you want to see her strip?"

        "Let's go piece by piece":
            Stacy "That's a good idea. Shall I start with my top?"

            jump domStacyBathroomStrip2

        "Get your tits out for me" if level >= 2:

            Stacy "With pleasure."

            jump domStacyBathroomStripquick2

        "Strip down to your panties" if level >=3:

            if domStacypanties == False and level <4:

                Stacy "I'm sorry, [povname]. I can't do that if I'm not wearing panties."

                Stacy "Would you like me to put them back on so I do that for you?"

                menu:

                    "Yes":
                        $ domStacypanties == True

                        Stacy "Alright, give me one second [povtitle]."

                        pause 1

                        play sound "audio/Cloth.wav" volume 0.5

                        scene Stacyintro9 with dissolve

                        pause 1

                        play sound "audio/Cloth.wav" volume 0.5

                        scene Stacyintro10 with dissolve

                        play sound "audio/Cloth.wav" volume 0.5

                        Stacy "Thank you for understanding."

                        Stacy "Now let's get the rest of these clothes off for you."

                        jump domStacyBathroomStripquick3

                    "No, but I'm not done making you strip":

                        Stacy "Okay. Thanks for not trying to force it, [povname]."

                        povname "(She's calling me by name again. I must have been close to the limit.)"

                        jump domStacyBathroomStrip1

            if domStacypanties == False:

                scene Stacydom5 with dissolve

                Stacy "I'm still not wearing any like you told me to, [povtitle]. You should just ask me to get naked!"

                scene Stacyintro10 with dissolve

                jump domStacyBathroomStrip1

            if domStacypanties == True:

                Stacy "Are you that pressed to get me naked, [povtitle]? I hope everything is alright."

                Stacy "If not, I hope this helps make it better."

                jump domStacyBathroomStripquick3

        "I want you naked and on your knees for me" if level >=4:
            "Oh, you must be in a rush today! I'll hurry then."

            jump domStacyBathroomStripquick4

label domStacyBathroomStrip2:

    scene Stacydom1 with dissolve

    play sound "audio/Cloth.wav" volume 0.5

    Stacy "Should I keep going?"

    menu SDBRS2:
        "Do you want to try and get her bra off?"

        "Yes":

            if level >=2:
                Stacy "As you wish, [povtitle]."

                jump domStacyBathroomStrip3

            if level <2:

                Stacy "I want to do that for you, but I don't think I'm ready yet."

                Stacy "Sorry, [povname]."

                povname "(Damn. She even slipped back into calling me by name.)"

                povname "(Guess I'll have to improve my control to make her go further.)"

                jump domStacyBathroomStripEnd

        "No":

            Stacy "If you're sure! I hope you had fun anyway."

            jump domStacyBathroomStripEnd

label domStacyBathroomStrip3:

    scene Stacydom2 with dissolve

    play sound "audio/Cloth.wav" volume 0.5

    Stacy "There, my tits are on full display now. It's actually nice to let them breathe like this."

    menu SDBRS3:
        "Push her to take her skirt off?"

        "Yes":

            if domStacypanties == True and level >=3:
                Stacy "I can do that for you, sure!"

                jump domStacyBathroomStrip4

            if domStacypanties == False and level >=4:

                Stacy "You told me not to wear any panties!"

                Stacy "Guess I'll just take my skirt off and strike a pose for you."

                jump domStacyBathroomStrip5

            if domStacypanties == True or domStacypanties == False and level <=3:

                Stacy "Sorry, [povname]. That's just asking too much right now."

                povname "(And there's the namedrop again. Guess she slipped out of it.)"

                povname "(At least there's progress.)"

                jump domStacyBathroomStripEnd

        "No":
            "Alright then. I hope you enjoyed the view. I'm going to let them breathe a little longer before I head out."

            jump domStacyBathroomStripEnd

label domStacyBathroomStrip4:

    scene Stacydom3 with dissolve

    play sound "audio/Cloth.wav" volume 0.5

    Stacy "Even if you've seen this much before, I'm still a little nervous!"

    menu SDBRS4:
        "Make the final push to get her naked?"

        "Yes":
            if level >=4:

                Stacy "Alright, I'm doing this for you. {i}Just{/i} for you, and no one else."

                Stacy "But if I'm going to even take my panties off, I'm striking a cute pose!"

                jump domStacyBathroomStrip5

            if level <=3:

                Stacy "I'm sorry, [povname]. I really like you, and I've been having so much fun doing this for you."

                Stacy "But I just... I can't yet. I'm sorry if I disappointed you."

                povname "(Fuck. I'm so close, I can feel it. Just a little more and I can break down the last barrier.)"

                povname "(I better reassure her to make sure I don't completely lose control.)"

                povname "You haven't disappointed me at all, Stacy."

                povname "I know I was asking a lot, and I really want to thank you for doing your best."

                Stacy "Really?"

                povname "Absolutely. Your best is all I can ask. As long as you're not upset that I tried, then we're all good."

                Stacy "I would never be mad at you! You've been so kind and understanding the whole way, I just... need a little more time."

                povname "I understand."

                povname "(You won't care soon enough. A little more practice and I can be sure of that.)"

                jump domStacyBathroomStripEnd

        "No":

            Stacy "Phew! This was nervewracking and exciting!"

            Stacy "I can't believe I stripped to just my panties in the Men's washroom!"

            jump domStacyBathroomStripEnd

label domStacyBathroomStrip5:

    scene Stacydom4 with dissolve

    play sound "audio/Cloth.wav" volume 0.5

    Stacy "There we are, [povtitle]. I'm totally naked and striking a cute pose for you in the Men's bathroom."

    Stacy "Do you like having me naked and on my knees?"

    Stacy "It's even the middle of a school day. I know this bathroom is mostly abandoned, but my heart is beating pretty fast!"

    Stacy "I don't know how you make you do things like this!"

    povname "Do you dislike it when I push you outside your comfort zone?"

    Stacy "... I didn't say that."

    pause 3

    Stacy "Can I get dressed now, [povtitle]?"

    menu SDBRS5:
        "Do you want to let her put her clothes back on and end the encounter?"

        "Yes":
            Stacy "This was so exciting. I hope you make me do this again, [povtitle]!"

            jump domStacyBathroomStripEnd

        "No":
            Stacy "If... if that's what you want, [povtitle]. I'll stay this way a little longer for you."

            pause 15

            "Can I get dressed now? Please, [povtitle]?"

            jump SDBRS5

        "Yes, but I want you to go without your panties for a while slut" if domStacypanties == True:
            "I'm only a slut for you~"

            play sound "audio/Cloth.wav" volume 0.5

            scene Stacydom2 with dissolve

            pause 1

            play sound "audio/Cloth.wav" volume 0.5

            scene Stacydom1 with dissolve

            pause 1

            play sound "audio/Cloth.wav" volume 0.5

            scene Stacyintro4 with dissolve

            Stacy "There, back to how we started!"

            povname "Are we really?"

            Stacy "Would you like to double check?"

            povname "Of course I would."

            Stacy "Are you sure you don't just want to stare at my ass?"

            povname "Shut up and show me already."

            Stacy "*giggles* Yes Sir, [povtitle] Sir!"

            scene Stacydom5 with dissolve

            pause 5

            povname "Good girl. That'll be all for now."

            povname "... try not to get caught."

            Stacy "Of course! I told you, I'm {i}your{/i} slut, [povtitle]. All of me is only for you."

            povname "Excellent answer love. See you next time."

            Stacy "I'll look forward to it more than you know."

            jump school

label domStacyBathroomStripquick2:

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom1 with dissolve

    pause 1

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom2 with dissolve

    Stacy "As you wanted, [povtitle] - I have freed the titties!"

    jump SDBRS3

label domStacyBathroomStripquick3:

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom1 with dissolve

    pause 1

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom2 with dissolve

    pause 1

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom3 with dissolve

    pause 1

    Stacy "There you are, down to nothing but my panties!"

    Stacy "Is there anything else I can do?"

    pause 1

    jump SDBRS4

label domStacyBathroomStripquick4:

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom1 with dissolve

    pause 1

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom2 with dissolve

    pause 1

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacydom3 with dissolve

    pause 1

    scene Stacydom4 with dissolve

    Stacy "Ta-daah! Just like that, your lovely assistant's clothes have disappeared! Would you like me to help pull a rabbit out of a hat next?"

    Stacy "Or maybe pull something else out of your pants~?"

    povname "Calm down, girl! I'll let you know."

    pause 5

    Stacy "Should I put my clothes back on now?"

    jump SDBRS5

label domStacyBathroomStripEnd:

    play sound "audio/Cloth.wav" volume 0.5

    scene Stacyintro4 with slowdissolve

    povname "Thank you, sweetheart. You did very well for me today."

    Stacy "Thank you too, [povtitle]. I always enjoy it when you push my boundaries like this."

    Stacy "It really gets my heart racing to think that I'm doing this at school of all places!"

    povname "Haha, I'm sure it does. For now I've got some other matters to attend to. Have a good day."

    Stacy "Glad I could make you happy. Call on me anytime,"

    extend " and I hope you have a good day too, [povtitle]!"

    "No money earned from this interaction. +1 Favor +50 exp"

    $ dollars += 0
    $ favor += 1
    $ exp += 50

    jump school
