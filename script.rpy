# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    config.movie_mixer = "sfx"

define Caroline = Character("Caroline")
define July = Character("July")
define Stacy = Character("Stacy")
define Susan = Character("Susan")
define Voice = Character("???")
define Namaah = Character("Namaah")
define Jeff = Character("Jeff")
define slowdissolve = Dissolve(3.0)


init:
    $ cum = Fade(1, 0, 1, color="#FFFFFF") # Fade to black and back.


image Jenniferrelation = "images/Jenniferrelation.webp"
image Carolinerelation = "images/Carolinerelation.webp"
image Hannahrelation = "images/Hannahrelation.webp"
image Schoolintro1 = "images/Schoolintro1.webp"
image Schoolintro2 = "images/Schoolintro2.webp"
image Schoolintro3 = "images/Schoolintro3.webp"
image Schoolintro4 = "images/Schoolintro4.webp"
image Schoolintro5 = "images/Schoolintro5.webp"
image Schoolintro6 = "images/Schoolintro6.webp"
image Schoolintro7 = "images/Schoolintro7.webp"
image Schoolintro8 = "images/Schoolintro8.webp"
image Schoolintro9 = "images/Schoolintro9.webp"
image Schoolintro10 = "images/Schoolintro10.webp"
image Schoolintro11 = "images/Schoolintro11.webp"
image Schoolintro12 = "images/Schoolintro12.webp"
image Schoolintro13 = "images/Schoolintro13.webp"
image Schoolintro14 = "images/Schoolintro14.webp"
image Schoolintro15 = "images/Schoolintro15.webp"
image Schoolintro16 = "images/Schoolintro16.webp"
image Schoolintro17 = "images/Schoolintro17.webp"
image Schoolintro18 = "images/Schoolintro18.webp"
image Schoolintro19 = "images/Schoolintro19.webp"
image Schoolintro20 = "images/Schoolintro20.webp"
image Schoolintro21 = "images/Schoolintro21.webp"
image Schoolintro22 = "images/Schoolintro22.webp"
image Schoolintro23 = "images/Schoolintro23.webp"
image Schoolintro24 = "images/Schoolintro24.webp"
image Schoolintro25 = "images/Schoolintro25.webp"
image Schoolintro26 = "images/Schoolintro26.webp"
image Schoolintro27 = "images/Schoolintro27.webp"
image Schoolintro28 = "images/Schoolintro28.webp"
image Schoolintro29 = "images/Schoolintro29.webp"
image Schoolintro30 = "images/Schoolintro30.webp"
image Schoolintro31 = "images/Schoolintro31.webp"
image Schoolintro32 = "images/Schoolintro32.webp"
image Schoolintro33 = "images/Schoolintro33.webp"
image Schoolintro34 = "images/Schoolintro34.webp"
image Schoolintro35 = "images/Schoolintro35.webp"
image Schoolintro36 = "images/Schoolintro36.webp"
image Schoolintro37 = "images/Schoolintro37.webp"
image Schoolintro38 = "images/Schoolintro38.webp"
image Schoolintro39 = "images/Schoolintro39.webp"
image Schoolintro40 = "images/Schoolintro40.webp"
image Schoolintro41 = "images/Schoolintro41.webp"
image Schoolintro42 = "images/Schoolintro42.webp"
image Schoolintro43 = "images/Schoolintro43.webp"
image Schoolintro44 = "images/Schoolintro44.webp"
image Schoolintro45 = "images/Schoolintro45.webp"
image Schoolintro46 = "images/Schoolintro46.webp"
image Schoolintro47 = "images/Schoolintro47.webp"
image Schoolintro48 = "images/Schoolintro48.webp"
image Schoolintro49 = "images/Schoolintro49.webp"
image Schoolintro50 = "images/Schoolintro50.webp"
image Schoolintro51 = "images/Schoolintro51.webp"
image Schoolintro52 = "images/Schoolintro52.webp"
image Schoolintro53 = "images/Schoolintro53.webp"
image Schoolintro54 = "images/Schoolintro54.webp"
image Schoolintro55 = "images/Schoolintro55.webp"
image Schoolintro56 = "images/Schoolintro56.webp"
image Schoolintro57 = "images/Schoolintro57.webp"
image Schoolintro58 = "images/Schoolintro58.webp"
image Schoolintro59 = "images/Schoolintro59.webp"
image Schoolintro60 = "images/Schoolintro60.webp"
image Schoolintro61 = "images/Schoolintro61.webp"
image Schoolintro62 = "images/Schoolintro62.webp"
image Schoolintro63 = "images/Schoolintro63.webp"
image Schoolintro64 = "images/Schoolintro64.webp"
image Schoolintro65 = "images/Schoolintro65.webp"
image Schoolintro66 = "images/Schoolintro66.webp"
image Schoolintro67 = "images/Schoolintro67.webp"
image Schoolintro68 = "images/Schoolintro68.webp"
image Schoolintro69 = "images/Schoolintro69.webp"
image Schoolintro70 = "images/Schoolintro70.webp"
image Schoolintro71 = "images/Schoolintro71.webp"
image Schoolintro72 = "images/Schoolintro72.webp"
image Schoolintro73 = "images/Schoolintro73.webp"
image Schoolintro74 = "images/Schoolintro74.webp"
image Schoolintro75 = "images/Schoolintro75.webp"
image Schoolintro76 = "images/Schoolintro76.webp"
image Schoolintro77 = "images/Schoolintro77.webp"
image Schoolintro78 = "images/Schoolintro78.webp"
image Schoolintro80 = "images/Schoolintro80.webp"
image Schoolintro81 = "images/Schoolintro81.webp"
image Schoolintro82 = "images/Schoolintro82.webp"
image Schoolintro83 = "images/Schoolintro83.webp"
image Schoolintro84 = "images/Schoolintro84.webp"
image Schoolintro85 = "images/Schoolintro85.webp"
image Schoolintro86 = "images/Schoolintro86.webp"
image Schoolintro87 = "images/Schoolintro87.webp"
image Schoolintro88 = "images/Schoolintro88.webp"
image Schoolintro89 = "images/Schoolintro89.webp"
image Schoolintro90 = "images/Schoolintro90.webp"
image Schoolintro91 = "images/Schoolintro91.webp"
image Schoolintro92 = "images/Schoolintro92.webp"
image Schoolintro93 = "images/Schoolintro93.webp"
image Schoolintro94 = "images/Schoolintro94.webp"
image Schoolintro95 = "images/Schoolintro95.webp"
image Schoolintro96 = "images/Schoolintro96.webp"
image Schoolintro97 = "images/Schoolintro97.webp"
image Schoolintro98 = "images/Schoolintro98.webp"
image Schoolintro99 = "images/Schoolintro99.webp"
image Schoolintro100 = "images/Schoolintro100.webp"
image Schoolintro101 = "images/Schoolintro101.webp"
image Schoolintro102 = "images/Schoolintro102.webp"
image Schoolintro103 = "images/Schoolintro103.webp"
image Schoolintro104 = "images/Schoolintro104.webp"
image Schoolintro105 = "images/Schoolintro105.webp"
image Schoolintro106 = "images/Schoolintro106.webp"
image Schoolintro107 = "images/Schoolintro107.webp"
image Schoolintro108 = "images/Schoolintro108.webp"
image Schoolintro109 = "images/Schoolintro109.webp"
image Schoolintro110 = "images/Schoolintro110.webp"
image Schoolintro111 = "images/Schoolintro111.webp"
image Schoolintro112 = "images/Schoolintro112.webp"
image Schoolintro113 = "images/Schoolintro113.webp"
image Carolineboobjob1 = Movie(play="Carolineboobjob1.webm")
image Susanblow1 = Movie(play="images/Susanblow1.webm")
image Namaahfootjob1 = Movie(play="images/Namaahfootjob1.webm")
image Namaahfuck1 = Movie(play="images/Namaahfuck1.webm")
image Dreamintro1 = "images/Dreamintro1.webp"
image Dreamintro2 = "images/Dreamintro2.webp"



