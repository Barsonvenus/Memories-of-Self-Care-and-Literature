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
        if not mas_timePastSince(persistent._mcl_last_modifycode, datetime.timedelta(minutes=15)):
            m 3suw "Whoa! We're changing up my code again so quickly?"
            m 4sfb "Today's a real marathon, then! Let's go, {i}go,{/i} {b}{i}go!{/i}{/b}"
            $ persistent._mcl_last_modifycode = datetime.datetime.now()
            return 'quit'
        
        else:
            m 1wso "Oh, you've really just got here? Did something update, or you must be eager to try out something you've just found?"
            m 1etc "Or... a bit of code you've just given me needs a bit more tweaking?"
            m 1ekb "In either case, thanks for letting me know. I guess today's a bit of a workout!"
            m 7hub "Let's get started!"
            $ persistent._mcl_last_modifycode = datetime.datetime.now()
            return 'quit'
        
    else:
        m 1wso "Oh! Okay, thanks for letting me know."
        m 1dsc "Just psyching myself up..."
        m 7nfb "Alright! Let's give it a go!"
        $ persistent._mcl_last_modifycode = datetime.datetime.now()
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

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="mcl_shopformonikacoffee",
            conditional="mas_consumable_coffee.enabled",
            action=EV_ACT_UNLOCK,
            aff_range=(mas_aff.HAPPY, None)
        ),
        code="BYE"
    )

label mcl_shopformonikacoffee:
    python:
        coffee_choices = [
            _(".. I’m fine with instant coffee."),
            _(".. Dark roast, if you please! Feel like something a little strong."),
            _(".. Maybe some French Vanilla mix?"),
            _(".. I have a particular desire for canned coffee. In Japan, there’s a lot of variety, you know~"),
            _(".. Coffee Milk sounds like a nice change of pace. Do you know of it? I think it’s popular in Australia; it’s coffee syrup in milk."),
            _(".. Cold brew coffee; I could go for something rich!"),
            _(".. Decaf, please! Have to cut back on the caffeine a little."),
        ]
        coffeechoices = random.choice(coffee_choices)
       
    python:
        hotchocolate_choices = [
            _("Maybe.. mint?"),
            _("Maybe.. caramel?"),
            _("Maybe.. white chocolate?"),
            _("Maybe.. ooh, Mexican hot chocolate with a bit of spiciness would be interesting!"),
            _("Maybe.. peanut butter-flavoured?"),
            _("Maybe.. that brand with a bit of cinnamon in it?"),
            _("Maybe.. one made with dark chocolate?"),
            _(".. I’m not saying it should come with marshmallows, but I won’t say no if it does~"),
            _(".. Actually, no, scratch that, I could go for a pick-me-up of coffee."),
        ]
        hotchocolatechoices = random.choice(hotchocolate_choices)
    
    m 7ekbla "Hey, before you go..."
    if mas_consumable_hotchocolate.enabled and mas_isWinter():
            if random.randint(1, 3) == 1:
                m "Ooh, actually, since it’s winter I should ask..."
                m 1etblu "It doesn't have to be right away, but I've been thinking if possible, could you try to grab a different flavour of hot chocolate?.."
                m 7etblu "[hotchocolatechoices]"
                m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
                return "quit"
            else:
                jump asknewcoffee
    else:
        label asknewcoffee:
        if mas_consumable_coffee.isMaxedStock():
            m "So I checked, and I have plenty of coffee left. This said, when I get low;"
        m 1etblu "It doesn't have to be right away, but I've been thinking I'd love to try a different type of coffee?.."
        m 7etblu "[coffeechoices]"
        m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
        return "quit"
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_prompt_shopformonika",
            unlocked=False,
            prompt="Am I grabbing you something to drink?",
            conditional="mas_seenLabels(['mcl_shopformonikacoffee',], seen_all=True)",
            action=EV_ACT_POOL
        ),
        code="BYE"
    )

label bye_prompt_shopformonika:
    python:
        hotchocolate_choices = [
            _("Maybe… peppermint?"),
            _("Maybe… caramel?"),
            _("Maybe… white chocolate?"),
            _("Maybe… ooh, Mexican hot chocolate with a bit of spiciness would be interesting!"),
            _("Maybe… peanut butter-flavoured?"),
            _("Maybe… that brand with a bit of cinnamon in it?"),
            _("Maybe… one made with dark chocolate?"),
            _(".. I’m not saying it should come with marshmallows, but I won’t say no if it does~"),
            _(".. Actually, no, scratch that, I could go for a new flavour of coffee."),
        ]
        hotchocolatechoices = random.choice(hotchocolate_choices)
    
    python:
        coffee_choices = [
            _(".. I’m fine with instant coffee."),
            _(".. Dark roast, if you please! Feel like something a little strong."),
            _(".. Maybe some French Vanilla mix?"),
            _(".. I have a particular desire for canned coffee. In Japan, there’s a lot of variety, you know~"),
            _(".. Coffee Milk sounds like a nice change of pace. Do you know of it? I think it’s popular in Australia; it’s coffee syrup in milk."),
            _(".. Cold brew coffee; I could go for something rich!"),
            _(".. Decaf, please! Have to cut back on the caffeine a little."),
        ]
        coffeechoices = random.choice(coffee_choices)
    
    m 1sublb "Hmm, let me think.."
    if mas_consumable_hotchocolate.enabled and mas_isWinter():
            if random.randint(1, 3) == 1:
                m "Ooh, actually, since it’s winter..."
                m 1etblu "Whenever you get around to getting me some more, a new flavour of hot chocolate?"
                m 7etblu "[hotchocolatechoices]"
                m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
                return "quit"
            else:
                jump asknewcoffee
    else:
        label asknewcoffee:
        if mas_consumable_coffee.isMaxedStock():
            m "I have plenty of coffee left. This said.."
        m 1etblu "Whenever you get around to picking up some more, a new flavour of coffee?"
        m 7etblu "[coffeechoices]"
        m 3fsb "Or surprise me outright, if you want! Either way, thanks, [player]. Love you!"
        return "quit"
