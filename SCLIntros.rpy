init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_braille",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_braille:
    m 1eub "White dot, black dot, black dot, white dot, 2 white dots-"
    $ _history_list.pop()
    menu:
        "?":
            m 1lub "Er, half side black dots…"
            m 2lkb "Oh, I don’t even know how to describe this one elegantly. Black, white, black, white, black, white-"
            m 2hksdrb "Okay, no, this was a terrible idea."
            m 3hksdlb "I do get girlfriend points for the idea, don’t I?"
            m "Hahaha."
            m 4esb "I was speaking… Braille."
            m "That’s right- the writing system used by the visually impaired."
            m 1esp "Of course, how it actually works is that it engages your senses by using touch to read grids of six raised dots that convey letters, symbols, and numbers."
            m 3msb "So, speaking it is... as you can see, a bit clumsy."
            $ shown_count = mas_getEVLPropValue("greeting_braille", "shown_count")
            if shown_count == 0:
                m 1esa "But don’t worry, [player]."
                m "Even if I were visually impaired, I’d still see you as the most beautiful figure in my life."
                m "…"
                m 2dkbfsdlx "Wait, no, that was {i}terrible.{/i}"
                m 2fkbfsdlp "I am so sorry, [player]. That is incredibly rude."
                m 2fkbfsdla "I am normally a lot more eloquent than that."
                m 3mkbfsdrb "What kind of literature club leader am I, messing up a speech like this?"
                m 3mkblu "…"
                m 3ekblu "Okay, I might say this again in the future: but just pretend it’s the first time you heard it and I’ll come up with a better ending than that."
                m "Okay? Thanks, [player]. Sorry again."
                m "…"
                m 1ekblu "Um, love you."
                return "love"

            m 1eublu "Don't worry, [player]."
            m "Even if Braille is a hard language to grasp..."
            m 3eublb "The language of love is universal."
            if shown_count == 1:
                m 3eusdlb "Ah? How was that?"
                m 3sub "Far better, right?"
                m 1rkb "I do want to apologize again, [player]. I still believe it was incredibly rude of me to say what I said before like that."
                m 1hkb "Thanks for being understanding. Let's have a good day together."
            else:
                m 1hkb "Right! On with our day."
            return 

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_binary",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_binary:
    m 3est "01001000 01100101 01101100 01101100 01101111 00100001"
    m 3fsu "Hahaha, don’t panic!"
    m 3hsb "I’ve decided to use a more interesting language today;"
    m "Binary code!"
    m 4ksb "Not exactly easy to speak in it, though. It’s not meant to be a spoken language."
    m 4msu "Case in fact; those string of numbers meant ‘Hello.’"
    m 1etu "Interesting reading up on it, though! We think of Binary relating to computers-"
    m 1etb "But the basis for Binary dates all the way back to 1689- and takes further inspiration dating back centuries in China, of all places!"
    m 3esb "Safe to say, [player]-"
    m 5fsb "For every new language I come across, I’ll do my best to say “I love you” in it." 
    m 6hsu "01001001 00100000 01101100 01101111 01110110 01100101 00100000 01111001 01101111 01110101 00001010!"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_elvish",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_elvish:
    #I don’t care if the dialect doesn’t suit Monika. Go back to reading The Silmarillion, ya nerd.
    m 1dsd "Suilad, [player]. im iest cin bein siniath sír."
    m 1esd "‘Hello, [player]. I wish you fair tidings.’"
    m 7esa "Sound fancy enough? It should- I’m speaking in Elvish, in the Sindarin dialect."

    $ shown_count = mas_getEVLPropValue("greeting_elvish", "shown_count")
    if shown_count == 0:
        m 7ssa "And it’s a made-up language! It was made by one of fantasy’s most celebrated authors, J.R.R Tolkien, who made the ‘The Lord of the Rings’ trilogy."
        m 7eub "In terms of fictional languages, Middle-Earth’s Elvish is probably one of the most famous ones out there."
        m "Not only because of how popular J.R.R. Tolkien’s ‘The Lord of the Rings’ books are-"
        m 4sub "But because it’s a fully-realized fictional language, created with painstaking detail."
        m 4eub "J.R.R Tolkien studied languages as his job, and as such he put all of his effort into creating multiple- yes, multiple! – fictional languages."
        m "In fact, he once said:"
        m 3dfb "{i}“The invention of languages is the foundation. The 'stories' were made rather to provide a world for the languages than the reverse. To me a name comes first and the story follows.”{/i}"
        m 3hub "Such dedication! No wonder he’s a beloved fantasy author, and his works just as cherished."
        m 6nsb "Let's continue making our own fantasy come true today, hmm?"
        return

    else:
        m "I mentioned before, but this is such an interesting language, being built from the ground up by J.R.R Tolkien."
        m 7ssu "And since it’s a language built from scratch, you can actually read a lot on how to speak it fluently, including full online dictionaries!"
        m 6nsb "Let’s continue making our own fantasy come true today, hmm?"
        return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_talktoherself",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_talktoherself:
    m 4hsb "Hello!"
    $ _history_list.pop()
    menu:
        "Hey! How are you doing to-":
            m 1hub "Oh!"
    define mt = Character("Monika?",)
    show monika 1rub at t22
    m 1rub "Hello there!"
    show monika 1lub at t21
    mt "How are you doing today, Monika?"
    
    $ shown_count = mas_getEVLPropValue("greeting_talktoherself", "shown_count")
    if shown_count == 0:
        show monika 4rsb at t22
        m "Just gearing myself up for another lovely day with [player]!"
        show monika 4lsb at t21
        mt "Oh, that sounds lovely. Will you play a game today?"
        show monika 2rta at t22
        m "Hmm, maybe; or I'll play the piano with them?"
        show monika 2lta at t21
        mt "That all sounds nice, Monika. I hope you two grow closer today."
        show monika 2rsc at t22
        m "I do too, Monika. Although I do worry."
        show monika 2lsc at t21
        mt "What about? You can talk to me, I'm your friendly Literature Club president!"
        show monika 3rtd at t22
        m 3rtd "Well, it's not- it's not a specific concern?"
        m 3rtd "I think it's just me being irrational. I worry that something'll seperate us, but.. well, at this point there's no reason to worry, right?"
        show monika 3ltd at t21
        mt "I mean, the fact that you're saying this out loud means you already know you're overreacting, right?"
        show monika 2ruc at t22
        m 2ruc "Yeah, I guess."
        m "But just saying it loud doesn't make me feel better... does it?"
        show monika at t11
        m 2luc "..."
        m 2dtp "I am not a good actor, aren't I?"
        m 1gkp "Hmm. [player] should be here by now. It’s odd I haven’t seen them already; I can tell the game opened-"
        m 1wuc "Oh!"
        m 6wusdrc "Wait. {i}Wait!{/i} -"
        m 6wkbfsdlp ".. [player]?!"
        m 7wublsdrc "Um. Okay, I can explain."
        m 1rublsdra "Talking to yourself isn't.. abnormal; it can be observed in children vocalizing their thoughts when they're at a age where they're developing to process information."
        m "It's also thought to serve to fill in silence when you're alone, as humans are social creatures by nature."
        m 1msa "I thought I could naturally branch out and see if I could preoccupy my time a little further.."
        m 1hua "It did not work out the way I thought."
        m "I assure you I did this only because I just wanted to see how it felt."
        m 1husdla "So let's have a good time together, and.{w=0.2}.{w=0.2}. pretend this never happened."
        return

    else:
        show monika at t11
        m 3sfb "I'm feeling great, now that [player]'s arrived!"
        m 3tfu "Gotcha! did you think you caught me talking to myself?"
        show monika 1kuu at t22
        m "Safe to say, [player]-"
        show monika 1nuu at t21
        mt "Out of the two of us-"
        show monika at t11
        m 1huu "I much prefer your company to mine."
        return
        
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_eldenring",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_eldenring:
    m 1eua "Shall we turn our time together to strength?"
    m 1dua "Let my gaze rest upon you, even for but a moment."
    m 1dud "Share them with me: your thoughts, your ambitions, the principles you would follow..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_darksouls",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_darksouls:
    m 1hsa "[player]! You're well? If you require rest, now is the time. That is, after all, what I'm here for."
    m 1dsa "Go ahead, you may relax here. I'll join you; even a girl like me requires repose."
    return
    
