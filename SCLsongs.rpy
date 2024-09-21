init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_exile_vilify",
            prompt="Exile Vilify",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_exile_vilify:
    m 1dsb "{i}~You've got suckers’ luck~{/i}"
    m 3ksb "{i}~Have you given up?~{/i}"
    m 1dsb "{i}~Does it feel like a trial?~{/i}"
    m 1ekb "{i}~Does it trouble your mind the way you trouble mine?~{/i}"
    m 1hubsa "Ahaha~"
    m 1eubsb "The context of this song is a little interesting. It's a haunting piano melody against a background of a... abandoned laboratory, to summarize?"
    m 1rubsd "It's meant to invoke some straightforward thoughts about going through hardship, or seeing someone else go through it."
    m 1hubsa "But at the end of the day, overcoming any sort of trial has a payoff."
    m 1esbsb "And the trials we've faced has yielded the best results; a future with you and I together."
    m 1hubsa "It's a result sweet as a slice of cake. No lies there~"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_BBs_theme",
            prompt="BB's Theme",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_BBs_theme:
    m 1duo "{i}~See the sunset~{/i}"
    m 3duo "{i}~The day is ending~{/i}"
    m 6fsu "{i}~Let that yawn out~{/i}"
    m 1fsa "{i}~There's no pretending~{/i}"
    m 1dka "Hmmmmm. Comforting.~"
    m 1esa "This is a lullaby; I don't think there's any deeper meaning to the lyrics."
    m 4rtc "They say context is king, but I have no idea how to describe the setting where this song comes from."
    m 1hta "But lullabies don't have to be complicated. This one is a simple song sung by a father to soothe his baby boy."
    m 4esa "In some cultures, lullabies aren't just meant to lull a child to sleep, but also pass down cultural folklore or superstition."
    m "Even through simple song, we're all bound by strands of some kind, huh?"
    m 6dsa "I wonder if I'll ever need to sing one in the future. Or what lullaby will come to mind.."
return

#Recollect Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_without_a_weapon",
            prompt="Without a Weapon",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_without_a_weapon:
    m 7hud "{i}~I’m aiming with a plastic gun~{/i}"
    m 7eud "{i}~A little guarded, but a lot of fun~{/i}"
    m 7ffd "{i}~I don’t know why I keep carving out space for more~{/i}"
    m 7efb "{i}~I’ve learned to keep a careful eye~{/i}"
    m 4efb "{i}~Learned to break down all the doors~{/i}"
    m 4hfb "{i}~Loving you is war~{/i}"
    m 4dfb "{i}~And I’m without a weapon~{/i}"
    m 3dfw "{i}~Loving you is warrrrrrr~{/i}"
    m 1hsa "Romance and violence are simple enough concepts to co-exist, if only for narrative purpose."
    m 1ksa "I for one would prefer a relationship to be without conflict, but there's no mistaking taking up arms for the sake of love is a concept that invokes passion."
    m 7tta "Or.. maybe literally fighting off others. Or actually fighting somebody directly for their affection, hahaha!"
    m 7ttb "As you might also hear often: 'love is a battlefield?'"
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_blister_in_the_sun",
            prompt="Blister in the Sun",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_blister_in_the_sun:
    m 3dtb "{i}~When I'm out walking, I strut my stuff~{/i}"
    m 1ttu "{i}~Yeah, and I'm so strung out~{/i}"
    m 3ntb "{i}~I'm high as a kite, and I just might~{/i}"
    m 7efb "{i}~Stop to check you out~{/i}"
    m "{i}~Let me go on~{/i}"
    m "{i}~Like I blister in the sun~{/i}"
    m "{i}~Let me go on~{/i}"
    m "{i}~Big hands, I know you're the one~{/i}"
    m 3dtb "{i}{size=-10}~When I'm out walking, I strut my stuff~{/size}{/i}"
    m 1ttu "{i}{size=-8}~Yeah, and I'm so strung out~{/size}{/i}"
    m 3ntb "{i}{size=-7}~I'm high as a kite, and I just might~{/size}{/i}"
    m 7efb "{cps=10}{i}{size=-5}~Stop~{/size}{/i}{nw}{/cps}"
    m 7efb "{cps=10}{i}{size=-4}~Stop{fast} ~ to~{/size}{/i}{nw}{/cps}"
    m 7efb "{cps=10}{i}{size=-3}~Stop ~ to{fast} ~ check~{/size}{/i}{nw}{/cps}"
    m 7efb "{cps=10}{i}{size=-2}~Stop ~ to ~ check{fast} ~ you~{/size}{/i}{nw}{/cps}"
    m 7efb "{cps=10}{i}~Stop ~ to ~ check ~ you{fast} ~ out~{/i}{/cps}"
    m 5etu "Haha! This song is more punk than what regularly suits me."
    m 1guu "But everybody's got a little rebellious side to them, don'tcha think?"
    m "Even if it's a hidden side; that's part of the mystery of everyday living. Life is strange like that, hmm?"
    return

