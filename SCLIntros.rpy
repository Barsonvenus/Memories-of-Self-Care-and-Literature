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
