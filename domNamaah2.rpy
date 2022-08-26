default NFTQ = False
default NFTF = False
default domDMona = False

label domNamaahcall:

    scene Namaahcall1 with dissolve

    Namaah "Did you need me for something, [spovtitle]?"

    menu domNamaahtrade:

        "Sex Menu":

            if Quest1 == True:

                Namaah "Sorry, [spovtitle] - I can't really do that again until your power has had a chance to stabilize."

                Namaah "Using it on Stacy a time or two should be enough, but until then I'm off limits for your own safety."

                jump home

            else:

                povname "Time to fuck, slut."

                Namaah "As always, you have such a way with words."

                if NFTF == False:

                    povname "What can I say, it makes me happy to be mean to you."

                    Namaah "I am aware, [spovtitle].{size=-20} It's a good think I like it...{/size}"

                    povname "I knew you'd warm up to it."

                    Namaah "You should have at least pretended not to hear that!"

                    Namaah "(Sigh) What would you like me to do for you?"

                    $ NFTF = True

                if NFTF == True:

                    menu:

                        "Ride me with the lights out":

                            Namaah "Oh, again? I thought you'd want that to be a little brighter this time."

                            povname "I'm feeling romantic."

                            Namaah "... I don't know how to deal with you sometimes."

                            povname "It's more fun that way, isn't it?"

                            povname "Now close the curtains and let's get on it with it, you adorable demonic whore."

                            Namaah "Yes, [spovtitle]."

                            jump domNamaahRideRepeat

                        "I changed my mind":

                            Namaah "Oh. I'm actually kind of disappointed to hear that."

                            povname "I might still change my mind."

                            jump domNamaahtrade

        "Favor Shop":
            menu Favorshop:

                "What do you mean by Favor Shop?":

                    Namaah "The process of converting lust into power isn't a lossless one, unfortunately."

                    Namaah "Every time you gain strength from interacting with a girl, there's some energy that can't be entirely stored in the mark I gave you."

                    Namaah "I am still able to capture that energy and put it to use in other ways, but I thought you might enjoy getting some benefit from it as well."

                    Namaah "For ease of naming, I've just decided to call it 'Favor'."

                    Namaah "So, I'll collect and keep track of any Favor you've generated, then you can trade it in like a currency."

                    povname "What can I trade it for?"

                    Namaah "As I belong to you thanks to the contract regardless, I can't really withold anything from you should you demand it."

                    Namaah "From time to time if I think up something fun or different to do though, I'll have it as a shop option so you can 'unlock' it."

                    Namaah "Mainly this is just to keep things fun for you."

                    Namaah "In reality I imagine you'll be generating more favor than you know what to do with."

                    Namaah "Oh, also - if you find some interesting items as you go about your daily life, I might be able to put the Favor to more practical use."

                    Namaah "I can use it to conjur some rather enjoyable {i}dreams{/i} for you."

                    povname "I'm slightly concerned by the way you said dreams."

                    Namaah "It's just your imagination~"

                    povname "... I'm gonna skip over that for now, but I'll keep an eye out for items that could be used for these dreams."

                    povname "This does seem entertaining, even if I feel like it's more for your fun than for mine, so good job. I appreciate the effort."

                    jump Favorshop

                #"Boobjob for 2 favor":
                    #if favor >= 2:
                        #jump Namaahboobjob
                    #else:
                        #jump Namaahnofavor

                "Dreams":
                    menu domDreams:

                        "Kitsune costume" if kitsuneears == True and kitsunepart1 == False:

                            Namaah "Oh, fox ears?"

                            Namaah "I can generate a nice dream for you if you'll let me use 3 Favor."

                            menu:
                                "Sounds interesting, let me see it":

                                    if favor >= 3:

                                        Namaah "{i}As you wish.{/i}"

                                        scene black with slowdissolve

                                        $ favor -= 3

                                        jump domStacykitsune

                                    else:

                                        jump domNamaahnofavor

                                "Maybe next time":
                                    Namaah "I understand. Feel free to save it if you wish. I could always thank you for your efforts in the flesh for it too, [spovtitle]."

                                    Namaah "Ask me again any time you'd like to try."

                                    jump domNamaahtrade

                        "Streetwalking Witch" if domDMona == False:

                            Namaah "I've got another dream for you, if you'd like."

                            Namaah "It's not your beloved animal eared beauties, but I think you'll like it anyway."

                            Namaah "I'll need to use 10 favor to let you see it, though. Would you like to use it?"

                            menu:

                                "Sounds like fun, show me":

                                    if favor >= 10:

                                        Namaah "{i}Then, sweet dreams...{/i}"

                                        scene black with slowdissolve

                                        $ favor -= 10

                                        $ domDMona = True

                                        jump domMona1

                                    else:

                                        jump domNamaahnofavor

                                "Go back":

                                    Namaah "Changed your mind? Something else, perhaps."

                                    jump domDreams

                        "Replay dreams":
                            menu:
                                "Kitsune" if kitsunepart1 == True:

                                    Namaah "Oh, you wanted to have this dream again?"

                                    Namaah "You won't be able to change anything that's happened within, just so we're clear."

                                    Namaah "I do hope you enjoy it anyway, [spovtitle]."

                                    Namaah "Sweet dreams~"

                                    scene black with slowdissolve

                                    jump domStacykitsune

                                "Streetwalking Witch" if domDMona == True:

                                    Namaah "I see you took a liking to her! Not that I can blame you."

                                    Namaah "I did say you'd probably like it."

                                    Namaah "Don't forget, the dream will play out the same this time around, too."

                                    Namaah "Have fun, [spovtitle]~"

                                    scene black with slowdissolve

                                    jump domMona1

                                "Go back":

                                    Namaah "Changed your mind on seeing a dream again?"

                                    Namaah "If there's any others you'd like to have again, just say the word."

                                    jump domDreams



                        "Go back":
                            jump domNamaahtrade

                "Go back":
                    scene Namaahcall1 with dissolve
                    jump domNamaahtrade
        "Ask her questions":

            if level >=3 and NFTQ == True:

                jump domNamaahquestion

            povname "Have I proven my worth enough to have you answer some questions now, Namaah?"

            if level <=2:

                Namaah "Not yet. I need you to try a little harder before I'll be willing to give you more details."

                Namaah "Strengthen yourself, and you shall have more of my cooperation."

                povname "I could just order you to tell me according to the contract."

                Namaah "You could, but I don't believe you are the type of man who will."

                povname "... Fine."

                jump domNamaahtrade

            if level >=3 and NFTQ == False:

                Namaah "Honestly, I'd like you to make more progress before I tell you everything."

                Namaah "You have shown that you're willing to work with me, though."

                Namaah "You'd have a very different answer to this if you'd tried to dominate me entirely against my will --"

                Namaah "Or worse, caused damage to yourself and others by trying to forcefully use my powers."

                Namaah "I'd say that your self control and good will deserves some answers."

                Namaah "What would you like to know?"

                $ NFTQ = True

            menu domNamaahquestion:

                "Is there a reason you chose me and this world?":

                    scene Namaahcall2 with dissolve

                    Namaah "A fair question."

                    scene Namaahtalk4 with dissolve

                    Namaah "This world is an anomaly among all others I know of."

                    povname "How so?"

                    Namaah "You've felt it yourself. You instinctively know that there's something wrong when you seem to crave and desire women, when no others seem to."

                    scene Namaahtalk3 with dissolve

                    Namaah "Your world has been twisted. The natural desire of men to breed and propagate the species has fallen nearly out of existence."

                    scene Namaahcall3 with dissolve

                    Namaah "The birthrate has declined drastically, and of those precious few children born - they are overwhelmingly female."

                    Namaah "This is the only place I know of that this has happened throughout all my existence."

                    scene Namaahtalk5 with dissolve

                    Namaah "There are still those that are trying to resist the decline of civilization by force."

                    scene Namaahtalk6 with dissolve

                    Namaah "The governments of your world have started changing laws and implementing policies to try and control the issue."

                    scene Namaahcall3 with dissolve

                    Namaah "Unfortunately at this rate, there will be nothing left of the humans in just a few short years."

                    povname "[Carolinerelation] had mentioned things like that before, too. I guess I never really paid attention to how serious it was."

                    scene Namaahcall1 with dissolve

                    Namaah "It is a very serious thing."

                    scene Namaahcall7 with dissolve

                    Namaah "Your women have been forced by their predecessors to seek financial interests and pursue careers."

                    Namaah "It's truly a shame they no longer know the importance of raising a family - of nurturing their own futures."

                    povname "You say that as if it's something you can't have."

                    scene Namaahcall3 with dissolve

                    Namaah "That's not important to the discussion."

                    povname "Alright."

                    povname "You've answered 'why this world' - how about you move on to 'why me'?"

                    povname "The government already has men put to work doing exactly what you hope. Wouldn't the experienced have fit the bill?"

                    scene Namaahtalk5 with dissolve

                    Namaah "Hah. Hahahaha!"

                    scene Namaahtalk4 with dissolve

                    Namaah "Do you honestly believe that in this wide world of yours, there is any man so desiring of pleasure and power -"

                    Namaah "That he would stake his life on being able to control and dominate a Demoness?"

                    povname "... When you put it that way, I suppose not."

                    scene Namaahcall6 with dissolve

                    Namaah "The men your governments have put to work are nothing more than sex slaves to sate the disproportionate lust and loneliness of women."

                    Namaah "They do not have either the will or ability to control or lead others. They are themselves lead by fear of force and the desire of money, nothing more."

                    scene Namaahtalk4 with dissolve

                    Namaah "You, my dear [spovtitle] are more of an anomaly than the rest of the world."

                    scene Namaahcall2 with dissolve

                    Namaah "I hadn't even imagined that you'd have such force of will when I approached you."

                    Namaah "Let alone that you would exercise that will while still being conscious of others."

                    Namaah "At the sake of flattering you, I would call it the correct disposition for a King."

                    povname "That's an unexpected compliment. Thank you for your honesty."

                    scene Namaahcall6 with dissolve

                    Namaah "It's exactly moments like this that make me say it."

                    scene Namaahtalk4 with dissolve

                    Namaah "You have not puffed yourself up with pride or arrogance even when praised."

                    Namaah "Your natural understanding of how to control yourself leads to an equally natural understanding of how to control others."

                    Namaah "You are needed in this world, [povtitle]. The future of it is essentially in your hands alone."

                    scene Namaahcall6 with dissolve

                    Namaah "Or more specifically, in your pants!"

                    povname "I would criticize you for the joke, but it was adorable and honestly I'd rather encourage that."

                    scene Namaahcall5 with dissolve

                    Namaah "I've not behaved like this with a mortal in all my long life, [spovtitle]. I hope you remain aware of how unique our relationship is."

                    Namaah "I agreed to and abide by the contract because I am putting my trust in you. Don't let me down."

                    scene Namaahcall1 with dissolve

                    jump domNamaahquestion

                "Are there more like you?":

                    scene Namaahcall2 with dissolve

                    Namaah "More Demons and Demonesses?"

                    povname "Yeah. It seems like you'd lead an awfully lonely life if there weren't."

                    scene Namaahcall3 with dissolve

                    Namaah "... There are. I don't want to go into detail about that yet."

                    povname "Alright. I'll ask again in the future. You can tell me when you're ready."

                    scene Namaahtalk5 with dissolve

                    Namaah "Thank you for understanding."

                    scene Namaahtalk2 with dissolve

                    Namaah "Though having said that, there are myriads of other mythical creatures around, too."

                    povname "Really? Any that I might recognize?"

                    scene Namaahcall7 with dissolve

                    Namaah "Mythology is mostly the same across many worlds, so you would likely know many."

                    scene Namaahcall5 with dissolve

                    Namaah "Succubi and of course their male counterparts, the incubi; Lycanthropes and other similar half-beasts; Fairies and Ogres, Trolls and Dragons..."

                    scene Namaahcall3 with dissolve

                    Namaah "... Even some of the dark high ancient gods."

                    pause 3

                    scene Namaahcall4 with dissolve

                    Namaah "Perhaps you'll run across them one day if you continue down this path of power. The life of an Incubus is long, after all."

                    povname "What about the girls from the dreams you've shown me? Do they exist?"

                    scene Namaahcall6 with dissolve

                    Namaah "In a sense."

                    scene Namaahcall4 with dissolve

                    Namaah "Perhaps they as individuals and their worlds do not exist. Perhaps they do. In general though, yes - their kind and similar realms do exist."

                    povname "Would it be possible to search one out and bring them to my world?"

                    povname "I'm sure there are outcasts that would look favorably upon being mine here rather than suffering in their current condition."

                    scene Namaahcall6 with dissolve

                    Namaah "It is possble, but it would take a great amount of effort and favor to make it happen. Depending on how things go, it may even be a girl you are familiar with."

                    povname "You mean...?"

                    scene Namaahtalk1 with dissolve

                    Namaah "I can't answer any more questions about it for now."

                    povname "Alright. I'd say that's worth putting in the effort for regardless."

                    scene Namaahcall1 with dissolve

                    jump domNamaahquestion


                "Can you give me any details about how these powers work?":

                    scene Namaahcall2 with dissolve

                    Namaah "Not without many years of study in magical theory."

                    scene Namaahcall5 with dissolve

                    Namaah "The simplest answer is that you have an energy about you - an aura of sorts."

                    scene Namaahcall4 with dissolve

                    Namaah "I likened it before to growing a third arm. Exercising your power through activies of lust and sex convert those energies into your own strength."

                    scene Namaahtalk4 with dissolve

                    Namaah "You've seen already how even if it's not full control, you are able to influence the minds of mortals."

                    scene Namaahtalk3 with dissolve

                    Namaah "But as it is, think of it like a child trying to move a boulder. At most, it is a gentle push you can exert upon the mind."

                    Namaah "Even then, you have to be in physical contact to plant the seed of that control and... attune them to your aura, as it were."

                    scene Namaahcall5 with dissolve

                    Namaah "The more you feed on that energy created though, the greater the range your aura can influence."

                    Namaah "Consider it a change from the gentle push of a child, to the much stronger force of a man."

                    scene Namaahtalk3 with dissolve

                    Namaah "A child may nudge the boulder, but a grown man may move it. Beyond that, he can even move it from a distance by controlling others."

                    Namaah "In the same way, you will at least be able to break down mental barriers through your increased strength, and you may affect a larger area as well."

                    scene Namaahcall3 with dissolve

                    Namaah "You may gain new abilities as you grow, too - but it's hard to tell what kind of abilities they may be while you're yet a fledgling."

                    scene Namaahtalk5 with dissolve

                    Namaah "So far, you are leaning towards abilities akin to mind control or puppeteering as you'd hoped."

                    povname "Neat."

                    povname "Thank you for the information."

                    scene Namaahcall1 with dissolve

                    jump domNamaahquestion


                "What happens to the women I control and manipulate with your power?":

                    povname "You'd said before that no harm would come to them, but what else happens?"

                    scene Namaahcall7 with dissolve

                    Namaah "Is there something specific you're asking about?"

                    povname "Mainly if they'll remember anything from the interactions. Having them recall it and then run to the police or the news would be... bad."

                    scene Namaahtalk4 with dissolve

                    Namaah "You've seen first hand that they do carry over the memories, correct?"

                    scene Namaahtalk2 with dissolve

                    Namaah "Both Stacy and your [Jenniferrelation] were aware of what happened and the things they felt."

                    Namaah "They may not understand why their feelings for you changed so quickly, but they will be aware of it."

                    scene Namaahcall3 with dissolve

                    Namaah "Like a sailing ship moved by the wind, they'll notice the results, but be unaware of the cause so long as it's not too drastic."

                    povname "What about the puppeteer type abilities you said I was leaning towards?"

                    scene Namaahcall4 with dissolve

                    Namaah "If you end up developing those particular abilities further, then like I mentioned at the time of the contract -"

                    scene Namaahtalk3 with dissolve

                    Namaah "You would be able to have intense, immediate, absolute control for as far as your skill at the time would allow."

                    Namaah "It would cause them to move and act exactly as you wished, but they would not remember anything of the encounter."

                    scene Namaahcall5 with dissolve

                    Namaah "I suppose it's like how you don't remember the time passing when you're asleep. You are simply aware of one moment, then the next. What happens between is irrelevant."

                    povname "Interesting. Thank you for explaining."

                    scene Namaahcall1 with dissolve

                    jump domNamaahquestion


                "You said you're a Demoness, but what does that mean exactly?":

                    scene Namaahcall3 with dissolve

                    Namaah "There's still not much I'll disclose on the subject, but I'll tell you a little."

                    scene Namaahtalk6 with dissolve

                    Namaah "A Demoness is the female form of a Demon. The place in most mythos called 'Hell' is actually more of a melting pot, or a forge for the various worlds."

                    Namaah "As a natural born inhabitant of the realm, I am able to freely traverse any worlds I know of since I am aware of their relative locations."

                    povname "Natural born? You mean you're not some of spirit?"

                    scene Namaahtalk2 with dissolve

                    Namaah "In a sense I am, but my kind too is generally born the same way humans are, though it is a Matriarchal society. Most of our kind regard the Queen as our Mother."

                    scene Namaahcall3 with dissolve

                    Namaah "Regardless of if she gave birth to us individually or not."

                    scene Namaahcall4 with dissolve

                    Namaah "I trust you understand now why I said that the sense of distance you felt with Caroline was unnecessary for our kind."

                    povname "It does make more sense knowing that."

                    povname "And I certainly don't feel the repulsion I had expected I otherwise would."

                    scene Namaahtalk1 with dissolve

                    Namaah "... That's actually only part of it. The other part was just that your desires outweigh your reason in that regard."

                    Namaah "Were you not so strong willed, it may have taken far longer to come to grips with finding those in your household sexually viable."

                    scene Namaahtalk2 with dissolve

                    Namaah "Consider the transformation in your case the difference between putting a ramp up a small set of stairs and trying to climb a ramp to the top of a building."

                    scene Namaahcall4 with dissolve

                    Namaah "Your sense of how important that boundary is was significantly lower to begin with."

                    povname "Fair enough."

                    scene Namaahcall2 with dissolve

                    Namaah "I realize the conversation took a turn that might be unsatisfying, so I'll digress."

                    scene Namaahtalk6 with dissolve

                    Namaah "As Demons in a forge of worlds, we don't have many traits or abilites specifically tied to our race."

                    scene Namaahtalk4 with dissolve

                    Namaah "Though we do have powers that trend towards those our parents developed."

                    scene Namaahtalk3 with dissolve

                    Namaah "You already know that I can influence and control minds, so as your spiritual parent, it's likely your powers will develop similarly."

                    povname "Interesting. What about the 'lowly succubi' you talked about when we first met?"

                    scene Namaahtalk2 with dissolve

                    Namaah "Ah, yes. I suppose you would be curious about your counterpart, the Succubus."

                    scene Namaahtalk6 with dissolve

                    Namaah "What do you know about them from your worlds mythos?"

                    povname "Simple things mostly. They usually take the form of beautiful women adorned with wings and horns."

                    povname "Usually they're said to invade the dreams of men to suck out their souls and drive them mad - plus fucking them until they die."

                    scene Namaahcall6 with dissolve

                    povname "Honestly until I met you, I'd thought it was just an excuse historical cheaters used to try and escape consequences."

                    povname "Like how tribes in the mountains described a Wendigo in famine to justify their cannibalism."

                    scene Namaahcall4 with dissolve

                    Namaah "Don't even get me started on the Wendigo. Those nasty things."

                    scene Namaahtalk2 with dissolve

                    Namaah "For the most part you are correct though. Especially the part about them fucking you to death."

                    Namaah "Generally, they are creatures born of desire and twisted by uncontrolled negative emotions - insatiable desire for sex among them."

                    scene Namaahcall7 with dissolve

                    Namaah "Demons usually try and cull the ones that have been born twisted to protect fledgling worlds from their malice, but there are some that escape that fate."

                    povname "What about me? You said you were going to turn me into an Incubus - does that mean I'm just a lower level being driven mad?"

                    scene Namaahtalk4 with dissolve

                    Namaah "No, you're a special case. Though they are rare, we have at times turned men into Incubi before in order to help repopulate worlds after periods of intense war or disease."

                    scene Namaahtalk2 with dissolve

                    Namaah "In those cases though, we usually just inhabit a suitably disposed incubus inside a host body and let him go to work."

                    scene Namaahtalk6 with dissolve

                    Namaah "That wasn't an option here because of how twisted the world itself is. The presence of something like that would have only hastened it's destruction."

                    scene Namaahtalk4 with dissolve

                    Namaah "You, on the other hand, formed a contract with me to gain the powers without the possession. It's a unique situation."

                    scene Namaahtalk2 with dissolve

                    Namaah "Frankly, I don't know if your transformation will be into a complete incubus, or something entirely new as a result."

                    scene Namaahcall6 with dissolve

                    Namaah "At the very least, you've skipped the worst case scenario of losing yourself to the madness of lust. I'd expected to need to control you, but instead you've ended up reversing that."

                    Namaah "Unusual case upon unusual case, haha!"

                    povname "Hold up. Madness of lust?"

                    scene Namaahtalk4 with dissolve

                    Namaah "I told you just now that natural born succubi are only culled when they have twisted desires, yes?"

                    scene Namaahtalk2 with dissolve

                    Namaah "Even when having one inhabit a mortal body, they tend to be fixated on violating as many living creatures as they can."

                    Namaah "The mythos of Zeus, for example, was one such fellow possessed by an Incubus. That's why there's so many tales of his escapades with various creatures."

                    Namaah "Humans, spirits, horses... that one really didn't have any limits or distinctions. If it had a hole and a pulse, he was interested."

                    Namaah "While this is in general true of both natural born Succubi and Incubi..."

                    scene Namaahtalk6 with dissolve

                    Namaah "Intercourse with most creatures only staves off their lust. That's part of why they go mad - only fucking with another of their own kind gives them release from their desire."

                    Namaah "They can't usually breed successfully though as they are just empty incarnations of lust."

                    Namaah "Aside from the twisted ones we cull, the rest are mostly just left to their own devices to indulge in each other until they eventually just fade away... totally spent."

                    scene Namaahcall7 with dissolve

                    Namaah "Sad creatures, really. Though as you said when you feared me as a succubus, death by fucking is not the worst way to go. *giggle*"

                    povname "That's truly all they exist for?"

                    scene Namaahtalk4 with dissolve

                    Namaah "For the moment. Unfortunately we've yet to be able to break them from being slave to their desires."

                    povname "I see."

                    scene Namaahcall1 with dissolve

                    jump domNamaahquestion

                "Go back":

                    povname "I think that's all the questions I have for now. Thank you for your explanations."

                    Namaah "You're welcome, [povtitle]. I'm glad I could help."

                    povname "(Huh. No sass on that one. I wonder if she's just getting more comfortable with being submissive to me in general now?)"

                    Namaah "[spovtitle]."

                    povname "Right, right. Mind reading. Nevermind."

                    scene Namaahcall1 with dissolve

                    jump domNamaahtrade

        "About Jennifer" if Quest7 == True:

            $ persistent.Hannahrelation = Hannahrelation

            $ persistent.Carolinerelation = Carolinerelation

            $ persistent.Jenniferrelation = Jenniferrelation

            $ persistent.povname = povname

            scene Namaahcall6 with dissolve

            Namaah "That was quite the event wasn't it, [spovtitle]?"

            povname "Yep. What was going on in there to cause her to scream so much?"

            povname "I've heard her yell because of her quick temper, but screams of pleasure were entirely new."

            scene Namaahtalk2 with dissolve

            Namaah "That's probably the effect of the suggestion you planted in her."

            povname "Oh, I told her to think of me when she feels good because of the toy."

            Namaah "Correct. You didn't realize you'd put her into a pleasure loop with that."

            scene Namaahcall7 with dissolve

            Namaah "She'd think of you and get pleasure, then the pleasure would make her think of you."

            scene Namaahtalk2 with dissolve

            Namaah "I think the only reason she calmed down is because she passed out. I can only sense a general glow of happiness from her."

            scene Namaahtalk5 with dissolve

            povname "Hopefully that's enough to have her drop her guard with me."

            povname "Though the best case scenario would be to have completely removed the block and make her more vulnerable to my power."

            Namaah "I believe you've done more than enough to make that happen."

            scene Namaahtalk4 with dissolve

            Namaah "You should be careful about such things in the future, actually."

            scene Namaahtalk2 with dissolve

            Namaah "I didn't have to interfere this time, but pleasure loops can lead to consequences unless you keep a tight reign on them."

            povname "Fuck. That would have been good to know beforehand."

            scene Namaahtalk3 with dissolve

            Namaah "I told you before you went in, firsthand experience is better than being told."

            Namaah "A command given thoughtlessly or without restraints can lead to problems."

            Namaah "I felt it best for you to understand just how little it would take to cause harm with the power you've been given."

            scene Namaahtalk4 with dissolve

            Namaah "Rest assured, not only am I bound by the contract, but I still need your cooperation and ultimately, your skill."

            scene Namaahtalk5 with dissolve

            Namaah "I'd have stepped in had it honestly become dangerous."

            povname "Great power and responsibility, eh...?"

            povname "Alright. Although it could have been dangerous, you helped me learn safely. I'll take the lesson to heart."

            povname "Thank you."

            scene Namaahcall6 with dissolve

            Namaah "... That straightforward honesty is going to make me blush."

            Namaah "Plus I'm getting too used to being praised and thanked after feeling good. I think you got me a little wet, too."

            scene Namaahtalk5 with dissolve

            Namaah "In any case, unless she has an ironclad will like yours, your [Jenniferrelation] should be far more easily swayed."

            scene Namaahtalk2 with dissolve

            Namaah "That was actually my intention by giving you that dream of your teacher the night we formed our contract as well."

            povname "Ah."

            povname "That was a nice dream. I still haven't 'thanked' you for ending it early, come to think of it."

            scene Namaahcall7 with dissolve

            Namaah "Oh, come now! You gained supernatural powers, titfucked your [Carolinerelation], then fucked me in the span of an hour - AND you gained exclusive rights to me!"

            Namaah "Isn't that enough!?"

            povname "If I said no, would that get you wet?"

            scene Namaahcall6 with dissolve

            Namaah "... Hush."

            povname "Muwahaha!"

            scene Namaahtalk5 with dissolve

            Namaah "That is an awful evil laugh."

            povname "Perfect, that's what it was meant to be! But we got distracted on the thought of your fun-ishment."

            povname "Back on the subject of Jennifer. Exactly how far could the feedback loop manipulate or influence her?"

            scene Namaahtalk4 with dissolve

            Namaah "You've been a special case the entire time because of your surprising will. I only approached you that way because I believed you were inclined to accept to begin with."

            povname "You believe that my [Jenniferrelation] is inclined to open herself to me as well?"

            scene Namaahtalk6 with dissolve

            Namaah "She is, but she's trying to deny it to herself."

            scene Namaahtalk5 with dissolve

            povname "I'll take your word on it for now. Any thoughts on how to press the issue?"

            scene Namaahtalk6 with dissolve

            Namaah "Yes, I was hoping to get to that."

            scene Namaahtalk4 with dissolve

            Namaah "What's your current goal with Jennifer?"

            povtitle "The same as it is with all others - strengthen my control and influence with them until they're mine."

            scene Namaahtalk2 with dissolve

            Namaah "Then I'd suggest you start by talking to some of her friends. Not only will they have inside information on her, but you can also use that opportunity to get closer to them."

            scene Namaahcall7 with dissolve

            Namaah "If you've already shrunk that distance ahead of time, you'd also find it easier to corrupt them when your skills have matured enough to do so."

            povname "That does sound like a good place to start. Thanks."

            scene Namaahcall6 with dissolve

            Namaah "Mmph"

            povname "Haha, I'll have to keep in mind how often I thank you if I want to avoid turning my room into a swimming pool!"

            scene Namaahtalk5 with dissolve

            Namaah "Oh, hush!"

            scene Namaahtalk7 with dissolve

            povname "Not even a cloud of smoke she disappeared so fast this time!"

            povname "Heh. She's definitely getting cuter. Or at least, more fun to tease."

            povname "Now then, time to carry through and gather some info."

            povname "July is probably Jennifer's best friend. I'm not quite sure how to approach her, but I'll text her to start."

            povname "If I'm lucky, I'll convince her to meet me somewhere."

            povname "I forgot to check if Namaah had any more potential marks for me, but I don't want to rely on her evaluations forever either."

            povname "If I get the chance to start working on July, I might just take it regardless."

            $ Quest7 = False

            $ Quest8 = True

            $ julyfirsttext = True

            jump home






        "Dismiss Namaah":

            povname "That'll be all for now."

            Namaah "I understand. Call if you need me."

            jump home

label domNamaahnofavor:

    Namaah "Sorry [spovtitle], looks like you're short on Favor for the moment. You'll need to go interact with some girls before I've got enough power to do this."

    jump Favorshop