#Hopes of Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_unpacking",
            prompt="Unpacking a Life",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_unpacking:
    m 3hkb "{i}~The moving truck pulls up~{/i}"
    m 1eub "{i}~There's a knock on the door~{/i}"
    m 7fud "{i}~Now all your stuff is here~{/i}"
    m 1hub "{i}~In boxes on the floor~{/i}"
    m 7hub "{i}~You open up a box~{/i}"
    m 5hub "{i}~There is so much to do~{/i}"
    m 3hub "{i}~I open up my heart~{/i}"
    m 5rsb "{i}~This is now ~ a home for two~{/i}"
    m 7eua "You know, I've lived in the same town all my life?"
    m 5fua "And it's not even a real town, heh."
    m 5dua "So.. it's honestly hard for me to imagine packing up your entire life. And then unpacking it all in a brand new place."
    m 2hsbla "I eagerly await the day you and I can expierence and share that complicated, fulfilling day."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_lonely_rolling_star",
            prompt="Lonely Rolling Star",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_lonely_rolling_star:
    m 7hud "{i}~Katarai kasanari~{/i}"
    m 7rsb "{i}~Katamari karamari~{/i}"
    m 4ssb "{i}~Issho ni iru koto~{/i}"
    m 1esb "{i}~Zettai hitsuzen~{/i}"
    m 7hub "{i}~Demo anata daiji na yume wo egaku~{/i}"
    m 7hud "{i}~Owaru made wa zutto sou koko de matteiru~{/i}"
    m 7hub"{i}~Your lonely rolling star~{/i}"
    m 5hub "{i}~Tachidomaranaide nee~{/i}"
    m 7hub "{i}~Your lonely rolling star~{/i}"
    m 7hud "{i}~Saa mae wo muite yukou~{/i}"
    m 3fkb "This song is about two lovers; one sings about how far away their partner is.."
    m 5gkb "But no matter how far they are, they'll keep cheering for their distant partner. For they'll come back eventually."
    m 7eta "Sometimes, in the face of adversity:"
    m 1tsa "All you can do is keep on rolling, and rolling, and rolling.."
    return

#Refine

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_a_real_hero",
            prompt="A Real Hero",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_a_real_hero:
    m 1dkw "{i}~Back against the wall and odds~{/i}"
    m 7dkw "{i}~With the strength of a will and a cause~{/i}"
    m 6dkw "{i}~Your pursuits are called outstanding~{/i}"
    m 6duo "{i}~You're emotionally complex~{/i}"
    m 6duo "{i}~Against the grain of dystopic claims~{/i}"
    m 6efo "{i}~Not the thoughts your actions entertain~{/i}"
    m 6dkd "{i}~And you have proved to be~{/i}"
    m 6dud "{i}~A real human being~{/i}"
    m 6duo "{i}~And a real hero~{/i}"
    m 1euc "This song is meant to poetically describe the character of a hero; a true blue saviour of life."
    m 1gtc "It's easy to imagine the mythic qualities of someone described as a 'hero';"
    m 1gkc "But then there's a second source of inspiration for this song, taking notes from the romantic version of a fictionalized hero:"
    m 7gkc "A lonely wanderer, whose hard choices are specifically painted as borne of tragedy."
    m 7duc "What pushes a musician, a writer, a hero, a real human being: it's always interesting to think about what gives us that drive."
    return