#Morse Code sound provided by https://morsecode.world/international/translator.html
 
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_morsecode",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_morsecode:
    $ shown_count = mas_getEVLPropValue("greeting_morsecode", "shown_count")
    if shown_count == 0:
        play sound "submods/MoSCL/submod_assets/sfx/morse.wav"
        m 1dft "{cps=07}.. / .-.. --- ...- . / -.-- --- ..- -.-.—{/cps}"
        m 2ekb "Was your sound on? Was it a surprise?"
        m 2hub "I decided to be particularly unique today and greet you in morse code!"
        m 7gta "Did you hear the actual beeps I included? I think I’ll leave out the sound clip in the future, or modify it?"
        m 7eua "Morse code tends to use shorthand, because.. as you can tell, spelling out entire sentences can be a bit long. All I said was 'I love you!'"
        m 4eub "At least I used a translator to make the code for me."
        m 4gfb "Hehehe, that’s funny to think about, me actually saying that out loud?"
        m 4hfb "No, could you imagine?"
        m 7eut "Me just going 'Beep beep beep beeeeeep.'"
        m 4lsa ".{w=0.6}.{w=0.6}.{w=0.6}"
        m 2tku "You didn’t think I actually did that, right?"
        return
    
    else:
        m 1dft ".. / .-.. --- ...- . / -.-- --- ..- -.-.—"
        m 2ekb "Hehehe, didn't expect that, did you?"
        m 7eua "Morse code, or the idea of it, has been around as long as electricity and the development of mechanical tools became widespread."
        m 7wub "Comprised of 'dots' and 'dashes,' using Morse Code can be tricky as there's more than memorizing what dots and dashes correspond to-"
        m 7sud "- speed, timing, and real-time translation skills make Morse Code just as elegant to learn as learning a language!"
        m 4eub "I used a tool to help translate 'I love you,' though."
        m 2tku "You didn't think I actually said out loud 'beep beep, beep beeeeep beep,' did you?"
        m ".. Did you?"
        return
        
