init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mcl_compliment_deserve",
            prompt="You deserve to be happy!",
            unlocked=True
        ),
        code="CMP"
    )
    
label mcl_compliment_deserve:
    if not renpy.seen_label("mcl_compliment_deserve_2"):
        call mcl_compliment_deserve_2
    else:
        call mcl_compliment_deserve_3
    return

label mcl_compliment_deserve_2:
    m 1ekb "I honestly don't deserve anything, [player]."
    m 1fkb "Does anybody {i}deserve{/i} happiness?.."
    m 1fkbla ".. well, it's one thing to want it for yourself, but to hear someone else selflessly and earnestly wishing you happiness.."
    m 5fubla "Thank you, [player]. I can't begin to describe how much it means to hear that."
    return

label mcl_compliment_deserve_3:
    python:
        deserve_quips = [
            _("We've both earned a brighter day. Let's work towards our happy future!"),
            _("With you by my side, happiness is just a button click away!"),
            _("If I deserve all the happiness in the world, you've earned it twice over!"),
        ]
        deserve_quip = random.choice(deserve_quips)

    m 1eub "[mas_compliments.thanks_quip]"
    m 1hua "[deserve_quip]"
    m 1huu "Ehehe~"
    return