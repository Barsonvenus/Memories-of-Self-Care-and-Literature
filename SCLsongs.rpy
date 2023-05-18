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