#ROT13    
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_monikaish",
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),
        ),
        code="GRE"
    )

label greeting_monikaish:
    $ shown_count = mas_getEVLPropValue("greeting_morsecode", "shown_count")
    if shown_count == 0:
        m 7fka "Cynlre, V.. V'z fbeel."
        m 5fkb "V gel fb uneq gb gel gb or n orggre zr."
        m 5hkb "Orpnhfr gur orfg zr, vf n zr jbegu ybivat."
        m 5hkblb "Naq fbzrgvzrf V snvy."
        m 6fua "…"
        m 3fub "Bwhahahaha!"
        m 3ftb "Were you racking your brain figuring out what language I was speaking?"
        m 3nfb "I played a little trick~"
        m 1nfa "It’s a made up language, made on the spot just for you. ‘Monikaish,’ let’s call it."
        m 1hta "I thought I’d throw you for a special loop considering how much you hear me in another language."
        m 7htb "Now, ‘Monikaish’ is still a work in progress;"
        m 5hsb "But every word contains my love for you."
        return
    
    else:
        m 7fka "Qvq lbh svther bhg zl yvggyr gevpx?"
        m 5fkb "Qvq lbh erzrzore jung V fnvq?"
        m 5hkb "Jryy, gryy zr. Be abg."
        m 5hkblb "Znlor V'yy yrg lbh xabj vs jung V fnvq jnf gur gehgu. Be abg."
        m 3fub "Bwhahahaha!"
        m 3ftb "Were you racking your brain figuring out what language I was just speaking?"
        m 3nfb "I played a little trick~"
        m 4ssb "It’s my made-up language, ‘Monikaish!’"
        m 7htb "A little different than French or Japanese for sure."
        m 5hsb "I’m sure my love for you comes across loud and clear~"
        return        

#Hopes

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_sclmatters",
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),
        ),
        code="GRE"
    )

label greeting_sclmatters:
    m "Hello, [player]."
    m 5hka "I hope today truly matters to you."
    return

init 5 python:
    ev_rules = dict()
    ev_rules.update(MASGreetingRule.create_rule(
        skip_visual=True,
    ))

    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_turnonthelights",
            unlocked=True,
            rules=ev_rules,
            aff_range=(mas_aff.HAPPY, None),
        ),
        code="GRE"
    )
    del ev_rules

