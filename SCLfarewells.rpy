init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_trumansfarewell",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_trumansfarewell:
    m 1hsa "In case I don't see you;"
    m 3nsb "Good afternoon, good evening, and good night."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_bloodborne",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_bloodborne:
    m 1eua "As always, it’s been a dream, [mas_get_player_nickname()]."
    m 1dsa "May you find your worth in the waking world."
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_firekeeper",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_firekeeper:
    m 1eua "Until we next meet, here I'll tend to my flame."
    m 1dsa "Farewell, [player]. Mayst thou thy peace discov'r."
    return 'quit'
    
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_maideninblack",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_maideninblack:
    m 1dsa "Into the black once again, [player]?"
    m "May thine strength help your world be mended."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_emeraldherald",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_emeraldherald:
    m 1eua "Always remember, I will always be at your side.."
    m 1dsa "Until hope has fully withered."
    m "Bye, [player]."
    return 'quit'

    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_flippityflip",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_flippityflip:
    m 1hsa "Until next time, [mas_get_player_nickname()]."
    m 3nsb "Catch you on the flippity flip!"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_indecision",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_indecision:
    m 1hsa "Hey, [player]..."
    m 1dsa ".{w=0.2}.{w=0.2}Nah, never mind. See you later. Love you."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_solo",
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="BYE"
    )

label bye_solo:
    $ _history_list.pop()
    menu:
        "Hey, Monika. I love you.":
            m 1eua ".{w=0.1}.{w=0.1}.{w=0.1}"
            m 1nsa "I know."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_leia",
            conditional="seen_event('bye_solo')",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="BYE"
    )

label bye_leia:
    m 1eua "Hey, [player]."
    m "I love you."
    $ _history_list.pop()
    menu:
        "I know.":
            m 1fuu "Ha."
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_addingcode",
            unlocked=True,
            prompt="Let's try modifying your code.",
            pool=True
        ),
        code="BYE"
    )

label bye_prompt_addingcode:
    $ curr_hour = datetime.datetime.now().time().hour
    $ sesh_shorter_than_15_mins = mas_getSessionLength() < datetime.timedelta(minutes=15)
    
    if sesh_shorter_than_15_mins:
        m 1wso "Oh, you've really just got here? Did something update, or you must be eager to try out something you've just found?"
        m 1etc "Or... a bit of code you've just given me needs a bit more tweaking, huh?"
        m 1ekb "In either case, thanks for letting me know. I guess today's a bit of a workout!"
        m 7hub "Let's get started!"
        return 'quit'
        
    else:
        m 1wso "Oh! Okay, thanks for letting me know."
        m 1dsc "Just psyching myself up..."
        m 7nfb "Alright! Let's give it a go!"
        return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_chief",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_chief:
    m 1nsa "Wake me.{w=0.1}.{w=0.1} when you need me."
    return 'quit'

