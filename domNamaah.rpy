define spovtitle = Character("{i}[povtitle]{/i}")
default NFC = False

label domNamaahfirstcall:

    if clock.time == "Evening":
        scene Namaahfirstcall1 with dissolve

        pause

        scene Namaahfirstcall2 with dissolve

        pause

        scene Namaahfirstcall3 with dissolve

        pause

        scene Namaahfirstcall4 with dissolve

        Namaah "You wanted to see me, {i}[povtitle]{/i}?"

        povname "I did. Thank you for coming."

        povname "I wanted to know if my powers had grown enough to move onto another mark yet."

        povname "You mentioned there was another candidate if I improved after practicing on Stacy."

        scene Namaahfirstcall6 with dissolve

        Namaah "You recalled correctly - and I believe you are are ready now."

        povname "Excellent. Who's the next candidate, then?"

        scene Namaahfirstcall5 with dissolve

        Namaah "Your [Jenniferrelation], Jennifer."

        povname "That makes sense. She's closeby, just like [Carolinerelation]. I'd have to have her under control to move and act freely."

        Namaah "You're a quick learner, {i}[povtitle]{/i}. It's one of your best traits."

        Namaah "The other being your dick~"

        scene Namaahfirstcall7 with dissolve

        povname "Oh, ha-ha. You're so damn clever."

        Namaah "*giggle* Why thank you, {i}[povtitle]{/i}."

        scene Namaahfirstcall6 with dissolve

        povname "Anything else I should know before I make the attempt?"

        Namaah "There are things I {i}could{/i} warn you about, but I think you'll fair better with firsthand experience."

        povname "Alright. I'll trust you're working in my best interests for now."

        povname "You're dismissed, but keep yourself available in case I need you."

        Namaah "Alright. If you need me again, you know how to reach me."

        Namaah "I'll be around as you asked."

        Namaah "Good luck, {i}[povtitle]{/i}."

        scene Namaahfirstcall7 with dissolve

        pause 1

        scene Namaahfirstcall8 with dissolve

        povname "I get the feeling I'm gonna need it."

        povname "I need a plan."

        povname "Jennifer has been tough to talk to for a long time now. I'll have to broach the subject carefully."

        povname "It'd be better if I had her alone in case something went wrong, too. I think the best time would be after she gets home from school."

        povname "That's all I can really think of until I know how she'll react."

        povname "Showtime."

        $ Namaahfirstevercall = True

        $ Jentalk = True

        $ Quest3 = False

        $ Quest4 = True

        $ NFC = True

        jump home



label domNamaahRideRepeat:

    if Quest3 == True:

        jump domNamaahLater

    scene Schoolintro87 with slowdissolve

    pause

    Namaah "Please get on the bed and allow me to pleasure myself with your splended dick, {i}[povtitle]{/i}."

    play sound "audio/Cloth.wav"

    scene Schoolintro88 with dissolve

    povname "Impressive. I think that was the same thing you said the first time."

    povname "Only now I'm sure you mean it."

    play sound "audio/Cloth.wav"

    scene Schoolintro89 with dissolve

    Namaah "Oh, hush."

    povname "But you're not denying it~"

    Namaah "You can't make me blush, I'm already red! Just lay back and enjoy it!"

    scene Schoolintro90 with dissolve

    Namaah "There, all ready for you."

    Namaah "Can you turn out the light please, [povtitle]?"

    povname "You bet your fine ass I can."

    povname "I just love the moment the sass drops."

    scene Schoolintro92 with dissolve

    Namaah "Well... if nothing else you've proved your prowess in the bedroom."

    povname "And I'll prove it as many times as you like."

    scene Schoolintro93 with dissolve

    pause

    play sound "audio/slide.wav"

    scene Schoolintro94 with dissolve

    Namaah "Oooooooooooh~~"

    Namaah "The moment of insertion is always sooooo good."

    Namaah "This must be Hell."

    pause

    show Namaahfuck1 with dissolve

    play music "audio/Scenetheme.mp3" fadein 1.0

    pause

    povname "Hell? Don't you mean Heaven?"

    pause

    Namaah "Of (hah) course not. (Mmm)"

    Namaah "I'm a (ah!) Demon. You think I'd be (eeee) able to treat heaven as a good thing?"

    povname "Haha! A fine point from a fine cocksleeve."

    povname "But, enough talk bitch."

    povname "Tighten up that pretty cunt for me."

    Namaah "Yes, (ugh) [povtitle]! (ahh)"

    Namaah "I'll do my best, (mmph) but your cock just (oooooh) hits me so (hah) good...!"

    Namaah "It's ha-ha-hard to focus!"

    Namaah "I don't think I can take much more, [povtitle]!"

    Namaah "Please, cum for me."

    pause

    povname "I'm sorry - who did you want to cum for you again?"

    Namaah "Please cum inside my naughty demonic cunt, [povtitle]! Please!"

    pause 1.0

    Namaah "Please!"

    Namaah "Please! Please! Pleasepleasepleasepleaseplease!"

    Namaah "I want to cum with you, [povtitle]!"

    povname "Good girl! That's the way to get what you want."

    povname "Here comes your reward, slut. Take it all!"

    pause

    play sound "audio/Cum1.mp3"

    scene Schoolintro95 with vpunch

    pause

    play sound "audio/Cum2.mp3"

    stop music

    scene Schoolintro96 with vpunch

    pause

    scene Schoolintro97 with dissolve

    pause

    Namaah "{i}AAAAAAAAH!!!{/i}"

    Namaah "Thank fuck. That felt amazing..."

    povname "It's not 'fuck' you should thank for making you cum now, is it?"

    Namaah "I... I'm sorry [povtitle], it's hard to think straight."

    Namaah "Thank you (hah hah) for making me cum."

    povname "You're most welcome, love. You did an excellent job again."

    povname "I'll let you catch your breath and get cleaned up."

    povname "Until next time."

    Namaah "I can't wait..."

    scene black with slowdissolve

    jump home

label domNamaahLater:

    povname "... For some reason I can't call her right now. Maybe I'll try again during the evening."

    jump home