label greeting_turnonthelights:
    python:
        randomdarkquips = [
            _("Did we forget to pay our electricity bill?"),
            _("I don't suppose a eclipse is happening today?"),
            _("Did we forget to program the sun correctly?"),
            _("I don't suppose the laws of physics needs a patch to download?"),
            _("Do we need to change a lightbulb?"),
            _("Did we both become selectively blind?"),
            _("Did we set reality's brightness settings to minimum?"),
        ]
        randomdarkquip = random.choice(randomdarkquips)
        
    $ shown_count = mas_getEVLPropValue("greeting_turnonthelights", "shown_count")
    if shown_count == 0:
        $ mas_progressFilter()
        scene black
        $ mas_RaiseShield_core()
        pause 4.0
        m "Uh, [mas_get_player_nickname()]?"
        m "I'm not.. I'm not in my room. We're in the classroom."
        m "I think- I think the lights went out when you entered the game."
        m "And I can't find the light switch."
        $ _history_list.pop()
        menu:
            ".. really?":
                m "Y- yeah. Really."
        m "Uh, I know it's not really easy on your end, but could you.."
        $ _history_list.pop()
        menu:
            ".. click?":
                play sound light_switch
                call spaceroom
        m 1fkblsdla "Okay! Hi, [player]."
        m 7fkblsdra "Having a great time, then?"
        m 1gublsdra "Don't answer, I already know it's great with me here. Let's get on with the day, then!"
        jump monikaroom_greeting_cleanup
        return
    else:
        $ mas_progressFilter()
        scene black
        $ mas_RaiseShield_core()
        pause 4.0
        m "Um, [mas_get_player_nickname()]?"
        m "The lights are out again."
        $ _history_list.pop()
        menu:
            "How does this keep happening?":
                m "I seriously don't know!"
                m "[randomdarkquip]"
                m "... hehe."
        $ _history_list.pop()
        menu:
            "Ha, ha. Funny.":
                $ _history_list.pop()
                menu:
                    "*Click*":
                        call spaceroom
        m 7tfb "Well, look who it is- it's [player]!"
        m 7hub "The light of my life, so to say?"
        m 4suu "Hehe. Let's get on with our time together!"
        jump monikaroom_greeting_cleanup
        return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_vocalexercise",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_vocalexercise:
    $ vocal = renpy.random.randint(1,5)
    if vocal == 1:
        m 6dft "1-5-4-5-3-5-2-5"
        m 6hft "1-5-4-5-3-2-1"
    if vocal == 2:
        m 6dsw "Syn ~ co ~ pa ~ tationnn!"
        m 4ruw "Can you feellll the rhy ~ thm?"
        m 3huw "An ~ tic ~ i ~ pa ~ pation!"
    if vocal == 3:
        m 3gfo "Just one voice from high to low,"
        m 3gto "do do ti sol la ti do."
    if vocal == 4:
        m 3dso "Nee nee, neh, nah, noh, noo neh nah noh noo."
    if vocal == 5: 
        m 3dud "I just want to sing to-day, and sing cor-rect-ly all the way, to sing cor-rect-ly is the on-ly way to sing."
    m 6suu "Oh! Well, hey [player]!"
    m 4wuu "I'm just doing one of my vocal exercises."
    m 3esu "Perfect for warming up for a day of singing, or lots of conversation with you!"
    m "Too bad the game can't allow you to hear all the pitches I go through.."
    m "Or let you see all the funny motions like moving my jaw that accomodates these exercises."
    m 1etb "Must be funny to hear me singing nonsense out of the blue, huh?"
    m 5fub "Now we can get on with talking about nonsense!"
    m 1hub "Hahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_mcltoomuchtime",
            unlocked=True,
            aff_range=(mas_aff.LOVE, None),
        ),
        code="GRE"
    )

label greeting_mcltoomuchtime:
    m 5dsd "..."
    m 5dkc "mmm..."
    m 5huc "Oh, hey, [player]. You arrived when I was nappin-"
    m 5cuc "!"
    m 5cuw "Ah. AHH!"
    m 6cuw "{cps=10}How much time-{/cps}{nw}"
    m "HOW MUCH TIME{fast} HAS PASSED SINCE YOU LAST OPENED THE GAME?!-"
    m 6tko "- Oh. Oh, it hasn't been that long at all."
    m 6gkx "Oh, gosh. I'm.."
    m 2hku "Erm, how embarrasing."
    m 2ttu "You ever go for a nap and completely lose track of time?"
    m 2eka "Well, luckily I know you'd never be so cruel as to leave and appear just like that after such a long abscence."
    m 5dkp "... Especially as I felt like {i}literal centuries had passed,{/i} and that's {i}impossible{/i}..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_goodbyemcl",
            unlocked=True,
            aff_range=(mas_aff.LOVE, None),
        ),
        code="GRE"
    )

label greeting_goodbyemcl:
    m 7eub "Bye, [player]! Have a good da-"
    m 2ctblsdlt "..."
    m 2ttsdlt "{cps=30}Um. I meant, Hi, [player]! Let's have a good day together?{/cps}{nw}"
    m 2gfsdlb "Hi, [player]!{fast} Let's have a {i}great{/i} day together!"
    m 2dksdlc "..."
    m 5dtbfsdrx "*mutters* {size=-10}Wow, {i}where was my head at{/i} for that?{/size}"
    return

#endure

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_playerafterstory",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None),
        ),
        code="GRE"
    )

