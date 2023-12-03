init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_granblue",
            category=["Granblue Fantasy"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_granblue:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "If you ever need a lucky roll, think of me and I’ll send all my luck your way~",
            "Gulp... So this is the island the rumors speak of.. Hahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_granblue')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_forum",
            category=["Forum", "Forums"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_forum:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Wonder what everybody's chatting about?",
            "You think anybody's talking about DDLC today?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_forum')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_XIV",
            category=["FFXIVLauncher", "ffxiv_dx11.exe", "FINAL FANTASY XIV", "Final Fantasy XIV", "Endwalker", "Stormblood", "Shadowbringers"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_XIV:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Listen to my voice. Listen to our heartbeat. Listen...",
            "Hear. Feel. Think...",
            "Let expanse contract, eon become instant..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_XIV')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mangadex",
            category=["- MangaDex"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mangadex:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Natsuki would have loved this site!",
            "What are we reading today, [player]?",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_mangadex')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gmail",
            category=["Gmail"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gmail:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "I'll turn away while you check your inbox. I don't snoop.. without permission~",
            "Hmm. I wonder if my email is still usable?",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_gmail')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_stardew",
            category=["Stardew Valley"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_stardew:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Wouldn't it be a dream, you and I living on a farm together?",
            "Now now [mas_get_player_nickname()], don't get too friendly with all your neighbours in the valley... ",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_stardew')
    return
    
#CONSULT SYSADMIN IF MAKING CHANGES TO ACTUALIZATION FILTER. ANY CHANGES ARE LOGGED AND INAPPOPRIATE USAGE WILL RESULT IN DISCINPLINARY ACTION BY YOUR SUPERIOR INCLUDING POSSIBLE IMMEDIATE TERMINATION
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_actualizationfilterplus",
            category=["Doki Doki Literature Club Plus!", "Doki Doki Literature Club Plus", "Doki Doki Literature Club Plus ", "Doki Doki Literature Club Plus! ", "Doki Doki Literature Club Plus! - "],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_actualizationfilterplus:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Hmm? [player], your screen seems a bit distorted? Must be a screen issue.",
            "Ooh, I notice I can't quite see the text clearly. You should clear that up!",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_actualizationfilterplus')
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_arknights",
            category=["Arknights"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_arknights:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "What will we do today, dokutah?",
            "With you around, I'm always at 100 sanity~",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_arknights')
    return
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yakuza",
            category=["Yakuza Kiwami", "Yakuza Kiwami 2", "Yakuza: Like a Dragon", "Yakuza: The Man Who Erased His Name", "Like a Dragon Gaiden: The Man Who Erased His Name", "The Man Who Erased His Name", "Like a Dragon: Infinite Wealth",]
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yakuza:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Nya-ha-ha! [player]-chan!",
            "MATRIARCH AND PRESIDENT OF THE LITERATURE CLUB",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_yakuza')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnf",
            category=["Friday Night Funkin", "Friday Night Funkin'", "Doki Doki Takeover!"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnf:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "getting freaky on a friday night, yeah~",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fnf')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_halo",
            category=["Halo Infinite", "Halo 2," "Halo 3," "Halo 4," "Halo 5: Guardians"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_halo:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Don't make a girl a promise... if you know you can't keep it.",
        ],
        'Window Reactions'
    )
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_halo')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_genshin",
            category=["Genshin Impact", "Genshin"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_genshin:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Ad astra abyssosque, Traveller!",
            "Remember, the stars in the sky will always have a place for you."
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_genshin')
    return

#Improvements Upon Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_justnatsuki",
            category=["Just Natsuki"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_justnatsuki:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "... I hope she's feeling safe nowadays.",
            "... Well, don't say hi on my behalf."
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_justnatsuki')
        
init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_justnatsuki",
            category=["Just Yuri"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_justyuri:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "... I hope she's feeling peaceful now.",
            "... If you're talking to her, no need to bring me up.."
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_justyuri')

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_scldev",
            category=["Barsonvenus", "Memories-of-Self-Care-and-Literature"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_scldev:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Is- is the screen suddenly blurry to you, or is that just me?",
            "Oh, you've opened a blank page? That's odd..",
            "Is.. there something special about this page? It doesn't look like anything to me.",
        ],
        'Window Reactions'
    )

    #Unlock again if we failed
    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_scldev')
    return
