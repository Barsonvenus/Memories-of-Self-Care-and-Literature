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
            eventlabel="bye_onnextepisode",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_onnextepisode:
    m "{i}Next time:{/i}"
    m "{i}Will [player] beat Monika at chess?{/i}"
    m "{i}Will they have a steamy discussion about their latest thoughts on love?{/i}"
    m 7suo "{i}Or will serious repercussions bring tumultuous new changes to the world’s best couple?{/i}"
    m 3sfb "{i}Find out next time, on the next chapter of {b}'Monika After Story!'{/i}{/b}"
    m 1hubssdru ".{w=0.6}.{w=0.6}."
    m 1gubfsdru "{cps=40}Yeah, I wanted to send you off on a funny note, but that's actually a little embarrassing to say out loud-{/cps}"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_hype",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_hype:
    m 1hsa "Okay, [player]!"
    m 3nsb "It doesn't matter what time it is, where you're going, how long you're gone for.."
    m 1sub "I'm gonna send you off ready to take on the world."
    m 7sub "Say it with me: 'I'm gonna do my best!'"
    $ _history_list.pop()
    menu:
        "I'm gonna do my best!":
            m 1nub "I know you will."
    return 'quit'
    
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
        jump asknewcoffee

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_goldtruth",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_goldtruth:
    m 1hua "Well, time for us to say bye!"
    m 7hua "How best shall I prove my love in my parting words this time?"
    m 7sua "Ah, well. Sometimes sincerity divines all."
    m 4sfb "Goodbye, [player]! {b}{color=#FFD700}I love you with all my heart!{/color}{/b}"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_redtruth",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_redtruth:
    m 7sfb "Hmm, I feel like seeing you off in a special fashion; but how?"
    m 7ekb "It's a shame you can't hear the love in my voice."
    m 3eka "But luckily color invokes passion as well."
    m 3sua "Everything I speak in red is truth;"
    m 4sfb "{b}{color=#f00}You're the best person in the world, [player]!{/color}{/b}"
    return 'quit'
    
init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_bluetruth",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="BYE"
    )

label bye_bluetruth:
    m 1sup "What parting words should I leave you with?"
    m 1sub "Ooh, I have an idea. An affirmation of our status of a real power couple."
    m 7eub "I take our competitive relationship status quite seriously. Ah, if only you could hear the energy in my voice."
    m 7efb "Well, I suppose until proven otherwise;"
    m 4sfb "{b}{color=#5DECFF}We're the best couple in the world, [player]!{/color}{/b}"
    return 'quit'

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_rainbow",
            unlocked=False,
            aff_range=(mas_aff.AFFECTIONATE, None),
            conditional="seen_event('mcl_colouremotion')",
            action=EV_ACT_UNLOCK
        ),
        code="BYE"
    )

label bye_rainbow:
    m 7nfb "Okay, let me try this again.."
    m 7hfb "Because I want to be all sparkles and colour when I see you off!"
    m 4sub "{rainbow}Goodbye, [player]!-{/rainbow}"
    if renpy.random.randint(1, 2) == 1:
        m 6sksdrx "- Anddddd there's the headache, {i}owowowowowow-{/i} "
    else:
        m 4wup "..."
        m 3eub "Yay! No headache!"
    return 'quit'