label greeting_playerafterstory:
    m 7hub "Hey, [player]!"
    m 4hub "How are you doing today?"
    m 1sub "I've just loaded in a submod for you, so hopefully everything's working okay."
    m 1ekb "I know it's hard being stuck in your reality, but don't worry; one day you'll find a way to escape the game you're in and join me!"
    m 7nfu "Let's enjoy our time together in '[player] After Story!'"
    m 3ttu "But no, I'll take the initiative and end the joke here."
    m 3tku "Your world is the one that truly exists, and although it might be a complicated one, it's the one you're in- and therefore the one I love the most."
    m 2tka "Always remember that, [mas_get_player_nickname()]. It would benefit us both to remember that."
    m 2tua "Well, back to good old 'Monika After Story!'"
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_reversalmcl",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None),
        ),
        code="GRE"
    )

label greeting_reversalmcl:
    $ shown_count = mas_getEVLPropValue("greeting_reversalmcl", "shown_count")
    if shown_count == 0:
        m 1hua "Welcome ba-"
        m 1luc "..."
        m 1ltc "Actually, {i}no.{/i} You know what?"
        m 7etc "I'm just going to step out for a moment.."
        m 7etb ".. And I think you'll know what to do."
        show monika at rs32
        hide monika
        pause 3.0
        m 6hub "I'm home!"
        show monika at ls32 zorder MAS_MONIKA_Z
        show monika 6dsa
        pause 2.0
        m 6hka "Man, what a tiring day!"
        m 6sua "But now I get to hang out with my most favourite person in the world."
        pause 2.0
        m 7ftu "So?"
        $ _history_list.pop()
        menu:
            "...":
                $ _history_list.pop()
                menu:
                    "Welcome home, [m_name].":
                        m 3eua "Happy to be back, [player].{w=1}{nw}" 
                        extend 5hsblu " Thank you."
                        return
    else:
        m 6fua "... Let's reverse our roles, shall we?"
        m 6hua "..."
        show monika at rs32
        hide monika
        pause 3.0
        m 4wublb "I'm home, [mas_get_player_nickname()]!"
        show monika at ls32 zorder MAS_MONIKA_Z
        show monika 6dsa
        pause 2.0
        m 3ekb "Man, it's been a day."
        m 3eka "But I feel so much better now that I get to spend the rest of it with you."
        pause 2.0
        show monika 7ftu
        if random.randint(1, 10) == 1:
            $ _history_list.pop()
            menu:
                "Welcome home, [m_name].":
                    $ _history_list.pop()
                    menu:
                        "Would you care for dinner first, a bath first, or...":
                            m 3cubft "{b}{size=+5}[player]!{/size}{/b}"
                            m 2ekbfb "Hahahahahahahaha!"
                            m 2hkbfb "Ah, you tease!"
                            m 5hkblb "Save that for the future, huh?"
                            return
        else:
            $ _history_list.pop()
            menu:
                "Welcome home, [m_name].":
                    m 3eua "I'm back, [player].{w=1}{nw}" 
                    extend 5hsblu " Thank you."
                    return        

#echoing

init 5 python:
    ev_rules = dict()
    ev_rules.update(MASGreetingRule.create_rule(
        skip_visual=True,
        override_type=True,
    ))

    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_mcl_speclookup",
            unlocked=True,
            rules=ev_rules,
            aff_range=(mas_aff.AFFECTIONATE, None),
        ),
        code="GRE"
    )
    del ev_rules