default Quest1 = False
default Namaahfirstcall = False



default dollars = 100
default favor = 0
default level = 1
default exp = 0





# The game starts here.

label start:

    if persistent.MCDomtoggle == True:
        jump domstart

    "Havgar" "Before the game starts,"

    extend " with patch 0.3.0 a new storytelling mode has been added courtesy of L33chtheguy."

    "Havgar" "It makes the MC less wimpy, and more dominant at the start of the game, and introduces more Maledom related content."

    "Havgar" "Most of the content remains the same, but it's used in a way so You won't miss out on anything, but have a completely different experience!"

    "Havgar" "If Maledom focused content isn't Your cup of tea, there is no need to turn it on for any additional content."

    "Havgar" "Do you want to turn on the Maledom storytelling?"

    menu :
        "Yes":
            $ persistent.MCDomtoggle = True

            jump domstart

        "No":
            $ persistent.MCDomtoggle = False



    scene black

    $ persistent.dildo = False

    $ povname = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your name mortal?{/font}{/size}", length = 32)

    $ persistent.povname = povname

    scene Jenniferrelation with dissolve

    $ Jenniferrelation = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your relation with Jennifer?{/font}{/size} (Default is Sister/Roommate)", length = 32)

    $ persistent.Jenniferrelation = Jenniferrelation

    scene Carolinerelation with dissolve

    $ Carolinerelation = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your relation with Caroline?{/font}{/size} (Default is Mom/Landlord)", length = 32)

    $ persistent.Carolinerelation = Carolinerelation

    scene Hannahrelation with dissolve

    $ Hannahrelation = renpy.input("{size=+10}{font=Charm-Bold.ttf}What is your relation with Hannah?{/font}{/size} (Default is Aunt/Roommate)", length = 32)

    $ persistent.Hannahrelation = Hannahrelation

    scene black

    "Havgar" "Thanks for checking out the game in its beta!"

    "Havgar" "Currently I had to cut some content, all the content missing that was in the Alpha will be reintroduced with some new scenes in the next update."

    "Havgar" "If u are interested in leaving feedback or just simply want to follow the progress of {font=Charm-Bold.ttf}Chosen{/font}
    check out the f95 post for a discord link."

    "Havgar" "And, big thanks the LusterSound for the allowing me to use his music inside the game, be sure to check him out!"

    "Havgar" "I hope you enjoy playing the game, and have a fantastic time doing so!"

    window hide

    stop music fadeout 1.0

    pause 2.0

    window hide

    play music "audio/Classroom.mp3" fadein 1.0 volume 1.5

    povname "{i}Ehhh...{/i}"

    scene Schoolintro1 with dissolve

    povname "It's getting kinda boring you know, I think i will just skip the rest of the lessons after this one."

    scene Schoolintro2 with dissolve

    Jeff "{b}Bro{/b},"

    extend " You are still on that shit with Susan?"

    scene Schoolintro3 with dissolve

    povname "Why do you even care?"

    scene Schoolintro4 with dissolve

    Jeff "'Cause It's getting kinda out of hand with you, [povname]."

    Jeff "Out of nowhere you start caring about pussy and getting laid."

    povname "..."

    Jeff "Me and the other fellas are scared we'll lose you buddy."

    scene Schoolintro5 with dissolve

    povname "Do you really think that having sex will change me into a different person?"

    scene Schoolintro6 with dissolve

    Jeff "{b}Man,{/b}"
    extend "{b} don't fuck with me.{/b}"

    Jeff "Stop acting like you lost your marbles out of nowhere."

    scene Schoolintro7 with dissolve

    Jeff "The last thing I want to hear, is that you are fooling around with that {i}Stacy{/i}."

    scene Schoolintro8 with dissolve

    pause 1

    Jeff "But hey man, even if you really get into that shit, just know that I won't turn my back on you."

    scene Schoolintro9 with dissolve

    Jeff "And, atleast when you will be okay with giving it to them, hook me up as your manager."

    povname "{i}What..?{/i}"

    scene Schoolintro10 with dissolve

    Jeff "{b}Dude{/b},"

    extend "you are acting like you were born yesterday."

    Jeff "When you get into that shit, most of people like you end up in the pleasure industry."

    Jeff "And having someone covering your back will help ya quite a lot."

    povname "{i}Haha, yeah,{/i} "

    extend "sure bro."

    scene Schoolintro11 with dissolve

    Jeff "Ay, It's good to see that you ain't atleast gloomy and all."

    Jeff "Anyway,"

    scene Schoolintro12 with dissolve

    extend " let's go to the classroom."

    scene Schoolintro13 with dissolve

    pause 1

    scene Schoolintro14 with dissolve

    povname "Sup Jenny."

    scene Schoolintro15 with dissolve

    Jennifer "Fuck off."

    scene Schoolintro16 with dissolve

    Jeff "{b}Haha{/b},"
    extend " damn,"
    extend " feisty as always ain't she [povname]?"

    scene Schoolintro17 with dissolve

    Jennifer "And as always, both of you act like damn apes."

    scene Schoolintro18 with dissolve

    Jeff "And here comes Stacy!"

    Jeff "Wonder how many cocks she sucked today."

    scene Schoolintro19 with dissolve

    July "What the hell Jeff..."

    Jennifer "Fucking jackass..."

    povname "I think you are taking it too far, man."

    Jeff "Come on..."

    extend "It was just a joke."

    scene Schoolintro20 with dissolve

    Jennifer "Seems like one of the chimpanzees is growing a brain."

    July "Awww, that's the first time You've said something so nice to someone..."

    scene Schoolintro21 with dissolve

    Jeff "You really going to take that from her [povname]?"

    scene Schoolintro22 with dissolve

    povname "I don't think calling her names is going to change anything."

    scene Schoolintro23 with dissolve

    Jeff "Damn man, you really are growing soft."

    povname "Yeah, and with each day you seem even more dull."

    Jeff "Haha, whatever man."

    Jeff "Anyway, "

    extend "I think it's time to go in."

    scene Schoolintro24 with dissolve

    povname "(I don't know if something is wrong with me, or it's just that the whole world is fucked.)"

    povname "(Most of my life i didn't even care about these things, but now...)"

    povname "(I should talk to Caroline about these things, maybe she will have some advice.)"

    scene Schoolintro25 with dissolve

    povname "(Here she comes...)"

    povname "(Man, how is it that I'm the only person that finds her attractive.)"

    scene Schoolintro26 with dissolve

    povname "(As always, both of 'em are talking during the lesson.)"

    povname "(I wouldn't give a care in the world about these math lessons if it wasn't for {b}Susan{/b}..)"

    pause 1

    play sound "audio/Deskbang.mp3" volume 0.7

    scene Schoolintro28 with vpunch

    Susan "{b}JENNIFER AND JULY, CAN BOTH OF YOU STOP YAPPING ALREADY!?{/b}"

    pause 1

    scene Schoolintro27 with dissolve

    Susan "{b}OVER HALF OF THIS CLASS IS GOING TO FAIL MATH, AND NONE OF YOU ACTUALLY GIVE A DAMN!{/b}"

    scene Schoolintro29 with dissolve

    Jeff "Ehh...?"

    scene Schoolintro30 with dissolve

    Jeff "Whatever..."

    scene Schoolintro32 with dissolve

    Susan "I'm talking about YOU {b}Stacy{/b} also."

    extend " For how many more years do u want to {i}dwell{/i} in this school?"

    pause 1

    scene Schoolintro31 with dissolve

    povname "(First time I've ever seen her mad like this...)"

    Susan "[povname] is the only person listening in this class, {b}and he is not even failing my class{/b}!"

    povname "Huh...?"

    pause 1

    scene Schoolintro33 with dissolve

    Susan "[povname] you are the only reasonable person in this class, and you know what?"

    pause 1

    scene Schoolintro34 with dissolve

    Susan "And i think it's a good time for a {i}reward..{/i}"

    povname "Wha-.."

    stop music

    pause 0.5

    scene Schoolintro35 with dissolve

    Susan "Come up here {i}{b}[povname]...{/b}{/i}"

    pause 1

    play sound "audio/Cloth.wav" volume 0.7

    scene Schoolintro36 with dissolve

    pause

    Susan "{i}You like what you see..?{/i}"

    Susan "[povname].... You are the only person who treats me with respect in this hole.."

    Susan "And you won't believe how much time I've waited to do {i}this{/i}.."

    povname "This must be a dream..."

    pause 1

    show Schoolintro37 with dissolve

    povname "Wow...."

    Susan "Let me treat you like a king [povname]... Thats what having good grades in your life grants you.."

    pause 2

    play music "audio/Scenetheme.mp3" fadein 1.0

    show Schoolintro38 with dissolve

    pause 2

    show Schoolintro39 with dissolve

    Susan "Such a big cock, fitting for a person like You..."

    scene Schoolintro40 with dissolve

    Susan "(I'll make him remember this day, for the rest of his life...)"

    show Schoolintro41

    show Susanblow1 with dissolve

    pause 2

    Susan "{i}Mmm..Mmmm...{/i}"

    povname "(She doesn't even care about the others in the classroom..)"

    pause 1

    povname "(I guess it all paid off in the end..)"

    Susan "(Ohh my, my..."

    extend " I can barely breathe with his cock in my mouth...)"

    pause 1

    Susan "(I {i}{b}just{/b}{/i} can't wait to feel it inside me..)"

    povname "({i}This feels even better than i imagined...{/i})"

    pause 1

    Susan "(Don't be shy... I want to feel your cum, {b}deep{/b} down in my throat...)"

    povname "(I'm soo close..)"

    $ persistent.gallerySusan = True

    $ persistent.Susanblow1 = True

    pause 1

    scene Schoolintro42 with dissolve

    stop music

    povname "(Huh..?)"

    povname "(Why did she stop!?)"

    povname "Miss {i}i-is{/i} everything okay?"

    Voice "{i}Ohh... myy.. such {b}Lewd{/b} fantasies holed up in your mind{/i}..."

    Voice "{i}You are perfect for this{/i}..."

    povname "(What the-)"

    scene Schoolintro43 with dissolve

    play music "audio/Creepyambient.mp3" fadein 1.0

    pause 1

    povname "({i}I-i can't move{/i}.)"

    Voice "{i}This must've been the happiest dream of your life{/i}.."

    Voice "{b}But I must not let you release your tension..{/b}"

    pause 1

    scene Schoolintro44 with dissolve

    Voice "Soo much potential hides within you."

    Voice "And I plans for you which you will really {i}{b}enjoy{/b}{/i}..."

    Voice "{b}{i}Let us get acquainted.{/i}{/b}"

    scene black

    pause

    stop music

    narrator "..."

    pause

    scene Schoolintro45 with slowdissolve

    play music "audio/Mainbackgroundmusic.mp3" fadein 1.0

    povname "(What a surreal dream.)"

    povname "(But {b}damn{/b}, they always end at the good part.)"

    povname "(But what was that creature doing there.)"

    stop music

    Voice "Calling somebody a {b}creature{/b} before we share names is kinda rude [povname]."

    scene Schoolintro46 with vpunch

    povname "{b}WHAT{/b}"

    scene Schoolintro48 with vpunch

    povname "WHO ARE YO-"

    Voice "Screaming isn't welcoming either."

    povname "BUT-"

    scene Schoolintro48 with dissolve

    Voice "Let {i}me{/i} explain all of this first, then you can proceed with your {i}mad{/i} ramblings."

    povname "..."

    povname "(What the fuck.)"

    scene Schoolintro49 with dissolve

    Namaah "Okay,"

    play music "audio/Mainbackgroundmusic.mp3" fadein 1.0

    extend " now,"

    extend " my name is Namaah and I'm a demoness, and i have a proposition for {b}You{/b}"

    Namaah "I'm in a dire situation,"
    extend " in short just not to bore You, I'm in a need of an {b}Incubus{/b}."

    povname "Okay..."
    extend " But, I'm not an incubus."

    Namaah "{i}Ehhh{/i}.... I need to make a contract with You."

    povname "Yeah that doesn't sound sketchy at all."

    scene Schoolintro50 with dissolve

    Namaah "I know this isn't the best way of approaching You about this, "

    extend "but I haven't even told you the terms yet, and you may find them very {b}attractive{/b}."

    povname "Emmm,"

    extend " {i}okay{/i}? I'm listening."

    scene Schoolintro51 with dissolve

    Namaah "Good,"

    extend " so,"

    extend "  my contract will benefit you with unmatched sexual prowess, provided by my powers that i offer at anytime."

    scene Schoolintro55 with dissolve

    Namaah "Aside from that after signing the contract my body will be yours..."

    povname "Huh..."

    scene Schoolintro53 with dissolve

    Namaah "But as you may think there is a catch to all this, Your mission will be to satisfy enough needs of women on this earth."

    Namaah "And as you may know, there are not that many males in this world, and women's needs grow day by day."

    Namaah "When you satiate enough lust in this world, our contract will be completed and you will be free of this task."

    povname "I.. don't know, I'm not really buying it that much."

    povname "All of this just sounds really sketchy to me."

    Namaah "Hmmmm...."

    scene Schoolintro52 with dissolve

    pause

    Namaah "You know [povname]... Women like Susan are really alone... They need some satisfaction in their lives..."

    scene Schoolintro58 with dissolve

    pause

    Namaah "{i}Imagine not only experiencing Her lips, but Her other {b}assets{/b} on her vuloptuous body{/i}..."

    povname "Are you trying to say that I..."

    scene Schoolintro59 with dissolve

    Namaah "{i}Yess{/i}..."

    scene Schoolintro60 with dissolve

    pause

    Namaah "So what do you think about my offer, does it interest {i}You{/i}?"

    povname "(I can't pass this offer, just thinking about all of this makes me go crazy...)"

    povname "Okay, I might regret this, but if these are all of the terms,"

    extend " then I agree."

    scene Schoolintro61 with dissolve

    Namaah "{i}{b}Good...{/i}{/b}"

    Namaah "I assure You, this will be the {b}best decision{/b} of Your life..."

    povname "Thanks..? By the way how do you even know my name?"

    scene Schoolintro57 with dissolve

    Namaah "A demon has appeared in Your room, and You are wondering why I know Your name?"

    povname "Yeah... {i}whatever{/i}."

    pause 1

    scene Schoolintro56 with dissolve

    Namaah "You know..."

    extend " taking into consideration that you really like rewards..."

    Namaah "I'm going to show you the reason {i}why{/i} I interrupted You..."

    scene Schoolintro62 with dissolve

    Namaah "But first..."

    scene Schoolintro63 with dissolve

    povname "{b}Wow{/b}... what is that?"

    Namaah "A mark of an incubus, the starting gift of our contract."

    scene Schoolintro64 with dissolve

    Namaah "But don't trouble Your mind with nonsense [povname]..."

    Namaah "Tell me [povname]..."

    extend " What do You think about {b}Caroline{/b}?"

    povname "What are you implying?"

    extend " She's my [Carolinerelation]."

    scene Schoolintro65 with dissolve

    Namaah "{b}Don't try to fool Me, [povname].{/b}"

    extend " I know how You feel about Her looks."

    scene Schoolintro66 with dissolve

    Namaah "Your relation with Her doesn't change anything..."

    scene Schoolintro67

    Namaah " And who knows..."

    scene Schoolintro68 with dissolve

    Namaah "{i}Maybe She is attracted to You too...{/i}"

    povname "Can you stop putting these thoughts inside my head?"

    extend " She is my {b}[Carolinerelation]{/b}, it's better for things to stay the way they are."

    povname " And, how do you know her name?"

    scene Schoolintro69 with dissolve

    Namaah "I know a lot more than You think."

    povname "({i}Cryptic...{/i})"

    scene Schoolintro70 with dissolve

    Namaah "The usage of sarcasm doesn't make Your mental gymnastics any more {i}intelligent{/i}."

    povname "(Great, and now she can read my mind.)"

    Namaah "{i}Come to her room [povname].{/i}"

    scene Schoolintro71 with dissolve

    povname "(She just vanished like that...)"

    povname "(What is she trying to do?"

    extend " I don't like this one bit.)"

    povname "(But maybe she isn't trying to do anything malicious...)"

    jump CarolineRoomIntro

    label CarolineRoomIntro:

    scene Schoolintro72 with dissolve

    povname "Well, here goes nothing..."

    pause 1

    scene Schoolintro73 with dissolve

    pause 1

    scene Schoolintro74 with vpunch

    povname "Huh!?"

    scene Schoolintro75 with dissolve

    povname "What's.."

    play sound "audio/Cloth.wav"

    scene Schoolintro76 with dissolve

    pause 1

    scene Schoolintro77 with dissolve

    povname "They look even better upclose..."

    scene Schoolintro78 with dissolve

    Namaah "She is waiting [povname]."

    Namaah "Slide Your cock between Her breasts..."

    extend " And don't worry She won't remember anything."

    povname "I feel like this is a trap..."

    Namaah "Would i really try to trick You like that when I need Your help?"

    Namaah "Think straight [povname], and let these thoughts go..."

    extend " You have such a beauty infront of You..."

    Namaah "I know that being in a situation like this-..."

    povname "..."

    povname "Fuck it."

    play sound "audio/slap.wav"

    scene Schoolintro81 with vpunch

    Namaah "{i}Ohh... Such a horny good {b}boy{/b}...{/i}"

    Namaah "Good... Very good..."



    stop music fadeout 1.0

    show Carolineboobjob1 with dissolve

    play music "audio/Scenetheme.mp3" fadein 1.0

    povname "{i}Ahhh{/i}..."

    pause

    Namaah "It's fun, watching you {b}squirm{/b} like that..."

    Namaah "The real thing feels a lot better, doesn't it?"

    povname "{i}Mhmm{/i}...."

    pause

    povname "(I can't believe this...)"

    povname "(I've always wanted to fuck these huge breasts...)"

    pause

    Namaah "You seem like a perfect fit for Her."


    Namaah "You don't know this but, She is really enjoying herself despite being hypnotized..."

    pause

    Namaah "I can see both of you getting along quite nicely."

    povname "(I didn't know she can be this lewd...)"

    Namaah "And i can see a proper use for Her {i}talents{/i}..."

    pause

    Namaah "She's getting impatient [povname]..."

    pause

    povname "Fuck..."

    povname "I'm going to blow..."

    Namaah "Don't worry, you can cum on Her breasts..."

    pause



    Namaah "{b}Come on let it out{/b}..."

    pause 1

    play sound "audio/Cum1.mp3"

    scene Schoolintro82 with vpunch

    pause

    play sound "audio/Cum2.mp3"

    scene Schoolintro83 with vpunch

    pause

    scene Schoolintro84 with dissolve

    stop music fadeout 1.0

    Namaah "{i}Such a good boy{/i}..."



    Namaah "And what a big load..."



    Namaah "{i}Looks really tasty{/i}..."



    povname "Ughh... What about the mess, won't she recognize what she is covered in?"

    pause 1

    scene Schoolintro85 with dissolve

    $ persistent.Carolineboobjob1 = True

    $ persistent.galleryCaroline = True

    pause 1

    Namaah "Don't worry, She wont waste such a tasty meal..."



    Namaah "Come to Your room, We are not finished {i}yet{/i}..."

    pause 1

    scene Schoolintro86 with dissolve

    Namaah "I hope You are satisfied."

    Namaah "Because it's going to be even better..."

    scene Schoolintro87 with dissolve

    pause

    Namaah "Get on the bed."

    play sound "audio/Cloth.wav"

    scene Schoolintro88 with dissolve

    Namaah "I'll make you feel proper {b}ecstasy{/b}..."

    play sound "audio/Cloth.wav"

    scene Schoolintro89 with dissolve

    Namaah "You dont even know how lucky You are..."

    scene Schoolintro90 with dissolve

    Namaah "I'm going to play with You for a {i}while{/i}..."

    pause

    show Namaahfootjob1 with dissolve

    play music "audio/Scenetheme.mp3" fadein 1.0

    Namaah "It feels good, doesn't it?"

    povname "{b}Faster{/b}... {b}{i}Please{/b}{/i}..."

    Namaah "{i}I don't think so{/i}..."

    pause

    Namaah "If you last long enough I'll make You remember this day for a {b}long{/b} while..."

    povname "(I can't believe it, I feel soo horny like I didn't cum just a while ago...)"

    povname "(Must be that weird symbol that she gave me..)"

    scene black with dissolve

    stop music

    $ persistent.Namaahfootjob1 = True

    $ persistent.galleryNamaah = True

    narrator "Some time later"

    scene Schoolintro91 with dissolve

    pause

    Namaah "You were such a {i}patient{/i} {i}good{/i} boy..."

    scene Schoolintro92 with dissolve

    Namaah "I think it's time for the finale."

    povname "(Finally...)"

    scene Schoolintro93 with dissolve

    pause

    play sound "audio/slide.wav"

    scene Schoolintro94 with dissolve

    Namaah "Mmmm... For a fresh incubus, You feel really good..."

    Namaah "I knew You were the right choice."

    pause

    show Namaahfuck1 with dissolve

    play music "audio/Scenetheme.mp3" fadein 1.0

    pause

    povname "({i}Fuck...{/i})"

    pause

    Namaah "It's going to be even better from here."

    Namaah "Just imagine how many women are there to satisfy..."

    Namaah "And if you will be good enough, You might even become a proper incubus..."

    povname "Your pussy feels amazing..."

    povname "And these juicy, hot red breasts..."

    Namaah "Ohh my... such a way with words [povname]."

    Namaah "You know how to make a woman feel {i}special{/i}."

    Namaah "Fill me up [povname]..."

    extend " Don't make me wait any longer!"

    pause

    Namaah "You are a sturdy one aren't You..."

    extend " Good..."

    extend " I'll have a lot of fun toying with You..."

    pause 1.0

    povname "I'm going to cum soon..."

    Namaah "{i}{b}Good{/i}{/b}, shoot as {i}deep{/i}, and as {i}much{/i} as You can..."

    Namaah "Come on, [povname] fill me up with that huge cock of Yours."

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

    Namaah "{i}Ahhhh... Finally{/i}"

    povname "I'm spent..."

    Namaah "Mmmmm... You taste even better..."

    Namaah "I must say... I enjoyed every second of this..."

    scene Schoolintro98 with dissolve

    pause

    Namaah "And you did well, You deserve some sleep..."

    scene Schoolintro99 with dissolve

    Namaah "{i}Goodnight, my little devil{/i}..."

    povname "(Mhmmm...)"

    pause

    scene black with slowdissolve

    $ persistent.Namaahfuck1 = True

    narrator "..."

    narrator "Meanwhile, somewhere else..."

    scene Dreamintro1 with dissolve

    "???" "She really is stubborn..."

    scene Dreamintro2 with dissolve

    "???" "I wonder how many lives She is willing to sacrifice to reach her goal..."

    scene black with slowdissolve

    narrator "..."

    pause

    Namaah "Wake up Sleepyhead..."

    scene Schoolintro100 with slowdissolve

    povname "Huh...?"

    scene Schoolintro101 with slowdissolve

    Namaah "Get up, We have to talk."

    scene Schoolintro102 with dissolve

    Namaah "Today is your first day of training."

    Namaah "And it is important that you..."

    povname "(She is still naked after that night...)"

    povname "(Her breasts look amazing...)"

    Namaah "Are you listening to me [povname]?"

    scene Schoolintro103 with dissolve

    povname "Y-yeah i'm listening."

    Namaah "Huh... I can see that you got a little {i}excited{/i}..."

    scene Schoolintro104 with dissolve

    Namaah "My little soldier always at the ready..."

    Namaah "It's really good that you find me attractive..."

    povname "(I wish I could pound her right now...)"

    Namaah "If You perform well, all of these {i}nasty{/i} thoughts of yours can become a reality..."

    scene Schoolintro105 with dissolve

    Namaah "But, now is not the time for this."

    Namaah "We must discuss what to do next."

    povname "Yeah, i'm listening."

    scene Schoolintro106 with dissolve

    Namaah "Now, if You want to increase Your strength as an incubus, you must feed on the lust of women in this world."

    povname "Okay, but how do i {i}feed{/i} on their lust?"

    scene Schoolintro107 with dissolve

    Namaah "All You need to do is to have sex with them, dummy."

    Namaah "Would it be by making them feel good, or even such a simple thing as a handjob will do the trick."

    scene Schoolintro108 with dissolve

    Namaah "When the power of Your mark increases You will be able to affect more women, and the effect itself will be stronger"

    povname "And... how do i use my powers?"

    Namaah "A simple touch will suffice."

    scene Schoolintro109 with dissolve

    Namaah "And I have a perfect candidate for Your first task."

    Namaah "After inspecting some of Your memories, I've concluded that Your friend Stacy is lewd enough for You to test the mark's power"

    povname "You did what!?"

    Namaah "Don't worry I already forgot most of the embarrassing stuff."

    povname "Ughhhh..."

    povname "Okay, i don't mind it that much. But can't i just train with you?"

    scene Schoolintro110 with dissolve

    Namaah "{i}Hahaha{/i}, I'm really happy you like me..."

    Namaah "But You won't get as much power from training with me."

    Namaah "...And I'll keep your request in mind..."

    scene Schoolintro111 with dissolve

    Namaah "{i}But, now lovely [povname]... You need to test Your powers on Stacy...{/i}"

    Namaah "{i}After you finish your task, We'll talk about the training part more.{/i}"

    scene Schoolintro112 with dissolve

    pause

    scene Schoolintro113 with dissolve

    povname "And she's gone again."

    povname "Wow... I'm {i}really{/i} starting to like all of this."

    povname "But now, I guess finishing her task is something i should focus on."

    povname "I can use my phone to message Stacy to maybe meet her somewhere private."

    povname "And i think i just got the right idea."

    $ Quest1 = True

    play music "audio/Mainbackgroundmusic.mp3" fadein 1.0

    jump home
