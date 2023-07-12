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

#Recollect Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent._mas_compliments_database,
            eventlabel="mcl_compliment_posture",
            prompt="You have great posture, considering you're sitting all the time!",
            unlocked=True
        ),
        code="CMP"
    )
    
label mcl_compliment_posture:
    if not renpy.seen_label("mcl_compliment_posture2"):
        call mcl_compliment_posture2
    else:
        call mcl_compliment_posture3
    return

label mcl_compliment_posture2:
    m 1etd ".. That's {i}very{/i} specific."
    m 7gkbfu "And despite that I'm extremely flattered, oddly enough."
    m 5ftbla "I guess I've never thought about it up until this very moment, but I'd like to think I associate good posture with grace, poise.."
    m 5dsbla ".. and being pretty."
    m 7ftblu "So thank you for making me feel pretty."
    m 4hsa "And I'm impressed; a good compliment should sometimes be specific. It shows you pay attention."
    m "And I *do* try to pay attention to my posture."
    m 4hsb "So I'm glad you do too!"
    return

label mcl_compliment_posture3:
    m "Oh gosh. Every time you say this, I feel like it's such a odd thing to be flattered about."
    m "Even by flattering standards, I'm quite happy hearing this compliment from you.."
    m "..And you already say some {i}very{/i} flattering things to me."
    m "So thank you again, [player]."
    m "Hehe."
    return