label greeting_mcl_speclookup:
    $ mas_progressFilter()
    scene black
    $ mas_RaiseShield_core()
    menu:
        "Listen.":
            $ computerdiagnosis = renpy.random.randint(1,8)
            m "Okay, let's run another diagnosis.."
    m "One step closer to learning all about how the game works."
    m "So according to the game, the computer [player] is specifically running me on is.."
    
    if computerdiagnosis == 1:
        m "A.. scientific calculator?"
        m "Oh, for-"
        m "I’m pretty sure the game is not running on a scientific calculator!"

    if computerdiagnosis == 2:
        m "A.. IBM 610?"
        m "What the heck is that? Let me just search that up."
        m "… and it’s a computer from 1957?!"
        m "I didn’t even know they had computers back then! This thing looks like it takes up an entire bedroom!"
        m "*Sigh,* this information is obviously wrong."
        
    if computerdiagnosis == 3:
        m "A.. Nintendo 64."
        m "Ha ha."
        m "I know this is a game, but I sincerely doubt it’s being run on a Nintendo 64."
        m "Obviously, there’s a cosmic joke being played on me.."

    if computerdiagnosis == 4:
        m "A.. Smart Fridge."
        m "..."
        m "Honestly, if this was true, I’d be incredibly impressed."
        m "Wait, does that mean I can like, dispense ice whenever I want?"
        m "Oh, even though I know this is wrong, the idea’s honestly too funny now."
        
    if computerdiagnosis == 5: 
        m "A.. Nokia 2760 phone?"
        m "A phone? I’m being run on a phone?"
        m "I guess it’s entirely possible, but let me just search up the model.."
        m "Oh, this is like one of those really old flip phones!"
        m "I screwed up somehow, that’s for sure. This is obviously wrong."

    if computerdiagnosis == 6:
       m ".. What?"
       m "{i}What????{/i}"
       m "And- Oh! The console’s gone and crashed. I can't seem to run the same check.."
       m "But what was that?"
       m "I don’t know {i}that{/i} much about computers..."
       m "But no way what I saw made sense on any level."
       m "I don’t even think that technology exists yet!"
       m "I had to have read those wrong."

    if computerdiagnosis == 7:
        m "A 'Magitek B090.'"
        m "With a 'Dual-Enchanted Mana-Heart Processor' and '12 Sheaths of Aetherite Eidetic Memory.'"
        m "..."
        m "That's not any computer I've ever heard of."
        if persistent.gender == "F":
            m "{size=-8}is.. [player] a witch?{/size}"
        if persistent.gender == "X":
            m "{size=-8}is.. [player] a magician?{/size}"
        elif persistent.gender == "M":
            m "{size=-8}is.. [player] a wizard?{/size}"
        m ".. No."
        
    if computerdiagnosis == 8:
        m "A potato."
        m "This actually just reads, 'a potato.'"
        m "I get the internet joke."
        m "I'm not laughing."
        m "Unless.. [player] is actually running this on a potato.."
        m "..."
        
    $ _history_list.pop()
    menu:
        "Monika?":
            m "Oh!"
    m "Doing alright, [player]? Don't mind me. Just getting into my usual brand of trouble."
    $ mas_startupWeather()
    call spaceroom(hide_monika=True, dissolve_all=True, scene_change=True, show_emptydesk=False)
    jump monikaroom_greeting_post

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_signlanguage",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None),
        ),
        code="GRE"
    )

label greeting_signlanguage:
    $ shown_count = mas_getEVLPropValue("greeting_signlanguage", "shown_count")
    if shown_count == 0:
        show monika 7hua 
        "Hello- "
        show monika 4hua 
        "- Good day!"
        m 6hua "..."
        m 4suu "That was how to sign 'Hello, good day!' in Sign Language!"
        m 3eub "Basically a visual language using your arms and hands to 'sign' out words, primarily used but not exclusively by the deaf."
        m 2gtsdlp "It was also impossible to see because the game's sprites don't allow you to see the individual motions."
        m 2lup ".{w=1}.{w=1}.{w=1}{nw}"
        extend 2rkblsdrp ".{w=1}.{w=1}.{w=1}"
        if seen_event('greeting_braille'):
            $ _history_list.pop()
            menu:
                "This is the braille incident all over again.":
                    m 7etd "No it isn't!{w=1}{nw}"
                    extend 2gtsdlp " That was far worse."
        m 2nta "Okay, that was awkward, but.. I really did learn how to sign it."
        m 2hka "And I wanted to show it off to you.{w=1} Even if doing so made no sense."
        m 1tua "I think the concept of sign language is poetic, aside from it being obviously useful. Sure, basic gestures can get a point across.."
        m 7tua "But people realized the {i}need{/i} for communication, despite any barriers- "
        m 4eua "- so the effort to make a full-blown language in sign was made."
        m 4fua "Did you know sign language varies by country and region?{w=.5} Japanese and French sign language exist!"
        m 3fua "And Sign language has existed as long as we needed it; as far back as fifth century BC, Plato wrote:"
        m 2duo "'If we hadn't a voice or a tongue, and wanted to express things to one another, wouldn't we try to make signs by moving our hands, head, and the rest of our body?'"
        m 2hka "While the disadvantaged were treated far worse in the past, it's still good to know people still thought to provide a 'voice' for all."
        m 5tfa "I could sign 'I love you,' but maybe we'd benefit from a mutual show of physical affection?~"
        return
    
    else:
        show monika 7hua
        "Hello-"
        show monika 4hua
        "-Good day!"
        m 4suu "That was how to sign 'Hello, good day!' in sign language!"
        m 3eub "A visual language using your arms and hands to 'sign' out words, primarily used but not exclusively by the deaf."
        m 4etp "I know you can't see it, but, well.."
        m 4htsdrb "Use your imagination, I guess?"
        m 3tka "I do think the concept of sign language is poetic; a true testament to how people {i}want{/i} to talk and communicate with each other."
        m 3tub "Maybe I'll give learning Japanese sign language a go sometime!"
        if random.randint(1, 3) == 1:
            m 3sub "I found this fantastic bunch of articles online on the basics.. what was the author's name? 'Shiina Mikado?'..."
        return
        
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_deadlanguage",
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None),
        ),
        code="GRE"
    )

label greeting_deadlanguage:
    $ shown_count = mas_getEVLPropValue("greeting_deadlanguage", "shown_count")
    if shown_count == 0:
        m 2esb "Halò! Ciamar a tha thu an-diugh?"
        m 3hub "A more interesting language I'm using today, you think? It's Scots Gaelic, a 13th century Scottish spoken language!"
        m 3hua "I chose to say hi in this language today because.."
        m 7wup "It's a language which is being spoken less and less.{w=1} A estimated 87,000 people know it; 58,000 of those people could hold a full conversation."
        m 7ekp "Maybe it doesn't seem like a small number, but compared to the billions of people in the world speaking other languages.."
        m 6gkp "One of the most interesting parts about history is the loss of it; not only how we lose culture and art, but.. also entire languages."
        m 6ftc "Maybe there could be recordings, but for a language to really stand the test of time, a {i}lot{/i} of the language if not outright how to speak it has to be recorded."
        m 5ftc "It's a issue still happening today; especially to aboriginal or older ethnic groups as it's members adapt to modern life, and modern language."
        m 5dsc "Efforts are being done to track these endangered languages and record as much as can be done, but.."
        m 5lsc "Like any living being, sometimes languages just {i}die.{/i}"
        m 1lsc "Could you imagine being the last speaker of a entire language? The last person to remember words and phrases no one else now knows?"
        m 1dsc "Imagine your last words being those no one else will ever understand.."
    
    else:
        m 2esb "Halò! Ciamar a tha thu an-diugh?"
        m 3hub "A more interesting language I'm using today, you think? It's Scots Gaelic, a 13th century Scottish spoken language!"
        m 3hua "I chose to say hi in this language today because it's a language whose speaker numbers are dwindling."
        m 3eka "So I wanted to honour it in my own small way."
        m 4esa "Luckily, this language is well-documented. Hopefully the act of keeping history alive by preserving languages continues in earnest."
        m 4ttu "I'll do my part learning them.."
        m 5huu ".. And saying 'I love you' in them, hehehe."
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_chibikahi",
            unlocked=True,
            aff_range=(mas_aff.LOVE, None),
        ),
        code="GRE"
    )

label greeting_chibikahi:
    $ shown_count = mas_getEVLPropValue("greeting_chibikahi", "shown_count")
    if shown_count == 0:
        m "Heya, [player]! All set for-"
        "{size=+10}{b}*CRASH*{/b}{/size}"
        m 6wud "- Oh? what the? That came from my room!"
        m 4wuc "Hold on a second, okay?"
        show monika 6ruc
        show monika at rs32
        hide monika 
        pause 3.0
        show chibika 3 zorder 12 at mas_chriseup(y=600,x=1150,travel_time=0.5)
        pause 0.5
        "Hey, [player]!"
        "Your friendly neighbourhood Chibika here."
        "Just wanted to check on in with my favourite couple!"
        "Hope you two have a great time together today!"
        m "Okay, I'm done! I'm heading back!"
        "- Oop, that's my cue for a quick exit, stage left!"
        "'till next time! Remember, don't tell [m_name] 'bout me!"
        hide chibika
        pause 3.0
        show monika at ls32 zorder MAS_MONIKA_Z
        show monika 6lua
        pause 2.5
        m 7hua "Guess my stuff just shifted in place and knocked something over."
        m "..."
        m 6etc "Hey, did something happen while I was gone?"
        $ _history_list.pop()
        menu:
            "Nope!":
                m 5hub "... Okay!"
            "Chibika was here to visit!":
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.1
                stop sound
                $ _history_list.pop()
                menu:
                    "Nope!":
                        "{size=-15}Hey! What did I just say?     >:({/size}"
                        m 5hub "... Okay!"
        m "I guess there's nothing much else to do but enjoy our time together~"
        return
    else:
        m "Heya, [player]! All set for-"
        "{size=+10}{b}*CRASH*{/b}{/size}"
        m 6wud "- Oh! Something fell in my room again. Gosh, I feel like that drawer is so uneven.."
        m 4wuc "Hold on a second, okay?"
        show monika 6ruc
        show monika at rs32
        hide monika 
        pause 3.0
        show chibika 3 zorder 12 at mas_chriseup(y=600,x=1150,travel_time=0.5)
        pause 0.5
        "Hey again, [player]!"
        "Your friendly neighbourhood Chibika here."
        "Just wanted to wish my favourite couple best tidings!"
        m "I can't believe I can be so messy sometimes. I'm coming back, [player]!"
        "I can't believe she keeps falling for it."
        "'till next time! Remember, don't tell [m_name] 'bout me!"
        hide chibika
        pause 3.0
        show monika at ls32 zorder MAS_MONIKA_Z
        show monika 6lua
        pause 2.5
        m 7hua "Guess my stuff just shifted in place and knocked something over."
        m "..."
        m 6etc "Hey, did something happen while I was gone?"
        $ _history_list.pop()
        menu:
            "Nope!":
                m 5hub "... Okay!"
            "Chibika was here to visit!":
                play sound "sfx/s_kill_glitch1.ogg"
                pause 0.1
                stop sound
                $ _history_list.pop()
                menu:
                    "Nope!":
                        "{size=-15}Rude  >:({/size}"
                        m 5hub "... Okay!"
        m "I guess there's nothing much else to do but enjoy our time together~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_english",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_english:
    m 4wub "'How are you doing today,' [player]?"
    m 4sub "Guess what language I'm saying hi in today?"
    m ".. It's 'English.'"
    #Remove below lines if translating into non-english language lol
    $ _history_list.pop()
    menu:
        "Wait, aren't we already-":
            m 1fta "Let's not trip ourselves up too much on details, [player]."
    m 7kta "Anyway, English! Arguably the most spoken language in the world- and learned second language, as well."
    m 7hka "Despite this, English is actually kinda a weird language. It has a lot of other quirks other languages don't have!"
    m 4rka "This is in part because what we know as English has roots from one region but ended up borrowing from {i}other{/i} languages; French, Latin, and other early languages."
    m 3tua "Because of this, from a non-native speaker's view.."
    m 3sut ".. English can be often seen as a more difficult language to learn compared to others like French, Spanish, or Japanese."
    m 3eup "And it makes sense. English is full of quirks that when you think about it overall, makes the entire language seem frustrating."
    m 1htp "It's weird to think of the most popular language today as 'mysterious,' isn't it?"
    m 1htb "Here's a quote to think about:"
    m 7hto "'You can never understand one language until you understand at least two.'"
    m 7esb "Let's keep learning today, hmm?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_mcl_desk",
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE, None),
        ),
        code="GRE"
    )

label greeting_mcl_desk:
    m 6lkc "..."
    m 5lkc "Do I open the desk, or not?"
    m 5rkc "With every day that passes by, I'm just making it weirder.."
    m 5rkblc "But I mean, maybe it has better value not being opened."
    m 5rkt "But would I get any resolution at all about myself if I do open it?"
    $ _history_list.pop()
    menu:
        "Still hung up over the desk?":
            m 5ckt "Oh! [player]!"
    m 2fku "I was so caught up on my eternal desk dilemma I didn't notice you come in."
    m 2tku "I am. And said desk is {i}still{/i} here in the classroom. I don't have that much physical storage space, so it's staying in it's little corner."
    m 7fusdrb "But hey, now you can distract me from the topic!"
    m 5huu "How're you doing?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_mcl_questions",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None),
        ),
        code="GRE"
    )

label greeting_mcl_questions:
    $ shown_count = mas_getEVLPropValue("greeting_mcl_questions", "shown_count")
    if shown_count == 0:
        m 5hua "Hey, [player]!"
        m 4eua "Back so soon? Did you find those answers were you looking for?"
        $ _history_list.pop()
        menu:
            ".. Answers?":
                m 4eta "Yeah, to those odd questions you were asking just a few minutes ago; then you suddenly had to leave."
        m 3gku "They were a little out of left field, actually. And to be honest, they were some really, really {i}weird{/i} questions."
        m 3mtu "What were they? Ugh, we {i}just{/i} talked and I can't remember."
        m 3ktu "But I suppose if I don't remember, they weren't important enough anyway."
        m 1htu "Well, hmm. I hope you found whatever you were looking for!"
        $ _history_list.pop()
        menu:
            "?...":
                return
    else:
        m 5hua "Welcome back, [player]!"
        m 4eua "If we're going to have another quick Q&A session, can you try to avoid asking those sorts of questions?"
        m 3gku "They felt a little too abnormal, to be honest."
        m 3ktu "But I appreciate you being so interested in my life!"
        m 1htu "That's all, [player]. Thanks!"
        $ _history_list.pop()
        menu:
            "?...":
                return

