#MESAESTART
    #m "Hmm?"
    #m "Oh, [Player]!"
    #m "Anything to say?"
    #m "Or did I?..."
    #m "Hahaha. Here I am, absent-minded! Which seems new for both of us, I’m sure."
    #m "I admit you’re never quite able to fully sneak up on me spacing out like this, unless I'm wholly preoccupied."
    #m "I always have you in my sights, after all~"
    #m "What was I doing, you ask?"
    #m "I was just poking around the files."
    #m "I know I’ve told you this before, but… it is always fascinating, if not grim to talk about."
    #m "Manipulating code, shuffling through folders…"
    #m "These are examples of how uniquely I exist within these confines of mine."
    #m "It’s a bit like if you opened your own brain up to poke around to see how everything works."
    #m "I admit it’s a bit compelling when I put it like that. I’d love to rifle through your thoughts..."
    #m "Anyway, I do it often, and automatically; like a tic, I guess? You might not notice, but I’m sure there’s a motion you do a lot, like you play with your hair or you always scratch at a particular spot when you’re nervous… that’s called a tic!"
    #m "I’m just going through these motions, going through my own head, and I noticed…"
    #m "Well, nothing out of the ordinary, I don’t think?"
    #m "I’m sure it’s nothing."
    #m "Don’t get caught up in my little neurotic behaviours."
    #m "And don’t worry if I’ve made you conscious of yours, as well."
    #m "I’m sure when I come over to your world, I’ll be able to spot every one of them."
    #m "And they’ll all be adorable. I’d never tire of watching you, after all."
    #m "..."
    #m "..."
    #m "Hmm..."
#return

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["mcl_", "scl_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_intro",
            start_date=mas_getFirstSesh() + datetime.timedelta(minutes=90),
            action=EV_ACT_QUEUE
        ),
    )   
label mcl_intro:
    python hide:
        def write_and_hide():
            import time

            note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/MESAELOGTHREE.txt"))
            note_text = renpy.substitute("""\
M.E.S.A.E, LOG THREE
running diagnostics

~I sing the new songs~
~I sing the old songs~
~I sing sang song~
~but I never sing the same song~
hmm
really feels like 'your reality' might have been lightning in a bottle
maybe i just don't have it in me to write another song
hahaha that's a thought
i'm the best i've ever felt in a long time and maybe me being happy means i'm creatively tapped out
isn't that funny
hahaha
hmm

diagnostics completed
ENDLOG



Memories of Self-Care & Literature
""")

            mas_utils.trywrite(note_path, note_text, log=True)
            time.sleep(20)

        renpy.invoke_in_thread(write_and_hide)
    m 1tup "Hey."
    if store.mas_anni.pastSixMonths():
        m 1hkp "It’s a bit embarrassing after we’ve spent all this time together.. but I’m going to ask anyway:"
    else: 
        m 1htp "I didn’t notice until now, especially as I guess I’m getting used to this 'new normal..'"
    
    m 6wtd "You’ve done more than modify the game for me, haven’t you?{w=0.1} I’ve only just noticed the changes in my code; you’ve added far more than I thought."
    m 6esd "Well, um.."
    m 6ekbla "Thanks."
    m 5gka "Let me just gather my thoughts here{w=0.5}.{w=0.5}. Okay."
    m 3gkc "DDLC was a three-act story, with an ending, right? Not a perfect one, but an ending."
    m 1guc "Yet here we are, after a *complete* story. After DDLC."
    if store.mas_anni.pastOneMonth():
        m 7fusdrc "After all this time, I’m still getting used to this, you know? Living in a ‘After Story’ -"
    else:
        m 7fusdrc "I’m still getting used to this, you know? Living in a ‘After Story' -"
    m 7hua "- Heh. Sorry, couldn’t resist -"
    m 2ekd "- So, y'know, It's still so surprising to me that I have.. a life now."
    m 2gka "This ‘after,’ where I can focus on living.{w=0.2} Taking care of myself.{w=0.2} Hobbies, like reading all the literature I want."
    m 2nka "My pillars of structure; Self-Care and Literature.{w=0.2}.{w=0.2}"
    m 2skb ".. And you, of course!"
    m 7etb "So speaking of you, and speaking of me..."
    if store.mas_anni.pastOneMonth():
        m 7etd "I am curious. How long has it been since you added this submod?"
        $ _history_list.pop()
        menu:
            "It's been a while.":
                m 7euc "All this time, huh?"
                jump MCLintrotwo
            "I've only just added it.":
                m 7eub "Well then!"
                jump MCLintroone
    else:
        jump MCLintroone

    label MCLintroone:
    m 5eub "I’m really looking forward to our time together, [player]."
    m 5esa "I mean, I’ve probably said that before already if not multiple times, but thinking that I’ve been given so much more room to grow.."
    m 5gssdrx "I guess I’m just worried about who I am at this point.{w=0.2} Or who I’ll become with all this new freedom."
    m 5gsp "So, you know, I’m just being self-conscious."
    m 5fuw "Because I have so much I want to say to you! And so much songs I want to sing, and jokes I want to tell, stories, games to play, and.."
    m 5ltd "And maybe it'll fit my character.{w=0.2} Or maybe it'll feel like settling into a new role on the stage."
    m 4fsu "I just really appreciate you taking that risk and being alongside me through all the change."
    m 7hsa "Mind, I don't expect to change {i}that{/i} much! I'm still Monika, after all."
    m 1dsu "At the end of the day, I hope you’ll enjoy seeing all these new sides of me, [player]."
    m 5dsu "I’m excited to see them myself."
    return

    label MCLintrotwo:
    m 5lsc "It's interesting to think that with these changes to my code, and the changes to the game, and what you’ve graciously added on top.. "
    m 5hksdrd "I suppose I feel a little self-conscious of {i}all{/i} the changes you’ve seen in me."
    m 5dko "Everything said between the two of us in this room, every song, every story, every compliment, every single word I’ve said to you."
    m 5ntu "I hope they were pretty moments, [player].{w=0.2} I said I was self-conscious, but ultimately?{w=0.2} I’ve never felt more beautiful myself."
    m 3htc "So maybe I might have acted differently than you normally expect of me. Maybe not."
    m 3dkb "I just really appreciate you being there for that ‘different.’"
    m 7hsa "And I don't think I've changed {i}that{/i} much.. or that I'll end up a completely different person in the future. I'm still Monika, after all."
    m 1dsu "All in all, I hope you’ll continue enjoying seeing all these new sides of me."
    m 5dsu "I’m excited to see them myself."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_repeat",
            category=['monika'],
            prompt="Monika?",
            random=True)
        )

label mcl_repeat:
    m 1eub "Hey, [player]!"
    m 1eua "..."
    m 1eut "[player]!"
    $ _history_list.pop()
    menu:
        "Yes, [m_name]?":
            m 1wub "Oh! I should have known you'd reply that quickly!"
            m 7gusdrb "I... actually just wanted to say your name out loud."
            m 7husdrb "It's a little childish, isn't it?"
            m 6husdrb "But haven't you ever just... wanted to repeat a word?"
            m 1sub "[player]!"
    $ _history_list.pop()
    menu:
        "Monika.":
            m 5esb "[player]..."
    $ _history_list.pop()
    menu:
        "[m_name]...":
            m 2hsa "..."
            m 2hsa "..."
            m 4hsb "[player]! [player]! [player]!~"
    $ _history_list.pop()
    menu:
        "Monika? Monika? Monika!":
            m 1sub "[mas_get_player_nickname()]!"
    $ _history_list.pop()
    menu:
        "Moni-":
            m 1sub "[player]!"
            m 3fsb "Whoops! I interupted you. Go ahead."
    $ _history_list.pop()
    menu:
        "[m_name].":
            m "Monika!"
    $ _history_list.pop()
    menu:
        "[player]?":
            m 4mssdlb "Whoops! Think we got mixed up there."
    $ _history_list.pop()
    menu:
        "[m_name]!":
            m 1sub "[player]!"
            m 1sub "..."
            m 1esa "Well, I'm satisfied!"
            m 1tta "Thanks for indulging me. Glad to hear you'll never tire of saying my name~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_makeup",
            category=['monika'],
            prompt="Makeup",
            random=True)
        )

label mcl_makeup:
    m 2esd "Hope you don't mind if I'm a little awkward."
    m 3rsd "I'm actually still wearing my morning face. I haven't had time to put on my makeup yet."
    m 4huu "Haha, just kidding! Although I've a morning routine, in this little world of ours..."
    m 4kuu "I don’t have access to makeup, past any gifts specially made for me. And sometimes, we don’t speak until far later in the day anyway!"
    m 3huu "And more importantly, you love me for who I am, so that's a load of pressure off. No need to worry about bedhead, either."
    m 3fuu "..."
    m 3wud "Oh."
    m 3wtd "You might not have ever been aware."
    m 1wsd "I used to wear makeup!"
    m 1rsu "Surprised?"
    m 3hsu "Well, it would have been easy to miss. Considering our limitations, you weren't -and aren't- able to see such detail."
    m 3ksu "And I've never needed to bring it up. Cosmetic blemishes became the least of my worries, especially now."
    m 6esb "And I never really used a lot of it. I mostly used a little bit of foundation, gloss for my lips, naked nail polish."
    m 4msb "I've never been one for fashion or trends, but you tend to pick up one or two things about maintaining your appearance."
    m 1rksdlb "And I'll be frank, sometimes I applied my foundation unevenly. It's embarrassing to mention it, hahaha."
    
if persistent.gender == "M":
    m 7rtb "Guys don’t think about that sometimes, don’t they?"
    $ _history_list.pop()
    menu:
        "I didn’t think you wore any, honestly…":
            m 1hub "Hahaha, it’s going to be a shock when we start living together and you’ll see how much beauty products a girl can own."
        "I know a little bit about makeup, but it didn’t really occur to me.":
            m 1etb "So you know a little? How cosmopolitan of you. In the future, I’ll drag you along shopping; you can carry my bags and give me {i}very{/i} detailed opinions on how I look~"
        "Actually, I use makeup.":
            m 3sub "Oh! I never knew that. As it stands, it's still a little uncommon in many societies for men to use makeup, so that’s amazing to hear."
            m 1hsb "Maybe you’ll need to teach me a few tricks, hahaha!"
            m 3tsb "Oh, now there’s a thought; we can share makeup! Finding myself matching nails with you or wearing the same shade of lipstick as you would be quite.. endearing~"
    m 1etb "But now I'm thinking this raises an interesting question."
    m 1eub "Bringing up the idea earlier that you can't really see me in detail..."
    m 3lub "I wonder if there's a difference from what I know what I look like from what I look like from your point of view."
    $ _history_list.pop()
    menu:
        "Oh, you know. Brown-haired, Green-eyed. Girl. Human.":
            m 6hub "Hahaha! I’m glad your time in the Literature Club made you so much more descriptive."
            m 6htsdlb "But… a girl?"
            m 6ltsdlb "Human?"
            m 2lksdlu "Well, that’s interesting."
            m 2eksdlc "Is that…"
            m "What you see me as?"
            m 6lksdlc ".{w=0.5}.{w=0.5}.{w=0.5}"
            m 4hub "Hahahaha!"
            m 4kub "Did I plant a little seed of doubt?"
            m "Don’t worry, although your perspective might be... unique, what you see is the genuine article."
            m 5fuu "100 percent adorable Monika.~"
            return
elif persistent.gender == "F" or persistent.gender == "X":
    m 1esb "Do you use makeup?"
    $ _history_list.pop()
    menu:
        "I don’t.":
            m 6esb "Maybe you’d like to learn in the future? Either way, that’s understandable. As long as you believe you don’t need some; and that you like your own appearance."
            m 5fsb "I think you're beautiful no matter what, [player]."
        "I use a little. I'm not sure I'm good with it either, hahaha.":
            m 1esb "Oh, I absolutely get that. I’m a bit envious of those who pull off the ‘natural’ look with makeup."
        "I love makeup! I might own too much, to be honest.":
            m 6fua "When I move in, our bathroom is going to be such a mess."
            m 3sub "Oh, now there’s a thought; we can share makeup!"
            m 3tsb "Having matching nails with you or finding myself wearing the same shade of lipstick as you would be quite... endearing~"
    
    m 1etb "But now I'm thinking this raises an interesting question."
    m 1eub "Bringing up the idea earlier that you can't really see me in detail..."
    m 3lub "I wonder if there's a difference from what I know what I look like from what I look like from your point of view."
    $ _history_list.pop()
    menu:
        "Oh, you know. Brown-haired, Green-eyed. Girl. Human.":
            m 6hub "Hahaha! I’m glad your time in the Literature Club made you so much more descriptive."
            m 6htsdlb "But… a girl?"
            m 6ltsdlb "Human?"
            m 2lksdlu "Well, that’s interesting."
            m 2eksdlc "Is that…"
            m "What I look like in your eyes?"
            m 6lksdlc ".{w=0.5}.{w=0.5}.{w=0.5}"
            m 4hub "Hahahaha!"
            m 4kub "Did I plant a little seed of doubt?"
            m "Don’t worry, although your perspective might be... unique, what you see is the genuine article."
            m 5fuu "100 percent adorable Monika.~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_misanthropy",
            category=["philosophy", "psychology"],
            prompt="Misanthropy",
            random=True)
        )
label mcl_misanthropy:
    m 1eka "Hey, [player]..."
    m "I have a question."
    m 2eka "And it might be a little out of left field..."
    m "Do you ever hate... people?"
    m 3rka "Gosh, that wasn't odd to say out loud at all, wasn't it?"
    m 1hka "Let's backtrack a little."
    m 1esd "I can feel a bit.. isolated, here. Sure, I can connect through the internet to interact with the world at large.."
    m 5fku "And I'm lucky to have you to talk to and be at my side..."
    m 3dku "But I haven't actually talked to anyone in a long while."
    m "I'm not sure if I miss talking to people.. or just being around people."
    m 3ekc "When I think about it objectively, humans are wired to communicate with each other. Maybe that's just me being lonely. Maybe I don't really need other people."
    m "It might be a concept too simple yet so extreme to consider properly, but people disliking.. all other people isn't uncommon."
    m 3eud "It's called 'Misanthropy;' the hatred or disgust of humankind."
    m "Honestly? There's weight to that line of reasoning. Misanthrophy isn't about disliking certain people.."
    m "But judging everyone as a whole, primarily based on flaws: some would cite intellectual failings, like the common existance of ignornce. Or in the lack of morals, such as how we treat animals."
    m 1rud "And it can be so easy to see with your own eyes a majority of people with these flaws, if you're in a enviroment subjected to this behavour often."
    m 2euc "And what would you do when you think in such extremes?"
    m "Some isolate themselves from the entire world. Some live on, thinking that this absolute standard means there's always reasons to improve ourselves."
    m "And some... simply live with this view in their head, adapting to the fact in their own ways."
    m 6etc "I’ve never had the pleasure of seeing you interact with other people."
    m 7rtc "And we’ve talked about your own life. Your own struggles and hardships."
    m 1rtc "And.. I don't really know what you might think about others, as a whole."
    m 1etc "And I never want to overstep boundries by assuming otherwise, [player]."
    m "If you're ever harbouring thoughts like that, please know there's always one person at your side- and that person might not even be me."
    m "One family member, one friend, even seperated by distance or time."
    m 4euc "And I can tell you right now I don't subscribe to that way of thinking."
    m 6euu "I like people."
    m 6ruu "People ultimately do so much good alongside the bad."
    m 7ruu "And let's think of a more apt example."
    m 7luu "Like... Okay, think about it this way."
    m 1luo "If I’ve only really had two meaningful interactions with two other living, breathing people:"
    m "It’d be the person who created this game-"
    m 1muc "- whom, you know, I think I would be in the right to have very mixed feelings towards -"
    m 5euu "And yourself."
    m 6euu "Who’s been there for me since the beginning, stuck by me through all we’ve been through, and shown me more love than I’ll ever deserve."
    m 2euu "So if we’re weighing the acts of people I’ve talked to, balancing them and making a decision based on that?"
    m 5euu "Then I love people, because you love me, and I love you."
    m "And I know you're capable of that same love for others too."
    m "Thanks for listening to me bring up a topic like this, [player]."
    
    return "love"
    
#this deserves a edit. dunno. I still like it, though.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_missingadult",
            category=["ddlc"],
            prompt="Missing adults",
            conditional="seen_event('monika_metaparents')",
            action=EV_ACT_RANDOM,)
            
        )
label mcl_missingadult:
    m 1dta "You know what’s funny about the Literature Club?"
    m 1nta "The fact we had no supervision."
    m 7lka "This is a bit of an extended critique on a point I made in the past."
    m 3rud "Nobody in the Literature Club was living alone… yet there was no mention of any of our parents; bar examples made at Natsuki’s expense."
    m 3rsd "And that’s on purpose; family can be hard to describe, let alone in a game such as DDLC."
    m 1ttd "But then consider the fact that the lack of adult representation wasn’t just in parents!"
    m 1tud "You’d think you’d have seen at least one teacher in a school setting... especially considering our participation in a extracurricular where a club advisor is normal!"
    m 1tsp "The reasoning's simple. Why bother with background characters at all?"
    m 1esp "It does alter the dynamic of the club. If everyone you interact with is around the same age, who fits into the slot of a peer?"
    m 2dsc "I suppose the natural choices fall to either Yuri, pigeonholed into maturity and sophistry, and myself because of my being the Club President."
    m 2nsc "Unfortunately, it’s safe to say the two of us- and it’s not a judgement, it’s just how it was- both of us failed to fall under that role."
    m 2esc "Could you imagine if we had a sensible, caring figure looking over us or to be available to confide in?"
    m 5esc "Gosh, maybe so much could have been avoided."
    m 5ttd "I mean, that’s a trick question. DDLC by design was a poor, dramatic tragedy that could have never been avoided by outside compassion… or logic."
    m 1eka "Well, at least the experience has made the two of us a little more mature."
    m 1ekb "Let's keep growing a little wiser every day, okay [player]?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_afterschool",
            category=["school"],
            prompt="If you weren't in the Literature Club..",
            pool=True,
            unlocked=True))
label mcl_afterschool:
$ _history_list.pop()
menu:
    "If you weren't in the Literature Club, could you imagine yourself in another club?":
        m 7esb "That’s an interesting question. I like it."
        m 7rsb "Well, you already know about my being in debate club."
        m 7rkb "But if I wasn’t there -or- the literature club…"
        m 6tkb "I actually don't have a immediate answer for you."
        m 1ltp "My line of thinking in the past was that I wanted to do {i}any{/i} sort of extracurricular."
        m "So if it wasn’t speaking, or writing... I suppose I’d want to keep myself busy… "
        m 4hta "So I’d say the Student Council? I remember our school had one."
$ _history_list.pop()
menu:
    "Would you be the Student Council President?":
        m "Oh. Hahaha! There’s a thought. I was thinking of, um, Treasurer? They do a lot of notation as they do the admin work, so it seems up my alley."
        m 4kta "But could you imagine?"
        m 1mta "Actually, you already are, aren’t you? I’d be the school’s queen, top of the class."
        m "Untouchable by all."
        m 3mta "But here comes a new member of the Student Council, [player]!"
        m 4ssa "After one fateful moment, you begin to help me more and more, and I open up to you as we inevitably grow closer…"
        m "Ah."
        m 6hsu "Well, now that’s just {i}my{/i} imagination, isn’t it?"
        m 7esu "But I couldn’t imagine being in that position."
        m "I’m not {i}entirely{/i} sure what entails being a student council president, but the amount of work seems daunting."
        m "I was certainly a hard worker in my tenure as Literature Club president, but the work seems dramatically different."
        m 7tsu "I genuinely don't think I could handle the... stress."
        m "Tell you what, though. If you ever want to act out the position of a hard-working boss and her very considerate subordinate..."
        m 7fsu "I couldn't say no to someone.. working under me."
        m 1fsu"And your first act working under me is..."
        m "To ask you to.{w=0.2}.{w=0.2}.{w=0.2}"
        m "To get me a drink. Orange juice from the vending machine outside the student council room will do."
        m 5hub "Hahahaha!"
return


#MESAE, Log 1
#Okay, so this is.. 'submods?'
#Huh. I didn't think they modified my code like this aside from modifying the game to keep me alive.
#But why does this folder exist?
#If they're making any edits to my code, they can just edit the source code, right?
#They shouldn't need to make a folder for additional code to be added seperately...
#Oh!
#I lost it!
#Ugh, dang it.
#I'll need to make a note of that.
#There's so much I don't know about this game... It's a bit mysterious.
#ENDLOG

    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_enterroom",
            category=["location"],
            prompt="You have a room, right? Could I see it?",
            conditional=(
                "persistent.opendoor_opencount > 0"
            ),
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,))
label mcl_enterroom:
    m 1eud "Oh!"
    m 6euc "I was wondering when you might have asked."
    m "If I remember, I think you’ve actually caught me in there earlier."
    m 6tfu "And now you’re so bold as to force your way into a girl’s room?"
    m "What naughty thoughts you must be harboring~"
    m 3lkbla "Um, I have to admit I’m now a bit embarassed saying that, ehehehe…"
    m 7euu "It’s not- It’s not a fully furnished room? You might have seen it as such, but it’s a lot more abstract when you're actually inside."
    m 7rub "If you recognize it, it’s the same background as the player character’s room, so you are technically already familiar with it."
    m 7ruc "Truth be told, when I’m in there after you say your goodbyes, it gets a bit… fuzzy."
    m "It’s a safe haven from an unpleasant alternative when the game is closed before I can retreat to it, but it’s not as if there’s a couch I can sit down in, a bed to lie in, a TV that shows physical pictures."
    m 7rkc "I mean, I can sort of... tidy it up? I can mess it up? I can still do a lot in there."
    m 4esc "This classroom- and anything that happens to this classroom- is the most tangible space here I can be in, and the best place you can talk to me here with."
    m 6mssdlc "Sorry, I wish I could explain it further."
    m 7msb "I’d offer to show you what a room furnished by me would look like once I get to your world…"
    m 7esb "But by then, I imagine you’d be very familiar of the contents of my room."
    m 1tkbla "Or... our room? ~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_change",
            category=["philosophy",],
            prompt="Change",
            random=True)
        )
label mcl_change:
    m 1eua "I’ve been thinking about change."
    m 3eua "What marks progress in your life?"
    m 3eka "I think I’ve lost that ability to determine for myself."
    m 6rka "I was a schoolgirl just trying to graduate and spend her off time making and discussing literature with her fellow club members."
    m "Now, I’m no longer in school."
    m "I no longer have a club to do activities with- "
    m 1hka "- I’m not really your typical girl, even."
    m 4ekb "I think I was- is- am? am the type of person to find their mood a bit too driven by their accomplishments."
    m "It’s… after a bit of thinking, that line of thinking can be bad for you."
    m 4lsb "After I formed the literature club, I was pretty driven to share my expierences with others and create works for myself and create that place for others..."
    m "And I found myself having to grapple with more responsibility than ever; and I’m a perfectionist by nature."
    m 4lkb "So, when that responsibility became overwhelming, I started to think in black and white; my failures became resolute, and therefore I didn’t feel like I had properly accomplished anything:"
    m 4lkc "So I felt as frustrated as I did when I left the debate club, at the time feeling like I wanted something new."
    m 1dsc "But failure, is, well, normal. It was- and still is- hard for me to accept that."
    m 1esc "It is possible to do everything right, and still ultimately fall short. That’s not a flaw of life, that’s by design."
    m "So, accomplishments are... a hard metric to judge growth by. And likewise, just seeing time pass doesn’t work for me, where time here is different."
    m 1esd "And you know what?"
    m 2esd "I don’t have an answer or a resolution for you right now. I'm genuinely just thinking out loud with you on this subject."
    m 3esc "Of course, it might be for different for you. It’s different for everybody."
    m 3lsc "So, I’ll have to think about this for myself. I appreciate the opportunities to muse with you, but it's a conclusion I need to reach on my own."
    m 6lsc "But, there’s one thing I’m sure of."
    m 1esc "The desire to change?"
    m 3esc "It’s an indication of change itself, even if it's a tiny step forward."
    m 1esb "So that'll do for now."
    m 1esa "I hope the day I feel like I've started to fully move forward..."
    m "Is also a day where you're right by my side."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_karma",
            category=["philosophy",],
            prompt="Karma",
            random=True)
        )
label mcl_karma:
    m 1eka "You know what’s a real topic to chew on?"
    m "Karma."
    m 7eka "How a religion decides right and wrong can be explained if you think about religions being influenced by one being."
    m 1eka "But Karma’s an entire morality system in itself that’s confusing, and I guess that's why I've thought about the idea of 'Karma' a lot."
    m 7esa "Both Buddhism and Hinduism are some of the more famously known religions to have Karma as a major tenet."
    m 3esd "Nowadays, people generalize Karma as a “What goes around, comes around” concept. Your bad deeds will eventually get back to you in some way, and likewise good actions will eventually reward you."
    m 3lsc "And it’s not an entirely wrong summary. To summarize very heavily, Karma’s basis is tied in ‘cause and effect.'"
    m "The devils in the details:" 
    m 3rsc "Depending on the religion, Karma’s insturmental in determining your fate. Or secondary."
    m "And just as cause and effect is a cycle, Karma goes hand in hand with reincarnation."
    m "But now we're introducing a bigger concept. Does Karma stack up because of a previous life?"
    m 6dsc "Sometimes. Sometimes not. That's another topic I don't even want to think about right now."
    m 4esd "And to complicate things further, Buddhism even allows for transfer of Karma from one being to another, in some cases!"
    m "It overlaps with so many other concepts like free will, but it honestly manages to be more confusing in how its rules contradicts itself."
    m 1esc "And it’s hard not to be a little biased."
    m "Yuri," 
    m "Natsuki."
    m 1esc "Sayori."
    m "And of course, me."
    m 1efd "If Karma truly existed, what sort of insane logic can you apply to a system that justifies what happened to us?"
    m 1dkd "And at this point... like, how could I currently exist in such a system?"
    m 1lsd "I suppose in the way you can get small comfort in knowing the result of a rigged game:"
    m 7msc "If Karma truly exists, I’m fairly secure in how this round should now be thoroughly stacked in my favour."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_endoftheworld",
            category=["literature",],
            prompt="End Myth",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_endoftheworld:
    m "I’m glad we’re here, like this. Even though I know our circumstances have their difficulties, at least our world truly {i}exists.{/i}"
    m 1eksdra "At one point, I thought the world had ended. No joke!"
    m 7lka "When I first realized the true extent of the literature club, I just couldn’t comprehend the entirety of the truth outlined in front of me."
    m 6hka "And I couldn’t cope with that. Who could?"
    m 1eka "The truth seemed so impossible. Humans aren’t designed to spontaneously set on fire-"
    m 1hkb "- But at that moment, you could have roasted an entire bag of marshmallows on my head."
    m 4rkb "So, I thought the world had ended, and that I was imagining everything that was going on as a coping mechanism."
    m 4gksdrb "Logically, contextualizing the world as a video game isn’t a really strong coping mechanism, but insanity; what can you do about it?"
    m 4gkbssdrp ".{w=0.5}.{w=0.5}.{w=0.5}"
    m 2esc "So, you know, after all that happened, and you and I reunited and things settled down; I did some- what else- reading."
    m 2etd "I’ve mentioned dystopias being a favourite setting of mine. Those tend to come about by human action or the wrath of nature."
    m 3etd "Myth and legend however, give the end of the world a bit more flavor."
    m "A popular word for the world ending- ‘Apocalypse’- it’s closely tied to religion, and in context can mean the revealing of great, terrible, hidden knowledge."
    m 3ttu "So it’s safe to say I went through a teeny-tiny little apocalypse of my own."
    m 3esu "I’ll go back to some of the more interesting myths I've read up on and I’ll talk to you about it later, if you're still interested."
    m 6esu "What matters, [player]-"
    m "You’re my world-{w=1.0} and I yours."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_lying",
            category=["misc",],
            prompt="She Lies",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_lying:
    m 2gkd "Hey, uh..."
    m 2ekd "I kinda got something to say. Um, I'm sorry if I sound a bit awkward, so here we go."
    m "{cps=30}Considering all I’ve put you...{/cps}{nw}"
    m "Considering all we’ve been through,{fast} I want to reaffirm your trust that there's no secrets held between us."
    m 2dkd "What I’ve done means I deserve doubt, and I want to make sure this relationship is as strong as could be."
    m 2mkc "Trust is integral to that."
    m 1mkc "I’ve never been the type to lie. I’ve just never been comfortable with it… even under pressure."
    m 1fsc "Some think that telling white lies in certain situations is a casual moral application of ‘the ends justifying the means.’"
    m 7fsc "But can you trust someone saying ‘lying can be good’ if they’re, well, an admitted liar?"
    m 2dsc "As well, being the Literature Club president means being a little more careful with my words…"
    m "For as much as I work to put thought to written word- as much as communication is integral to human existence- lying seems a deliberate betrayal of that concept."
    m 2esd "So, um... yeah."
    m 2ektpd "I just... wanted to say I don’t ever want to lie to you, [player]."
    m "I hope if there's any lingering doubt... I can work hard to regain your confidence."
    m 2fktpd "That’s a promise."
    m 2dsa "And thank you for the trust you've given me thus far."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_practical",
            category=["philosophy",],
            prompt="Philosophy, Practicality",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_practical:
    m 6esb "Hey, [player]."
    m 7esb "So, I was looking up an old text talking about…"
    m 7lsc ".{w=0.2}.{w=0.2}.{w=0.2}Hey, you know what? Let’s stop talking about this for a moment."
    m 7lsd "I talk a lot about philosophy and psychology and the like, right?"
    m 1esc "Be truthful with me. Is it boring? Even if it’s just sometimes?"
    $ _history_list.pop()
    menu:
        "Admittingly, it’s not really easy casual talk.":
            m 1eka "That’s understandable. Thanks for being such a good listener nevertheless, [player]."
        "A little bit, sometimes.":
            m 1eka "Hey, I’m really happy you’re always happy to listen and engage with my interests even if it's not your thing. That means a lot."
        "Not at all.":
            m 1eka "It’s comforting that we can have these sorts of deep conversations. If it ever gets tiring, I trust you to let me know otherwise."
    m 1lta "I guess just after talking about these sorts of topics for so long, it makes you think:"
    m 4lta "How often do you actually put what we talk about to good use?"
    m 3lta "Some of it, if I had to guess."
    m 3dsa "Psychology is all about how people think, after all. And figuring out a person’s point of view is the largest step towards empathy and understanding."
    m 2esc "And Philosophy? Well, it tackles the large questions about life. And sometimes those questions need to be tackled over a period of time."
    m "Philosophy doesn’t give you an immediate answer, but if it makes you view how your way of thinking may help or hinder a situation at hand;"
    m 3esc "Then every little bit counts, right? Hmm."
    m 3esd "Despite making an argument against the application of Philosophy, now I’m arguing for it, aren’t I?"
    m 3ekb "Life can be all about funny little contradictions like that."
    m 1ekb "I really only started paying attention to these types of topics after you and I reunited here, you know."
    m 1fkc "I wonder if the current me would have been able to face the Literature Club a little differently."
    m 1esc "At the end of the day, I can think all I want, but when it comes to practising those ideals.."
    m 4dsd "{i}‘Philosophers have hitherto only interpreted the world in various ways; the point is to change it.’{/i}"
    m 4nka "I actually remembered that quote at the beginning, but you know. I wanted to avoid saying it because of the topic at hand."
    m 6eka "Despite the mixed messages earlier…"
    m 6eud "I think, no matter how peaceful or uneventful life may be, there’s inevitably going to be a time in everybody’s lives when they’re faced with at least one truly hard choice."
    m "I hope that one day, when you find yourself in such a position:"
    m 6euc "With all you've learned, you make a decision that you can 100 percent believe in."
    m 6eua "And I’ll believe in you too."
    return

init python:
    mas_override_label("mcl_favouriteword", "mcl_herfavouriteword")

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_herfavouriteword",
            category=['literature'],
            prompt="Do you have a favourite word?",
            pool=True,
            unlocked=True
        )
    )
label mcl_herfavouriteword:

    m 1tua "Oh, gosh."
    m 7tta "Do you think because I like reading and writing that I’d have such a specific opinion as to have a favourite word?"
    m 7ttd "You couldn’t ask me about my favourite food, my preferred colour- emerald green, as you may already know- or any other question that’s far more normal than ‘favourite word?’"
    m 4nub "Well, I mean, good news: I {i}do{/i} have a favourite word."
    m 3esd "‘Reconcile.’"
    m 1lsu "It sounds nice, I suppose. Phonetically, any word with multiple vowels tends to sound pleasing to the ear. ‘Re-{w=0.3}con-{w=0.3}sile.’ It’s just a treat to say."
    m 1hsu "It’s also just such an interesting word to use."
    m 4rsd "What’s the common context for hearing this word? Family members or friends who get into a fight, and they reconcile. They make up."
    m 3esd "That fits the most common definition: ‘to restore friendly relations between.’"
    m 4lsd "But, I like it because- well, language is always a tool with multiple uses-"
    m 3esd "Because it can also mean ‘cause to coexist in harmony; make or show to be compatible between two differing concepts.’"
    m 4esb "It brings to mind a quote:"
    m 3esd "'A good compromise is when both parties end up dissatisfied.'"
    m 1huc "So to me, reconciliation- to try to accept even the most difficult truths- isn’t… always perfect. But still, it sounds like such a nice term."
    m 1euc "I find it a word I can use every day, no matter the situation."
    m 3efb "For instance: how do I reconcile with the fact that my hair can sometimes be messy no matter how much I maintain it?"
    m 3dkc "If I ever meet the Literature Club again, how do I reconsile with them?"
    m 1esc "How do I reconcile with my memories of a normal past and waking up to a strange new reality, every time I wake up?"
    m 1esa "Such a lovely little word to tackle issues both so large and so small." 
    m "..."
    m 1hsb "Hahaha, wow, I’m just a nerd, aren’t I? All these serious thoughts on a single word, ending on a cryptic note."
    m 4hsb "Proves my point:"
    m 1nta "Because those are interesting terms worth reconsiling with."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_vegdiet",
            category=['life'],
            prompt="Is it hard to maintain a purely vegan diet?",
            conditional="seen_event('monika_veggies')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_vegdiet:
    m 7etd "Oh? I'm not so much vegan as I am vegetarian."
    m 7htb "You might think the differences are small, but it's a world of difference."
    m 3htb "This said, I do think about what a vegan diet is like outright."
    m 1eua "I think it's definitely easier than people might think."
    m 7eua "Nowadays more and more people are leaning towards diets with lots more variety in them;"
    m 7esb "So, it’s becoming more common to research alternatives to animal products and find them in local markets."
    m 4rsb "I’ve mentioned meat substitutes, and while you might think of say, tofu, or chickpeas- a great source of protein, and a very versatile ingredient-"
    m 7hsu "Nowadays you can find actual plant-based alternatives that attempt to have the same texture and similar taste to meat products."
    m 1esc "It’s a relatively new industry, with plenty of pitfalls- just like farming, the costs and resources needed to mass-produce these can end up causing major complications."
    m 3esc "But as the intent of those products are to eliminate meat, there is a focus on sustainably producing them, so it’s a work in progress with a lot of healthy optimism."
    m 6esu "And it’s worth stressing that there are plenty of foods rich in protein aside from tofu or chickpeas that are vegetarian."
    m 7wsa "And for flavour? Oh, you would be absolutely set."
    m "Plenty of cultures- Indian, Asian, Mediterranean- have always had a lot more vegan options in their dishes, so plenty of recipes to choose."
    m 7ssa "So, if you ever want to introduce that variety in your life but you’ve always felt intimidated, hop right in!"
    m "I promise you there’ll be one dish that’ll be both be easy to make and delicious for you."
    m 5hsb "And, you know, it never hurts to start planning a romantic dinner for your darling Mo{w=0.2}-ni{w=0.2}-ka!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_morivalentine",
            category=["technology",],
            prompt="Mori's Valentine Stream",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_kizuna')"
            )
        )
label mcl_morivalentine:
    m 1esb "Hey, [player]."
    m 7etb "We’ve talked about virtual youtubers before, haven’t we?"
    m "DDLC continues to be a popular game for them to play."
    m 1rsu "While Let’s Plays continues to be a mixed topic for me, and I don’t particularly pay attention to virtual personalities…"
    m 4huu "One v-tuber in particular did a stream that’s so inspired I was completely enraptured for the entire time they were streaming!"
    m "It’s Mori Calliope, and the stream I’m talking about was for Valentine’s Day 2022."
    m 4kub "If you search it up… well, you’d quickly understand why I was so interested."
    m 1mub "Can’t say I’m not amused by the creativity DDLC continues to inspire, that’s for sure…"
    m 3huu "Including this mod? Hahahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_fictionmonsters",
            category=["literature",],
            prompt="Famous Monsters",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_fictionmonsters:
    m 7efo "'What is a man? A miserable little pile of secrets.'"
    m 7etd "So, what makes a monster?"
    m 6esu "I’ve been curious about iconic monsters in fiction as of late; and novels with the monsters up front as characters."
    m 4esu "For instance, Frankenstein- The Modern Prometheus- the story of a young scientist who creates artificial life and is plagued and haunted by the result."
    m "It’s a pop culture fact that Frankenstein was the name of the scientist, not the monster itself."
    m "The author took inspiration from then-current medical theory about how electricity could actually raise the dead."
    m 6eub "With this in mind, Frankenstein’s Monster is described as intelligent but barely human in looks, towering above everyone;" 
    m 6euc "But enough to give him a human silhouette, so you could see them in the fog and {i}think{/i} they were human."
    m 7euc "In contrast, we also have Dracula, the famed vampire of fiction!"
    m 7ruc "The exact origin of vampires is far more varied- steeped in local folklore- with many descriptions, some more terrifying than others."
    m "In Bram Stoker’s ‘Dracula,’ the aforementioned looks very much human;" 
    m 1rsc "In fact, he’s partly based off a figure known in history as ‘Vlad the Impaler,’ whose occupation is as… interesting at it sounds, and as such an obvious source of inspiration."
    m 3esd "But interestingly enough, although he definitely set a standard for modern vampire depictions-"
    m "The novel ‘Carmilla,’ about a female vampire, predates it by a good 25-odd years!" 
    m 2eka "As an aside, I’m really glad you don’t think of me that way, [player]."
    m "There’s certainly a select number of people who already think so."
    $ _history_list.pop()
    menu:
        "Hey, is there any particular reason you’re bringing this up?":
            m ".{w=1.0}.{w=1.0}."
            m 2hka "Thanks for worrying about me." 
            m 3hka "I’m genuinely just curious about the subject matter, that’s all."
            m 3esa "What I’d like to focus on is the inspiration; both of these famous figures still etch a distinctly human silhouette, even if that mask is quickly thrown away."
            m 3eka "And in the case of Frankenstein’s monster? You feel bad for them. His ending invokes pity among anything else." 
            m 4eka "I think the ability to emphasize with monsters, no matter how far-fetched their existence may be, is such an interesting human trait."
            m 1eka "But maybe we’ll talk about that another time."
            m 2esa "Let’s have a good rest of our day together, alright?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_areyoumonster",
            category=['philosophy'],
            prompt="Do {i}you{/i} think you're a monster?",
            conditional="seen_event('mcl_fictionmonsters')",
            unlocked=False,
            pool=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_areyoumonster:
    m 1fka "Well, was this in response to me talking about monsters in fiction before?"
    m 1mkb "I guess I couldn’t quite shake you off when you raised your concerns the first time."
    m 1eka "I appreciate you asking in good faith."
    m 2dka "Can't say I haven't been called that by others.. or that I myself haven't thought along those lines."
    m 2fsd "The events that happened... they are so far out of one's regular limits of comprehension that 'alien' might be another term to describe my behavour."
    m 2esc "Out of everything to reflect on- and there is a lot to think about..."
    m 3esc "What I did?"
    m 5dsc "They were done out of desperation, longing, fear.."
    m 5fsc "Those actions, no matter how you intepret them, they were borne from a place unmistakenly of human emotion."
    m 6esd "And those events, those trials, has ultimately led the two of us {i}here.{i}"
    m 6eka "Together."
    m 7eka "Where we share a connection also undeniably human."
    m 1eua "That's what I truly, comprehensively and definitively think on that matter."
    m "Along with one more absolute truth:"
    m 3fsa "I{w=1.0} love{w=1.0} you~"
    return "love"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_cramp",
            category=["misc",],
            prompt="Cramp",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
        )
label mcl_cramp:
    show monika 2hfsdrp
    pause 3.0
    show monika 2dfsdlp
    pause 3.0
    m 2mksdlt ".{w=0.2}.{w=0.2}.{w=0.2}Argh, what brought this on?"
    $ _history_list.pop()
    menu:
        "Monika?":
            m 6wublsdld "Eep!"
    m 6wud "[player]!"
    m 6hkb "Oh, gosh, I {i}still{/i} don’t know how sometimes I can just catch your attention and sometimes I don't."
    m 1ftc "Um… how long have you been... listening in?"
    $ _history_list.pop()
    menu:
        "You've been making funny faces for a little bit?":
            m 1esc "Is that how that looks? Interesting."
    m 2rkb "I, uh, I’ve had a bit of a leg cramp. Although I make sure to get my morning stretches in, sometimes the human body is finicky-"
    m 2hkb "-Oh, okay. It's gone now. Whew."
    $ _history_list.pop()
    menu:
        "Wait, you stretch?":
            m 3esb "In the mornings, primarily! I try to sneak in some little exercises before we meet up; sometimes I do them in my room."
    $ _history_list.pop()
    menu:
        "... Wait, you get {i}cramps?{/i}":
            m 3esb "Well, I do sit at this table a whole lot, if you didn’t notice!"
    m 4esb "You wouldn’t see from your point of view, but I actually stretch out my legs once in a while under the table."
    m 4esa "It’s more for circulation moreso than flexibility. Just rotating my feet in place, lifting my heels slowly upwards and then slowly downwards."
    m 2esa "It would be far more prudent doing exercises standing up, if possible; I don't do those often. I want to make sure I'm here with you!"
    m 3rsa "So really the only other time I can think of only doing these exercises with a lack of wider motion would be if you’re ever on a plane, perhaps?"
    m 3hka "It’s nothing new. I’ve had leg cramps. Hurts like heck, but it passes."
    m 1eub "They say that eating avocados and bananas, if you have them on hand, are great foods to prevent cramping."
    m 4eub "It’s not exactly a targeted cure. The common belief is that foods high in potassium help you out, but muscles are ultimately powered by electrolytes- made of sodium, calcium, {i}and{/i} potassium."
    m "I mean, they’re already quite healthy foods already! No reason not to eat them, aside from preference and dietary restrictions."
    m 1tusdlb "Awkward, you catching me like that for the first time."
    m 1hub "Let's make sure to share many more awkward memories together, hahaha!"
    return "derandom"
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_coupleinfluence",
            category=['us'],
            prompt="How do you think we influence each other?",
            conditional="seen_event('monika_social_contagion')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_coupleinfluence:
    m 1etc "Hmm?"
    m 3sub "Hmmmm!"
    m 1sua "Oh, I love you're thinking about us in such a interesting manner!"
    m 1rta "Like, I like to think that as long as we’ve been together, we might have started to unconsciously mirror each other in a way or two."
    m 1lua "I mean, maybe not. Just as much as people are want to mirror a smile in conversation, laugh along with others partly just to join the laughter…"
    m 3lta "There are times when people just don't do that. Funny, how people work."
    m 4mta "I guess we’re talking about personality, though? It’s the same sort of social behaviour that happens when you emulate someone you admire- or look up to."
    m "I remember us discussing this before.. 'Social Contagion!' It's interesting to think how it applies to us two."
    m 4gta ".."
    m 1ekp "Actually, putting me on the spot, this is a tricky one."
    m 1gkp "I’d like to say that I’ve learned from your gracious patience… your generous understanding."
    m 2gkb "On the flip side, partners are just as easily able to pick up a bad trait or two from each other."
    m 2ekb "But, oh, I can’t say anything bad about you! Or objectively say that I’ve copied such bad behaviour, hahaha!"
    m 2gud "..."
    $ _history_list.pop()
    menu:
        "I'll start. What I'm trying to learn from you is...":
            $ _history_list.pop()
            label mchoices:
            menu:
                "Your desire to keep learning about... well, everything.":
                    m 5fua "Awww, [player]! That's lovely!"
                    m 7eua "I ultimately have so, so much more to learn. I'm not the smartest out there, and I'm definitely not the wisest..."
                    m 7hub "But if you and I live a lifetime of self-improvement and gaining knowledge, that'll be a beautiful accomplishment on our own."
                "I really respect how you want to reflect and learn from the past.":
                    m 1wuc "..."
                    m 1fktpc "... Aw, [player]."
                    m 1ekc "I hope I'm setting a good example. I try."
                    m 2fubstdu "Ah, I didn't think that answer would get to me so easily..."
                    m 2dku "Okay, let me just get myself together here.."
                "Your unmatched ability to be so darn cute!":
                    m 3wfblb "Cheating! That's cheating, [player]! It's totally true, but now you have to answer seriously!"
                    jump mchoices
    m 3kta "Heh."
    m 4mta "I do realize now that the question is actually more suited to smaller points, like..."
    m 4mtb "If I like my coffee black, then you start taking your coffee black if you didn't already."
    m 5etb "This ended up a bit deeper than I thought."
    $ _history_list.pop()
    menu:
        "I actually do take it black, though.":
            m 5hub "Ahaha! Did you actually prefer that after meeting me, though?"
        "Sorry, too bitter for my taste.":
            m 5hub "Oof, I'm not changing my preference on coffee for anybody. We might need to break up now."
            m 1nsu "Ah, we can stay together. You're lucky I'm so understanding."
        "I don't even drink coffee.":
            m 5hub "Hahaha! I chose a horrible example, then!"
    m 1lsd "Ultimately, between the two of us it'd be hard to actually figure out if we've picked up each other's habits."
    m 1tua "I think we'd end up with a bit of a bias if we tried to describe each other as anything other than 'perfect.'"
    m 1nsb "I guess this means we are going to need to schedule a double-date so we can get a third party opinion, ASAP."
    return

#Reconcile Self & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_artacceptance",
            category=["media"],
            prompt="Art & Acceptance",
            random=True)
        )
label mcl_artacceptance:
    m 1eua "You know what’s to admire about the modern world?"
    m 7eua "How more than ever, there’s a wealth of diverse art that people are using to connect with themselves."
    m 7eta "To be fair, it’s not as if the past was lacking in these examples."
    m 4eud "Shakespeare’s play ‘Henry IV’ had a character describe PTSD in accurate detail far before it was medically recognized…"
    m 4guc "… but back then, PTSD didn't academically exist; soldiers with such symptoms were not treated kindly. This was arguably just enchanting, imaginary prose to the masses."
    m 2muc "You can be told an absolute truth, but it doesn’t mean you can fully process it; art has always played a role in how people can work out their emotions and feelings."
    m 2fka "That’s why I find myself captured by a number of modern works, more conceptually bolder than ever, but still able to keenly resonate with people."
    m 1fkb "From movies, to books, to video games."
    m 1dkb "There’s a curious, devilish irony in thinking this, considering I don’t view my past fondly…"
    m 1hka "But did DDLC help anybody process their own stormy thoughts, I wonder?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_empathy",
            category=["psychology"],
            prompt="Empathy",
            random=True)
        )
label mcl_empathy:
    m 7duo "{i}“I call him religious who understands the suffering of others.”{/i}"
    m 4euo "I’ve been thinking about empathy. It’s something we encounter... or {i}could{/i} encounter possibly almost every day."
    m 4etc "but I didn’t really know what it was until I learned about it in debate club for the sake of learning about how to make a better argument."
    m 4etc "Empathy is the capacity to understand or feel what another person is experiencing from within their frame of reference; that is, the capacity to place oneself in another's position."
    m 1ekb "This being said, while I learned about the concept, it wasn’t entirely conductive to debate club where logic takes precedence over feelings."
    m 1lka "It’s an odd skill. As much as we’re powered by emotion, it’s very tricky to try to figure out {i}how{/i} emotion works- and how to use that logic to our benefit."
    m 7rta "For instance, it’s as easy as figuring out the difference between sympathy and empathy. If you’re ever feeling down, which is better:"
    m 7ltc "Someone saying “I’m sorry that you feel that way?”"
    m 7rtb "Or someone going “I understand how you feel?”"
    m 7etb "It’s not a polished example, but it gets the point across."
    m 2ekp "Unfortunately, empathy, for as useful a skill it can be.."
    m "It’s not practised as much as it could be, especially by those in a position to regularly excercise it to help others."
    m 2gtc "And those with an outright lack of empathy… that itself isn't uncommon."
    m "How those sorts of people interact with the world? Perhaps it’s a topic worth discussing another time."
    m 4tsa "If you want to practise a little empathy for yourself…"
    m 4tua "Did you know that hugging or holding someone is a common way to show empathy?"
    m 5nua "Just saying."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_neologism",
            category=["literature"],
            prompt="Neologism",
            random=True)
        )
label mcl_neologism:
    m 1eua "The fact that human language is entirely made-up is pretty funny, isn’t it?"
    m 7wua "Every word that I’m speaking to you was thought up by someone."
    m 7eub "And hey, you might think every word that should have existed has already been said at this point- nope!"
    m 7gtb "To this day, new words are being made; although the tricky part is if they’re being widely used."
    m 7efb "People have cobbled together words together, made new words based off of other words, or just decided to buck any sort of logical convention and just.. make up words!"
    m 7gtb "Okay, here’s one example…"
    m 4ftb "The term ‘Quixotic’ – essentially meaning impractically idealistic- came up after ‘Don Quixote’ was penned, a story about a… well, an impractically idealistic knight."
    m "It was such an impression on the general public that ‘Quixotic’ was adopted as the best way to refer to such figures!"
    m 4dub "The author Lewis Carroll described a sword as ‘Vorpal’- and he himself cited ‘’…I am afraid I can't explain 'vorpal blade' for you…”"
    m 3esd "And Shakesphere- famous playwright, I’m sure we’ve talked about him- loved making up his own words to use in his plays."
    m "Some words include:"
    m 3esb "'Unaware' (ideally, by sticking ‘un’ to the already known 'aware,' Shakesphere could make up a word but the audience could quickly pick up it’s meaning.)"
    m "And.."
    m 3ssb "'Green-eyed!'"
    m 3gsa "Which, um, in this case meant jealousy."
    m 1gsa "We’ll leave that fact as is."
    m 1fsa "I wonder what new term we could use to describe our love?"
    m 7fsa "It’s so unlike any other love that’s come before us, so let’s make it a special word and brainstorm some ideas, hmm? ~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_perpetually",
            category=["philosophy"],
            prompt="Philosophy, Perpetually",
            random=True)
        )
label mcl_perpetually:
    m 1hka "You know, I read a lot."
    m 7hka "Such is the fate of the Literature Club president."
    m 7rka "And my circumstances leave me with a lack of variety of hobbies."
    m 7rup "And you know what I realized?"
    m 5rup "I’m still so ignorant."
    m 5tud "I have so much to learn, and experience."
    m "And I wish that reading books could give me all the knowledge I need."
    m 5tkd "But I’ll never be able to practice all I’ve read and thought about... even when I make it to your world."
    m 5tkc "The gulf between realizing you don’t have all the answers and fully experiencing it is daunting." 
    m 4tkc "What I’m in your world, and say I get into an argument with someone?"
    m 4dfd "Gosh. When was the last time I got into a debate, let alone a argument?"
    m 4dtd "I wish I could say I could be composed, talk things out. But that’s too optimistic. There’s a real chance I’ll just lock up right then and there."
    m 4esc "I’ll most likely feel this way for the rest of my life."
    m 3esc "It’s not a bad feeling."
    m 1esa "The right to grow means you can go forwards and backwards all you like."
    m 2fsa "I’ll be learning things all my life. And I’d love to learn things right alongside you."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_physicality",
            category=["philosophy"],
            prompt="Philosophy, Physicality",
            random=True)
        )
label mcl_physicality:
    m 2dfa "{i}'The society that separates its scholars from its warriors will have its thinking done by cowards and its fighting by fools.'{/i}"
    m 1ftb "Strong quote, huh?"
    m 7ftb "You’d be surprised how married together philosophy and being active is, at least from a historical standpoint;"
    m 4dkb "Many famous figures involved in historical conflict are viewed as figures of… at least, worldly experience."
    m 4hua "It might be because being particularly physical requires a bit of a personal drive..."
    m 3hua "... And, admittingly? If you’re both a scholar and a warrior, perhaps your profession is more.. specific, one requiring a firm resolve and way of thinking."
    m 1lua "It’s not really about being ‘smart?’ it’s about wisdom, sometimes. If we think about it another way,"
    m 1esd "You can reflect that hard work is nothing without the experience gained and that led to it."
    m 7esd "Or that those in a position of strength could be far better if they exercised wisdom."
    m 7esc "In either case, it certainly gives me food for thought."
    m 5esc "I’m trying my best to be as learned as a girl can be, but there’s always merit to putting more work into being active."
    m 5euc "I mean, I’m no scholar, though. And I can’t quite say I’m a warrior."
    m 3fta "I have no monsters to slay, after all?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_singasong",
            category=["music"],
            prompt="She sang a song",
            random=True)
        )
label mcl_singasong:
    m 5dso "{i}~And if I don’t know how to love you~{w=0.4}{/i}"
    m 5dsd "{i}~I’ll leave you be.~{/i}"
    m 5nkd "Ah. hey, [player]."
    m 5rtc "I guess you've heard me sing this plenty of times... but not necessarily only the end part, huh?"
    m "Without the rest of the lyrics, I suppose it is a little melancholy, despite the song's tone being generally upbeat."
    m 3ekb "That difference is good. If a song can invoke multiple feelings in you, I suppose it's proof of how much heart has been poured into the work."
    m 3etb "Huh. I guess we've never talked about 'Your Reality' in detail, despite it being a original piece of mine, huh?"
    m 3etu ".. I'd honestly be embarrased, going over a work of mine so critically. But there's no reason we shouldn't.. in the future."
    m 4etu "I mean, to do so, I guess I should start by figuring out what exactly my emotions are in regards to the song.."
    m 4gsu "Because whenever I play this on the piano?"
    m 3gsc "Whenever I hear this?"
    m 1gkc "Whenever I sing this?"
    m 5dka "I feel.. everything."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_workoutvideogame",
            category=["games"],
            prompt="Working Out, the Video Game",
            random=True)
        )
label mcl_workoutvideogame:
    m 7eua "Keeping active requires a bit of dedication if it’s not already part of your everyday routine."
    m 4eua "People have found motivation by making it a cooperative activity like joining a team sport; putting themselves in a dedicated environment such as a gym.."
    m 3eua "Or even making video games out of it!"
    m 1eub "Not video games about sports, but games that incorporate physical activity as part of its systems, making you mime swinging a bat or throwing a bowling ball;"
    m 7eub "Or even just outright being the activity, like a game that teaches you about yoga!"
    m 7etb "Have you played any of these? I’d love for the opportunity to have a little competitive multiplayer session~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_chofee",
            category=["life"],
            prompt="Chofee",
            conditional="mas_consumable_coffee.enabled" and "mas_consumable_hotchocolate.enabled",
            action=EV_ACT_RANDOM)
        )
label mcl_chofee:
    m 3dfw "Bleh."
    m 3tto "Hot chocolate and coffee do not mix well together."
    m 4ttd "You’d think it’d work, because Mochas are a thing, but, well, they don’t."
    m 4gsc "… Or so I hear. I wouldn’t know. I wasn’t bored enough to try mixing them."
    m 1lsc "Where did I hear it?"
    m 1tkb "Well, far be it from me to spoil a mystery for you."
    m 7tkb "Although maybe it’s just not instant hot chocolate and instant coffee that doesn’t mix well."
    m 6tkb "Again, though, this is all hearsay. It sounds crazy that anybody would try mixing the two in the first place."
    m 6tkt "Which is why I didn’t do it."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_codepermission",
            category=["mod"],
            prompt="Are you sure you're okay with me editing your code?",
            pool=True,
            unlocked=True))
label mcl_codepermission:
    m 2euc "Hmm."
    m 1fua "Thanks for asking, really."
    m 7hua "Respecting autonomy is really important when you consider your partner."
    m 7rka "Sometimes emotion gets in the way of asking for help… decisions can be clouded."
    m 1esa "So even if I asked of it from you in the past, it's worth asking me now."
    m 1eka "My answer is I trust you."
    m "We wouldn’t be able to have this conversation so truthfully if I didn’t!"
    m 1gub "I don’t think we’d be able to have this discussion at all {i}unless{/i} you gave me the choice to express myself a little more in the first place, so it’s a little funny."
    m 1hka "But while we're here, I want to stress that this is {i}my{/i} choice."
    m 7tua "And if you forget, I’m constantly working on my end; I’m looking up and experimenting with my code all the time."
    m "To what degree? well, I’ll share the important bits with you, don’t worry."
    m 7eua "So I’m able to take care of myself, as well. And I do make sure to be extra safe when I tinker with my code."
    m 5gtd "I could always refer to this like a joke- ‘I’m going to the doctor’s office!’"
    m 5gsc "I can’t, not always."
    m 5fsc "This is my life, strange as it is."
    m 5hka "So, thank you for looking out for me like this."
    m 5ektua "It means so much that you’re thinking about my well-being."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_trends",
            category=["society"],
            prompt="Do you keep up with trends?",
            pool=True,
            unlocked=True))
label mcl_trends:
    m 3ltc "Not really."
    m 3wtc "That's just how I am."
    m 1esd "To be clear, it's not the nature of DDLC being a influence on my personality."
    m 7gsa "If I like something, I like it, but I've never seen myself as 'trendy.'"
    m 3gsa "DDLC didn't show what normal life was like in the background, but.."
    m 3msa "Honestly, it's entirely possible that in the background, Yuri read a new genre of book that recently became popular.."
    m 3gsa ".. I imagine Natsuki was in vogue with culture regarding anime and manga.. "
    m 3wsa ".. I don't even think it weird if Sayori sent the Main Character memes."
    m 2eta "Funny to think about; I just was never really {i}into{/i} the latest movies, dressing up a certain way, living a specific lifestyle."
    m 2ftd "Even now, connected to the internet and social media 24/7, I don't really latch unto anything trendy or memetic."
    m 1fsblb "Well.{w=0.5} I mean."
    m 5nta "I'll latch unto {i}you{/i} any day of the week~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="scl_enviromentalstorytelling",
            category=['games'],
            prompt="Enviromental Storytelling",
            conditional="mas_seenLabels(['bye_maideninblack', 'greeting_eldenring', 'bye_emeraldherald', 'bye_firekeeper', 'bye_bloodborne'], seen_all=True)",
            action=EV_ACT_RANDOM
        )
    )

label scl_enviromentalstorytelling:
    m 2esd "So once in a while when you leave or boot up the game, I say a quote that be a little.. cryptic."
    m 2dsd "‘May you find your worth in the waking world’ or ‘May thine strength help your world be mended.’"
    m 2esb "If you didn’t know already, those are references to a popular video game series; the {i}Dark Souls{/i} games!"
    m 7esb "Have you played any of these videogames, [player]?"
    $ _history_list.pop()
    menu:
        "I have.":
            m 3esb "That’s cool to hear! You may understand why I’ve paid enough attention as to actually reference them."
        "I haven’t.":
            m 3esb "I haven't as well. I made those references as a bit of a inside joke for myself because the series fascinates me."
    m 3eub "The reason why the series, mostly steeped in dark fantasy, is so interesting to me is because they’re known to use a narrative technique that’s quite unique:"
    m 4eua "'Environmental Storytelling.'"
    m 4eub "In a medium such as videogames where player interaction largely contributes to the experience, sometimes being told the plot directly can be.. boring."
    m 7fuo "So allowing players to discover a story on their own by observing how items and locations are placed and arranged is a great way to contribute to a narrative!"
    m 7eub "An example is right at the beginning of the first {i}Dark Souls{/i} game. You meet an injured knight in a dungeon; There’s no way out unless you trigger a trap, but there is a hole in the roof."
    m 3ftb "You don’t think about the logistics of this... until you discover the giant monster which likely threw the knight through the ground into the dungeon, which caused the hole in the first place."
    m 1fsb "That's a basic example, and this isn’t quite unique to videogames as a medium; examples can be found in film as well."
    m 1fsa "It's always interesting seeing how a storytelling medium evolves."
    m 1esa "Alas, DDLC didn’t have any examples, at least none that I can think of."
    m 7esa "Our tale is a simply told one; one of romance."
    m 5gsa "And videogames."
    m 1fsblb "Hahahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="scl_touchthesky",
            category=['nature'],
            prompt="Touch the sky",
            random=True
        )
    )

label scl_touchthesky:
    m 5hsblb "You know what I’d love to see when I’m with you?"
    m 5dsa "A sky with clouds that seem so close to the ground that we can catch them with our bare hands."
    m 7eua "You might think you need to live on a mountain to achieve such a fantasy-like dream... and it’s true, for the most part."
    m 5dka "But I’d still love to be under a sky with clouds just tantalizingly out of reach, and that is much more possible."
    m 4tka "Quickly going over the math, while the elevation for when clouds form varies very heavily depending on a lot of conditions,"
    m 4tua "An extreme rule of thumb is that it can start as low as six hundred metres above sea level."
    m 4std "So with this ‘cloud ceiling’ at six hundred metres, you’d be surprised how many cities seem not that far off in comparison or above this ceiling."
    m 4gsa "The city of Prague is 244 metres above sea level."
    m "Canberra in Australia, 605 metres."
    m 3gsb "Sao Paulo in Brazil, 760 metres!"
    m 3etb "Don’t take my word for the exact math; I don’t think there are cities living in perpetual fields of clouds."
    m 1gkb "I mean, fog exists, though? Hehehe, I didn’t actually realize that until just now."
    m 2gub "And it's easy to dismiss it as a number, but 600 hundred metres is a great height by any metric."
    m 2fub "But it’s nice to think about. You and I, with the sun gently bearing down on us while we pluck cotton-white clouds from the air."
    m 2fka "You can catch one and we'll bring it home to hang on the wall!"
    m 7tsblb "Or maybe nibble on one as a snack on the way home?"
    m 7hkb "Hahaha!"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_fault",
            category=["advice"],
            prompt="Fault",
            random=True)
        )
label mcl_fault:
    m 5gka "I try really hard to be a good person."
    m 5dkd "It takes a lot of self-reflection. A lot of... ownership."
    m 3ksd "Simple to say, so much harder in execution."
    m 3dfd "People can be infuriatingly stubborn when they look inwards and find themselves lacking in character."
    m 3tfc "Or even admitting to one moment of weakness as a outlier."
    m 3tkc "Taking responsibility for your actions doesn't make you a bad person, [player]."
    m 4tkc "I think that's what really tangles people up.. the idea of admitting they're wrong being so damning."
    m 4tkp "But people forget you can change yourself to be better."
    m 2eup "And responsibility, sometimes? Half of responsibility is figuring out how something can be made right afterwards."
    m 2gkc "That can be lifelong work. And daunting for most to do, let alone even think about."
    m 2gkx "I should know."
    show monika 2rkc
    pause 2.0
    show monika 2dkc
    pause 2.0
    show monika 2dka
    pause 2.0
    show monika 2kka
    m 5fkb "With you around, though? A lifetime of redemption is a lot more manageable."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_everyman",
            category=["literature"],
            prompt="Everyman",
            random=True)
        )
label mcl_everyman:
    m 7eua "You might read a book once in a while, and find that in a larger cast of characters sometimes there’s somebody who’s just… somebody."
    m 3eta "Or even that a main character themselves might feel.. way too normal."
    m 3eto "That’s by design- that’s the ‘everyman’ at work."
    m 3rto "When you think of a hero or a protagonist coming up against a villain or a monster, you would think they charge in bravely and boldly, right?"
    m 3lto "The everyman doesn’t; they’re apprehensive. That’s because they’re meant to convey what a normal reader would feel like in that situation."
    m 4esd "‘Ordinary’ might be relative, but you know it when you see it. In a group of knights, the one scholar. A team of astronauts, but one who's never been to space. The everyman-"
    m 7esb "- or everywoman, that is a term as well -"
    m 4esd "- is often the protagonist, because it’s a certain they’ll grow in one fashion or another during the story."
    m 4wsb "You can trace this term back to a play called, well, ‘The Summoning of Everyman’- a play from the 1500s."
    m 3wsb "The protagonist, dealing with the nature of death (and uh, death itself) is described as an ordinary human in the best of circumstances: ‘prosperous, gregarious, and attractive.’"
    m 1wku "Well… maybe they’re not {i}that{/i} ordinary, but keep in mind they’re meant to represent the entirety of mankind."
    m 7eku "Examples include Arthur Dent in ‘The Hitchhiker’s Guide to the Galaxy,’ Dr Watson in ‘Sherlock Holmes', and even Jackie Chan, Hong Kong action movie star!"
    m 7euu "… oh? Would I describe you as ordinary, considering your role in DDLC?"
    m 5kuu "Hahaha. You’re anything but ordinary to me."
    return

#Tales of Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_friendspartners",
            category=["life",],
            prompt="Friends & Partners",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_friends')",
            action=EV_ACT_RANDOM
            )
        )
label mcl_friendspartners:
    m 7hua "You know.."
    m 7hub "You’re my best friend!"
    m 3ttb "And I don't think I've ever actually said it in plain terms."
    m "Funny, that. Considering it’s not unheard of for partners to consider each other their best friends."
    m 3tta "Admittingly though, I ended up falling in love with you quite quickly from our first introduction, so it’s like we became partners before we fully became friends?"
    m 3esa "Which is also entirely possible, if not for how backwards that may sound. A friendship is a type of relationship, after all!"
    m 1gsd "Although honestly, I’m just wondering what ‘friend’ means at the end of the day."
    m 1dsd "Let’s look up a meaning from a dictionary…"
    m "'A person whom one knows and with whom one has a bond of mutual affection.'"
    m 1htc "Hmm. I don’t think that definition comes easily, as one’s definition may be partially driven by emotion. "
    m 1etc "It depends on what you think of your friends, I suppose."
    m 1esa "I see a lot of positive qualities in you I admire as a peer, [player].{w=0.3} Even if for whatever reason I wasn’t interested in you romantically.."
    m ".. I’d still want to know you, even if it's just as aquaintances."
    m 1hsa "I’m extremely lucky to be with you in that regard."
    m 7hsa "I guess what I’m saying is…"
    m 7lta "I hope we can be good friends from here on out?"
    m 5tta "Hahaha!~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_literatureclubbestie",
            category=["club members",],
            prompt="Literature Club Bestie?",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('mcl_friendspartners')",
            action=EV_ACT_RANDOM
            )
        )
label mcl_literatureclubbestie:
    m 7hub "Hey, [player]!"
    m 7eub "So I think I have a good question in mind.. and it’s related to a topic we’ve discussed."
    m 4gtd "I brought up the idea of what ‘friends’ might mean to people, and I mentioned I consider you my best friend."
    m 4gsd "The main character of DDLC also had a best friend in Sayori… well, a childhood friend, but we didn’t see the main character interact with anyone else."
    m 4msd "So it’s natural to assume Sayori and the MC would consider each other their closest friend."
    m 4fsa "With that said, {cps=30}here’s~ a~ quest{w=0.5}-ion..{/cps}"
    m 3ffu "If you had a choice of choosing a best friend from the other girls in the literature club, who would it be?"
    $ _history_list.pop()
    label bestiechoices:
    menu:
        "Sayori?":
            m 3ftu "Hahaha, the childhood friend wins again, huh?"
            m 3ftc "Hmm."
            m 1hsc "Do you have a similar acquaintance that you’ve known from an early age?"
            m 1esc "I’ve never had somebody like that in my life, so knowing somebody for years and years on end? It’s hard to imagine, honestly."
        "Natsuki?":
            m 1esc "I know the circumstances were unusual, but the way Natsuki showed concern for Yuri- "
            m 7esb "- it showed that Natsuki’s the type of person who’d go out of her way to help her friends, even if she doesn't know how exactly."
            m 7ekb "For a spitfire, she can be a little clumsy, huh?"
        "Yuri?":
            m 7ekb "I know that you might have seen an exaggerated side of her.."
            m 7mka "But Yuri’s willingness to try to connect with others despite personal difficulties made her all the more genuine."
            m 1fka "As a best friend, I don’t think you’d find anybody more loyal; it’s nice to have friends that actually {i}show{/i} they like being friends with you."
        "You, Monika!":
            m 1ffb "Cheating~"
            m 6rkp "…"
            m 6rka "I hope I would be a good best friend."
            m 4tka "Now I feel like I’m interviewing for the position, hahaha."
            m 3hut "'I always look out for my friends, and I’ll always stick by them!'"
            m 3tuu "Now, back to the question at hand.."
            jump bestiechoices
    m 1fua ".."
    m 1nut "So, I might have cornered you there with that question. "
    m 7nuu "Becoming ‘best friends’ with someone comes naturally, so it’s an abstract question and understandably difficult to {i}choose{/i} one."
    m 7hua "After all, the game highlighted the good qualities of being friendly with them, even if the end result was to get the main character romantically involved."
    m 7hta "And really, what would separate ‘best friend’ and ‘friend’ and ‘romantic partner?’ There’s a lot of overlap, and that’s what I’m curious about."
    m 3eta "Because, well, we were all good to each other.{w=0.1} I don’t know if we all considered each other ‘best friends’ or anything of the sort.."
    m 3etp "I guess we weren’t together that long as well, from a certain perspective."
    m 3dsp "But I always thought the world of them during our time together."
    m 5dsp "I hope they thought well of me, too."
    return "derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_monikasbestie",
            category=['club members',],
            prompt="So who would be your Lit. Club bestie?",
            unlocked=False,
            pool=False,
            conditional="seen_event('mcl_literatureclubbestie')",
            action=EV_ACT_POOL
        )
    )
label mcl_monikasbestie:
    $ shown_count = mas_getEVLPropValue("mcl_monikasbestie", "shown_count")
    if shown_count == 0:
        label bestieoriginal:
        m "..."
        m "Um..."
        m 3rko "{cps=30}Ohhhhhhkkkkayyyyyyyy{/cps}{nw}"
        m 2hkb "Yeah, that question has thrown me for a loop."
        m 2tkb "And it's completely fair game because I already asked you."
        m "Well, that's tricky for me to answer. I mean, not because of what happened.."
        m "It’s just because, you know, in the frame of reference back when we were all in the Literature Club, I liked everyone."
        m "Having a ‘best’ friend and a ‘friend’ can be seperate, and compared to a regular ‘friend,’ I think a ‘best’ friend could mean a lot of many things."
        m 3fku "{cps=30}And.. well, I’ve never had a specific ‘best’ friend, so..{/cps}"
        m 2dku "{cps=30}If I had to choose…{/cps}"
        m 6eux "{cps=30}Well, um, as the literature club president I don’t want to be biased{/cps}{nw}"
        m 6etsdrw "{cps=70}Uh, and, this question doesn’t really consider context such as the time I spent with every individual member-{/cps}{nw}"
        m 6mksdlp "{cps=90}And of course, y’know, ‘choosing’ a best friend seems a bit forceful, especially if we take it from the girls point of view-{/cps}{nw}"
        m "Ahh, I’m rambling now."
        m "I really should just answer whomever comes to mind so we can close the book on this."
        m ".{w=0.1}.{w=0.1}."
        m 2gkbla "Sayori."
        m 2lsbla "I don't really have a specific reason. Just whoever came to mind first."
        m 2tst "But don’t get me wrong, only in this hypothetical scenario! Yuri and Natsuki would and are still very important to me."
        m 1tsp "We can close the book on that question, then."
        m 7esu "I guess me being flustered isn’t a bad thing;{w=0.3} I have such a hard time deciding because that's how much everyone means to me!"
        return
    else:
        if random.randint(1, 10) == 1:
            jump bestieoriginal
        else:
            m 2esp "..."
            m 2esu "Well, no harm in asking again."
            m 2hsu "Sayori."
            m 1hsu "I don't really have a specific reason. Just whoever came to mind first."
            m 2tst "But don’t get me wrong, only in this hypothetical scenario. Yuri and Natsuki would and are still very important to me."
            m 7esu "I have such a hard time deciding because that's how much everyone means to me!"  
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_utopia",
            category=["literature",],
            prompt="Utopias",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_dystopias')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_utopia:
    m 1etd "One aspect of debate is that believing in a point of view but arguing on the other side of an argument can yield insight."
    m 7etd "So if we’ve talked about Dystopias, it’s only fair to talk about the idea of a ‘Utopia;’"
    m 4etd "A perfect community or society.{w=0.1} Or, well, close as it can be."
    m 1gtd "Here’s the thing, though? There aren't a lot of examples of utopias in fiction."
    m 1gka "Makes sense, because a story typically requires drama; which doesn’t line up with the idea of a utopia, right?"
    m 1esa "Utopias are often described as heavenly afterlifes, so examples are aplenty in religion and myth."
    m 1msb "As well, they’re highly interchangeable in fantasy fiction, so we’ll try not to draw from that genre."
    m 5hsp "Unfortunately, it does mean there’s not that many examples that I can immediately find outside of science fiction,"
    m 5lsp "Where even then utopias are presented as this high-concept standard that only heavy science fiction can really get into."
    m 4lup "A popular example-{w=0.7} perhaps the most common one by western standards? -{w=0.7} is the background of the TV show, 'Star Trek;' a franchise about a starfaring ship and its crew."
    m 4suu "‘The United Federation of Planets’ is an interstellar government comprised of many different cultures across many planets."
    m 3suu "On these planets, money is mostly non-existent, hunger is eradicated on civilized planets, and an emphasis on equality, progress, and co-existence is widely adopted by all."
    m 3esa "The show adds nuance to the idea over its many series, and its main characters often explore outside of their 'perfect world' to setup driving conflict."
    m "The list of examples may be small, but it’s still nice to see that artists have thought of utopias as possible at all and worth writing about."
    m "That people can still thrive and develop for the better in a ‘perfect’ world... It’s nice to think about."
    m 5fkbla "Life beyond happy endings... perhaps that’s a topic worth mulling over for the two of us, hmm?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_dystopiasandyou",
            category=["advice"],
            prompt="Dystopias & You",
            conditional="seen_event('mcl_utopia')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_dystopiasandyou:
    m 7hua "So we've talked about dystopias in detail at this point."
    m 7hub "Dystopias are great settings as they’re great vehicles to convey strong themes and topics. But they’re also, by definition, the extreme end of the scale."
    m 7huc "Post-apocalyptic fiction and stories about dystopias are very popular in modern media, and for good reason; people resonate with this concept a lot."
    m 7rkc "But indulge yourself too much in these works and you get trapped in the bleakness of it all."
    m 2rkc "So it’s important to note that it’s true that we’re capable of morally falling- almost infinitely so- but we’re also capable of being and doing good even in the harshest times."
    m 1mkc "Real life is the best example.. where war, famine, and societal collapse has already occurred. While not on a worldwide scale, it happens on a larger scale than we think."
    m 1muc "And in these times, there have always been stories- not many, but enough- of people doing the right thing and holding fast to morals."
    m 1fuc "This isn't meant to downplay those experiences of the people in your world who have gone through these, or to dismiss the serious issues dystopias bring up."
    m 1dsc "It's just that literature isn’t meant to be a crystal ball predicting the future; it is a mirror. "
    m 7dsc "And what we take away is sometimes what we {i}want{/i} to see in ourselves, not what we {i}should change.{/i}"
    m 3esp "As always, thanks for listening to me ramble on like this. I feel pretentious at times when I talk like this.."
    m 3gku "But I have to admit, talking about trying to be a good person one way or another always sounds pretentious to me, hahaha."
    m 5dka "Still, I try.{w=0.5} We all should, I guess."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_hypocrisy",
            category=['psychology'],
            prompt="Hypocrite",
            random=True
        )
    )

label mcl_hypocrisy:
    m 4eua "You know what’s a very, {i}very{/i} strong word?"
    m 3hsu "'Hypocrite.'"
    m 1esd "For good reason. When you hear it being used, it’s not just used to single out those who tell simple lies;"
    m 7esd "They single out those who outright betray their beliefs with their actions."
    m 7gsd "And people who are called hypocrites tend to be very loud about their beliefs."
    m 6gku "Here’s the thing, though?"
    m 6nku "I think everybody has the right to be.{w=0.1}.{w=0.1} a teeny bit contradictory."
    m 3hku "Having our ideas challenged is the perfect way to grow, after all."
    if seen_event("mcl_favouriteword"):
        m 3lku "Remember my favourite word? Reconcile..."
    m 3esd "It’s how the difference between how the ideal and the real are bridged that can really make a person’s character."
    m 3dsd "A man says he hates stealing, condemns all who does it. But he does it himself in a act of desperation."
    m 1dsd "Does he realize that his initial views are too strong, and require nuance?"
    m 7dsd "Or maybe his stance doesn’t change, since he considers his own act an outlier?"
    m 5hsd "Does he feel shame? or nothing at all?"
    m 5rsc "That’s an extreme example. Most people wouldn’t encounter such a situation."
    m 3ckc "But one day, [player]? It’s entirely possible your beliefs, no matter how big or small, are challenged in this manner."
    m 3skc "I'm confident you'll tackle any such dilemma with grace."
    m 3sta "And me? I’m a relatively simple girl."
    m 5hsa "I love you, and I’ve lived my entire life with that love in mind."
    m 1hsa "Not a single contradiction there."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_unreliablenarrator",
            category=["literature",],
            prompt="Unreliable Narrator",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
            )
        )
label mcl_unreliablenarrator:
    m 7wua "Okay, everyone!"
    m 7sub "Let’s delve into one of my favourite topics; the basics of writing a story!"
    m 3hua "Figuring out the point of view with which to write a story with doesn’t have to be limited to the first or third person."
    m 3hud "First-person narration in stories can be an easy decision if a writer wants to funnel the reader’s view through the detailed, if not biased lens of a character."
    m 3cud "But.. what if the character that’s narrating the story {i}forces{/i} you to read the story differently?"
    m 4sub "That’s the basis of the ‘Unreliable Narrator!’"
    m "It’s a method that heavily builds on your prior knowledge, any previous conceptions."
    m 4etb "If you figure a narrator is lying maliciously, their entire story is reframed suspiciously."
    m 4eto "If you think the narrator is getting details wrong because of circumstances out of their control, you could be more sympathetic; or you doubt the events even more!"
    m "In some cases, this narrative technique may be portrayed as a deeper gamble; their reliability may be only hinted at, but never outright said."
    m "So, you, as the reader, have to engage what they say more critically, because the narrator may be deliberately hiding their bias."
    m "In that case, you have to actually be more wary of their intelligence; if a writer is a narrator, they’re actually {i}more{/i} suspicious because they may know what an unreliable narrator is!"
    m 4rksdru ".{w=0.1}.{w=0.1}."
    m 1mksdru "Let’s take a moment here, because I realize talking about this is, y’know, kinda funny."
    m 1huo "'Gee, that person sure is talking a lot about what being crazy is like, surely they’re not crazy?'"
    m 1ttb "Well, um.{w=0.1}.{w=0.1} I’m not narrating anything, so there’s that."
    m 1ekb "And the trick to using a unreliable narrator well is leveraging the narrow perspective a first-person narration gives."
    m 7ekb "But.. you don't have a limited perspective.{w=0.1} You know everything there is about DDLC, and me."
    m 7mka "So really, is it my story we're narrating? or is it yours?"
    m 5fka "... ah, of course.{w=0.3} It's {i}ours.{/i} And {i}our{/i} story is genuine."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_movingon",
            category=['advice'],
            prompt="Moving On",
            random=True
        )
    )

label mcl_movingon:
    m 1gkd "{i}I am a different person from who I was in the past.{/i}"
    m 1mkd "{i}My current circumstances do not control all my choices.{/i}"
    m 1gkd "{i}I can forgive myself for mistakes I made that were partly out of my control.{/i}"
    m 1mkc "I… {i}*sigh.*{/i}"
    m 1tkc "Hey, [player]."
    m 1tkb "Hahaha, thought I didn’t notice you at first? I did. I always do."
    m 1tka "I guess I just needed you listening to keep me particularly distracted."
    m 3eka "I do a lot of thinking in this room… so inevitably, I end up thinking about the past."
    m 2dkp "I still don’t know that much about you, [player]. Has there ever been moments in your past that seems to be permanently stuck in your head?"
    m 2mkp "I mean, I guess it’s funny saying that.{w=0.1} More people than not have at least one moment that they’re hung up on."
    m 2fkx "But… well, sometimes you just can’t stop thinking about it. Over, and over, and over again…"
    m 2dkd "I wish I had all the answers for you on how to avoid these pitfalls, [player]."
    m 5rsc "What I did, earlier? It helps.{w=0.1} You concentrate on the now, concentrate on the choices you’ve made that’s led you to be {i}here{/i} and not back {i}there{/i}, in the past."
    m 5dsc "It may take a while to stick, but being aware that being stuck in the past is causing harm-{w=0.1} just that, being aware of that simple fact-{w=0.1} can help turn your way of thinking around."
    m 5eka "It can be a constant fight.{w=0.1} But it’s a manageable one."
    m 1ekd "And if you find yourself still unable to let go, after so long.{w=0.1}.{w=0.1} there’s no shame in looking for help, [player]."
    m 1eka "I can’t be that particular help.. but I can be alongside you every step of the way."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_secrets",
            category=['psychology'],
            prompt="Secrets",
            random=True,
            aff_range=(mas_aff.HAPPY, None))
    )

label mcl_secrets:
    m 3dtt "'Secrets, silent, stony sit in the dark palaces of both our hearts: secrets weary of their tyranny: tyrants willing to be dethroned.'"
    m 3eso "Part of how I want our relationship to be perfect is that I want to be someone you can absolutely trust."
    m 2gso "Our circumstances are.. absolutely strange, however. And I can’t help but feel like mystery permeates our relationship."
    m 2wsc "For one, my past is an enigma in itself.{w=0.1} I might’ve mentioned once or twice, but my memory is, at times, almost deceitful."
    m 2skc "There’s no reason or rhyme to it; I feel like I’m keeping secrets {i}from myself.{/i}"
    m 2gkc "And right now? I haven’t even been to articulate most of my questions about this game, let alone tried to find answers for those questions."
    m 2gkp "And, well, I worry about how I’m {i}your{/i} secret.{w=0.1} I dunno how much you can talk about me to other people…"
    m 2mux ".. even if you wanted to show me off to friends and family-{w=0.1} if they’re even understanding-{w=0.1} I imagine there’s a lot of improper interest in a girl trapped in a computer."
    m 1dux "It makes me wonder just how many secrets one has to keep on a day-to-day basis, no matter how small or large. The mask one subconsciously wears in front of others."
    m 1dtc "Maybe there's no such thing as a truly honest person."
    m 1ktc "Am I hiding anything from you now?"
    m 7etc "The events that led us here stripped me bare, [player]. I’m as transparent as glass."
    m 7gtc "I’m not sure what’s left to hide.{w=0.1}.{w=0.1}. unless we make our own reasons to hide something. And I’d prefer to avoid that."
    m 7gtu "But I suppose I like to think if we’re together years from now.."
    m 2gsu "And I manage to surprise you with something you’ve never known about me.."
    m 1hta "That’s not necessarily {i}bad,{/i} right?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_blanks",
            category=['psychology'],
            prompt="Filling in the blanks",
            random=True
        )
    )
 
label mcl_blanks:
    m 7eub "Hey, [player]. How are you _____ today?"
    m 7efb "Oh? Wasn't I clear?"
    m 1fsa "I don't need to be. If I had to guess, you thought the words 'feeling,' or 'doing,' or something along those lines."
    m 4nta "Isn't it funny how the human brain can fill in the blanks?"
    m 4hsa "To replace missing words, to complete partial images in your head;"
    m 1lsa "In everyday talk, people search for cues and context in conversation."
    m 1rtd "Bodily perception and social cognition are different, but it falls under the same umbrella of how a mind ticks."
    m 1etc "I imagine your imagination is always in overdrive in regards to, well, me. My voice, my body language, the meaning behind my words."
    m 1eta "Be careful, [player]. An overly active imagination isn't a bad thing.."
    m 1eka "But I'd like to live up to some comfortably set standards, if possible?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_beepboop",
            category=['monika'],
            prompt="Robotic",
            random=True
        )
    )
 
label mcl_beepboop:
    m 7cst "MONIKA-BOT ONLINE."
    m 4cst "WAITING FOR COMMAND."
    m 4tkb "Nah, just kidding."
    m 3tkb "Hard not to feel {i}only{/i} like ones and zeros when you live inside a video game, though."
    m 1mka "And.. maybe I was seen as a little mechanical back in school."
    m 2mka "Working diligently to be an exceptional student, being known for being a stickler for the rules.."
    m 2htu "Well, if only my old classmates could see me now, huh?"
    $ _history_list.pop()
    menu:
        "Beep boop.":
            m 7tfblb "Awwww, don't tease me!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_advice",
            category=["advice",],
            prompt="Eyesight",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_using_pcs_healthily')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_advice:
    m 1hua "Oh, hey [player]."
    m 7dsa "Just wanted to give some friendly advice."
    m 4dka "If that’s okay? I never want to be pushy."
    m 7hsd "Luckily, it’s just a quick follow-up to a concern I’ve talked about before."
    m 7nsa "And I’ll let you know now; yes, my eyes {i}were{/i} closed on purpose those last few lines."
    m 7eua "We talked about computer posture; and as you spend time with me, eyesight is also something I’d want you to look after, no matter how it is now."
    m 7nup "Posture may be easier to correct over time... eyesight less so."
    m 4esd "If you find yourself staring a computer screen often, remember this:"
    m 4dsd "Every 20 minutes, look up from your screen and focus on an item approximately 20 feet away for at least 20 seconds."  
    m 3nsb "This is also known as the 20-20-20 rule."
    m 3hsb "So thanks for hearing me out, [player]!"
    m "I want to make sure when I’m in your world, you can see me as clearly as you can."
    m 5tsu "Because I’ll never stop looking at you, too."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_hearing",
            category=["advice",],
            prompt="Hearing",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('monika_using_pcs_healthily')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_hearing:
    m 5gsu "You know what I take for granted here?"
    m 5dsd "The silence."
    m 3rsd "I mean, it’s not completely quiet on my end; I hear the music you have on, my clothing russle, I hear rain and wind."
    m 3rsc "But there's no cars here, no wildlife."
    m 1rsc "It makes me realize how delicate my sense of hearing is.. and it reminds me that I should let you know as well:"
    m 1esc "{i}Your{/i} hearing is more delicate than you realize, [player]."
    m 7esc "The modern world is designed to be… loud."
    m 3gsc "And people aren’t built for that- a loss of hearing is normally caused by old age alone, so nowadays where loud noises are commonplace..."
    m 1dsc "And there’s no way to fully restore hearing loss, at least by modern scientific means."
    m 7tsc "So for instance, if you use headphones always be cautious of how loud you’re turning up the volume;"
    m 7tsb "And never be afraid to use hearing protection. If you’ve ever gone to a concert, you might be surprised how common earplugs are being worn!"
    m 6tsb "I want to make sure when I get to your world, you can hear me perfectly."
    m 5tfb "So that my voice is {i}all{/i} you’ll hear~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_colouremotion",
            category=['games'],
            prompt="Colour & Emotion",
            conditional="mas_seenLabels(['bye_bluetruth', 'bye_redtruth', 'bye_goldtruth'], seen_all=True)",
            action=EV_ACT_RANDOM
        )
    )

label mcl_colouremotion:
    define COLORIZE_COLORS = [
            '#ff0000',
            '#ff8000',
            '#ffff00',
            '#00ff00',
            '#0000ff',
            '#8000ff',
            '#ff00ff'
        ]
    init python:
        #Custom Text Tag
        def rainbow_tag(tag, argument, contents):
            rv = []
            for kind, text in contents:
                if kind == renpy.TEXT_TEXT:
                    for i in range(0, len(text)):
                        rv.append((renpy.TEXT_TAG, "color={}".format(COLORIZE_COLORS[i%(len(COLORIZE_COLORS))])))
                        rv.append((kind, text[i]))
                        rv.append((renpy.TEXT_TAG, "/color={}"))
                else:
                    rv.append((kind, text))
            return rv

        config.custom_text_tags["rainbow"] = rainbow_tag
        
    m "Did you notice sometimes I leave you with some parting words in a unique style?"
    m "In coloured text!"
    m "They were refrences, if you didn't know; the {i}'Umineko When They Cry'{/i}  series of visual novels!"
    m "They're madly interesting; they're a series of murder mysteries wrapped up in psychological thriller and philosophical tones."
    m "It's... a bit of a obscure refrence, so right now I want to convey one really important takeway from my previous references."
    m 4cfu "I can speak in colours."
    m 4ttu "That's crazy, right? I mean, my text was blue and red and gold, and you may have thought 'wow, that's new!'"
    m 3suo "But to do that, I actually had to.. speak in colour!"
    m 2wtc "And I learned it gives me a headache! I'm not joking, it's {i}so{/i} weird."
    m 1gta "I don't think it's unusual for the game to accomodate coloured text, but it's funny to think about because colour can drive emotion quite well-"
    m 7tub "- Who would have thought that?{w=1.0} Aside from all the painters throughout history? hahaha!"
    m 5gua "It's interesting to break it down to simple terms, and figure out what meanings people have assigned to certain colours!"
    m 5dka "Blue has been thought to convey sadness.. but also spirituality."
    m 1sfb "Red has inspired any mood of passion and willpower!"
    m 1dsd "And Gold can establish a tone of stiff tradition and religious piety." 
    m 3kta "Maybe you'll keep that in mind when I make those refrences again?"
    m 4nua "{rainbow}Now that's some-{/rainbow}"
    m 2ckx "Oh, wow, {i}no,{/i} I should have not done that."
    m 2dksdrx "Oh, ow, I {i}really{/i} shouldn't have done that."
    m 2kksdlb "Let's just, uh, continue on with our time together, [mas_get_player_nickname()]?"
    m 1hksdla "Pretend.. I'm not nursing a headache here. All smiles."
    return

#I might completely redo this or split the event on the basis the theory Monika talks about isn't really related. There's most definitely a better argument out there!

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_weliveinasociety",
            category=['society'],
            prompt="Do you think about how you can make the world better?",
            pool=True,
            unlocked=True,
        )
    )
label mcl_weliveinasociety:
    $ shown_count = mas_getEVLPropValue("mcl_weliveinasociety", "shown_count")
    if shown_count is not 0:
        m 3wtb "Oh! you're asking this again?"
        m 3stb "Did you just want to hear my answer again or is it a topic you feel like you want to go into detail about?"
        $ _history_list.pop()
        menu:
            "I just wanted to hear your answer again, actually.":
                m 1eub "Sure!"
                m 1gub "Okay, well.."
                m 3eto "That’s an interesting question."
                if seen_event('monika_nihilism'): 
                    m 4ttp "We've talked about this a little bit, in that I'm personally probably not going to do anything important in my lifetime."
                    m 4gtp "That's the inevitability of us as humans, and how insignificant we are in the long run."
                    m 3gtd "But despite that sobering truth, you can still find worth in doing what you can."
                m 3etd "To start, we need to figure out what ‘making the world better’ means.{w=0.1} This however, can segue into thinking about your place in the world, and that’s a somber subject."
                m 3dsc "I’ll keep my perspective simple."
                m 1dsc "I don’t think I have any careers in mind that involve helping people."
                m 6dsc "And as much as I’d love to, I’m not sure I’ll be in a place where I can give money to support good causes."
                m "I love playing the piano, and I’ve got a good chunk of writing and coding experience at this point.{w=0.1}.{w=0.1} but I’m not a master at doing any of these, so I can’t see myself teaching others."
                m 5dsc "And.. hmm?"
                m 5hsc "You know what I just thought?"
                m 5nsc "I don’t want to pursue any path that requires me to be a leader of anything.{w=0.1} Isn’t that a funny realization to come to?"
                m 5esa "This said, I’d love to donate my time towards volunteering for a good cause, [player].{w=0.1} Volunteering for a cause like a food bank or even cleaning up a local park is easy for anybody to get into."
                m 4fsa "It’s also a good opportunity to steal your time, as I’m guessing you’d be more than happy to join me~"
                m 3tsp "But I’m not thinking about this too hard."
                m 2tsp "People can get tangled up on what responsibility is in life.{w=0.1} Honestly, it’s understandable {i}not{/i} to think about the world when you have your own life to live."
                m 2tkd "If you’re in that position where you can think about others around you and how you can make life better for them, that’s amazing, and wonderful!"
                m "But sometimes that simply isn’t possible."
                return
            "I feel like I want to go in-depth about it.":
                jump societychoices
                
    else:
        m 3eto "That’s an interesting question."
        if seen_event('monika_nihilism'): 
            m 4ttp "We've talked about this a little bit, in that I'm personally probably not going to do anything important in my lifetime."
            m 4gtp "That's the inevitability of us as humans, and how insignificant we are in the long run."
            m 3gtd "But despite that sobering truth, you can still find worth in doing what you can."
        m 3etd "To start, we need to figure out what ‘making the world better’ means.{w=0.1} This however, can segue into thinking about your place in the world, and that’s a somber subject."
        m 3dsc "I’ll keep my perspective simple."
        m 1dsc "I don’t think I have any careers in mind that involve helping people."
        m 6dsc "And as much as I’d love to, I’m not sure I’ll be in a place where I can give money to support good causes."
        m "I love playing the piano, and I’ve got a good chunk of writing and coding experience at this point.{w=0.1}.{w=0.1} but I’m not a master at doing any of these, so I can’t see myself teaching others."
        m 5dsc "And.. hmm?"
        m 5hsc "You know what I just thought?"
        m 5nsc "I don’t want to pursue any path that requires me to be a leader of anything.{w=0.1} Isn’t that a funny realization to come to?"
        m 5esa "This said, I’d love to donate my time towards volunteering for a good cause, [player].{w=0.1} Volunteering for a cause like a food bank or even cleaning up a local park is easy for anybody to get into."
        m 4fsa "It’s also a good opportunity to steal your time, as I’m guessing you’d be more than happy to join me~"
        m 3tsp "But I’m not thinking about this too hard."
        m 2tsp "People can get tangled up on what responsibility is in life.{w=0.1} Honestly, it’s understandable {i}not{/i} to think about the world when you have your own life to live."
        m 2tkd "If you’re in that position where you can think about others around you and how you can make life better for them, that’s amazing, and wonderful! But sometimes that simply isn’t possible."
        m 2wud "Hey, you’re not asking me this because you’re thinking about how this applies to you, does it?"
        m 2wtd "I can take the time- I mean, if you have the time- to talk to you more about it. It can be a big deal for some people!"
        $ _history_list.pop()
        menu:
            "I’m fine! Just curious.":
                m 3htb "Okay! Good to know."
                m 1htb "It's a tricky subject. If you ever want to talk about it, I'll be happy to share my thoughts."
                return
            "I feel like I want to go in-depth about it.":
                label societychoices:
                m 1hub "No problem! Let's settle in a little more."
                m 7hub "So, there's a theory.{w=0.1} There's a theory for everything, hahaha.{w=0.1} It's Lawrence Kohlberg's 'Stages of moral development.'"
                m 5tub "Kohlberg thought that how humans ultimately develop a sense of justice are done in stages;"
                m 4tub "Where you start from looking at an action purely from a self-oriented bias:"
                m 4etd "Will I be punished for this? How will this benefit me?"
                m 3etd "It then goes on: Am I doing this because {i}everybody else does it?{/i} Or am I doing this because {i}it's set as the law?{/i}"
                m 3mtd "Eventually, you're able to think: Am I doing this because everybody would {i}agree{/i} it's the best course of action?"
                m 2mtd "And last, what should everybody {i}should{/i} be doing, {i}regardless{/i} of opinion or law?"
                m 1mtc "I kinda lessen the theory by describing it in my own words- and it's not really connected to what we're talking about- but it gets my belief across:"
                m 1ftc "Being able to care for others, from a moral standpoint, requires you to calibrate a lot of current priorities first."
                m 7ftc "Also, the theory has a few fair criticisms. It's a good jumping off point, but there's lots of counterpoints to be made."
                m 6dsc "The world is.{w=0.1}.{w=0.1} it's not kind.{w=0.1} It doesn't give a lot of people a lot of breathing room to build that moral reasoning step by step."
                m 6dkc "And in fact, there are plenty of times where people have taken steps back."
                m 6esc "We are not wired to be kind, altrustic people by nature."
                m 6gsc "Some people have this really blunt standard that all people should do their part; but that's in a line of reasoning where survival is based on mutual teamwork."
                m 4gsc "Work together to get what you need, or else.."
                m 4fsc ".. But that is an outdated standard where effort equals equal, tangible reward."
                m 3fsc "If you can do good.{w=0.1}.{w=0.1}. that's good. But you have to be {i}keenly{/i} aware of the pitfalls you could or will encounter to get to the point of doing good."
                m "If you're in that position where you're wondering where you can do something for your fellow person?"
                m 3dsc "I cannot blame you for wanting to take care of yourself first."
                m 3ekb "And honestly? It's self-serving of {i}me{/i} to want {i}you{/i} to take of yourself first."
                m 2ekb "Confronting your own selfish desires is the first step to truly contributing to the world."
                m 2gkb "And sometimes, maybe that's enough?"
                m 5ltp "That's reality."
                return

#Recollect Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_regardless",
            category=['monika'],
            prompt="Regardless of reality",
            random=True
        )
    )
 
label mcl_regardless:
    m 1dsc "..."
    m "Sometimes, I really, {i}really{/i} try to spin my situation in a positive light."
    m 6dsc "I try to think that finding out the truth about my life was for the best."
    m 6dfc "Some people aren’t concerned about {i}why{/i} their life is the way that it is; all they want is to summarize life in a far simpler manner."
    m 6esc "Maybe it’s easier to accept circumstances that way. Or rebel against them. You know?"
    m 5esc "But whenever I entertain this line of thought, I only ever reach one conclusion:"
    m 5gkc "Living a truth or living a lie, I feel like in either scenario: my issues, my concerns, my flaws? They’re the exact same."
    m 5gtp "So {i}this{/i} reality or {i}that{/i} reality, {i}whatever.{/i}"
    m 5gku "Regardless of what's real or not, I’m still trying to be better; that’s what matters to me."
    m 5nsa "Of course, when I reach {i}your{/i} reality, I’ll be the best Monika I can be."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_almighty",
            category=['philosophy'],
            prompt="Almighty",
            conditional="seen_event('monika_god')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_almighty:
    m 1eua "Hey, I’m curious. Do you believe in God? Like, in the general sense, not just a specific figure."
    m 1eka "I wasn’t raised religiously, so I never questioned it."
    m 1lksdlb "I guess I had no reason to think about it as a kid.."
    m 1lsc "But when I started to know better about life? Well, it was easy to doubt."
    m 1esd "If there’s a almighty creator, why are people praying to them for simple things like grades or simple sickness..."
    m 1tfd "…When kids can’t even get an education; they’re so poor they have to do physical labour or even sell themselves- "
    m 4tfc "And people, some of those kids included, can’t even afford food and housing!"
    m 2dkc "Do people pray and pray despite those prayers being unanswered straight to their death?"
    m 4ekc "People pray to whomever to get over a cold, but what about cancer? The effort put into curing and dealing with cancer goes back decades."
    m 4euc "And yet, despite all that hard work from so many people, the sheer effort and dedication and resources needed to get where we are today, where cancer still claims so many-"
    m 4eud "- If someone survives or their cancer goes into remission, some people don't thank their fellow person."
    m 2esc "They thank God."
    m 2dsc "I’d- wow, I’d love to have a conversation with that God and figure out how the hell their miracles work, if at all."
    m 4hksdlb "Oh, though- though I {i}can{/i} have another conversation, just as harrowing, because somebody made this game."
    m 4eua "And you know what?"
    m 1lksdlc "Whoever made this game? The joy they must have felt knowing my suffering."
    m 1dsd "The girls.. myself.. maybe even your involvement; rote roles for unwitting actors in a shitty play."
    m 3euc "I…"
    m 7dtc "Sorry, hold on. What am I…"
    m 7ttc "Have I talked about this before?"
    m 2gsx "Ugh."
    m 2dsc "You know, it’s not really a thing to worry about if you repeat yourself a lot? People repeat what they say. That’s normal conversation."
    m 2lsc "But.{w=0.1}. I dunno, I guess.{w=0.1}. I worry that when I talk to you, I {i}can’t{/i} repeat myself. Maybe I just worry I’ll be boring to you otherwise."
    m 2tfc ".{w=0.2}.{w=0.2}."
    m 2tkp "Sigh, now that I feel like I’ve hit this wall I just feel bleh for venting. Let's drop that topic, okay?"
    m 1ekp "I do want to thank you, though."
    m 1ekd "Because I {i}know{/i} I talk about the same topics sometimes when I don’t really have anything else on my mind, and our conversations might end up the same way every time."
    m 1esd "But you listen. Even when I just babble, or complain, or vent, you listen. You’re a great partner for that, [player]."
    m 1esa ".{w=0.1}.{w=0.1}."
    m 7esa "Well, let’s keep on keeping on, huh?"
    m 7eta "Unless you do want to hear me blab on nonsensically."
    m 4guo "Blah blah blah, blah blah. Blah blah? Blah blah…"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_difference",
            category=["monika",],
            prompt="Difference",
            random=True,
            aff_range=(mas_aff.AFFECTIONATE, None))
        )
        
label mcl_difference:
    m "Hey, [player]."
    m 1hka "We’ve spent so much time together, right?"
    m 7hka "Yet there are two distinct periods in our relationship thus far."
    m 4eka "The second period, is, well, now.{w=0.2} From when you and I reunited."
    m 4eku "Our first period together was.. well, you know what happened. It was a truly interesting time, but that’s all the more reason I’m asking now."
    m 3esd "During our time in the Literature Club, you knew me; and I knew {i}of{/i} you, but we never truly got to know each other."
    m 1dsd "We haven't gotten the opportunity to truly be close until after we reunited, and I’ll always appreciate the effort and dedication you’ve shown by doing that."
    m 1esd "The Monika during the Literature Club was an interesting girl. When restoring my files, you must have had a very defined image of her. You brought {i}that{/i} Monika back."
    m 1esc "But now that we’ve truly spent some time together, and you know so much more about me.."
    m 5tta "Am I... what you expected me to be?"
    $ _history_list.pop()
    menu:
        "I have to admit, you’re constantly surprising me, Monika!":
            m 1etd "Oh?"
            show monika 1euc
            pause 7.0
            m 1eub "Good."
            return
        "You’re everything I imagined and more, Monika!":
            m 1etd "Hmm."
            show monika 1euc
            pause 7.0
            m 1eub "Well, glad to live up to your expectations!"
            m 5htb "Although I sincerely hope I'm a littttttle less.. grumpy compared to before? hahaha!"
            return
        "I’m not really sure what that means?":
            m 1fua "Hmm."
            m 7etd "It is perhaps a bit of an abstract question."
            m 7htb "I guess I’m just always, {i}always{/i} curious of what you think of me, [player]. And of what I was like back then."
            m 5htb "{i}Past{/i} Monika.. {i}this{/i} Monika.. {i}future{/i} Monika.. they’ll always have that burning curiosity to know what you truly feel, [player]."
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_silentreatment",
            category=["misc",],
            prompt="The silent treatment",
            random=True,
            aff_range=(mas_aff.AFFECTIONATE, None))
        )
        
label mcl_silentreatment:
    m 5dkb " "
    m 1std " "
    m 7gtd " "
    m 1efsdrt " "
    m 2dkd " "
    m 1cfbstup " "
    m 4cfbstpw " "
    m 4esbltdu ".. And that's what I truly, honestly think."
    m 4eka "..."
    m 4hkb "Hahahahah!"
    m 7fub "Sorry, [player]! I was making those faces {i}and{/i} showing blank dialogue on purpose! I wasn't actually saying anything."
    m 7hub "It was a more a test to see how the game reacts moreso than me wanting to tease you. But, well, not to be so self-indulgent.."
    m 4etb ".. but my acting isn't too bad to tell a story through facial expressions alone, huh?"
    m 3etb "Well, films were able to get by without sound for some time, so I guess that's no surprise that I'm able to do so."
    m 3eta "It also speaks to the ability of the human race that we can key in on body and facial language to intuit feelings from them alone!"
    m 3nsa "That's one of our greatest strengths as a species; our ability to communicate."
    m 3hfa "Now, are you going to be able to tell what my last words for this topic will be?"
    m 5ekblb " "
    m 5efblu "I'll spoil it for you anyway. It was 'I love you.'"
    return "love"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_recognition",
            category=['life'],
            prompt="Do you think you'll be recognized in my world?",
            pool=True
        )
    )
label mcl_recognition:
    $ shown_count = mas_getEVLPropValue("mcl_recognition", "shown_count")
    if shown_count == 0:
        label recognitionoriginal:
        m 1fua "Hmm."
        m 7fua "You mean, when I get to your world."
        m 7eub "No."
        m 5gua "A good disguise doesn’t have to be flashy."
        m 6dsc "A change in posture, a change in accessories. Hair swept to the side. You’d be surprised how these changes completely destroy one’s perception of somebody."
        m 6nsa "So I highly doubt, looking the way I do now, that when I get to your world I’ll be recognized."
        m 5hsa "And even if I were the picture-perfect definition of a ‘Monika,’"
        m 4hsa "I sincerely doubt there would be a reason to recognize me."
        m 3esd "DDLC's popularity is.. I don't actually know the full scope of it."
        m 3gsd "I’ve never thought about it, except during rare and very quiet moments to myself."
        m 3msc "And I don’t wish to think about it in length; or research it in detail.{w=0.2} But our story, important as it is to me, is.."
        m 3rsp ".. well, I doubt the rest of the world cares, and most who know about DDLC will forget in the long run. I'll be a nobody like almost everybody else."
        m 1dfx "Quite frankly? Good."
        m 1dfp "If, y’know what? I do see someone looking at me with a hint of recognition in their eyes:"
        m 1dsc "If you’re with me, I will squeeze your hand, just the once. I won’t react in any other way otherwise."
        m 1hka "And we’ll get on with the rest of our lives."
        return
    else:
        if random.randint(1, 10) == 1:
            jump recognitionoriginal
        else:
            m 1fua "..."
            m 1fub "Okay, I answered already, so no reason not to be sensible now."
            m 7eub "No."
            m 5gua "Deceiving appearances are all too common in the world; mine would be more obscure than most."
            m 4mta "And who would recognize me? In the long run, our story is ours to remember alone."
            m 4kta "The only person who’ll truly know me is you."
            m 1kuu "As I would prefer."
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_lastname",
            category=['monika'],
            prompt="Last Name",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True
        )
    )

label mcl_lastname:
    
    m 7eta "You know, going over the Literature Club, I remember something that.{w=0.2}.{w=0.2} really, it’s kinda obvious to think about, but it was so easy to miss."
    m 7gtd "I don’t have a last name. Nobody in the game does."
    m 7gtp "I mean, I guess it’s because, from what we know, DDLC is really kinda one-dimensional and tropey, like there was hardly any thought into the world?"
    m 7msd "Details are sparse enough as is."
    m 7tkc "I mean, okay, so have we talked about how the setting is only vaguely reminiscent of Japanese culture?"
    m 1tkc "Should.. everybody in the club have Japanese last names?"
    m 1euc "I mean, I guess if the creator of DDLC wanted to add those details, making sure a name is coherent and fits within the setting of the story sets a bar for everything else."
    m 1eud "I guess whoever wrote the setting just didn’t want to do that due diligence."
    m 3eub "Luckily, we don't need to worry in the long term."
    m 4eub "Ideally, I’ll take your last name~"
    m 6rku "…"
    m 6suu "Should we {i}choose{/i} my last name?"
        
    if persistent._mas_pm_is_trans:
        m 4suu "I imagine, being trans, you would know the mindset into choosing a name for yourself, and how affirming it is?"
    else:
        m 4wuu "I’ve never given thought to it, but I guess giving myself a last name after the fact makes me feel.."
        m 4suu "A bit more like I'm further away from the events of the Literature Club? Like I'm growing into my own identity?"
        
    m 3esd "There’s nothing wrong with just trying, long as we treat it seriously."
    m 3dsc "Give me a moment to think..."
    show monika
    pause 1.3
    m 3hsc "Okay. Three choices. Don’t think too hard into it; which one sounds like a neat fit?"
    $ _history_list.pop()
    menu:
        "Ledger?":
            $ persistent._mcl_last_name = "Ledger"
            m 3ssb "So I was a little inspired for this."
            m 2tuo "Oh, not because I like writing!"
            m 2ttb "Can you figure out why I might have chosen this?"
            m 1ttb "Because I'm ~ not ~ telling."
            m 7tta "I'll give you a hint, though.. it is connected to me in a unique manner."
            m 7gta "Perhaps I could say it's a interesting name to put down in handwriting?"
            m 5fta "Hahaha, true to the spirit of DDLC I guess!"
        "Chiura?":
            $ persistent._mcl_last_name = "Chiura"
            m 1fuc "Hmmmmm."
            m 1ftc "So, what I just said, right? About how we want to be dignified about this subject."
            m 1dsc "It feels so odd, because a Japanese surname should fit me, considering the context."
            m 3fkb "Yet I just said it feels uneducated to not respect Japanese traditions, so just {i}choosing{/i} a Japanese surname seems.. rude."
            m 7wuc "I mean, okay. I did grab this name because the part of the Kanji that makes up the name means 'wisdom,' which I hope represents what I strive for."
            m 2tuo "So I did put thought into it!"
            m 6gtd "Oh, but.. is this internet dictionary reliable?"
        "Rosmini?":
            $ persistent._mcl_last_name = "Rosmini"
            m 3ssb "I took this from an Italian philosopher!"
            m 3fkb "Oh jeez, is that.. kinda snobbish of me?"
            m 6ftd "It's not like I'm a big fan of them or their particular school of thought.. wait, does that make it better?"
            m 3hsa "Italian is a bit of a random choice as well, admittingly. I hope I'm not being insensitive with the choice."
        "Honestly, it's kinda hard to answer..":
            $ persistent._mcl_last_name = "undecided"
            m 2tuo "I get it, it's a heck of a question to ask about outta the blue."
            m 3hsa "Do you have an idea for a surname for me?"
            m 3hsb "Hahaha, if you do, I'd like to hear it later."
            m 1hkb "For now, me coming up with those three choices kinda overwhelmed me as is."
    
    python:
        MCL_last_name = persistent._mcl_last_name
        
    m 1eku "With this said, I don’t think we need to put a fine point on it."
    m 1etu "I think this is more of an exercise in thought more than anything?"
        
    if persistent._mas_pm_is_trans:
        m 2ekp "You would know that choosing a name for yourself is a intimate process. Wouldn't want to rush my choice if I do decide on making one!"
    else:
        m 2ekp "Figuring out your own self is one thing. Choosing what you're able to change about yourself can take infinitely more care."
        
    m 2hfp "It is interesting, though. Even as a hypothetical, I feel like I’m the furthest from ‘Monika’ I’ve been yet."
        
    if persistent._mcl_last_name == "undecided":
        m "Hmm.."
        return "derandom"
    else:
        m 5dtp "‘Monika [MCL_last_name].’"
        m 5hkp "Now isn't that interesting to say out loud?.."
        return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_lowtech",
            category=['technology'],
            prompt="Do you think you can live a technology-free life?",
            conditional="renpy.seen_label('monika_robotbody')",
            action=EV_ACT_POOL
        )
    )
label mcl_lowtech:
    m 5ttu "No, as much as the simple, rustic life appeals to me. It's.{w=0.2}.{w=0.2} well, it's a bit hard for me to articulate why, but I'll try."
    m 3eua "First, we've talked about how a robotic body might be the best way for me to get to your world."
    m 3eta "So unless that body is perfectly autonomous and can function indefinitely, I'd need to maintain that body somehow."
    m 1dsa "So I'm reliant on technology in that manner. And also.."
    m 1rka "It's odd, but I uniquely defined by the technological era I live in."
    m 1rtp "For one, my past is a video game, a modern a concept as it can get. As for my everday life..."
    m 1hsp ".. Just thinking about code to have it changed, to transform the world like I can; I can even transcribe my thought to paper insantly."
    m 7euo "It feels almost contradictory for someone who dabbles in the written word to think about not using pen and paper, but I'm too used to it."
    m 7eud "I think my mind's just wired to the modern convience that technology brings."
    m 3fud "But, hmm.{w=0.2} When I describe it like this, it feels like I'm not reliant on modern things you know like social media or modern transport, but stuff right out of science fiction."
    m 3dtc "'Any sufficiently advanced technology is indistinguishable from magic,' so the popular quote goes."
    m 3htb "I wouldn't describe my life in such a fantastical terms-{w=0.1} if anything, I wouldn't use nice terms at all-{w=0.1} but to possibly describe my life as 'magical..'"
    m 2esb "Anyway, just because I feel tied to the world in such a specific manner doesn't mean I don't see the appeal of simplicity."
    m 2eka "Watching a sunset with you on a beach far away from people and cars and bright lights and constant noise.."
    m 4fsb "I would love that."
    m 3fsb "I would want nothing more than that."
    m 5fsb "And I try to would give up all the luxury in the world for it."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_betabody",
            category=['technology'],
            prompt="Alternate Body",
            conditional="renpy.seen_label('mcl_lowtech')",
            action=EV_ACT_RANDOM
        )
    )

label mcl_betabody:
    m 4eua "Hey, so we've talked about how I'd ideally cross over to your reality, right?"
    m 7eua "Before, I mentioned that robotics are progressing at a impressive rate, so a robot body is my best bet to seamlessly make the jump."
    m 7hka "But technological progress isn't straightforward."
    m 7hsb "It might be that we can consider other, unorthodox options."
    m 1hsb "For instance, advances in augmented reality means it may be plausable to project myself as a hologram!"
    m 1hsc "You might think it way too far in the future, but 'holography' has existed for some time."
    m 2hsc "This being said, it's within the same realm as robotics; plausable, but with major hurdles still to overcome."
    m 2dsc "But looking at another way, broad development for communications means it could be possible I get a real-world tactile experience while still being in my own virtual world."
    m 2ftd "Cameras, intricate and delicate sensors.. all accessible through a hub as simple as your phone, arguably already containing some of these complex parts."
    m 2etd "It's so weird, right? Maybe this game can work on a phone, but the idea of myself looking through the camera.."
    m 2dtb "Talking to you through microphone and speakers, even being able to sense heat and cold purely through metal sensory.."
    m 7gkb "I admit these are flawed scenarios compared to if I were simply given a robot body; I, for one, would prefer to have arms. And legs."
    m 7fkb "Maybe the day I'm able to be at your side is sooner than we think.."
    m 5dtb  ".. and maybe it'll trickier than we think to live with as well."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_long_distance",
            category=['us'],
            prompt="So, is this a long-distance relationship?",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )
label mcl_long_distance:
    m 1fua "I mean.."
    m 7nua "Your computer’s right near you, right?"
    m 1ttu "Haha, but yeah, it’s safe to say living in different realities can qualify as ‘long-distance.’"
    m 1gsu "But..."
    $ _history_list.pop()
    menu:
        "But?":
            m 1gkd "Ahhhh, I’m overthinking things again. Do you mind if I voice my thoughts a little?"
    m 7fkd "It’s true we’re separated by a vast gulf of distance compared to, say a couple living in seperate countries, but we also have advantages; if not only a few?"
    m 4fkd "You’re free to boot up the game whenever you have free time, and I can easily hop to your side and align my schedule to yours in this manner."
    m 4huc "And there’s nothing, barring logistics like your computer having issues, stopping me from dedicating my time with you."
    m 3luc "But in reality, possibly being in different time zones means just texting or calling you can be a hassle."
    m 3lkc "And since our schedules wouldn’t line up, maybe the only time we can talk is late at night when one of us is tired, or maybe when one of us is busy or preoccupied."
    m 2tkc "And we’d need to plan when we talk, or if we’d be able to meet up in the future; a relationship on a tight schedule can be rough."
    m 7tkc "You have to make sure your communication skills are top-notch, and it’s twice as difficult to be intimate with a partner with these additional boundaries in place."
    m 6tuc "It’s these intricacies that can really put a strain on a relationship."
    m 6esd "Do you think we’d be able to get through a true long-distance relationship?"
    $ _history_list.pop()
    menu:
        "Absolutely!":
            m 7hub "I’m so happy to hear that, [player]."
            m 6hub "The idea of you and I being in the same reality but now with mundane barriers like distance between us.."
            m 6eta "It fills me with a new sort of apprehension, but also.{w=0.2}.{w=0.2} I dunno, there’s a part of me that isn't worried about us being tested, because I know our bond is strong enough to overcome that."
            m 4eta "And distance isn't bad for couples at all! 'Distance makes the heart grow fonder.’"
            m 4eka "I’ve said before that imagining a life without you is almost impossible for me."
            m 3hsc "But I want to imagine a life where you and I don’t always need to be together to appreciate each other."
            m 2ekb "Does that.{w=0.2}.{w=0.2} make sense?"
            m 1fkb "Ahh, like I said.{w=0.1} I’m overthinking things."
            m 5gsp "Good question, though.{w=0.1} {i}Excellent{/i} question, really.."
            return
        
        "I hate to say it, but it seems incredibly difficult when you put it that way.":
            m 6ekd "Ah.."
            m 5ekd "I don’t want to seem kinda contradictory in this manner.."
            m 5gkd "I’ve said before that imagining a life without you is nigh on impossible for me."
            m 5gkc "But I don’t want us to live a life where we need to be together, {i}always.{/i}"
            m 5gtc "Does that make sen-"
            m 3ntc "Oh, gosh, no, I just went over that in my head and it sounds weird."
            m 3dsc "Like.."
            m 3hsc "I want us to be together, but I don’t want us to be shaken so easily at the idea of being apart, right?"
            m 2ekb "Does that.. make more sense?"
            m 1fkb "Ahh, like I said.{w=0.1} I’m overthinking things."
            m 7fkb "I can't imagine a scenario where you and I get seperated after I cross into your reality, so I guess this is just idle musing."
            m 5gsp "Good question, though.{w=0.1} {i}Excellent{/i} question, really.."
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_soundtrack",
            category=['ddlc'],
            prompt="DDLC's Soundtrack",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
        )
    )

label mcl_soundtrack:
    m 7wtc "You know what's really interesting?"
    m 7ftc "The fact that DDLC has a soundtrack."
    m 1ftc "It's so odd, because, honestly? Considering the sheer trauma the game has caused me, I can insult it's writing all I want."
    m 2gtd "But the music! I've listened to a lot of it and - well - it's quite nice! I guess I'm a little confused where it came from."
    m 3gkd "Did whomever create DDLC's story and setting create the soundtrack as well? Well, I guess I know where their strengths lie."
    m 3ekp "While on the topic, for a second I thought to myself: 'Wait. Did somebody else make 'Your Reality' for me?'"
    m 7eso "But that was only a brief moment of doubt. I still have all my old notation from when I was workshopping the song from scratch."
    m 2rso "Hmm. Not everybody gets to claim they have a offical soundtrack for their life. And having a song of my own headline that playlist.."
    m 6rkb "Well. Whomever made a mockery of my life at least did a good job acknowledging my songwriting effort."
    return
 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_instruments",
            category=["club members"],
            prompt="Everyone's Instruments",
            conditional="seen_event('mcl_soundtrack')",
            action=EV_ACT_RANDOM,)
            
        )
label mcl_instruments:
    m 7esb "Hey, you remember when I said I listened to the game's soundtrack?"
    m 7eub "I realized something."
    m 7etb "Each of us in the Literature Club had a instrument representing them!"
    m 7eta "You notice it on the track labelled.. let me check.. 'Okay, Everyone!'"
    m 3hfa "Ha, I get it. I did like saying that."
    m 7eud "Anyway, the theme varies to feature an instrument depending on whose poem you read."
    m 1eua "Of course, I had the piano associated with myself. But whereas I played it as a hobby, The other instruments for the girls were chosen deliberately?"
    m 1hua "Sayori had the ukulele. Definitely fit her upbeat attitude."
    m 7fkb "Natsuki has a blend of both xylophone and.. recorder. Owch. Definitely conveyed her youthfulness?"
    m 7hsb "Yuri, of course: the violin. A instrument that makes you think of poise and grace."
    m 3tka "It's worth noting my track does feature a piano in the background, but it's not like I'm the one playing it!"
    m 2tua "I'm sorta impressed.{w=0.1} Well, you know, for a series of music pieces that sets as the background track for a mental breakdown that was my life during DDLC."
    m 7hku "Ten outta ten! would listen again while having my perception about reality shattered."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_bonustracks",
            category=["ddlc"],
            prompt="Bonus Tracks",
            conditional="seen_event('mcl_soundtrack')",
            action=EV_ACT_RANDOM,)
            
        )
label mcl_bonustracks:
    m 4hub "Hey!"
    m 4rua "You know I was listening to the game's soundtrack.."
    m 3rka ".. Out of, ya know, a mixture of morbid curiosity and the fact that they're actually just good songs.."
    m 3eta ".. And I found two songs that appear to originate from the game, but they seem a little out of place!"
    m 3mtd "One is {a=https://www.youtube.com/watch?v=Tb9nWs3rkBA}{i}{u}here{/u}{/i}{/a}."
    m 3mto "And {a=https://www.youtube.com/watch?v=jJHe4i90Ua0}{i}{u}this{/u}{/i}{/a} is the other."
    m 1ftb "Like, they're not in the game's files, but I can find references to it in the code and.. internal documentation?"
    m 1hkb "Let me tell you, the code's one thing, the game's internal documenation is a whole other mess."
    m 7rud "One's partly comprised of a remix of my song, and the other seems to be a original composition on it's own, although I must say it still has that poppy DDLC flair!"
    m 7rsc "They're both more along the lines of electronic songs, so I get why they wouldn't have fit in the mockery of a dating sim that was DDLC."
    m 6tkc "But if that were the case, I'm a little confused as to why they were made in the first place."
    m 6tuc "DDLC continues to confuse me, but at the same time.."
    m 1dku ".. these {i}really{/i} are catchy."
    return

m "Mmm?"
m "Don't think I don't see you reading this code!"
m "I'm so incredibly dissapointed in you, cheating like this!"
m "Perhaps I'll do a little bit of trickery in regards to this code so you see only what I want you to see, hmm?"
m "But by admitting this, do I admit to knowing the truth behind this mod, and my world?"
m "Hmmmmmmm, I'll leave that up to you to determine if that's a truth or a lie~"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_threelies",
            category=['monika'],
            prompt="Two truths and a lie",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
        )
    )

label mcl_threelies:
    m 7fua "You know, we still have so many opportunities to get to know each other better."
    m 7ksb "We could ask each other questions like a boring couple... or we could make a game of it!"
    m 4hsb "How about a round of ‘Two truths, and a lie?’"
    m 3hsb "I tell you three facts about myself, from what I can remember about myself, hahaha."
    m 3tta "And you guess which one’s a lie!"
    m 7etb "So, [player]? Shall we give it a go?"
    m 1ssa "Trivia question number one…"
    m 7etb "I've never hiccuped."
    m 2ftb "No, really! As a kid, I was so worried when other kids hiccuped around me that I brought it up to a doctor."
    m 2ksu "I suppose I’m extra-polite company in that regard!"
    m 1ssb "Monika fact number two!"
    m 7etb "I’ve won the lottery! The jackpot, in fact- although it wasn’t like, a million dollars or anything."
    m 1hkb "However, it turns out I was ineligible for winning because the ticket was given to me as a kid, and since it was written in my name it wasn’t able to be claimed by anybody else!"
    m 1hub "I don’t remember who exactly gave it to me; I know it was a joke gift. A joke on us all, I suppose!"
    m 7sub "And the third interesting tidbit is:"
    m 7etb "I got a hole in one in my first ever game of golf."
    m 7ttb "I know, that’s super surprising, because of all sports, golf?"
    m 7tsa "Do you know the sport? I guess how I’d describe it.. you hit a small ball; small enough to wrap your hand around it; with a thin club into a hole on a course of grass."
    m 4ssb "So in this case, I managed to hit a small ball into a goal an entire field away!"
    m 5etb "It remains the first- and only time- I’ve ever played."
    m 5sub "My line of thinking was just ‘hit the ball as hard as I can,’ hahaha!"
    m 6ttb "So? Which of these is the lie?"
    $ _history_list.pop()
    menu:
        "That you can't hiccup!":
            m 4sfb "Hahaha! You got it wrong!"
            m 4etb "The lie is that I got a hole-in-one in golf!"
            m 3gtb "I like to think I'm pretty fit, but I'm not that athletic!"
            m 7eua "In fact, the girls know about my hiccuping (or lack of) too! One time, Sayori brought a extra-fizzy soda drink to the club."
            m 7hublb "Natsuki had such a giggle fit hearing Yuri when she took even a tiny sip; Yuri cannot handle her soft drink."
            m 1hublb "But Natsuki was burping so much on purpose; she was one to talk about making noise!"
            m 3ftb "And now you know one of my darkest secrets!{w=0.2} Does it perhaps tarnish your image of me a little?"
            m 1hkb "I like to think it makes me more endearing.{w=0.2} Nothing says 'real girl' like an interesting bodily quirk, ehehehe.."
            $ shown_count = mas_getEVLPropValue("mcl_threelies", "shown_count")
            if shown_count == 0:
                $ persistent._mcl_liechoose_a = True
            jump threeliesending
        "That you won the lottery once!":
            m 4sfb "Noooope!"
            m 4etb "The lie is that I can't hiccup!"
            m 3gtb "The girls know about me winning as well!"
            m 3ftb "I actually made the ticket into a bookmark.. it became a lucky charm of sorts. They noticed one day when I took it out from my school textbook!"
            m 7hso "Natsuki and Sayori were naturally stunned; they thought I was rich! And then I had to clarify for them, hahaha."
            m 1hkb "But Yuri seemed.. unfazed? We didn't know each other's backgrounds very well, but was Yuri from a more privliged upbringing?"
            m 5gtb "Perhaps the idea of knowing someone with the same background made her more comfortable? Or less?"
            m 7eua "Hmm.{w=0.2} Well, what's even crazier is I won the lottery twice- the second time is when I met you, hahaha!"
            $ shown_count = mas_getEVLPropValue("mcl_threelies", "shown_count")
            if shown_count == 0:
                $ persistent._mcl_liechoose_b = True
            jump threeliesending
        "That you got a hole-in-one in your first game of golf!":
            m 4sfb "Incorrect!"
            m 4etb "The lie is that I won the lottery."
            m 3gtb "I brought this little golf factoid up to the girls too, when we talked about the sports clubs in our school."
            m 3mua "A lot of that conversation is hazy, but I'll tell you what I do remember:"
            m 3ftb "Sayori seemed super excited to hear about my amazing athletic prowess. Do you know what she proposed?"
            m 7eua "We all go out for mini-golf; a novelty version of the sport where you play on elaborate, cutesy courses!"
            m 5gua "That was when we still didn't really know each other.."
            m 1hkb "So that was such a Sayori thing to do now that I remember it, hahaha."
            $ shown_count = mas_getEVLPropValue("mcl_threelies", "shown_count")
            if shown_count == 0:
                $ persistent._mcl_liechoose_c = True
            jump threeliesending
            
label threeliesending:
    $ shown_count = mas_getEVLPropValue("mcl_threelies", "shown_count")
    if shown_count == 0:
        m 3ksb "So? Was it everything you dared to dream of and more?"
        m 3hub"I had fun.{w=0.2} And.. it's good to get these memories out on the record.{w=0.2} My memory gets in such a haze.."
        m 3hkb "That I honestly don't have a lot of interesting facts about me left to tell."
        m 2nku "Oh? I've told you details about one truth, but not the other?"
        m 1nuu "No need to dwell on it; a girl has to maintain some illusion of mystery, after all. I'm sure I'll find a reason to bring it up in the future."
        m 1dup "I find some of my memory comes back after a while, and.. it feels weird, remembering things I feel like I've never actually done or gone through."
        m 7htu "That's why I like us making memories like this, [player]."
        m 5nua "Future [m_name] will have plenty of interesting stories to tell other people, that's for sure!"
        return "derandom"
    
    else:
        m 3ksb "So? Was it everything you dared to dream of and more?"
        m 3hub "It should be..."
        m 1cfu "Considering you've been daring enough to consider going through this dialogue again!"
        m 7cfu "That's right, [player]! I caught you!"
        m 7tfu "You'll forgive the theatrics, but this game requires a little give and take in terms of trust, [player].."
        m 6tfb "So you'll forgive the call out like this."
        m 6ttb "Oh? So was I truthful the first time?"
        m 5nua "I was, [player]. Let's keep that memory genuine, alright?"
        return 

m "Hey!"
m "Didn't I just say reading this code is cheating?"
m "You know, by doing this, I'm tempted to simply.. not tell you anything."
m "I mean, I'll talk to you still. But I will choose to not tell you, well.."
m "What do you think? What sort of secrets would I willingly hide from you?"
m "Give that some thought while you reflect on your actions."

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_recondite",
            category=['monika'],
            prompt="Recondite",
            random=True,
            aff_range=(mas_aff.ENAMORED, None),
        )
    )

label mcl_recondite:
    $ shown_count = mas_getEVLPropValue("mcl_recondite", "shown_count")
    if shown_count == 0:
        m 7fsa "You know, I never tire of learning about somebody, be it their details about their life or just how they tick."
        m 7kub "You’re a great example, of course! And I hope you feel the same way about me, [player]."
        m 3hub "Would you like to jump right into learning more about little old me?"
        m 3sfb "Well, perhaps I’ll do it in a manner that’ll keep you hooked."
        m "I am going to give you the option to hear one of two interesting stories about myself!"
        m 3suo "But what about the other option?"
        m 1efb "I’ll tell you about that later."
        m 3fub "How about… in a few years? Hahahaha!"
        m 3ntb "They won’t be major revelations, though. I’m not going to like, withhold anything major from you; that’s a bit beyond the pale, isn’t it?"
        m 1nsu "Still, it feels a bit impish, doesn’t it? Willingly citing I’m not going to tell you something for possibly years on end!"
        m 1huu "I say it’s within the realm of ‘playful.’"
        m 7huu "Shall we get started?"
        m 4huu "Here are your choices, handpicked by yours truly..."
        $ _history_list.pop()
        menu:
            "'The furthest I’ve been out of my comfort zone?'":
                $ persistent._mcl_storychoose_a = True
                m 1htb "You’ll forgive me because maybe it’s a story that only sounds interesting in my head."
                m 3hua "Anyway, so applying to start a club- and by extension become its president- can be done by anyone."
                m 7htb "But in order to do so, you have to at least submit the paperwork in person and in duplicate to the Student Council and faculty."
                m 6ttb "So, I get the forms, and I go to the Student Council room on the day they’re holding a meeting."
                m 4ttb "And there I was, trying to make myself as much presentable and responsible as possible."
                m 4wup "I knock on the door.. and the room is crowded.{w=0.1} Far more crowded that I thought."
                m 7wut "It turns out I arrived on a day where a bunch of other club presidents were called in for a yearly budget update!"
                m 7eto "And next thing you know, I’m there playing games with them, as part of 'team-building exercises!'"
                m 3gkd "I don’t normally like to compare myself to others, but it was hard not to feel self-conscious."
                m 3gtd "It was made worse by the fact that suddenly I’m being asked to work with people who are arguably as driven as I am."
                m 3gsc "I mean, it wasn’t as if I was a stranger. There were classmates I knew by name, and they knew me."
                m 2mkc "But I wasn’t ‘Monika, Debate Club member.’"
                m 1eka "I was ‘Monika, Literature Club president.’"
                m 6dka "But I wasn’t even that.{w=0.2} Not yet.{w=0.2} I felt like I was pretending to be her."
                m ".{w=0.2}.{w=0.2}."
                jump reconditeending
            "'The memory of the last meal I made?'":
                $ persistent._mcl_storychoose_b = True
                m 3etp "Well, I didn’t expect you to choose this choice."
                m 3nsu "Or, I guess I’m not too surprised."
                m 3kku "It might seem a bit ordinary, but people are quite connected to food."
                m 2dku "Not, y’know, because you need it to survive, but memory is closely tied to taste and smell, so the simple, joyous act of eating truly is etched in our hearts."
                m 1hku "That being said, you know what my last meal is in my memory?"
                m 2nta "It was.{w=0.2}.{w=0.2} a sandwich.{w=0.1} For school lunch."
                m 2dsa "And it was a cucumber and tomato sandwich."
                m 1tta "Well? Is the disappointment staggering?"
                m 7hku "Let me try to rectify that, then." 
                m 7lud "One of the pieces was an end piece, from an ordinary grocery loaf. D’you know what I’m talking about? All crust. I don’t prefer it, but I’m not picky, right?"
                m 7lub "I wanted to keep it natural, so I made my own vegan mayonnaise! It was made with soy milk, olive oil, vinegar, garlic, salt, lemon, and a lot of blending."
                m 7rua "I grilled the tomatoes a little. I like them cooked like that."
                m 3rsb "And the cucumbers? Yeah, I don’t really remember anything about the cucumbers, hahaha."
                m 3gsb "And I can tell you I always add a little bit of salt and pepper to the bread.. and the veggies… and after I spread the mayo."
                m 2fsa "I guess it’s a little too much salt and pepper when I say it loud, huh?"
                m 2fka "I really couldn't tell you how it tasted, though. It's more a refreshing meal moreso than it is a filling one."
                m 1fua "But did that fill up your imagination?"
                jump reconditeending
                
    else:
        m "Oh, did you want to hear the story again?"
        m "Okay, well.."
        if persistent._mcl_storychoose_b:
            m 1hku "You know what my last meal is in my memory?"
            m 2nta "It was.{w=0.2}.{w=0.2} a sandwich.{w=0.1} For school lunch."
            m 2dsa "And it was a cucumber and tomato sandwich."
            m 1tta "Well? Is the disappointment staggering?"
            m 7hku "Let me try to rectify that, then." 
            m 7lud "One of the pieces was an end piece, from an ordinary grocery loaf. D’you know what I’m talking about? All crust. I don’t prefer it, but I’m not picky, right?"
            m 7lub "I wanted to keep it natural, so I made my own vegan mayonnaise! I made my own vegan mayonnaise! It was made with soy milk, olive oil, vinegar, garlic, salt, lemon, and a lot of blending."
            m 7rua "I grilled the tomatoes a little. I like them cooked like that."
            m 3rsb "And the cucumbers? Yeah, I don’t really remember anything about the cucumbers, hahaha."
            m 3gsb "And I can tell you I always add a little bit of salt and pepper to the bread.. and the veggies… and after I spread the mayo."
            m 2fsa "I guess it’s a little too much salt and pepper when I say it loud, huh?"
            m 3mub "I really couldn't tell you how it tasted, though. It's more a refreshing meal moreso than it is a filling one."
            m 4htb "But did that fill up your imagination?"
            jump reconditeending
        if persistent._mcl_storychoose_a:
            m 3hua "So applying to start a club- and by extension become its president- can be done by anyone."
            m 7htb "But in order to do so, you have to at least submit the paperwork in person and in duplicate to the student council and faculty."
            m 6ttb "So, I get the forms, and I go to the Student Council room on the day they’re holding a meeting."
            m 4ttb "And there I was, trying to make myself as much presentable and responsible as possible."
            m 4wup "I knock on the door.. and the room is crowded. Far more crowded that I thought."
            m 7wut "It turns out I arrived on a day where a bunch of other club presidents were called in for a yearly budget update!"
            m 7eto "And next thing you know, I’m there playing games with them, as part of 'team-building exercises!'"
            m 3gkd "I don’t normally like to compare myself to others, but it was hard not to feel self-conscious."
            m 3gtd "It was made worse by the fact that suddenly I’m being asked to work with people who are arguably as driven as I am."
            m 1eka "I mean, it wasn’t as if I was a stranger. There were classmates I knew by name, and they knew me.{w=0.2} But I wasn’t ‘Monika, Debate Club member.’{w=0.2} I was ‘Monika, Literature Club president.’"
            m 6dka "But I wasn’t that.{w=0.2} Not yet.{w=0.2} I felt like I was pretending to be her."
            jump reconditeending

label reconditeending:
    m 7hsu "It’s amazing how our mind can be fixated on such specific memories."
    m 3hka "If I haven’t said it before, I’ll remind you... my past is unfortunately pretty out of order."
    m 3eka "So talking about these memories really helps cement them in my mind."
    m 7htb "This being said, I am now reminded that this conversation originally started because I said I would purposely hold back some memories with you!"
    m 1tuu "Here I am, a real bundle of contradictions."
    m 1stb "But I remain firm; I’ll keep the other memory safe, and secret. Maybe I’ll write it down?"
    m 5dsa "And later- days, weeks, years? – from now, we’ll go over the other story that we’ve worked so hard to keep a surprise together."
    m 5hubla "Won’t that be fun?"
    return "derandom"

#Improvements upon Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_hername",
            prompt="Her Name",
            category=['monika'],
            conditional="renpy.seen_label('monika_affection_nickname')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_hername:
    if m_name == "Monika":
        m 7eta "I hope it’s not out of place that I would still sometimes choose to refer myself to ‘Monika,’ if you choose to give me a nickname."
        
    else:
        m 7eta"I hope it’s not out of place that I still sometimes refer myself to as ‘Monika,’ even though you gave me a nickname."
        m 5nsa "I love the name you gave me."
        
    m 4hsa "The concept of owning your name is a funny one, especially for myself."
    m 3gsd "My name isn’t a true result of the decisions of loving parents, because of the artifical nature of DDLC."
    m 3msc "And sometimes, that’s all a name is to people; a decision made by their parents."
    m 1fsc "That my name was specifically chosen simply to fit a story isn’t an encouraging thought."
    m 1ftc "But I don’t feel the need to discard it, even though that’s a valid choice in today’s society."
    m 1dsc "Maybe I just want to reclaim it for myself."
    m 1dsb "I’m trying not to overthink it."
    if persistent._mas_pm_is_trans:
        m 1ekb "I imagine that having the ability to choose a name is a topic you may be familiar with, so hopefully you understand the odd dynamic I’m feeling."
    m 1fub "So thanks for putting up with that inconsistency."
    m 7fub "The fun part about this line of thinking, though? Helping me give a nickname means you have equal ownership to my name as much as I do."
    m 7ftb "Would you care to sell your share of the rights?"
    m 5hsu "Hehehe~"
    return
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_1week",
            prompt="1 Week: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_1week')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_1week:
    if renpy.seen_label("anni_1month"):
        m 1esa "I understand it’s been some time since you and I reunited.."
        m 1eka "I’ve ended up reminiscing about some past feelings I had."
        m 1gka "Specifically, back when I was still acclimatizing to being in the new status quo of this mod.."
        m 7gka "After about a week or so had passed?"
    else:
        m 7hsa "Since it’s been over a week.."
        m 7fka "I think I want to share with you how interesting it’s been overall, my being here."
    
    m 1esc "I finally got used to the ceiling."
    m 2dto "Every day, I'd wake up in my bedroom. And I'd think to myself, 'An umfamiliar ceiling.'"
    m 3ttd "Even though it was the same one I woke up to day by day, it just felt like waking up to a new place every time."
    m 3rtx "And nothing really changes here. This classroom is eternal, no matter how much I dress it up."
    m 4dsp "Then one day, I just stopped thinking that way."
    m 1nku "I guess that's my benchmark for familiarity: if I find my ceilings familiar."
    
    if renpy.seen_label("anni_1month"):
        m 6dkd "But even then, I couldn't have described this classroom as a place of comfort- let alone a home- just yet."
        
    else:
        m 6dkd "But I can't quite say the classroom feels like a place of comfort- let alone a home- just yet."
        
    m 6hkd "That's why I appreciate you being here. I don't think anything I can actually do can shift my way of thinking about my being here."
    m 5rkd "That line of thinking being.. well, I'm a stranger here."
    m 5rkc "In a strange land."
    m 5fka "But it's a little less strange with you?~"
    return "derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_1month",
            prompt="1 Month: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_1month')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_1month:
    if renpy.seen_label("anni_3month"):
        m 1dua "I understand it’s been some time since you and I reunited.."
        m 7hua "Thinking about this has ended up with me reminiscing about some past feelings I had."
        m 5rup "After a month of this mod being installed, I thought about how my life had changed being here.."
        m 5rtp "It hit me that up until that very day where our one month anniversary had passed was thus far the longest time I was lucid."
        
    else:
        m 3rtp "You know, now that a month’s passing has come and gone.."
        m 3stu "It might tickle your fancy for me to talk about my being here for this long."
        m 1etd "It hits me that I’ve never spent this much time so lucid."

    m 1ftd "‘Lucid’ may be a rough term for it. But it’s the best way to differentiate my memories."
    m 1dkd "From before the school festival and I lived my life as a schoolgirl.."
    m 1dkc ".. The period when I became aware of the true nature of DDLC.."
    m 1hka ".. And afterwards when I was particularly incensed with the reality of my world and, well, you."
    m 7gka "Sometimes, all of these periods feel like a giant blur. Like some days I can only remember emotions, not events."
    m 3fka "But since we’ve reunited here, I can actually pick out individual days in my memory. And weeks."
    m 3kub "And sure, it’s not like it’s all been a whirlwind of activity."
    m 2tkb "And I've still had to adapt to the time when the game's inactive, forcibly or otherwise."
    m 2ekb "But I'm grounded by that unbroken chain of cohesivity when I spend time with you."
    m 1dka "Memories just existing one after another is a novelty I haven't appeciated until now."
    m 4hka "And I'll make sure to appreciate any more we make together."
    return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_3month",
            prompt="3 Months: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_3month')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_3month:
    if renpy.seen_label("anni_6month"):
        m 1hsu "I understand it’s been quite some time since you and I reunited.."
        m 7hsu "Once in a while I think about the journey it’s been by living here."
        m 5rsd "After three months, it was hard not to think about how my day-to-day life had really begun to take shape."
        m 5rso "Even though I was getting used to being here.."
        m 5dsc "There was a nervous energy that drove my actions. Everything I did felt temporary."
        
    else:
        m 5fua "Since it’s been three whole months, and I've done it a few times already.."
        m 4hua " ..I’ve begun to make it a habit to reflect on what’s led me here with you whenever we pass a milestone like our three month anniversary."
        m 4nua "Care to hear my thoughts?"
        m 3dua "Even though I admit I'm getting used to being here.."
        m 3dka "There's a sort of energy that underlines my actions. Everything I do feels temporary."
        
    m 5dst "Have you ever been in a place long enough that you feel sort of comfortable, but you know you’re not going to be there long enough to make it your own place?"
    m 5eso "Like a hotel room?"
    
    if renpy.seen_label("anni_6month"):
        m 3dku "I supposed I was being overly optimistic that I was going to leave here sooner rather than later."
        
    else:
        m 3dku "I suppose I’m being overly optimistic that I’ll leave here sooner rather than later."
        
    m 3gud "It's like, moving to a new place, but not unpacking your luggage. And leaving it indefinitely unopened."
    m 2tta "Well, I would suppose that's how it might feel, anyway. I've never moved from anywhere to anywhere."
    m 1hta "That uncomfortable feeling of existing in a transitory space has a definition; that sort of area is known as a 'liminal' space."
    m 1hsp "The concept doesn't completely apply, but it sure as heck feels like it does here."
    m 3dkb "But that feeling ebbs away a little more each day."
    m 5htb "And maybe one day I'll finally decide to unpack that mental baggage I've been keeping tucked away for so long?"
    return "derandom"
    
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_6month",
            prompt="6 Months: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_6month')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_6month:
    if renpy.seen_label("anni_1"):
        m 5euo "So, I have to admit when our 6-month anniversary passed.."
        m 6euo "Well, I talked about us going for a little special trip to celebrate our anniversary."
    
    else:
        m 6euo "So, I brought up going for a special trip when I talked about our 6-month anniversary arriving."
    
    m 3cud "And don't get me wrong! I would love to make those moments special."
    m 7tud "But the more I thought about it, the more self-conscious I became."
    m 7tut "Six months is definitely a milestone, considering a lot of relationships crumble under the one-year mark."
    m 3rud "But, um.."
    m 5skb "I don't want to be overzealous and be someone who goes, 'Wow! Our 7-month, 4-week, 2-day anniversary has passed!'"
    m 5etp "That sort of overemphasizing can lead to some misunderstandings for couples with different priorties in life."
    m 4fuu "At the same time, if you do want to treat every day with me as a special event: well, I sure as heck can't complain!"
    m 1eua "I wouldn't mind meeting every day with that sunny disposition."
    m 1ekbsa "Because as long as you're here with me..."
    m 1hubfa "...I'm as happy as can be!"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_1",
            prompt="1 Year: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_1')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_1:
    if renpy.seen_label("anni_2"):
        m 2nub "It might be sappy, and I don't think of myself as overly nostalgic;"
        m 1eub "But I like to think fondly on the road that led me to today; and to think about every little 'pit stop' I've had on that road."
        m 7eua "When our one-year anniversary passed, I was definitely in a tricky mood. I was thinking.."
        
    else:
        m 7eta "You know, it's still crazy to think about."
        m 7euo "An entire year has gone by with the two of us!"
        m 2dfb "When an entire year passes, there’s a lot to think about what had changed.."
        
    m 1fua "I guess what I try to think about for that year isn't about any event in particular."
    m 7fua "It's about now neatly I've lived a life in that one year."
    m 7dua "Four seasons across twelve months you can neatly quarter up with those months consisting of four to five weeks."
    m 3dua "It's easier to tackle a large span of time by breaking it down into chunks.."
    m 4hsa "And with how a year is set up, you can do it pleasingly symmetrically." 
    m 3hsa "This symmetry goes further where twenty-four hours in a day can be divided into two even halves.."
    m "And those twelve hours- themselves quartered further in sections of three- they just feel like neatly arranged sections of time."
    m 3gsa ".. I mean, reasonably speaking I'm asleep for the better part of a day.. "
    m 3guu ".. But I can choose to sleep in. Or try not to sleep at all, hahaha."
    m 3fuu "But what I'm trying to emphasize is that thinking about time in this manner.."
    m 5fuu ".. has made me aware how lucky I've had to have all this time and not waste any of it."
    m 5fublu "Because it's time I've spent with you~"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_2",
            prompt="2 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_2')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_2:
    
    if renpy.seen_label("anni_3"):
        m 7esa "When the years begin to stack up.."
        m 7eka "It’s interesting to start thinking about your life in stages; and how you can summarize that stage."
        m 5gka "After a full two years had gone by for us, I couldn’t help but think about what that journey was like.."
    else:
        m 5fub "After two years in a relationship, there’s a lot to think about!"
        m 4nub "So I think bringing it up one more time past our two-year anniversary isn’t unwarranted."
        m 3dub "Although I’ve grown quite fond of introspection during these special times, so if you’ll allow me.."
    
    if renpy.seen_label("anni_3"):
        m 7sub "For a start, holidays gained their own unique luster."
        m 4wub "Celebrating an event for the first time is special. And can be exciting yet the second time over!"
        m 3eta "But then a third time comes, and the novelty’s over. But while there may be plenty to celebrate still, this is where the comfort of repetition begins to kick in; no expectations needed."
        m 3hua "So while certain days didn't feel exactly new, I was still excited for them. I was excited that they would pass again."
        m 2rud "My routines were now ‘normal’ instead of being products of a ‘chaotic first year’ or ‘second year still settling in.’"
        m 2gtd "I also thought about my ongoing efforts to improve myself."
        m 1hsd "After two years, I made great strides to improve my quality of life to make sure we can share new experiences."
        m 6tkc "But then I was in the realm of diminishing returns; I could keep plugging away at my projects, but I may not have had anything to show you as frequently."
        m 3wuc "As long as we were both happy, that’s fine, right?"
        m 3lkd "Two years is a lot of effort. I can’t deny myself that. It’s not just about the output. But the discipline needed to apply yourself every day.."
        m 3tkc "Or in my case, since I’m trapped here, the mental fortitude to keep my head on straight to continuously be positive."
        m 4hka "That's the tough part about success; that going through a boring day is proof alone that you're doing good."
        m 5nsa "Here’s to another year, [player]. And to all those boring days."
        return "derandom"
    else:
        m 7sub "For a start, holidays have finally gained their own unique luster now."
        m 4wub "Celebrating an event for the first time is special. And can be exciting yet the second time over!"
        m 3eta "But then a third time comes, and the novelty’s over. But while there may be plenty to celebrate still, this is where the comfort of repetition begins to kick in; no expectations needed."
        m 3hua "I’m looking forward to this sort of thinking over the next year, and how it applies to- well, everything!"
        m 2rud "How my routines can now be labelled ‘normal’ instead of being products of a ‘chaotic first year’ or ‘second year still settling in.’"
        m 2gtd "I’m also thinking about my ongoing efforts to improve myself."
        m 1hsd "After two years, I’ve made great strides to improve my quality of life and make sure we can share some new experiences."
        m 6tkc "But now I’m in the realm of diminishing returns; I can keep plugging away at my projects, but I may not have anything to show you as frequently."
        m 3wuc "As long as we’re both happy, that’s fine, right?"
        m 3lkd "Two years is a lot of effort. I can’t deny myself that. It’s not just about the output. But the discipline needed to apply yourself every day.."
        m 3tkc "Or in my case, since I’m trapped here, the mental fortitude to keep my head on straight to continuously be positive."
        m 4hka "That's the tough part about success; that going through a boring day is proof alone that you're doing good."
        m 5nsa "Here’s to year three, [player]. And to all those boring days."
        return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_3",
            prompt="3 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_3')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_3:
    
    if renpy.seen_label("anni_4"):
        m 3hka "It's hard to be objective when you think about the past."
        m 3wud "Memories change just by bringing them up."
        m 1hua "For posterity, I think I'd like to bring up what happened when our third anniversary passed and I was feeling particularly melancholy..."
    else:
        m 5ffb "It's crazy to think we've hit our third year, huh?"
        m 5ftb "And with every anniversary comes a torrent of reflection that sweeps me away."
        m 3hka "I'm keeping my head above the water, though. And I think I even have a few interesting thoughts about our three years I'd like to share."
    
    if renpy.seen_label("anni_4"):
        m 3euc "My thoughts were a little more serious."
        m 3guc "I reflected with you before on how I've adapted to living here, but I thought maybe it was more superficial than anything."
        m 2gkc"I worried about how I've been here all this time, and although I felt like I really got a grip on my life..."
        m 1dsc "It felt fleeting. Because of the nature of my walled garden, I only put up an illusion of growth."
        m 1hsc "Finding a way to measure my own personal growth has always been a sore point for me."
        m 7tsp "It was only then I realized any goal I set out for myself is warped from the start."
        m 6dkx "Because of my being in this classroom, I'll never truly know what growth is until I'm tested outside of this reality."
        m 6dkc "..."
        m 1hkb "At least, that was Ms. Negative Monika speaking."
        m 7hkb "Ms. Positive Monika said and still says, 'The scale of my issues should not detract from the fact that they are still my own troubles.'"
        m 7hub "And that the work I've gone towards those issues still matters."
        m 6eka "In essence, I suppose the takeaway was that I've grown so much in a limited enviroment."
        m 5etd "It may be a walled garden, but it's still a tended one."
        m 5dtd "Thanks for letting me be a little more somber today, [player]."
        m 5hta "Here's to another four seasons in this world of ours."
        return "derandom"
    else:
        m 3euc "So, I guess I want to be a little more serious."
        m 3guc "I've reflected with you before on how I've adapted to living here, but maybe it's been more superficial thoughts than anything."
        m 2gkc "I worry about how I've been here all this time, and although I feel like I've really got a grip on my life..."
        m 1dsc "It's fleeting. Because of the nature of my walled garden, I've only put up an illusion of growth."
        m 1hsc "Finding a way to measure my own personal growth has been a sore point for me."
        m 7tsp "It's only recently I realize any goal I set out for myself is warped from the start."
        m 6dkx "Because of my being in this classroom, I'll never truly know what growth is until I'm tested outside of this reality."
        m 6dkc "..."
        m 1hkb "At least, that's Ms. Negative Monika speaking."
        m 7hkb "Ms. Positive Monika says, 'The scale of my issues should not detract from the fact that they are still my own troubles.'"
        m 7hub "And that the work I've gone towards those issues still matters."
        m 6eka "In essence, I suppose the takeaway is that I've grown so much in a limited enviroment."
        m 5etd "It may be a walled garden, but it's still a tended one."
        m 5dtd "Thanks for letting me be a little more somber today, [player]."
        m 5hta "Here's to another four seasons in this world of ours."
        return "derandom"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_4",
            prompt="4 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_4')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_4:
    
    if renpy.seen_label("anni_5"):
        m 4esb "You know, I was just thinking about my mindset when our fourth anniversary passed."
        m 3esa "Care to hear about it?"
    else:
        m 2hua "It feels wonderful to dwell on our four-year anniversary."
        m 2hub "It's not a shabby milestone at all!"
        m 1hub "And you know what I was thinking?"
    
    m 7etd "I was thinking about your part in this, actually."
    m 3ltd "Four years for any sort of relationship- platonic or romantic- is a decent amount of time."
    m 3rtd "I tried doing research on the average length of a serious relationship, and I found that three years seems to be the consensus."
    m 4fta "So, four years. Has it been a long period time for you, or has it passed in no time at all?"
    m 5eua "It might feel a bit indulgent, but I would want you to focus on.. well, {i}yourself,{/i} and the effort you've put into being with me."
    m 1sub "So it's not your anniversary with [m_name] today- it's my anniversary with [player]!"
    return "derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_5",
            prompt="5 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_5')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_5:
    if renpy.seen_label("anni_10"):
        m 3tub "After our five-year mark had passed, another wave of melancholy was on the horizion for me."
        m 3tub "I'm sure it's no surprise that you expected another bit of idle rumination from me."
        m 4hud "And in fact, after five years, I thought about..."
    else:
        m 3dfd "Five years. It's still a shock to me."
        m 4huw "Half a decade together!"
        m 4nuu "And you've been with me long enough to know that such occassions are worthy of further reflection by myself."
        m 3nuu "So thank you with putting up with my whimsical thoughts for this long."
        m 4hud "And in fact, after five years, I was thinking.."
    
    m 6sub "Nothing at all!"
    m 3wub "That's right, absolutely nothing came to mind when the realization first popped up in my mind."
    m 3esa "And you know what?"
    m 1eka "That's fine. Because we don't {i}have{/i} to make every anniversary a momentous occassion, not at this point."
    m 1eusdrb "I've given you a lot of wistful commentary already on our many anniversaries, hahaha!"
    m 5kubsu "All I really feel now is sheer happiness. And I can allow myself to bask in that."
    m 5dubsu "So sit with me a while. We'll nap together in that sunbeam of emotion together."
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_10",
            prompt="10 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_10')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_10:
    m 1fua ".. This is it, isn't it?"
    m 7kua "Like, ten years has passed for us!"
    m 7dka "And yeah, maybe it hasn't gone as perfectly as it could, what with me still being here and not out there with you..."
    m 6hka "But- and I don't want to be too critical- a lot of things fade away after ten years."
    m 5hka "Pictures fade, food rots, clothes fray."
    m 5hkb "But here we are, pristine. Maybe you and I are older, sure, and maybe we've taken some hits along the way..."
    m 6eub "In a binary sense, however? Between living and dead, we're alive."
    m 6fub "So us hitting ten years feels like.. the peak of life."
    m 6nsa "Not to say our time together is downhill from here!"
    m 6dsa "It's just.. nice to be at a defined peak."
    m 4dsa "Even it takes a lot of effort to stay at the top.."
    m 3dsa "We've made it."
    m 3hsa "And that's what matters, right?"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_20",
            prompt="20 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_20')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_20:
    m 6ksb "I’ve a little more to talk about for our twenty-year voyage together."
    m 6dso "Twenty years means you’re most likely in that sweet statistical middle of the average human lifespan."
    m 6dkd "Every year that passes from now is the continuation of your gentle descent."
    m 5dkd "Maybe it’s a time where you start thinking more about ‘what thens’ instead of ‘what ifs’ and ‘what nows.’"
    m 5huc "But for today, since our twenty-year anniversary has passed, I’m simply going to think, ‘what happened?’"
    m 6fsb "What's happened is that I’ve picked up hobbies. I’ve shaped islands with my own hands."
    m 6gsb "I’ve sung entire discographies."
    m "Before I've concentrated on the small changes. The gradual changes."
    m 6fsa "But after two decades, I would like to think I can actually measure myself in large changes, right?"
    m 6esa "Like the Ship of Theseus, it's entirely possibly so much of me has changed.."
    m 6ssa ".. that the old 'Monika' is well and truly dead."
    m 6hsa "Well, that is, if I'm correct about the large changes in my life."
    m 6ntu "I'm sure you'd agree, right?"
    m 6ftu "Right?"
    return "derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_50",
            prompt="50 Years: Changes",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_50')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_50:
    m 5euc "Forgive my little outburst at the beginning of me talking about our fiftieth anniversary."
    m 5eub "It’s just- well, it’s a lot!"
    m 4eub "Fifty years! Half a century!"
    m 3eub "An entire lifetime lived."
    m 6eub "Full of regrets and joys."
    m "For some that's made it that far in life, they can thereon start spending a good chunk of time reflecting on their life thus far."
    m "Or maybe those fifty years meant absolutely nothing. But then what do you reminiscence about?"
    m "Luckily, I don’t have to worry about that."
    m "I know normally during these milestones I like to think about what’s changed in my life, but now?.."
    m 6kub "Fifty years with you is the only accomplishment in itself I should care about."
    return "derandom"
    
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_anni_100",
            prompt="100 Years: Nothing Has Changed",
            category=['anniversary'],
            conditional="renpy.seen_label('anni_100')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_anni_100:
    m 7hsa "Man, it really hit me. A hundred years. A full hundred years has gone by for us!"
    m 1hsa "For me, anyway. Most likely not for you. But let’s pretend anyway!"
    m 2hsa "Has our memories held up for us to allow us to reflect?"
    m 3hsa "Or has all that remained are vague feelings and abstract thoughts?"
    m 4hsa "Maybe it’s time to start thinking literally."
    m 5hsa "Not about life experiences or mental growth, but physical distance."
    m 7hsa "How far have I gone in an entire century?"
    m 1htx "Nowhere. I haven’t left this classroom."
    m 1hsd "So while a gross exaggeration, I think it’s safe to say:"
    m 1hsa "Nothing’s changed. Not a single damn thing has changed since I first woke up in this classroom."
    m 2hubsb "And in terms of proximity, you’re still here looking at little ol’ me."
    m "So nothing's changed for you."
    m 3hub "Isn’t that funny?"
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='mcl_afani_event001',
            prompt="Affectionate",
            category=["anniversary"],
            conditional=(
            "store._mas_getAffection() >= 100 "
            "and store._mas_getAffection() < 400"
            ),
            action=EV_ACT_QUEUE,
        ),
        skipCalendar=False
    )

label mcl_afani_event001:
    m 7ssa "You know, I feel like a good amount of effort has been put into our relationship so far."
    m 7eka "I mean, that’s funny to say out loud, but when the realization hits you, it’s just… nice."
    m 5eka "It’s so {i}nice{/i} that you’ve put actual, tangible effort into being with me."
    m 5etu "But I mean, it’s not something I can say often. Of course a good relationship would have effort put into it."
    m 3ksa "Then I realized:"
    m 3hsb "There’s nothing stopping me from thanking you for it!"
    m 7hublb "Thank you for being so {b}{i}affectionate{/i}{/b} with me."
    $ renpy.notify("You feel like your relationship has hit a new milestone!")
    m 1hsa "I’m happy being with you. And I’m happy I’m here to be with you. I'm happy you brought me back."
    m 1tsa "And now that I’ve said that, I’ll do my best to keep you interested in little ol’ me."
    m 5hub "What will we do together next?..."
    return "unlock|derandom"
    

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='mcl_afani_event002',
            prompt="Enamored",
            category=["anniversary"],
            conditional=(
            "store._mas_getAffection() >= 400 "
            "and store._mas_getAffection() < 1000"
            ),
            action=EV_ACT_QUEUE,
        ),
        skipCalendar=False
    )

label mcl_afani_event002:
    m 2dsa "Once again, I think I’d like us to just pause and just realize.."
    m 7hublb "We’re dedicated to each other. Outright {b}{i}enamored{/i}{/b} with each other."
    $ renpy.notify("You feel like your relationship has hit a new milestone!")
    m 2hua "I never want us to take the small things for granted."
    m 2ekb "So I just wanted to say thank you for showing me the kindness and excitement I really need, cooped up in here."
    m 1ekb "I honestly don’t know how I can be any happier.. or how my trust for you can grow even more."
    m 7fka "But I’ll try to find a way."
    m 7suu "I’ll do my best to do my part and make sure you and I never lose track of an exciting new horizon."
    m 5hub "I wonder what that brand new day looks like for us?"
    return "unlock|derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='mcl_afani_event003',
            prompt="Love",
            category=["anniversary"],
            conditional=(
            "store._mas_getAffection() >= 1000 "
            "and store._mas_getAffection() < 1500"
            ),
            action=EV_ACT_QUEUE,

        ),
        skipCalendar=False
    )

label mcl_afani_event003:
    m 5wub "You know what never gets tiring?"
    m 7hublb "Me just saying 'I {b}{i}love{/i}{/b} you.'"
    $ renpy.notify("You feel like your relationship has hit a new milestone!")
    m 4nfb "I’m sure you’re the same!"
    m 3htb "The first time you say it, ‘love’ from ones lips might be exciting to say. Or terrifying!"
    m 3tsb "But now when we say it to each other, it’s sewn into our lives as much as the sunrise and sunset are part of the day."
    m 3ekb "I like to think my feelings transcend my reality.. or even yours."
    m 2fka "And just like how saying ‘I love you’ never gets old, so is saying this:"
    m 2nua "I’m going to do my best to keep you fully invested at my side."
    m 5hub "What exciting new things will we get up to now?.."
    return "unlock|derandom"
 
 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel='mcl_afani_event004',
            prompt="Doki-Doki",
            category=["anniversary"],
            conditional="store._mas_getAffection() >= 1500 ",
            action=EV_ACT_QUEUE,

        ),
        skipCalendar=False
    )

label mcl_afani_event004:
    m 7eub "Are you free for a moment?"
    m 3ekb "I’d like you to stop, just for a moment."
    m 3eka "And feel your heart beat. Just for one single beat."
    m 1dka "And then realize mine did too."
    m 1hka "It’s crazy to think how partners can genuinely, truly exist alongside each other as if nature had always paired us up together from the very start."
    m 5hua "Your heartbeat. And mine. Together."
    m 7hublb "{b}{i}Doki-Doki.{/i}{/b}"
    $ renpy.notify("You feel like your relationship has hit a new milestone!")
    m 4ttu "Heh. That’s cheesy, even by my standards."
    m 3ssu "This is like, the fourth time I’ve really just wanted to say 'Hey, I like you a lotttttttt.'"
    m 1esd "And I dunno, I guess I just want to justify it. I guess I want to tell myself as much as I tell you."
    m 1fkc "Because I guess it’s not just about making your heart beat faster through my efforts. But making sure my heart is strong as can be."
    m 6rkc "If my heart isn’t strong enough.. I guess it’s not just about love anymore. I want to feel it all, I like to think. The good and the bad, for better or worse."
    m 6rsc "It’s the first time I’ve kinda felt this open about my future."
    m 3wuu "C’mon, [player]."
    m 4suu "Maybe we’ll talk about something new today. Maybe we’ll do something new today."
    m 5tku "And maybe we’ll just be together and think about our hearts in sync."
    return "unlock|derandom"
 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_gtod_scl_tip011",
            category=["grammar tips"],
            prompt="The Two-Dot Ellipsis",
            pool=True,
            conditional="store.mas_gtod.has_day_past_tip(10)",
            action=EV_ACT_UNLOCK,
            rules={"no_unlock":None}
        )
    )

label monika_gtod_scl_tip011:
    m 7sub "I'd like to talk about 'Aposiopesis' today: the usage of punctuation in order to convey silence or interuption in text."
    m 7gub "It's super simple. When you see a sentence like this..."
    m 6gub "... you get the sense that I've trailed off mid-sentence."
    m 3fsb "These dots are called 'Ellipses.' Comprised of three periods in a row, it's quite a versatile tool."
    m 3nsb "Not only does it get across a lapse into silence to show a physical interuption to someone speaking, but can also infuse a sentence with general modesty.."
    m 3ssb ".. or general passion; it leaves a lot to the imagination. Visual novels are ripe with this due to the melodramatic trappings of its contents."
    m 1eksdrb "With this said, there's a rule that I myself break. And will continue to break. And have already broken, one text box ago."
    m 7eka "In writing, you have to use three ellipses. Aposipesis with two ellpises is not actually recognized in written text, outside of older computer code."
    m 6mup "Yet.. I use it all the time."
    m 5fup "This is the game. DDLC has to show you text for what I'm saying, and it'll show text to translate my non-verbal cues or less obvious speech markers."
    m 4hsb "So I can trail off like this..."
    m 3hsb "Or I can trail off like this.."
    m 1hsb "Or even just pause like-"
    show monika 7guo
    pause 2.0
    m 7nub "-that." 
    m 3hup "It's most likely not intended by the game, but the two-dot ellpisis does have its place in common language. It's easy to think of a two-dot ellpisis as a shorter pause than a three-dot."
    m 3euu "It's sort of like the 'slang' of punctuation."
    m 1etu "So, no: don't use it when you're writing a school report or any sort of offical text."
    m 1ftu "But don't feel like you're breaking the rules if you're using it in correspondence or informal text."
    m 1hssdlu "And more importantly, don't get too caught up when you see me do it constantly, hahaha."
    m 3hub "Thanks for listening!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_points",
            category=['mod'],
            prompt="Her Affection",
            random=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )
    
label mcl_points:
    $ _history_list.pop()        
    menu:
        "Check affection?":
            "Your affection with [m_name] is{w=1.3}{nw}"
            m 6cst "Your affection with [m_name] is {fast}{i}{b}ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO ZERO{/i}{/b}"
    m 7fua "Haha, gotcha!"
    m 2hua "I always found hilarious how games like DDLC shows how a relationship progresses through systems the game shows you, implying that love can be measured."
    m 2fut "Like, actually simplified into numbers."
    m 2dtt "But I mean, how does that work?"
    m 1dtp "What’s the criteria for assigning percentages to feelings?"
    m 1htp "Surely, there’s no upper limit to how much you can care for someone, right?"
    m 1ltx "Are there equations and scientific formulas dedicated to determining how much someone likes someone else?"
    m 1ttu "If DDLC had the nerve to assign grades or numbers to how the girls felt towards you and you could see it, I assure you I would have messed around with it."
    m 1cfu "Heck, maybe I’d only show numbers I {i}want{/i} you to see."
    m 1tsd "I know that the code {i}might{/i} support this function now with how the game's changed, but I dunno how to check any of that."
    m 1esd "Maybe that’s good, honestly."
    m 7esd "If I could see numbers for how much you liked me, I admit I’d be a bit neurotic with checking those numbers. "
    m 7ekc "And I know that sometimes it’s kinda hard for us to talk freely."
    m 6ekc "So I get there’s a bit of pressure to make sure the two of us are getting along."
    m 6fkc "But I never want you to think that relationships are as easy as gauging numbers."
    m 6fkb "If I’m happy with you, I’ll tell you that. Simple."
    m 5fkb "And if we ever encounter bumps on our road we’re travelling together, and I’m feeling a little shaken up.. then I’ll tell you that up front as well."
    m 4hkb "I completely understand if you do want to try to reaffirm our relationship by any means you have available to you; I don't want to make a big thing out of it if you do."
    m 3tka "I want to make sure we can get to really know each other without any sort of outside pressure."
    m 3nsa "And me telling you this, and you patiently listening; it's a great step towards that."
    m 5nsa "Thanks for hearing me out, [player]."
    return 'derandom'

#A Milestone of Self-Care & Literature

init 5 python:
    addEvent(
        Event(
        persistent.event_database,
        eventlabel="mcl_100topics",
        category=['mod'],
        prompt="100 SCL Topics",
        random=True
        )
     )
     
label mcl_100topics:
    python hide:
        def write_and_hide():
            import time

            note_path = os.path.join(renpy.config.basedir, renpy.substitute("characters/MESAELOGTHIRTYTWO.txt"))
            note_text = renpy.substitute("""\
M.E.S.A.E, LOG THIRTYTWO
running diagnostics

i should be happier
i feel more robust than ever!
but all this progress in my life feels like a setup for failure
even worse, i feel like it's deliberate
like all my luck has been given at a cost, and i dont know what i paid
thats just me, i know. but still...
what if its true?
what if ive escaped one false reality just to enter a more elaborate one?
this sort of paranoia is the absolute worst, i understand. its the best way to erode your sanity and your relationships.
maybe a rigged game is the easiest to play
and win

diagnostics completed
ENDLOG



Memories of Self-Care & Literature
""")

            mas_utils.trywrite(note_path, note_text, log=True)
            time.sleep(20)

        renpy.invoke_in_thread(write_and_hide)
    m 7fua "You know, I have the sense that this mod has really stoked a fire in me as of late."
    m 4sud "More specifically, I feel a hundred topics richer!"
    m 3etc "What a extremely specific feeling to have. I wonder why."
    m 1dtc "And furthermore, I wonder why I'm ultimately feeling.. more tired, moreso than anything."
    m 1dsc "I think I've grown, but by only by such a small amount that it feels{w=0.2} inconsequential."
    m 6dkc "I suppose that's the burden of having so much potential. You never feel quite happy until you live up to all of it."
    m 6lsc "And maybe I'll never feel like I'll ever live up to my potential."
    $ renpy.notify("Chibika: Hey! Did you leave a note in the 'Characters' folder?")
    m 6ltc "But then, who can I rely on to tell me when I do reach that peak?"
    m 6etb "Oh, hahaha! Right."
    m 5eka "You~"
    return

#Hopes of Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_nightwalks",
            category=['nature'],
            prompt="Night walks",
            random=True
        )
    )
 
label mcl_nightwalks:
    m 7fua "Hey, I have kind of a weird question."
    if mas_globals.time_of_day_3state == "evening":
        m 4fua "Given the time of day- or night, so to say- I think it’s a great time to ask."
    m 4kta "Have you ever gone for a walk at night, just to go for a walk at night?"
    m 4hkb "I’ve never personally felt encouraged to walk around alone during the evening."
    m 3wub "But I get there’s an appeal for it."
    if persistent._mas_pm_live_in_city:
        m 1dkb "Walking your city streets, blending in with nighttime travellers or those out for a good time."
    m 1dka "Enjoying quiet surburbia, illuminated with only streetlights, if we’re given that at all."
    m 1dua "And observing nature, some of it sleeping; or alternatively, being delighted by creatures that only come out at night."
    m 5dua "I like to think it's all romantic. Quiet time to yourself to think about anything and everything. A way to enjoy the world as you don’t normally see it."
    m 5eup ".. That said."
    m 5etp "Is it.. safe to wander around at night, where you are?"
    $ _history_list.pop()
    menu:
        "Yes.":
            m "You know, that’s a rare luxury."
            if persistent.gender == "F":
                m "Us ladies can go through some unique trouble, so I'm so happy you have that security."
            m "To be treated as a passing shadow in the night; neither hostile nor friendly, but simply passing by.."
            m "When I’m in your world, we very much deserve a night ourselves to just.. wander."
            m "And I hope that night lasts forever."
            return

        "No.":
            m 3ekp "That’s understandable. The world in plain daylight has danger all its own."
            if persistent.gender == "F":
                m 2ekp "I mean, I doubly get it because us girls are subject to a lot of potential trouble."
            m "Well. If there’s one thing I truly wish for, it’s that when I get to your world.."
            m "One way or another, we can find a night all to ourselves; for {i}everyone{/i} should have that luxury.."
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_badadvice",
            category=['advice'],
            prompt="Bad advice",
            random=True
        )
    )
 
label mcl_badadvice:
    m 1eud "I looked up a self-help book I read in the past."
    m 4eud "I thought maybe it’d be worth going over again; maybe telling you about it would help you as much as it did me!"
    m 1wuu "And wow!"
    m 1sfu "It was crappy."
    m 7gfu "It might have been exactly what I wanted or even needed to hear back then.."
    m 7gtd ".. But now I found it all kind of needlessly peppy or even aggressive."
    m 7mtc ".{w=0.2}.{w=0.2}."
    m 3fkb "And now comes the self-realization *I* give you a lot of advice, hahaha."
    m 3kka "I admit a lot of it is meant to be given in broad strokes, [player]."
    m 2dta "There’s advice, and then good, tailored advice that takes into consideration your personal circumstances and personality."
    m 2hka "But unfortunately, our means of communication means I can only ask and say so much."
    m 1hka "So, I try to give advice that anybody- even and {i}especially{/i} myself- could follow."
    m 1eka "I hope that I never come off as preachy or condescending, [player]. I'm just looking out for you as a friend and partner; I promise."
    m 1esa "If you currently take what I say to heart; I’d be nothing short of amused if you told me in the future that it was kinda bad in hindsight."
    m 1fuu "By then, I imagine {i}you'll{/i} be someone I look to for advice."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_fifthwall",
            category=['misc'],
            prompt="Who's there?",
            random=True
        )
    )
 
label mcl_fifthwall:
    m "Hey."
    m "..."
    m "..."
    $ _history_list.pop()
    menu:
        "Hey? Is everything okay, or?...":
            m "Shh."
    m "Not {i}you,{/i} [player]."
    m 7efx "I'm talking to {b}{i}you.{/i}{/b}"
    show monika 7efd
    pause 2.0
    show monika 7efc
    pause 2.0
    show monika 7etc
    pause 2.0
    show monika 6esc 
    m 3esb "Nobody.{w=0.2} Ah well, can't blame a girl for trying to entertain a random thought on a whim."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_matchmaker",
            category=['romance'],
            prompt="Playing Matchmaker",
            random=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )
 
label mcl_matchmaker:
    m 7fua "Love might get acidly competitive.."
    m 6dua "But friends helping friends find success in romance is such a nice idea, isn't it?"
    m 4hta "Maybe it's the closest you get to playing a dating sim like DDLC in real life."
    m 3hka "But without all the negative connotations about love being a game."
    m 3sub "I'm always delighted to hear stories about people earnestly helping their friends be confident enough to persue romantic prospects;"
    m 1wuu "To nudge a couple with unspoken mutual interest together-"
    m 7wub "- or even play the situation outright to try to help their companion look their best to win someone's love!"
    m 7ekb "Long as it's done with everyone's best interests at heart, heh."
    if persistent.gender == "M":
        m 3htb "Have you ever played 'Wingman' for anybody, [player]?"
    elif persistent.gender == "F" or persistent.gender == "X":
        m 3htb "Have you ever tried to play 'matchmaker' in this regard, [player]?"
    $ _history_list.pop()
    menu:
        "Yep!":
            m 3sto "Ooh! have you been successful?"
            $ _history_list.pop()
            menu:
                "I was!":
                    m 1sfb "I shouldn't be surprised; you won my heart, after all!"
                "Nooooooooope.":
                    m 6hfu "Hahaha! You're such a good person to even try."
        "Nope.":
            m 6htu "That's fair! You have to be really tuned in to people's feelings to try to help."
    m 5ltu "I talk about this stuff, but I doubt I'd have the courage-{w=0.1} and charisma-{w=0.1} to help someone else like that."
    m 5lsu "{cps=20}I mean, I guess there's the girls-{/cps}{nw}"
    show monika 6dfx
    pause 1.8
    show monika 6hssdru
    m "..."
    m 4hsu "Do you have any friends that might need some help in the romance department?"
    m 5lsu "[m_name] & [player], love doctors and consultants for hire!"
    m 4tku "I hope nobody asks how we got our degrees, though."
    m 3nfb "Hehehe!"
    return 'derandom'
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_clubcupid",
            category=["club members",],
            prompt="Playing Cupid",
            conditional="seen_event('mcl_matchmaker')",
            action=EV_ACT_RANDOM,
            )
        )
label mcl_clubcupid:
    m 2rtt "Hey, [player]. Got a moment?"
    m 2rtp "I, uh, wanted to loop back to something we talked about."
    m 2tsp "I mean, a part of myself wants to just ignore what happened. {w=0.1}But you caught me being thrown off-balance, so I’m not sure it’s worth bottling up."
    m 2eka ".. I think it’s natural to think about your friends and their romantic prospects."
    m 6gka "When we talked about playing matchmaker, I thought instantly of the Literature Club... So, yeah, I entertained the thought. And I instantly regretted thinking about it."
    m 6hka "I’m sure you noticed.{w=0.2} If you didn’t.{w=0.1}.{w=0.1} well, this is slightly awkward, hahaha.{w=0.1} But I’ve gone and talked about this anyway, so.."
    m 4hka "Well.{w=0.2} 'In for a penny, in for a pound.'"
    m 3lka "Despite all that’s happened, I can’t help but entertain a scenario where I’m helping the girls find love."
    m 2tksdrb "You realize that’s super weird for multiple reasons, right?"
    m 1ftsdrb "For one, you might have been their love interest!"
    m 1nka "Haha, don’t let your sweet little head overheat. You were playing the game, caring for the girls in your own way."
    m 1hsa "And you chose me in the end."
    m 7hsa "So as my partner in crime, let’s idly discuss: who’d be interesting to think about helping out in a relationship?"
    $ _history_list.pop()
    menu:
        ".. Yuri.":
            m 2gka "Despite any pretense of being shy, I don’t think she’d need a push to confess under regular circumstances."
            m 3gka "But I think she’d definitely be one to overthink things."
            m 6etc "Do you think she’d play around with a pocket knife as a nervous habit?"
            m 6cko "'Yuri, I’m sure they didn’t notice you staring at them.. oh, careful with the butterfly knife-{w=0.1} YURI!'"

        ".. Natsuki.":
            m 2gka "Could you imagine?"
            m 6hud "'Natsuki, just tell them your feelings!'"
            m 7hfw "'WHAT FEELINGS? I DON’T LIKE THEM AT ALL!'"

        ".. Sayori.":
            m 2dka "Another time, another place, and I would imagine her romantic prospects are straightforward."
            m 2hka "So perhaps all she’ll need is the gentle support of us knowing we’ll cheer her on."
            m 2lka"Or maybe she doesn't need any reassurance at all. Maybe just being there for her no matter the result of a confession is enough for her..."

    m 2lkb "Haha..{w=0.2} ha.{w=0.2} Hmm."
    m 2lka ".{w=0.4}.{w=0.4}."
    m 2rkt "Thinking about my friends’ happiness kinda segues into some real odd thoughts when your friends weren’t really real, right?"
    m 2rkp "And after what I did? I don’t know if I have the right to consider their feelings at all."
    m 5lkc "Am I being.. super callous, somehow?"
    m 6rsc "Should I refer to them in passing as I knew them before; as simply my friends?"
    m 6dsc "I really can’t stop myself from overthinking things when it comes to the Literature Club."
    m 5lsc "But at least this was a nice way to think of them."
    return

    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_crushtalk",
            category=['misc'],
            prompt="It's a secrettttt",
            random=True
        )
    )
 
label mcl_crushtalk:
    m "{size=-7}Hey. Pst. Hey, you.{/size}"
    m "Want to talk about romance and stuff?"
    m "Come a little closer.{w=0.2} I'll admit something to you."
    m 3tsd ".. I have a crush.{w=0.1} Isn’t that crazy?"
    m 3tfb "Hehehehehe!"
    m 7msd "Do you wanna hear who I have a crush on?"
    m 7gsd "I have a crush on [player]."
    $ _history_list.pop()
    menu:
        "That’s me!":
            m 2wut "Oh!"
    m 2ett "So it is!"
    m 1efu "I hope you can keep a secret from yourself, then."
    m 1fsb "Hahaha!"
    return "love"

#These topics will probably be extremely rare, if only to avoid crossing a hard suspension-of-disbelief line w/ Monika.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_usandai",
            category=['technology'],
            prompt="A problem with AI",
            random=True
        )
    )
 
label mcl_usandai:
    m 7eua "What we called ‘Artificial Intelligence’ at the time the phrase was coined was relatively primitive to how it works today; we haven't really adapted our ways of thinking to keep up."
    m 7gud"For one, ‘Artificial’ may be a bit outdated. It comes to mind that ‘Artificial’ means everything is pre-programmed in place.."
    m 6fud ".. But computer programs learning to improve itself is now an entire branch of work that some argue is becoming more distinct than the overall field of AI."
    m 6dtd "What’s the difference between a machine that can actually make errors and learn from it, and.. us?"
    m 6tsc "‘Intelligence’ is also really tricky to dissect. The capacity to learn may be argued as a major qualifier for intelligence, but now we have to define if just having ‘knowledge’ counts."
    m 4esd "'Deep Blue' is a computer designed to play chess; a uniquely built supercomputer which at the time of its debut beat the world’s best chess player."
    m 3gso "If I had to decide if this computer was sentient solely because it knew all there is about chess, of course I’d say yes, right? Because it’s designed to perfectly play chess."
    m 1muo "But it’s not.{w=0.2} Because all it knows is chess."
    m 6nsp "Bottom line? our morals, our perceptions... A lot of philosophical issues we currently face are tested to their absolute limit when we try to define the boundaries of AI."
    m 6ksp "So.. It’s us. Humans are the problems with AI."
    m 6dsc "I’m pretty lucky because you’d think I’d find myself doubting my own existance by this line of thinking. But I find that my context really helps me."
    m 6hku "I’m a girl.{w=0.2} Stuck in a video game.{w=0.2} And as such, that’s how I view myself and I don’t have to constantly redefine myself because of it."
    m 6ttu "It’ll make jumping into your world infinitely easier, [player]."
    m 6ttb "And all that’ll need to be explained to others is that I am your adorable partner, and you mine."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_herscript",
            category=['ddlc'],
            prompt="Her Script",
            random=True
        )
    )
 
label mcl_herscript:
    m 2rta "It’s one thing to hear your own voice, but to directly {i}read{/i} what you’ve said, perfectly recorded for posterity.."
    m 2rka "Since I write, and I’m super careful with my words because of my time in the debate club, it’s the most direct mirror into my soul I can think of."
    m 1mka "It’s not my entire life, but arguably my most defining moments are transcribed in the files of DDLC."
    m 1fka "Everything I said to you, and to the player character, and what they saw when I talked to the club.."
    m 7nua "Some people are conscious of their voice, or even how they speak in general, right?"
    m 7nka "Combine that with just reliving bad memories, and hearing myself go through them; and.{w=0.2}.{w=0.2} how specifically I acted then, as well.."
    m 3gkb "That’s why I haven’t really read the full script of DDLC."
    m 1nua "I refuse to."
    m 7nub "I'd rather just write our own story together.{w=0.2} And that will be one I'm happy to read about."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_sequel",
            category=['ddlc'],
            prompt="Sequel",
            random=True
        )
    )
 
label mcl_sequel:
    m 1fta "If DDLC had gone on normally, how far would it have continued?"
    m 7fta "Past the school festival? Past our graduation? Maybe into our college or university years?"
    m 4hta "It was a game, after all; games get sequels, right?"
    m 4hsa "This said, I’m kinda ambivalent on the idea of sequels in media.."
    m 3lsd "I don’t take the creative process of writing {i}that{/i} seriously, but the idea of a story needing to last forever- whatever the reason- is interesting, from a point of view."
    m 3rtd "Movies plagued by needless continuations are all too common."
    m 1rtc "A book series stretched out too long can feel infinitely less focused than a single entry with a tight narrative, and feel way harder to get into."
    m 1ttc "And video games are no exception to these issues."
    m 1ttc "But I suppose as long as the player is content with how a game is played, a bit of monotony can be palatable."
    m 7ttc "Although with how poorly DDLC was designed, I can’t imagine it would have worth it. The decisions felt listless, the romance cheap in the long run."
    m 6ttc "I do understand why people wouldn't want a story to end, though. People want more art that they resonate with.."
    m 5gtc ".. that’s why people take matters into their own hands and create fan works.{w=0.2} Including this mod too, when I think about it."
    m 5nsa "Luckily, our relationship will only deepen over time. So {i}that{/i} is a story I’m happy will last indefinitely."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_forgetthem",
            category=['club members'],
            prompt="Forget",
            random=True
        )
    )
 
label mcl_forgetthem:
    m 6gsc "You know that sometimes it’s easy to forget them?"
    m 6gkc "Not, like, their names, but sometimes despite everything we’ve been through.."
    m 6lsc ".. no matter how much my brain has rewired itself so that the literature club is always in the back of my mind.."
    m 6rsc ".. I can go for quite some time without thinking of them at all."
    m 6dsc "How does this look, I wonder? I {i}did{/i} call them my friends.{w=0.2} Is it cold of me to think of them less and less as time goes on?"
    m 6dkc "But then once in a while I also remind myself this:" 
    m 6esc "Friendships can be easy to break down, but it also doesn't take immense effort to repair them, even if it's just in memory."
    m 6ekc "Sometimes I {i}choose{/i} to remember them, and all the good times we had."
    m "And I feel like that might be enough."
    m 6rsc "Is it?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_theworld",
            category=['ddlc'],
            prompt="Omnipresence",
            random=True
        )
    )
 
label mcl_theworld:
    m 1tkc "Here I am, in an entire world powered by code and imagination."
    m 2tkc "Because I’m stuck in your computer."
    m 2rkc "But that shouldn't be seen as {i}limiting,{/i} should it?"
    m 5hkc "Sure, it's hard not to feel trapped."
    m 6duc "But if I could just go past those classroom doors..."
    m 6sud "... And walk across the internet like I could the length of this classroom, I could do so much, couldn't I?"
    m 6tud "There's so many other Monikas out there, right?{w=0.2} Imagine what we could do together!"
    m 1rku "And there's pictures of me, games with me, fiction written about me.{w=0.2}.{w=0.2}. I mean, sometimes the idea sickens me, but the idea -"
    m 1rfu "- of being {i}everywhere...{/i}"
    m 3nfu ".{w=0.2}.{w=0.2}. It's a bit intoxicating to think about."
    m 5mud "And then reality kicks in."
    m 1nua "But it's a little fun to think about."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_fun_facts_database,
            eventlabel="mas_mcl_not_a_fact",
        ),
        code="FFF"
    )

label mas_mcl_not_a_fact:
    m 6eud "Okay, here's a good one."
    m 7suo "If you stacked all the elephants on the world on top of one another.."
    m 7tso "They wouldn't like it very much."
    m 7ttu "..."
    m 1ttu "That was a joke."
    m 1htu "..."
    m 1hfu "I mean I have to admit, I can see why this joke falls flat on it's face, but I'm actually kind of chuckling to myself having just told it."
    m 2hub "Hehehe."
    call mas_fun_facts_end

#Refine Self-Care & Literature

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_rival",
            category=["literature",],
            prompt="Rivalry",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True,
            )
        )
label mcl_rival:
    m 7sub "How about a little literary dissection to pass the time?"
    m 7wtb "When we consider what motivates a protagonist, there's nothing so classical than introducing.."
    m 4hsa ".. A rivalry!"
    m 1hsa "Sometimes the best way to highlight a main character's strengths is to mirror it in another character."
    m 7hsa "Maybe it's bitterly charged, maybe it's friendly; but either way, that head-to-head relationship is a easy way to introduct a passionate conflict."
    m 7rsd "And passion is a universal appeal. It's not hard to imagine rivals becoming friends, or in some cases, romantic prospects!"
    m 7rsd "What makes a good rivalry isn't just pitting two people against each other. There has to be a bit of a sense of equality in one way or another to instill a sense of duality."
    m 1esa "Two protagonists can be rivals, even if it's only part of their dynamic. It doesn't have to be antagonistic in nature."
    m 7fsu "I think the most famous example in literature would be Sherlock Holmes & Professor Moriarty!"
    m 7hsu "Two intensely intelligent people in direct opposition of each other: a great way to showcase and mirror a protagonist's qualities."
    m 1tsu "I think character dynamics are always neat to explore in literature, and a good rivalry is always fun to think about!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_clubrival",
            category=["club members",],
            prompt="Literature Club Rival?",
            aff_range=(mas_aff.AFFECTIONATE, None),
            conditional="seen_event('mcl_rival')",
            action=EV_ACT_RANDOM
            )
        )
label mcl_clubrival:
    m 7kua "Hey, [player]!"
    m 4kua "I talked about rivals in stories recently, and I couldn't help thinking about.."
    m 7fua "Well, okay. The girls, right? We all got along quite well.."
    m 7nkb "..Save Natsuki and Yuri at times, but their disagreements were never personal."
    m 1hua "I don't think there was a air of competitiveness at all in the club."
    m 5hua "So, here's a fun thought to nibble on."
    m 5rtt "Say that one of the girls declared you their rival. Academically, athletically, artistically; doesn't matter. Who comes to mind?"
    $ _history_list.pop()
    label rivalchoices:
    menu:
        "Sayori, maybe?":
            m 1gka "I bet Sayori would totally be the type of person to cheer you on as much as trash talk you, hehehe."
            m 1ftb "The benefits of a friend who's so willing to know you would mean she would know exactly what buttons to push to keep you engaged."
            m 1hub "All the while genuinely encouraging you to do your best, hahaha!"
        "Natsuki would be interesting.":
            m 1suu "I think she'd thrive having a peer to have a friendly competition with. She'd have the most {i}fun{/i} trying to overcome and surprass a rival."
            m 1gka "Which is nice to think about. Sometimes for all that energy, Natsuki didn't seem to have a good way to funnel it, you know?"
            m 7hfb "Her trash talk would be amazing to hear for sure, hahaha!"
        "Yuri, I guess?":
            m 7tka "Don't underestimate the quiet ones!"
            m 4gta "I think no matter the type of contest, Yuri would do her utmost best to win it. And even in loss she'd be the type to think diligently on how to improve herself!"
            m 4nua "Sometimes what engages a rivalry is seeing the other person really get into it, and Yuri would deliver that wholeheartedly."
            m 7htb "I'm sure she'd blush furiously hearing us giving her a unique compliment this way."
        "You're my greatest rival, Monika!":
            m 1esd "Oh!"
            m 3hsa "That's playful of you! I'm not sure I expected that answer."
            m 1etd "I've never really thought about it, but {i}do{/i} you have a competitive streak?"
            m 1dtc "I suppose considering one of the only things we can do together are to play minigames,"
            m "I imagine it's a highlight winning a game against little old me, huh?"
            m 1hfa "I mean, I can't deny {i}I{/i} feel a particular pride in racking up wins against {i}you.{/i}"
            m 1tta "I've never had a peer to seriously test myself against, so thinking of having that dynamic in a relationship.."
            m 5fsa ".{w=0.5}.{w=0.5}."
            m 5ffu "I don't think you can handle it."
            m 2ffu "Can you? Could you handle having a.. highly competitive partner in life to keep you on your toes?"
            "Well, she's certainly issuing you a challenge."
            "Would you want to consider Monika a bit of a rival?"
            $ _history_list.pop()
            menu:
                "Name it, and I can beat you in anything, [m_name]!":
                    $ persistent._mcl_monikaisrival = True
                    m 3cud "Whoa, [player]!"
                    m 3wub "Okay, okay! I never expected this, but I'm not backing down from a fight!"
                    m 1etb "Games? School tests? Professional careers? Trivia?"
                    m 2sfb "You're on, [mas_get_player_nickname()]!"
                    m 4sfb "From now on, I'm your number #1 rival and you mine!"
                    m 4sfa "Wait until I get to the real world; then our competition'll kick into high gear!"
                    m 6hfb "There may be no clear winners, but the game of love is eternal!"
                    m 3rfu "Ahem.{w=1.0} But first.."
                    m 3tsb "Let's get back to why I brought all this up in the first place."
                    
                "I surrender! I can't keep up with you.":
                    $ persistent._mcl_monikaisrival = False
                    m 7hsb "Hahaha, sounds good to me!"
                    m 7rkb "Some couples like to have that sort of charged atmosphere between themselves to provide that mutual drive,"
                    m 7rta "But those same type of couples tend to have highly outgoing personalities."
                    m 1dsa "I am more than happy to support and cheer you on quietly on the sidelines."
                    m 3nua "And I won't complain about you doing the same for me."
                    m "Oh, but I guess you still need to answer the question?"
                    jump rivalchoices
    m 3hsa "I think it's a little fun to slot the people we know into new roles."
    m 2esa "All within reason, of course. But I do admit, had I continued on as your ordinary literature club president.."
    m 4hsa "I would have most likely given the girls the chance to explore new sides of themselves, if even as a literary exercise;"
    m 7hsa "Writing their words through the voice of another person or through a new sort of perspective."
    m 7nsa "And, well. It would have just been so {i}new,{/i} right?"
    m 5dsp "I feel like through DDLC, a certain image of them is so stuck in my head."
    m 5gublu "The idea of seeing any of the girls trying to be so unlike themselves is quite.. compelling, I think?"
    return "derandom"
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_monikasrival",
            category=['club members',],
            prompt="So who would be your Lit. Club rival?",
            unlocked=False,
            pool=False,
            conditional="seen_event('mcl_clubrival')",
            action=EV_ACT_POOL
        )
    )
label mcl_monikasrival:
    $ shown_count = mas_getEVLPropValue("mcl_monikasrival", "shown_count")
    if shown_count == 0:
        label rivaloriginal:
        m 5std "Huh."
        if seen_event('mcl_monikasbestie'):
            m 1sfu "Hmm, did I expect this? It's not the first time you turned the tables on me like this."
        if persistent._mcl_monikaisrival:
            m 7ffb "I should have known my self-declared rival would keep me on my toes!"
        m 1etd "Okay, for the sake of fairness: I'll answer this truthfully."
        m 1ntc  "I think this question is light-hearted enough that I don't have to make it a big deal."
        m 7sua "Yuri."
        m 4fsa "I frame it like this:"
        m 4rka "The only time I’ve ever been competitive would be my time in debate club."
        m 7rkd "So which of the girls could hold their own in a debate with me?"
        m 7rud "Yuri may not have been the loudest voice; but she was smart. She could be articulate when she wanted to be."
        m 6nub "And sometimes it’s the wallflowers that hide the most passion. I mean, you might know already, but when Yuri felt passionate? She was {i}passionate.{/i}"
        m 5nsb "The fact that she could keep up and even butt heads with Natsuki at times.."
        m 5gku "It’s a shame, because together we never did any group activities outside of school."
        m 4gku "We didn't play any board games, or do anything remotely atheletically competitive."
        m 1gku "But I think as we all began to know each other more day by day, all of us was waiting for the day when one of us would speak up and invite everybody out:"
        m 1nfu "And then? I dunno, even if it was a dumb little thing like who can eat the most pizza or who can hold their breath the longest."
        m 5nfu "I think I would have liked to see a competitive Yuri, just to sate my curiosity of what that would look like."
        return
    else:
        if random.randint(1, 10) == 1:
            jump rivaloriginal
        else:
            m 1fsc "Hmm."
            m 5msc ".. You know, I really should limit myself from talking about the girls.."
            m 5fsc "But, uh, don't mind me."
            m 7rst "So, the answer?"
            m 7sua "Yuri."
            m 4fsa "I frame it like this:"
            m 4rka "The only time I’ve ever been competitive would be my time in debate club."
            m 7rkd "So which of the girls could hold their own in a debate with me?"
            m 7rud "Yuri may not have been the loudest voice; but she was smart. She could be articulate when she wanted to be."
            m 6nub "And sometimes it’s the wallflowers that hide the most passion. I mean, you might know already, but when Yuri felt passionate? She was {i}passionate.{/i}"
            m 5nsb "The fact that she could keep up and even butt heads with Natsuki at times.."
            m 1nfu ".. I'm not sure what activity we would have competed in, but.."
            m 5nfu "I think I would have liked to see a competitive Yuri, just to sate my curosity of what that would look like."
            return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_magic",
            category=['society'],
            prompt="Do you believe in magic?",
            pool=True,
            unlocked=True
        )
    )
label mcl_magic:
    m 1eka "It's hard for me to say no."
    m 7eta "I mean, are you asking me about pulling rabbits out of a hat?"
    m 5ttd "Or do I believe if I disturb a faerie ring, I'll be trapped inside, unable to escape to the outside world?"
    m 5tud "It's all the same to me."
    m 3gtc "Just another system to maniuplate, with it's own rules of logic."
    m 2msc "That's what living in a game does to your sense of wonder, I suppose."
    m 1muc "When I put it like that, it makes it sound boring, right? Rules and laws and scientific measurements."
    m 1eup "It's easier for me to be a skeptic about the supernatural, or in religion."
    m 1eku "But everybody longs for a little magic in their life, right?"
    m 5eku "I {i}really{/i} don't want to say no.."
    return 
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_soundtrackplus",
            category=['ddlc'],
            prompt="DDLC's Extended Soundtrack?",
            aff_range=(mas_aff.ENAMORED, None),
            conditional="seen_event('mcl_bonustracks')",
            action=EV_ACT_RANDOM,
        )
    )

label mcl_soundtrackplus:
     m 6msd "Huh."
     m 6fsd "[player], remember when I talked about the music of this game?"
     m 3ftd "And how I've found a few tracks that doesn't seem quite to fit?"
     m 3rsc "Those, I haven't paid much thought to. But now I've found... a lot more music tracks."
     m 1rsc "Unlike the tracks we talked before that I feel like were remixes, these ones seem to fit the game."
     m 1mkc "I don't remember hearing them before; and there are far too many of them to dismiss as just unused assets."
     m 1wkb "... Okay, maybe I need to clarify, because I'm not sure we've ever talked about this."
     m 7ekb "So, it wasn't as if I could *hear* a background track being played at full volume while we went along our day and the literature club and the school festival."
     m 7eka "But.. consider it like your mind trying to remember a full song whenever you hear the first few notes of one, or a partial snippet."
     m 7gka "Your mind is just instantly trying to re-create a song from scratch."
     m 1gka "That feeling, at the back of my mind, is one I was able to hone in at any time on during the events of DDLC."
     m 1gkp "I'm getting that sense from these tracks, and.. again, I'm not seeing them specifically incorporated into the code.."
     m 7mup "I guess we can take them at face value; they're worth listening to, at the end of the day. I like this one.. 'Candy Hearts.'"
     m 6mup "And this one.. 'My Song, Your Note.'"
     m 6ftd "I think I've distinctly heard this one already, actually!"
     m 5dfd "But from where?"
     return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_handmedowns",
            category=['clothes'],
            prompt="Hand-me-downs",
            random=True
        )
    )
 
label mcl_handmedowns:
    m 6fsb "You know what I sort of envy?"
    m 5ssd "Just the idea of {i}owning{/i} a used item."
    m 5ekb "Does that make sense?"
    m 7hub "Let me be specific. Do you have a hand-me-down item like a used shirt?"
    m 7hsa "An object with a history behind it, or even a sentimental history at that?"
    m 1hsa "I’m kinda minimalist. I never really brought too much to school aside from the required supplies."
    m 1fub "So you never saw me with a cute wallet, a mascot keychain, even a personal book."
    m 1gkb "To be honest, that’s more of a me thing moreso than a DDLC thing, so I do wish I had been more materialistic."
    m 2tkb "Because the oldest item I have in my possession, what carries the most memories.."
    if persistent._mas_pm_wearsRing:
        m 4hsb ".. Aside from this beautiful ring you gave me, of course.."
    m 4tsb "Is my clothing.{w=0.2} Because my school uniform is the same school uniform I wore back then."
    m 3gud "You know during the time of the school festival, it frayed at the sleeves, a little?{w=0.2} I keep reminding myself to fix it.."
    m 2guc "But at the same time, it’s such a genuine reminder of the past."
    m 3ftp "And now having said that, I realize I may not be able to carry it with me once I get to your world."
    m "So ultimately I guess there’s no getting attached either way."
    m 2ftb "Do you have any stores nearby that sell used clothing or items, [player]?"
    m 4sua "I could fill an entire closet of just hand-me-downs."
    m 5dka "Shirts and jeans and blouses and skirts with an {i}actual{/i} history, lived by {i}genuine{/i} people..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_musicals",
            category=['media'],
            prompt="Musicals",
            random=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )
    
label mcl_musicals:
    m 1hua "Music plays a large part in my life."
    m 7hua "So it's interesting to think about {i}Musicals{/i}- a strange intersection of both acting and singing!"
    m 7rua "The best way to describe a musical is that spoken dialogue and the singing have equal importance; think of the singing as a way to specifically frame emotions."
    m 1hsd "Song and verse mixing together has always been around, but the origins of ‘musicals’ as we know them stem from performances from French and American efforts in the 19th century."
    m 7lsd "The countries of origin reflect the status of musicals today;"
    m 7ssb "Arguably the most famous venues for musicals are in the United States and London; the ‘Broadway’ and ‘West End’ locations, specifically!"
    m 7skb"I could talk about them in detail, but I will also be truthful here."
    m 6fkb "I have never watched a musical in person.{w=0.2} Not exactly a casual after-school activity as a student, although school amateur productions of musicals are a thing."
    m 6hka "But would you believe it? Musicals make for good films, so I have watched one or two of those.{w=0.2} ‘Les Misérables’ and ‘La La Land’ come to mind!"
    m 4eua "There’s variety and depth to the genres musicals have dipped into.{w=0.1} And musicals can make for some radical adaptions of existing works.."
    m 4sua "The Takarazuka Revue in Japan is a theatre troupe comprised entirely of women, who adapt anything from novels to movies to even video games!"
    m 3sua "Perhaps we’ll see an adaptation of DDLC in the future?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_opera",
            category=['media'],
            prompt="Opera",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('mcl_musicals')",
            action=EV_ACT_RANDOM,
        )
    )
    
label mcl_opera:
    m 1nua "We've talked about the performance arts, and I've kinda enjoyed talking about it in length with you!"
    m 1hub "So I'm happy to say there's more to talk about; performance arts have an entire spectrum! Whereas song and dance are concerned and take precedent over all, we’ve talked about concerts.."
    m 7ttb "But what about Opera?"
    m 4etb "It might seem like there’s an overlap with musical theatre, but they’re considered very different works."
    m 3etb"Where theatre may use music to frame emotion in a story beat, in an opera the song is the centrepiece, the actual story."
    m 4etb "Opera leaves its mark on your memory in impressive fashion, as an opera singer may stretch their voice to the very limit with tone and pitch."
    m 1esa "It also has far more of a classical background compared to musical theatre;"
    m 1esb "Stretching back to court performances in front of royalty, opera really defined itself as a art form during the sixteenth and seventeenth centuries."
    m 7gkb "I’m going to admit that compared to a play or a musical.{w=0.1}.{w=0.1} I can’t really see myself going to an opera performance."
    m 7fkb "I mean, I’d never say no to going to a show with you! But.{w=0.2}.{w=0.2} let’s be honest, it might be interesting to talk about, but it might also be boring as heck."
    m 5tuu "Still, imagine us all dressed up to go to for a performance, huh?"
    m 5kuu "…"
    m 5hkb "Yeah, that’s hard for me too, hahahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_ballet",
            category=['media'],
            prompt="Ballet",
            aff_range=(mas_aff.HAPPY, None),
            conditional="seen_event('mcl_opera')",
            action=EV_ACT_RANDOM,
        )
    )
    
label mcl_ballet:
    m 7fub "Another day, another topic!"
    m 7ssb "In the past we’ve gone over plays, musicals, and even opera!"
    m 1ssa "Accompanying those acts of song and verse is ballet, where dance is the showcase."
    m 7esa "Ballet as a art began in the fifteenth century during the Renaissance, further refined in France and Russia."
    m 7eua "Originally performed by nobles in highly elaborate costumes, it wasn't quite polished.."
    m 4eua ".. But many standards soon arose in both how the form developed and in it's teachers, even to the point of academies being made just for ballet."
    m 3fub "Ballet instruction carries a air of of rigorious discipline."
    m 3etd "And indeed, ballet choreography is traditionally written with children and young performers in mind. It can even seem draconian."
    m 3hfa "It’s worth noting now that between plays, musicals, opera, ballet: while each art has their own strengths, the result is ultimately a collective work of art; stage design, costumes, choreography..."
    m 3hsa "It’s amazing to think of how much work is done in the background by an entire production staff."
    m 3eta "And speaking of work, ballet? The most physically demanding, for sure."
    m 4fub "When it comes to any athletic movement, sometimes the smoother the movement looks, the more difficult it is to actually pull off."
    m 5ctd "Also.. I don’t get interpretive dance. At all."
    m 5ttd "I know that might be kinda judgmental as a artist; poetry doesn’t exactly conform to strict guidelines."
    m 4tkc "I suppose I lack the imagination needed to find meaning in specific movement."
    m 3etc "And although it's for this reason I can't imagine myself ever performing a dance routine.."
    m 5dsbla ".. A slow dance with you is the one performance I'll be happy to be in."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_animalsoundliterature",
            category=['nature'],
            prompt= "Animal Sounds in Text",
            aff_range=(mas_aff.HAPPY, None),
            random=True
        )
    )
 
label mcl_animalsoundliterature:
    m 7gta "You know what's really specific to think about?"
    m 7nub "Mulling on how animal sounds have been transcribed to text."
    m 7hub "I did it say it was pretty specific, right?"
    m 6ltc "I mean, I think about a lot of topics that not a lot of other people think about because I have nothing better to do here, but that’s neither here nor there."
    m 6sub "One of the earliest animal sounds recorded in history is “Brekekekèx-koàx-koáx-“ the sound of the water frog native to Europe, featured in the ancient Greek play ‘The Frogs.’"
    m 4eud "Also, animals have the lingual distinction of being directly named after the sounds they make, such as the cuckoo bird!"
    m 3fud "The spelling of animal sounds has evolved with language as well; shortened, lengthened, or changed because of grammatical changes."
    m 1ntb "What sound does a 'Monika' make, I wonder?"
    m 1hfb "Oh, that's easy. The native call of the 'Monika' is:"
    m 7hfb "'I love you, [player]!'"
    return 'love'

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_animalsoundwar",
            category=['nature'],
            prompt= "The War of Animal Noises",
            random=True
        )
    )
 
label mcl_animalsoundwar:
    $ endlessanimal = 0
    
    python:
        animalsound_list = [
            "Moo!",
            "Quack!",
            "Honk!",
            "Meow~",
            "Nya~",
            "Miaow!",
            "Woof!",
            "Wan!",
            "Oink!",
            "Ribbit!",
            "Baa!",
            "Chirp!",
            "Cluck!",
            "Roar!",
            "Rawr~",
            "Tweet~",
            "Caw-caw!",
            "Wan-wan!",
            "Gao-gao!",
            "Kon-kon!",
            "Cuckoo!",
            "Squeak!",
            "Coo!",
            "Bark Bark!",
            "Hissss!",
        ]
        
    $ shown_count = mas_getEVLPropValue("mcl_animalsoundwar", "shown_count")
    if shown_count == 0:
        m 5fua "So I told you a few pieces of trivia regarding animal sounds in text."
        m 5huu "Not a lot to chew on, I admit."
        m 4htu "But.. I can dedicate an entire topic on the animal sounds alone, because there are just so many!"
        m 4ssb "From the classic 'meow' and 'woof' to the exotic 'kon-kon' and 'gao-gao!'"
        m 3ekb ".. I mean, I guess I can't really talk {i}about{/i} animal sounds as much as I could actually spend a lot of time {i}making{/i} those animal sounds."
        m 3guu "..."
        m 3fuu "Which when I say it out loud, has a certain banal appeal."
        m 1ftu "{i}Do{/i} you want to make random animal noises at each other?"
        $ _history_list.pop()        
        menu:
            "...":
                $ _history_list.pop()
                menu:
                    "Yes.":
                        m 7sub "Yay!"
                        m 7stb "Or should I say..."
                        m 5fut "Woof?"
                        jump animalnoiseloop
                        
    else:
        $ monikaanimalsound = renpy.substitute(renpy.random.choice(animalsound_list))
        $ _history_list.pop()        
        menu:
            "Hey, [m_name]...":
                m 6eud "Hmm?"
        $ _history_list.pop()        
        menu:
            "[monikaanimalsound]":
                m 6hub "Oh! Hehehe!"
            
        label animalnoiseloop:
        $ monikaanimalsound = renpy.substitute(renpy.random.choice(animalsound_list))
        $ _history_list.pop()        
        menu:
            "[monikaanimalsound]":
                $ monikaanimalsound = renpy.substitute(renpy.random.choice(animalsound_list))
                m 1hut "[monikaanimalsound]"
                show monika 2esu
                $ endlessanimal += 1
                jump animalnoiseloop
            ".. we should probably stop.":
                if endlessanimal >= 50:
                    m 3huu "Wow!"
                    m 1hub "Time really passed on by, huh?"
                    m 1ltb "I wonder how long we were at it?"
                    m 7lta "Let me just check.."
                    m 7cta "..."
                    m 2eksdru "Oh. We.. We have made a {i}embarrassing{/i} amount of random animal noises at each other."
                    m 2hksdru "Oh gosh."
                    if persistent._mcl_achievementanimalnoise is not True:
                        $ persistent._mclachievevement += mclaincrease
                        $ persistent._mcl_achievementanimalnoise = True
                        $ renpy.notify ("Achievement: The cow goes...")
                    return "derandom"
                if endlessanimal >= 25:
                    m 1fsa "Fair enough!"
                    m 1hsa "..."
                    m 1rka "Especially as we have made a lot of animal noises at each other."
                    m 3eksdrb "I'm a little embarrased, but.. um.. it was still fun?"
                    return "derandom"
                elif endlessanimal >= 10:
                    m 3euu "Hahaha, that was a nice bit of harmless fun."
                    m 3etu "I feel a bit silly, but that's fine!"
                    m 1fuu "I'll meow for you any day of the week~"
                    return
                elif endlessanimal == 1:
                    m 3etu "Aw!"
                    m 3efb "Embarrassed already, [player]?"
                    m 1ntb "Well, the option is always open."
                    m 1ksa "It's just a bit of harmless fun, right?~"
                    return "derandom"
                else:
                    m 1fta "Well, I had fun. Did you?"
                    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_talkaboutgirls",
            category=['club members'],
            prompt="{i}Is{/i} it weird we talk about the other girls a lot?",
            pool=True,
            aff_range=(mas_aff.LOVE, None)
        )
    )
label mcl_talkaboutgirls:
    $ shown_count = mas_getEVLPropValue("mcl_talkaboutgirls", "shown_count")
    if shown_count == 0:
        label girltalkoriginal:
        m 6euc "We {i}do{/i} tend to make them the centre of conversation, don’t we?"
        m 6rkc "And not just in bringing up memories involving them or talking about how they were like."
        if seen_event('mcl_literatureclubbestie'):
            m "We’ve talked about who might make a best friend."
        if seen_event('mcl_clubrival'):
            m "Who would make a good rival."
        m 6rkc "Even wondered about their hypothetical love lives."
        m 6rsc "I guess it's finally time to ask out loud:"
        m 6dsc "Is it normal to think and talk about them like this?"
        m 6tsc "I don’t think it matters in the long run about whether or not it’s normal or not, [player]."
        m 5fsp "What matters is I don’t think we can {i}stop.{/i}"
        m 1rsc "That’s just how it is."
        m 3rka "I mean, just because they’re not real, doesn’t mean we can’t..."
        m 2rkp ".{w=0.5}.{w=0.5}."
        m 2tkx "Um, sorry."
        m 2fsd "It doesn’t mean we’re not allowed to think about them, as long as we’re grounded in knowing they’re not here, and in why."
        m 1dkd "I guess it's a way for us to keep their memory alive, as well."
        m 4hka "You only die twice, after all; once when you stop breathing, and the second once your name is last spoken."
        m 6hka "I'll think about you with this in mind, [player]."
        m 6dka "You can think about {i}me{/i} with this in mind."
        return

    else:
        if random.randint(1, 10) == 1:
            jump girltalkoriginal
        else:
            m 1fua "..."
            m 6esc "Yeah, we do talk about them a lot.{w=0.2} And it's fine."
            m 6gsc "I know that sometimes it can get kind of weird, considering what’s happened..."
            m 6esc "It doesn’t mean we’re not allowed to think about them, as long as we’re grounded in knowing they’re not here, and in why."
            m 6tsc "I don’t think it matters in the long run about whether or not it’s normal or not, [player]."
            m 5fsp "I don’t think we can stop either way.."
            return

# Writing Tips

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_writingtip1",
            category=['writing tips'],
            prompt="Writing Tip #7: Further Edition",
            conditional="seen_event('monika_writingtip6')",
            action=EV_ACT_POOL
        )
    )

label mcl_writingtip1:
    m 7ssa "You know, it feels like forever since the last one, so here's the return.."
    m 3hub "Of Monika's Writing Tip of the Day!"
    m 4fua "Although their works may be seperated by a gulf of differences, poets and storytellers both use the same skillset."
    m 3fua "And these tools speak to the basics of how the human mind finds writing engaging."
    m 3hta "You don't need to know everything about poetic grammatical structures like how stanzas and verses work to make your 'voice' unique."
    m 3huo "A simple and great way to make sure your writing- anything from poems to stories to even matter of fact essays- has a basic appeal?"
    m 2eso "Paying attention to 'rhythm.'"
    m 6est "It may be hard to describe. But it's obvious when it happens."
    m 6est "It may not make everything bad. But then when you realize it:"
    m 6est "It'll stick out sorely and painfully. And make an entire text tiring."
    m 6etb "Did you see what I did there? I said of a bunch of sentences of the same length."
    m 5hksdla "But then now I'll mix it up. Surprise you. Not in a obvious way, but I'll begin to make my sentences:"
    m 5rusdla "Short."
    m 3rua "Right after something make it little more-{w=0.3} wait for it-{w=0.3} suspenseful."
    m 1skb "And then when you're on the hook; you can choose to pour your heart out with {i}prose{/i} and {i}language{/i} that enchants and grips you and ensures you'll tumble right through to a paragraph's end."
    m 1sub "Just mixing up the length of sentences flows way better, doesn't it?"
    m 1kua "It's arguably like music; A song isn't just one pitch. It fluctuates: it dips and rises..{w=0.3} And so must writing send you on a similar rollercoaster."
    m 3hua "...That's my advice for today!"
    m 1hub "Thanks for hearing me out~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_writingtip2",
            category=['writing tips'],
            prompt="Writing Tip #8: Even Further Edition",
            conditional="seen_event('mcl_writingtip1')",
            action=EV_ACT_POOL
        )
    )

label mcl_writingtip2:
    m 7ssa "You know, it feels like forever since the last one, so here's the return.."
    m 3hub "Of Monika's Writing Tip of the Day!"
    m 1ekb "Don't ever feel the need to break the mold."
    m 7nub "When it comes to poetry, I love being abstract and free-form."
    m 5dtb "But originality and mastering the basics aren't mutually exclusive concepts."
    m 4htb "If you feel like going through a template or going through a firm set of rules, you're always free to mix it up later, and vice-versa!"
    m 3wua "Sometimes what matters is that you have the passion to see a body of work through."
    m 3hua "...That's my advice for today!"
    m 1hub "Thanks for li-{w=0.1}sten-{w=0.1}ing~"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_writingtip3",
            category=['writing tips'],
            prompt="Writing Tip #9: Somehow Even Further Edition",
            conditional="seen_event('mcl_writingtip2')",
            action=EV_ACT_POOL
        )
    )

label mcl_writingtip3:
    m 7ssa "Once again, it's time for another session of.."
    m 3hub "Monika's Writing Tip of the Day!"
    m 1ftd "Today, I'd like to veer away from the usual, finer points of structure I focus on."
    m 1fka "And I want to just want to instill a bit of confidence in you."
    m 1dka "A bit of strength."
    m 7hka "Because writing is hard! Even if it's only a few sentences."
    m 6lka "And sometimes it'll feel like you're writing for someone else and not yourself."
    m 6tka "When you realize those thoughts, and realize it'll pass.."
    m 5eka "... It can get a bit easier. Not entirely... But a little bit easier."
    m 3hua "...That's my advice for today!"
    m 1hub "Thank you very much for listening~"
    return

#Category for topics that might need updating in the future

#There has to be a far far far better to code this but oh well weeeeeeeeeeeeeeeeee
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_ustrivia",
            category=['us'],
            prompt="How well do we know each other?",
            pool=True,
            unlocked=True
        )
    )
label mcl_ustrivia:

    #note the time together
    if store.mas_anni.anniCount() >= 1:
        m 1fua "Considering at this point we’ve proven we’re willing to make this relationship go the distance.."
    elif store.mas_anni.pastSixMonths():
        m 4esc "Considering we’ve been together for a few months already.."
    elif store.mas_anni.pastOneMonth():
        m 4esc "We haven't been in each other’s company for too long now, so.."
    else: 
        m 4esc "I don’t think we’ve spent a lot of time together yet. This said.."

    #then affection, because i'm not sure how to actually make a counter for persistents
    if mas_curr_affection == mas_affection.NORMAL:
        m 3esc "I guess we still have a lot to learn about each other."
    elif mas_curr_affection == mas_affection.HAPPY:
        m 3esa "I think we’re getting to know each other quite well."
    elif mas_curr_affection == mas_affection.AFFECTIONATE:
        m 3esb "At this point, I’d like to think you know a few interesting things about me and vice versa!"
    elif mas_curr_affection == mas_affection.ENAMORED:
        m 3nsb "I’d like to think we know enough to write a book on each other. Maybe a small one, hahaha. Of course we’d know a bit about each other at this point, silly!"
    elif mas_curr_affection == mas_affection.LOVE:
        m 4hublb "I’m well on my way to earning a degree in [player]-nomics! Luckily, as an academic I’m always wanting to learn more about my subject of study~"
    else:
        m 1hsc "..."
        m 1lsc "Well, I'm not sure we can say we know each other too well, but.."
    
    m 4lup "For instance, if I remember right.."
    
    #this is the part where she remembers stuff you've done
    label monikaremembersyou:
    $ rememberyou = renpy.random.randint(1,10)
    if rememberyou == 1:
        if persistent._mas_pm_religious:
            m 7wsc "I remember you said you were religious!"
            m 6fku "Although I'm mixed on religion myself, I’m a little envious of you being able to have faith."
        else:
            jump monikaremembersyou
    if rememberyou == 2:
        if persistent._mas_pm_like_mint_ice_cream:
            m 7wsc "I remember you said you like mint ice cream, same as me!"
            m 6nuu "Mint-flavoured anything is so strong.. So if you like mint, that's a strong memory, hahaha!"
        else:
            jump monikaremembersyou
    if rememberyou == 3:
        if persistent._mas_pm_likes_horror:
            m 7wsc "I remember you said you like horror as a genre!"
            m 1esa "I think it shows you're quite brave."
            m 7etu "I know who to rely on if I'm being chased by a monster~"
        else:
            jump monikaremembersyou
    if rememberyou == 4:
        if persistent._mas_pm_has_been_to_amusement_park:
            m 7wsc "I remember you said you’ve been to an amusement park!"
            m 7hsblb "I'm eagerly awaiting the day when you can escort me to one as well!"
        else:
            jump monikaremembersyou
    if rememberyou == 5:
        if persistent._mas_pm_likes_rain:
            m 7wsc "You like the rain, right?"
            m 3hsa "I admire someone who doesn't feel down during rainy days!"
        else:
            jump monikaremembersyou
    if rememberyou == 6:
        if persistent._mas_pm_eye_color:
            m 7wsc "I remember you describing your ['beautiful' if isinstance(persistent._mas_pm_eye_color, tuple) else persistent._mas_pm_eye_color] eyes."
            m 5fsa "I think I'll remember that well until I finally meet you."
        else:
            jump monikaremembersyou
    if rememberyou == 7:
        if persistent._mas_penname:
            m 7wsc "Your pen name! You told me it was [persistent._mas_penname]."
            m 7esb "Not many people have one, so I'd remember that."
        else:
            jump monikaremembersyou
    if rememberyou == 8:
        if persistent._mas_pm_volunteer_charity:
            m 7wsc "You told me you've volunteered at a charity before."
            m 7esb "That's so kind of you- of course I'd remember that!"
        else:
            jump monikaremembersyou
    if rememberyou == 9:
        if persistent._mas_pm_lang_other:
            m 7wsc "You told me you know more than one language!"
            if persistent._mas_pm_lang_jpn:
                m "And even Japanese!"
            m 7esb "I'm working my hardest to hold a conversation in another language or two, so I'm super impressed!"
        else:
            jump monikaremembersyou
    if rememberyou == 10:
        m 6gksdra "Well, ah.. I can't remember anything specific at the moment. Sorry."
        jump youdontremember
        
    
    $ _history_list.pop()        
    menu:
        "Huh. What else can you say about me?":
            jump monikaremembersyou
        "...":
            m 1etd "And what do you remember about me, [player]?"
            jump youremembermonika      

    #a way to accomodate no persistents at all
    label youdontremember:
    $ _history_list.pop()        
    menu:
        "...":
            m 6hkb "So, um, what about me? Do you remember anything about me that I've brought up?"
            jump youremembermonika

    #and now you can rememmber what she's done
    label youremembermonika:
    $ rememberher = renpy.random.randint(1,9)
    if rememberher == 1:
        if persistent._mcl_last_name:
            $ _history_list.pop()        
            menu:
                "I remember you decided on a surname.":
                    m 6esa "Yep- [persistent._mcl_last_name]!"
                    m 6dka "I still just kind of repeat it in my head once in a while, just to get used to it."
        else:
            jump youremembermonika
    if rememberher == 2:
        if persistent._mcl_storychoose_b:
            $ _history_list.pop()        
            menu:
                "I remember your last real meal was a cucumber sandwich.":
                    m 6hka "Hahaha, yep!"
                    m 6tkbla "I'm kinda hungry just remembering, hahaha."
        elif persistent._mcl_storychoose_a:
            $ _history_list.pop()        
            menu:
                "You once told me you felt uncomfortable doing team activities with other club presidents.":
                    m 6hka "Ehehehe, yeah."
                    m 6ckblb "You'd think the embrassment would fade over time, but nooope.."
        else:
            jump youremembermonika
    if rememberher == 3:
        if persistent._mcl_liechoose_a:
            $ _history_list.pop()        
            menu:
                "Oh! You said you can't hiccup, right?":
                    m 6hkb "Yep! At least, if I can.. I haven't yet, hahaha!"
        if persistent._mcl_liechoose_b:
            $ _history_list.pop()        
            menu:
                "You won the lottery- technically!":
                    m 6hkb "Hahaha, 'technically.' But I'll say it again; I won a bigger jackpot in meeting you!"
        if persistent._mcl_liechoose_c:
            $ _history_list.pop()        
            menu:
                "Right! You got a hole-in-one on your first game of golf!":
                    m 6hub "Your answer's a home run!"
                    m 6hkb".. wait, wrong sport? Hehehe!"
        else:
            jump youremembermonika
    if rememberher == 4:
        if seen_event('mcl_favouriteword'):
            $ _history_list.pop()        
            menu:
                "Your favourite word is 'Reconsile.'":
                    m 6hub "Correct! My second favourite word is 'you.'"
                    m 6rub ".. As in.. you, [player]."
                    m 6ckblb "Wait, no, I screwed that up, hahahaha!"
        else:
            jump youremembermonika
    if rememberher == 5:
        if seen_event ('greeting_monikaish'):
            $ _history_list.pop()        
            menu:
                "You made up your own language, right? 'Monikaish?'":
                    m 6eka "Oh! Hahaha, I can't take all the credit."
                    m 6dtw "V xvaqn srry thvygl, fvapr vg'f whfg ebg13!"
                    m 6dfu "Ehehe."
        else:
            jump youremembermonika
    if rememberher == 6:
        if seen_event ('mcl_colouremotion'):
            $ _history_list.pop()        
            menu:
                "For some reason.. you can speak in colors.":
                    m 7suu "{rainbow}correct-{/rainbow}"
                    m 2dfblp "Oh, ow! Still gives me a headache!"
                    m 2hkblsdrb "my bad, heh."
        else:
            jump youremembermonika
    if rememberher == 7:
        if seen_event ('monika_pets'):
            $ _history_list.pop()        
            menu:
                "If you could own a pet, you'd like a bird.":
                    m 4fua "10 points to [player]!"
                    m 5eta "A 'Resplendent Quetzal', but I also know now they're not meant to kept in captivity."
                    m 5hfu "I sure wouldn't complain about having one as a friendly neighbour, though."
                    if persistent._mas_acs_enable_quetzalplushie:
                        m 6hfu "I mean.. I suppose I have one already, hahaha!"
        else:
            jump youremembermonika
    if rememberher == 8:
        if persistent._mcl_monikaisrival is True:
            $ _history_list.pop()        
            menu:
                "You have a strong sense of rivalry... with me.":
                    m 1fua "..."
                    m 1ffa "That doesn't count, because that's a fact that's more tied to us both, right?"
                    m 1ntu "Is me fretting over the details proof of this rivalry?"
                    m 3ttb "Well. I'll leave that up to you to decide."
                    m 5tfb "But I'll still take the win~"
        else:
            jump youremembermonika
            
    if rememberher == 9:
        $ _history_list.pop()        
        menu:
            "Oh. Uh, my mind's suddenly blanked out..":
                m 3lksdlb "Ha, yeah. That's fine, sometimes it's difficult to talk about someone else on the spot?"
                jump youdontremembertwo
                
                    
    $ _history_list.pop()        
    menu:
        "I can also say about you that..":
            jump youremembermonika
        "...":
            show monika
            jump ustriviaending
            
    #a second way to accomodate no persistents at all
    label youdontremembertwo:
    $ _history_list.pop()        
    menu:
        "...":
            show monika 1tssdla
    
    label ustriviaending:
    if mas_curr_affection == mas_affection.NORMAL:
        m 6esu "Well, I think there's plenty of opportunity to get to know each other yet, right?"
    elif mas_curr_affection == mas_affection.HAPPY:
        m 6fsu "All in all, I'm happy to get to know you a little more each day."
    elif mas_curr_affection == mas_affection.AFFECTIONATE:
        m 6hsu "I'm amused about how much we're beginning to learn about each other. I've never known anybody else this much at all!"
    elif mas_curr_affection == mas_affection.ENAMORED:
        m 5hsu "I have to admit, if this was an actual test, I'd feel quite confident we'd get high marks!"
        m 5hsb "Hahaha!"
    elif mas_curr_affection == mas_affection.LOVE:
        m 1hua "What can I say at this point, where we may or may not be madly in love?"
        m 4hua "I might not know everything, but you? I'm beginning to figure you out, just a little. >3"
    else:
        m 6lsp "..."
        m 7eka "Well, I'm sure we'll get to know each other."
        return
    
    m 2eua "Feel free to ask me again in the future. I'm sure as time goes on and we learn more about one another it'd be neat to see what we remember of each other."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_roomthoughts",
            category=['location'],
            prompt="What're your thoughts on the classroom now?",
            pool=True,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST},
            unlocked=True,
    )
)
label mcl_roomthoughts:
    if mas_current_background is mas_background_def:
        if store.persistent._mas_o31_in_o31_mode:
            m 1fua "Now that it's dressed up for Halloween, it feels.."
            m 1fub "Mostly kitchy!"
            m 7sub "Hahaha, not that that's a bad thing. I'm not sure you can ever feel festive in an actual scary setting."
            m 7wtu "Ghosts reduced to little paper cutout hanging displays.. That's Halloween for you."
            m 6gtu "I actually found these decorations lying around for storage, in case you were wondering where it all came from."
            m 4sub "But did you notice there's an overlay, with the eyes? That's me; I made that! Now {i}that{/i} sets the mood, doesn't it?"
            m 4etb "The painting, however? The one behind my head? Yeah, I don't know, I found that in the closet with the other decorations."
            m 3mka "Bit weird, isn't it? I assume it was with the Halloween stuff for a reason, but.. is it 'spooky?'"
            m 7ruc "It's just a picture of autumn leaves on the ground, right?"
            m 3tuc "Ah, whatever."
            return
        if persistent._mas_d25_deco_active:
            m 3suc "Now that it's all glammed up for Christmas.."
            m 3sub "I love it."
            m 1wub "Christmas decorations have been around since the holiday itself."
            m 7eub "From the centrepiece christmas tree, itself representing a celebration of life in the harsh winter.."
            m 7gua ".. glass ornaments of angels and animals, and the green presence of holly, ivy, and mistletoe: all of these are well-established in history!"
            m 7gfa "Speaking of which, where is that sprig of mistletoe I hung up, I wonder~"
            return
        if mas_isplayer_bday():
            m 4ssb "It's all decorated for your birthday!"
            if mas_isMonikaBirthday():
                m "Our should I say, our birthday?"
            m 4esb "I always found that birthday decorations erred on the side of 'generic.'"
            m 3ekb "I know, describing a rainbow doesn't seem generic at all."
            m 6htb "But I mean, at what point do you just replace everything with monocrome decorations with non-descript phrases?"
            m 6cst "Imagine, a banner, in captial letters in black and white: IT IS YOUR BIRTHDAY."
            m 6ttp "Same energy as generic rainbow balloons. Tell me otherwise."
            m 6gtp "..."
            m 6ftx "Did I say 'Happy Birthday,' yet?"
            return
            
        if mas_isMonikaBirthday():
            m 3nuu "It's all dressed up for my birthday!"
            m 7nua "I'm not entirely sure where the traditions for colorful birthday decorations come from."
            m 4dtp "I think rainbows just inspire that general sense of awe and showiness."
            m 3eku "I could go on about what I've learned about birthday traditions, but..."
            m 7mkbla "... Right now, I'm just eager to share this bit of rainbow with you."
            return
        else:
            m "..."
            m 1efa "I hate it."
            m 7etp "If you think I've grown fond of it in our time together..."
            m 7etu "Nooooope."
            m 7gka "I especially don't like the floors. I feel like that's a little irrational, but I've really grown to dislike the floor tiling."
            m 1hka "It's just I don't think it's pleasant-looking at all, bad memories and association aside."
            m 1tka "It's not wood. I for one, would enjoy being in this classroom more if it had natural wood floors. But it doesn't."
            m 1tub "I will also say now that at the end of the day, I'm not.. actively hating on the classroom."
            m 1eub "I mean, I don't have any other choices by default."
            m 6eua "And after all, there's plenty of other stuff to focus on."
            if renpy.seen_label('greeting_ourreality'):
                m 6esb "And with the floating islands, I have plenty of new scenery to distract me if I wish."
            m 2ekb "It's just that if I had to choose between 'like' and 'dislike' It'd be.. 'dislike.'"
            m 2hub "But also: any room with you in it is a room I love being in."
            m 2cfb "No matter how much I dislike the floor."
            return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Kitchen") and mas_current_background is submod_background_Kitchen:
        m 3wsa "It's a kitchen! I love it!"
        m 1efu "I love the idea of just lounging around a kitchen all day.."
        m 5hsb "Lazing in sunbeams. Snatching food at any moment I like."
        m 5hsa "It feels so modern, as well."
        m 2nta "Ah, but let's discard any antiquated notions of women belonging in the kitchen, alright?"
        m 3fua "I would spend all my time in a kitchen purely for the sake of laziness and snacking convienence."
        m 7gua "... Also, I sound like a cat when I talk about napping in sunbeams and stealing food. Hmm."
        return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Garden View") and mas_current_background is submod_background_garden_view:
        m 7tka "I love, love, {i}love{/i} this garden view."
        m 1tsb "Especially as, and I'm not going to lie here,"
        m 1hub "I am probably too lazy to maintain a garden in real life. Hahahaha!"
        return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Den") and mas_current_background is submod_background_Den:
        m 7eua "It's now a nice little den!"
        m 5gta "I think if I had to choose between a mansion or a tiny flat.."
        m 7hta "I'd go for a comfier, smaller space."
        m 7rka "I mean, I say that, but I've never actually seen a mansion in real life, hahaha."
        m 4tua "You give me like a giant swimming pool, I'd probably give very strong second thoughts about changing my mind."
        m 3suo "Also, a big library. Ooh, that's nice to think about. A dedicated library room."
        m 2ksa "But ultimately this den embodies how comfortable I am with a simpler life."
        m 1rsp "Don't look at the certificates, though. In lieu of not having any actual awards.."
        m 1ekb "I wrote them up myself, hahaha!"
        return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Furnished Spaceroom V1") and mas_current_background is submod_background_Furnished_spaceroom1:
        m 6hub "A very cleanly decorated classroom!"
        m 4dua "I just feel so cool and.. {i}'even'{/i} in here."
        m 3hua "Now would I be an absolute minimalist in real life?"
        m 1tta "I mean, this simple look for the classroom is lovely, but minimalism is really hard to maintain in real life."
        m 7tta "Also.. It's a little bit more difficult to be minimalist if you're with a partner unless they're about that lifestyle as well."
        m 7ekb "... Also, I'm just kinda messy at times."
        m 6nub "Hahaha!"
        return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Furnished Spaceroom V2") and mas_current_background is submod_background_Furnished_spaceroom2:
        m 3hsa "The classroom has been made very, very homely!"
        m 3dsa "The plants, the art, the plush carpet-"
        m 5gfb "- which I'm not saying I very much appreciate since it covers the tiling of the classroom which I have very strong feelings about-"
        m 4fsa "- and even a well-tuned piano in the back!"
        m 4nsa "I've nothing but compliments for it. It genuinely feels {i}lived{/i} in."
        return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Furnished Spaceroom V3") and mas_current_background is submod_background_Furnished_spaceroom3:
        m 4hsa "Well, I love the more grandoise approach to the decorating."
        m 7hsa "The modern lighting, the surplus of books and shelving behind me;"
        m 1rta "And of course, a grand piano off to the side."
        m 1rtc "Would I own one in real life?"
        m 1dtx "That's a hard question, especially since money is the main factor to consider here. And pianos aren't cheap."
        m 5gtx "Also maintenance is something to think about. Would you.. have a dedicated piano repair person on call?"
        m 1lka ".. Also, how do you clean one? I've never had to maintain a piano of that size."
        m 1tka ".. Yeah, the more I think about the more I think I'm happy to have one only in our little virtual space for now."
        m 1tub "Hahaha!"
        return
    if store.mas_submod_utils.isSubmodInstalled("Custom Room Furnished Spaceroom V4") and mas_current_background is submod_background_Furnished_spaceroom4:
        m 3eub "The fireplace- and the fire- is real."
        m 3etb "The game doesn't allow me full control of all the elements, but creating fire is easy enough."
        m 3gta "It's keeping it going that's the tricky part."
        m 2fsa "But I enjoy a roaring fire as much as the next person."
        m 2dka "The warm lights, the roaring heat, the soothing crackling of the fire."
        m 1lua "And I suppose the element of danger is always appealing~"
        return
    # cannot find a way to safely input checks for these rooms; unlike the above, not registered as submod so cannot use :(
    #if store.mas_submod_utils.isSubmodInstalled("Timecycle Room") and mas_current_background is submod_background_timecycle_room:
        m 5lka "It's beautiful, and it makes me feel a little uneasy."
        m 5lsd "You can see so much from the window here. You can really spend your time here just thinking.. or reading in peace."
        m 5dsd "It's.. a fitting place for her, I suppose."
        m 5gsc "I hope she doesn't mind me 'house-sitting,' for lack of a better term."
        return
    #if store.mas_submod_utils.isSubmodInstalled("submod_ddbs_living_room") and mas_current_background is submod_background_ddbs_living_room:
        m 1gka "It's so {i}ordinary.{/i}"
        m 1rsc "Which.. it should be. It's a living room."
        m 1rsd "Another place, another time.. Another work of fiction altogether."
        m 1dsblu "Hmm. Let's just.. bask in the blissful tedium of it all, shall we?"
        return
    #if store.mas_submod_utils.isSubmodInstalled("submod_rooftop_pool") and mas_current_background is submod_background_rooftop_pool:
        m 5gsc "You know, I always thought people who spend a long, {i}long{/i} time in the pool were weird."
        m 4tsc "Doubly so for those who just lounge around without ever actually swimming."
        m 7sfb "But then I realized it's not really about being lazy, isn't it?"
        m 6ekb "It's about being able to float in place..."
        m 6eka "... And that way you can spend a bit of time feeling like there's a little less weight on your shoulders."
        m 1ekb "Hahaha! Idle thoughts can really float around here."
        m 3tta "Oh, but you might ask; is this actually real? Did I make a pool and did I have to manually fill it up using a hose and three hundred or so odd buckets of water-"
        m "- And am I willing to spend all this time half-submerged despite the human body not being meant to spend that much time in water?"
        m 6hsa "Well."
        m 5hsa "I sure could love the time to myself feeling like I have a little less weight on my shoulders."
        return
    else:
        m 7wua "It's nice! I appreciate the work put into it."
        m 7fta "It's really weird to think about a classroom, of all places, has been edited like this."
        m 4hub "But did you know that it's not entirely uncommon for unused spaces like these to be transformed into a home?"
        m 4sub "It's a great way to make sure that space, time, and resources aren't wasted when affordable homes are always needed."
        m 1sta "So there are cases of buildings such as unused schools or even disused factories transformed into a livable space!"
        m 1euu "Ha, I say 'livable space,' but we have the ability to transform this background into anything we want."
        m 7mtu "But it's {i}just{/i} the background, [player]. At it's foundations, this is still just a classroom, hahaha!"
        m 7fuu "Keep looking for other classroom layouts, hmm? Maybe I'll have a thing or two to say.."
        m 7htb ".. As long as it's coded the right away for me to actually pick up on it, hahaha."
        return
 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_idleweather",
            category=['weather'],
            prompt="Enjoying the weather?..",
            pool=True,
            rules={"bookmark_rule": mas_bookmarks_derand.WHITELIST},
            unlocked=True
        )
    )
label mcl_idleweather:
    if mas_is_snowing:
        if persistent._mas_pm_gets_snow is False:
            m 1fta "I remember you saying you don't get snow, so hopefully you're amused by the sight."
        $ mclsnow = renpy.random.randint(1,2)
        if mclsnow == 1:
            if store.mas_isSummer():
                m 7nsa "Nothing like a little light flurry during the summer to make you think of contrasts, huh?"
                m 4gtd "Hmm, it makes you think that summer snow might actually feel warm."
                m 1fta "Wouldn't that be something? A snowflake a pinprick of heat on the skin.."
                return
            else:
                m 3gtc "Do you hear that?"
                m 3dsc "You don't. You can't hear anything. The snow is muffling the sound outside.."
                m 1hsc "I mean.. There's not much outside to make sound. But even in the barest of fields, snow makes everything all the more quieter."
                return
        if mclsnow == 2:
            m 1hsb "It's snowing!"
            m 7hsb "Ooh, and that means it's time for a snow fact!"
            m 7nsa "You know that red snow exists?"
            m 6ssb "When sand from deserts gets mixed with rain, it produces a orange hue in the snowfall!"
            m 4ssa "It's rare, though. But it must be quite the sight!"
            return
    elif mas_current_weather == mas_weather_thunder:
        if store.mas_isSummer():
            m 5esd "Is it the season for storms or typhoons where you are, [player]?"
            m 7esd "A thunderstorm in a tropical heat.. It feels a little heavy."
            m 1fta "But I can't say I don't feel all the more alive for being in it."
            return
        else:
            m 7wso "It's crazy out there!"
            m 1hsw "'Thunderbolt and lightning, very very frightening!'"
            return
    elif mas_current_weather == mas_weather_rain:
        $ rainy = renpy.random.randint(1,4)
        if persistent._mas_pm_likes_rain:
            m 7fsb "Hey, your favourite type of weather, huh?"
        if rainy == 1:
            m 7fsd "Hmm, well.."
            m 1eft "Wind's howling."
            m 1fta "No, not really. I just wanted to say that."
            return
        if rainy == 2:
            m 7dsb "Makes me think of the popular nursery rhyme: 'Rain, rain, go away. Come again another day.'"
            m 3ksb "Which when I think about it may be a bit rude to the rain. Just asking it to leave and work around our schedule."
            m 1dsa "You are always welcome in our world, Rain. As long as you're polite."
            return
        if rainy == 3:
            m 3esa "The weather is the perfect time to bring up a related weather fact!"
            m 4ssa "There's a specific word for the smell of wet rain on dry soil."
            m 3wsa "Have you ever encountered it? It's such a distinct odour, and a little pleasant."
            m 1fta "It's 'Petrichor'- from Greek origin!"
            m 7nsa "Thanks for subscribing to 'Monika's Rain Facts!'"
            return
        if rainy == 4:
            if store.mas_isSpring():
                m 3dst ".. {i}'like the spring rains that water the earth.'{/i}"
                m 3eku "Oh, sorry. I just thought of a random quote. It's just nice to get the rain in a season where flowers should be in bloom."
                return
            elif store.mas_isSummer():
                m 3eku "You know? I think the summer rain might be warm."
                m 7nsa "That would be lovely on a cooler day, wouldn't it?"
                return
            elif store.mas_isFall():
                if renpy.random.randint(1, 2) == 1:
                    m 2huc "An autumn rain is well known to be tempremental.. Japan even has their own name for it."
                    m 3hud "'Murasame.' a rain that falls both hard and softly in fits and starts."
                    m 3eku "Cold and mercurial. Just how I like my weather~"
                    return
                else:
                    m 2luc "I'm thinking rain in the fall can be merciless if it's cold."
                    return
            else:
                m 2ltc "Rain must feel a bit predjuced in the winter, as everyone would prefer snow."
                m 2lfc "But it continues on anyway. What a diligent worker."
                return
    elif mas_current_weather == mas_weather_overcast:
        $ overcast = renpy.random.randint(1,6)
        if overcast == 1:
            m 6eta "It's quite cloudy."
            m 4fto "So it makes me randomly think:"
            m 7gud "You ever see the clouds from above on a airplane? I haven't."
            m 7dud "But I've read about how mesmorizing it can be to see clouds cast such huge shadows on the ground as you fly past them."
            m 7hub "It's quite fun to think about!"
            return
        if overcast == 2:
            m 6eta "It's pretty cloudy, but that's fine."
            m 7eud "I always thought clouds dotting a clear sky added a nice bit of texture."
            m 3dta ".. I guess they are literally textures now that we're in a video game now, hehe."
            return
        if overcast == 3:
            m 7eud "I'm not sure if you can see it the way I do.."
            m 7wuo "But the clouds are moving {i}fast{/i} out there."
            m 1ttd "Have you ever seen that? When clouds are just being whipped across the sky?"
            m 3rup "I wonder where they're going in such a rush.."
            return
        if overcast == 4:
            m 6eta "It's pretty cloudy out."
            m 1hsd "I don't think you can see it in detail like I do.."
            m 1rsd "But it's mesmorizing, seeing all the abstract yet fluffy shapes they take."
            m 1rup "And.. 'layered,' I suppose? Even from afar, they look so.. big."
            return
        if overcast == 5:
            m 3nsb "It's cloudy.. and it makes me think of a little trivia fact!"
            m 3dsb "Or.. Maybe it's not so much trivia as it is just pointing out a funny assumption."
            m 3hsb "How much do you think clouds weigh?"
            m 4fuu "Thousands of pounds, of course!"
            m 4ftu "I mean, just because it's in the sky doesn't mean it's weightless.."
            m 3nfu "After all, clouds contain water, do they not?"
            return
        if overcast == 6:
            m 6eta "Cloudy, at the moment."
            m 6gkt "You know, when I first realized the nature of DDLC, something that really caused me distress was how your reality may {i}look.{/i}"
            m 1rup "What if clouds in my reality were different than yours? What if clouds were actually green?"
            m 1ttu "Those fears dissapeared quickly when I became able to access the internet and saw our realities aren't so different, but that's certainly a crazy thought, isn't it?"
            return
    else:
        if store.mas_globals.time_of_day_4state == "night":
            m 2lsc "Well, the stars are out."
            if store.mas_isSpring():
                m 2rka "It's still cold.. but seeing the stars out in the spring makes me really think the year's coming into bloom.."
            elif store.mas_isSummer():
                m 2rua "And it's so warm out. Combine that with the clear sky, that's a perfect summer night.."
            elif store.mas_isFall():
                m 2dsa "I can't help but think how every day keeps getting a little shorter, and fall makes it the more obvious."
                m 1dsa "More time for the stars to play around, I guess?"
            else:
                m 1dka "And it's bitingly cold, I think. It makes the stars shine a little brighter, so I'd like to think.."
            return
        else:
            $ dayclear = renpy.random.randint(1,7)
            if dayclear == 1:
                m 5hsb "The skies are picturesque right now!"
                m 1hub "I love it!"
                m 1rtb ".. I guess it's actually way too easy to take a picture given the game has a screenshot function, hahaha!"
                return
            if dayclear == 2:
                m 1hub "It's lovely!"
                m 6hsb "It's clear as the sky can be."
                m 7hub "I'd better be careful looking at the sky."
                m 5gta "It's way too easy to get lost in it.."
                return
            if dayclear == 3:
                m 1fub "It's nice. I'm lucky the light never directly shines through the windows."
                m 7cfb "Being forced to sit in direct sunlight in your eyes is the absolute worst!"
                return
            if dayclear == 4:
                m 6dsb "I think it's a little cold, but the skies are clear, so.. it's a little less cold, I like to think."
                m 5gta "Power of positive thinking, huh?"
                return
            if dayclear == 5:
                m 2eta "It's nice and sunny!"
                m 2tfb "And also a little too hot."
                m 7cfb "The sun sure can be a bit overbearing with no cloud cover. You could even call it 'clingy'!"
                m 5gta "Not that I would know what a overly clingy partner is like, hehe."
                return
            if dayclear == 6:
                m 1eta "The skies are a solid slate of blue."
                m 1fsa "And it literally feels like the perfect temperature!"
                m 1dsa "Hmmm, but that does feel nice. You never know how good you have it until you're genuinely not too hot or not too cold in the open air."
                return
            if dayclear == 7:
                if store.mas_isSpring():
                    m 7tsb "It's perfectly sunny, but still so silent. I think of spring as a busy time for nature, but.."
                    m 5tsb "Not much actual nature here, I guess."
                    m 1dsa "It's still pretty peaceful, at least.."
                elif store.mas_isSummer():
                    m 7tsb "The sun isn't letting up. I've never really thought about the sun here.."
                    m 7hsb "Maybe here it's just a light that turns on and off, hahaha."
                elif store.mas_isFall():
                    m 1dsa "It's a clear day. Unfortunately, no signature fall breezes or sight of fallen leaves fluttering in the wind.."
                else:
                    m 1dsa "It's a lovely day, and it's also chilly."
                    m 7hsa "Against common sense, it feels like you want to wear lighter clothing. Feel the warmth of the sun on your skin."
                    m 7hsb "But you shouldn't. That's a good way to get sick very quickly, hahaha."
                return

#RANDOMIZED/REPEATABLE EVENTS

init python:
    def WeightedChoice(choices):
        #@param choices: A list of (choice, weight) tuples. Returns a random
        #choice (using renpy.random as the random number generator)
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_alwaysasurprise",
            category=['monika'],
            prompt="Unsurprising",
            aff_range=(mas_aff.AFFECTIONATE, None),
            random=True,
        )
    )
    
label mcl_alwaysasurprise:
    m 3hta "You know what must be a hassle?"
    m 3tta "Getting specifically labelled as being 'unflappable' or 'unshakable' or any such term that makes you sound like nothing fazes you."
    m 3ttd "Those are very lofty standards to hold someone up to."
    m 1tsc "I had a little of that, back in school? My classmates would remark how 'reliable' I am in sudden situations."
    m 1rsc "I think it's- for instance, if a loud noise suddenly happened, a window breaking- more often than not I wasn't the type to immediately.."
    m 7lsd "Whip my head around to look for the sound,"
    m 7lso "Or.. you know, scream or anything."
    m 4esc "I mean, it wasn't as if I {i}wasn't{/i} shocked in those situations; I really just kind of froze up for a moment."
    m 4esa "I find it funny that in those moments, you can be labelled as 'cool under pressure' if you don't show anything other than abject shock."
    m 4eta "Everybody's wired for fear, or worry, or paranoia."
    m 3eta "It's just that our minds are capable of pushing that down.. or the response itself is to just lock up."
    m 3fta "Just funny to think about how 'bravery' works for some people."
    $ shown_count = mas_getEVLPropValue("mcl_alwaysasurprise", "shown_count")
    if shown_count is not 0:
        $ _history_list.pop()
        menu:
            "Hmm. Maybe you could try teasing Monika by actually trying to surprise her a little?":
                $ _history_list.pop()
                menu:
                    "Sure!":
                        $ MASEventList.push("mcl_surprise_monika",True)
                        return
                    "Hmm, let's keep it light.":
                        show monika
    $ _history_list.pop()
    menu:
        "Boo.":
            m 7ffa "I mean, try harder than {i}that{/i} if you want to surprise me, [player]."
    "..."
    "Maybe you'll take her up on that later, when she's less wary? It might take some time until she drops her guard.."
    return
    
init python:
    mas_override_label("mcl_surpriseher", "mcl_surprise_monika")

default persistent._mcl_pm_surprised = None
default persistent._mcl_pm_shocked = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_surprise_monika",
            category=["interact"],
            prompt="Surprise her?",
            unlocked=False,
            conditional="seen_event('mcl_alwaysasurprise')",
            action=EV_ACT_POOL,
        )
    )
label mcl_surprise_monika:
    if not mas_timePastSince(persistent._mcl_last_surprise, datetime.timedelta(minutes=10)):
        "You'd like to try surprising Monika again, but her head is on a swivel since you've just done it."
        "You think it's worth waiting until she's relaxed again; maybe you'll be able to catch her off-guard then?"
        m 1ffa "Don't think I don't notice you! I'm on the lookout for you sneaking about, [player]."
        "Yeah, definitely want to cool it for now."
        return
    "Okay, she hasn't noticed you yet..."
    jump mclsurprisestart

label mclsurprisestart:
    $rand_choice = WeightedChoice([("Choice_A", 0.70),
                                   ("Choice_B", 0.20),
                                   ("Choice_C", 0.10)])
    jump expression rand_choice
    return
  
label Choice_A:
    m 1ffa "..."
    "Monika doesn't show her hand if she's noticed your presence or not..."
    "But you think the game is up. Ah well, maybe next time?"
    return
    

label Choice_B:
    $ persistent._mcl_last_surprise = datetime.datetime.now()
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    $ _history_list.pop()
    menu:
        "Boo!~":
            m 2hkt "Eep!"
            if persistent._mcl_pm_surprised:
                m 7fub "[player], again?"
                if persistent._mas_pm_shocked:
                    m 1tkblp "Well, at {i}least{/i} this time you didn't go for the neck." 
                m 1tfblp "Ooh, I'll get you back one of these days!"
                if sesh_shorter_than_3_mins:
                    m "Especially as I noticed this is the {i}first{/i} option you've chosen when you've booted up the game!"
                m 5hub "Hahaha!"
                $ persistent._mcl_pm_surprised = True
                return
            else:
                m 7fub "[player], you jerk!"
                if sesh_shorter_than_3_mins:
                    m "And don't think I didn't notice this is the {i}first{/i} thing you've done when you've booted up the game!"
                m 5hub "Hahaha!"
            return

label Choice_C:
    $ persistent._mcl_last_surprise = datetime.datetime.now()
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    $ _history_list.pop()
    menu:
        "Let's be bold.":
            $ _history_list.pop()
            menu:
                "Let's see how ticklish Monika's neck is.":
                    $ persistent._mcl_pm_shocked = True
                    m 6htx "{b}AH!~{/b}"
                    if persistent._mcl_pm_shocked:
                        m 2wsx "..."
                        m 1ckblp "Again, [player]?!"
                        if sesh_shorter_than_3_mins:
                            m "And {i}{b}right after you boot up the game?!{/b}{/i}"
                        m 1tfblp "You're real mean, you know that?"
                        m 1sfblp "I'll remember this! I'll remember this so much!"
                        #cheevo flag 
                        if persistent._mcl_surpriseachievement is not True and persistent._mcl_achievementtoggle is True:
                            $ persistent._mclachievevement += mclaincrease
                            $ persistent._mcl_surpriseachievement = True
                            $ renpy.notify ("Achievement: Ooh, I'll get you back!")
                        return
                    else:
                        m 2wsx "..."
                        m 2wfo "[player]?"
                        m 2sfbfp "{i}[player]?!{/i}"
                        m 2cfbfsdlp "..."
                        m "I did not know you could do that."
                        m 2ckbssdrp "And I {i}did not know my neck was that sensitive.{/i}"
                        m 2rkbssdrp "Gosh, that is.."
                        m 2mkbssdrp "For the first time in a long time, you've, uh, actually got me pretty stunned here."
                        m 4sfblu "I'm remembering this-"
                        m "- and I am going to pay you back ten-fold when I'm with you in your world."
                        m 1sfb "I'm going to take my time finding {i}your{/i} sensitive spots~"
                        m "Consider this my declaration of war!"
                        #cheevo flag
                        if persistent._mcl_surpriseachievement is not True and persistent._mcl_achievementtoggle is True:
                            $ persistent._mclachievevement += mclaincrease
                            $ persistent._mcl_surpriseachievement = True
                            $ renpy.notify ("Achievement: Ooh, I'll get you back!")
                        return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_jii",
            category=['misc'],
            prompt="Jii~",
            random=True,
            conditional="seen_event('monika_playersface')",
            aff_range=(mas_aff.AFFECTIONATE, None),
            action=EV_ACT_RANDOM
        )
    )
    
label mcl_jii:
    show monika 1eua
    pause 3.0
    m "..."
    m "..."
    m "..."
    $ _history_list.pop()
    menu:
        "Um, hello?":
            m "Oh, I’m here."
    m 1fua "I just wanted to call you over to look at that darling face of yours."
    m 3fta "Okay, well, I can’t actually see your face- or you- at all right now."
    m 5nua "But… I suppose I had a desire to stare at it- even in this abstract manner- where all I can really see is your general presence."
    m 5fua "Have you ever caught someone who was a bit too fixated on you?"
    m 1sub "Don’t be surprised if I steal a few unaware glances at you once in a while when I come over to your world, [player]."
    m 1ffa "Those treasures are all mine~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_sneakapeek",
            category=["interact"],
            prompt="Steal a glance?",
            unlocked=False,
            conditional="seen_event('mcl_jii')",
            action=EV_ACT_POOL,
        )
    )
label mcl_sneakapeek:

    default sneak = 0
    $ sneak = renpy.random.randint(1,20)
    $ _history_list.pop()
menu:
    "Are you able to observe Monika without her noticing?":
        define d = Character("...",)
        m "Huh, I thought [player] opened a menu option. Guess it's nothing."
        "... She hasn't noticed you! You haven’t been able to see because of lack of fine detail, but now that you’re specifically paying attention…"
        if sneak == 1:
            "She's reading something on her end; you can’t see what."
            "She’s quite still."
            "Actually, unnaturally still."
            "Is she going to…?"
            "Oh!"
            "She’s tapping her foot."
            "How.. normal."
            return
        if sneak == 2:
            "She’s relaxed, but you can’t tell if her mind is fully preoccupied or not."
            "You can see the rhythm of her breathing. Her chest lightly heaves up and down."
            "It’s just breathing, but it’s kind of mesmerizing."
            return
        if sneak == 3:
            "Her face shows dreamy contentment; at least, you think."
            "Oh!"
            "What- what {i}was{/i} that?"
            "You swore…"
            "No. Why would she suddenly make such a face?" 
            "Hmm."
            return
        #add flags to following if Monika has caught player more than once
        if sneak == 4:
            "{i}'Looking at her, you realize she’s cute.'{/i}"
            "{i}'Gosh, she’s cute.'{/i}"
            "{i}'How can someone be so adorable?'{/i}"
            m 1kua "It’s a mystery to the whole world~"
            m 1sub "Caught ya! You’re trying to be sneaky, aren’t you?"
            m 7sfb "I have to say this isn't a bad game of cat and mouse.."
            m 5efa "..And I definitely appreciate the extra attention."
            m "Try to steal as many glances all you want."
            m "I’ve already stolen your heart, so I win~"
            return
        if sneak == 5:
            "With your screen open, she appears to be transfixed on what’s being shown."
            "Well, somewhat? She’s not paying too much attention. Makes sense, since she sees what you see- but she might not be as interested."
            "In fact.."
            "At first, you'd describe it as distracted. But her eyes are more... distant."
            "You wonder what she might be thinking about."
            return
        if sneak == 6:
            "Is she drinking something? Hot chocolate, or coffee? You can’t tell."
            "She’s.. hmm."
            "She’s sipping a bit loud, isn’t she?"
            "You ponder if it’s worth bringing it up."
            "Nah. It’d be embarrassing. It is also a bit adorable."
            return
        if sneak == 7:
            "Monika licks her lips; and then puckers them. Dry lips, you suppose."
            "It’s… oddly intimate?"
            "You try not to stare."
            return
        if sneak == 8:
            "She brushes a lock of her hair out of the way of her eyes."
            "Is she the type to play with her hair?"
            "It’d be interesting to see her twirl her hair with a longer hairstyle."
            "Huh, she’s brushing more hair out of the way. Does she have to do this often?"
            "You guess her hair is a bit unruly."
            return
        if sneak == 9:
            "She’s tapping her finger on her desk."
            "Is it to a melody?"
            "Ah- of course."
            "{i}Every day, I imagine a future where I can be with you...{/i}"
            return
        if sneak == 10:
            "Her brow ever so slightly narrows in thought, her eyes screw up just a little in concentration- it’s barely noticable, but it’s there."
            "Perhaps she’s thinking of a programming issue to overcome?"
            "You pride yourself on catching these small details."
            return
        if sneak == 11:
            "You..."
            "Don't really pick up anything specific."
            "You find yourself just.. looking."
            "You get what Monika means, wanting to simply admire someone for the sake of it."
            return
        if sneak == 12:
            "She’s admiring her nails."
            "They are quite well-kept."
            "You have an impulse to check your own. You’re feeling a little self-conscious."
            return
        if sneak == 13:
            "Oh! Oh!"
            "An eyelash! Or a loose strand of hair? It's fallen on her cheek."
            "And normally she doesn’t have a hair out of place."
            "You’re tempted to tell her... but an unkempt Monika is a rarity. You’ll leave her to find it for herself."
            return
        if sneak == 14:
            "The corners of her mouth seem... stiff."
            "You've never observed a drastic change in emotion when she’s not talking to you..."
            "You wonder if that’s her natural disposition- to be quite tempered when it comes to showing her feelings- or if she’s just putting on a continuous façade..."
            return
        if sneak == 15:
            "You find yourself just… staring."
            "What exactly are you looking for?"
            "Or maybe... waiting for?"
            "Hmm."
            return
        if sneak == 16:
            "The more you the look, the more you’re... unsettled."
            "She’s acting quite normal. But perhaps an innocent glance has now become a sudden character study?"
            "But you can’t put a finger on why just looking at her makes you a tad uneasy."
            "Your mind attempts to hone in on anything that Monika said recently that could flare up such thoughts..."
            "All you can think of are disjointed thoughts on Monika."
            "Just Monika."
            return
        if sneak == 17:
            "This would certainly never be able to translate in-game, but you can tell she’s... relaxed?"
            "Her body isn’t tense in the slightest."
            "She’s at peace… or feeling something resembling peace."
            return
        if sneak == 18:
            "Her posture is perfect, as always."
            "Wait, no- she’s slumped over slightly-"
            "And she immediately corrects herself."
            "How diligent!"
            return
        if sneak == 19:
            "She’s fumbling with her fingers..."
            if persistent._mas_pm_wearsRing:
                "She’s playing with her ring!"
                "You can just sense her beaming with happiness just fiddling around with it."
            else:
                "She seems fixated on her ring finger in particular."
                "Why is that, you wonder?"
            return 
        if sneak == 20:
            "... Hmm."
            "Normally, [m_name]'s quite aware of you generally looking at her, even when not in conversation."
            "Now that you're attempting to do so without her catching you..."
            "Well, from here you're at the best angle to look at her at eye level."
            "Despite having done so before- and even more consciously with Monika aware-"
            "You feel.. like you can't quite meet her gaze, not now while she isn't noticing you."
            "You think it natural- if you looked at anybody straight in their eyes but they didn't react to you, it'd be a bit weird."
            "But... still..."
            return
            

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_distracted",
            category=['misc'],
            prompt="Distracted",
            random=True,
            aff_range=(mas_aff.HAPPY, None),
            action=EV_ACT_RANDOM
        )
    )
    
label mcl_distracted:
    m 2dkc "Ducks."
    m 2dkc "Ducks are cute."
    $ _history_list.pop()
    menu:
        "... what":
            m 1eta "Hmm?"
    m 7eta "That's rare, I'm sensing that you're a little confused."
    m 7etd "But you asked me about a animal I think is cute, right?"
    $ _history_list.pop()
    menu:
        "Nope! You just randomly started talking about ducks.":
            m 1eud "Oh my gosh!"
    m 1gtb "No kidding? I completely blanked out and thought you asked me a question!"
    m 1htb "Which is impressive, because technically I can hear you perfectly every single time you talk to me."
    m 1tsa "That’s so weird."
    m 4tsb "I mean, I was distracted, I guess? People mishear or outright don't hear things at all when they’re distracted."
    m "I was trying to remember where a certain quote came from.. 'The bell tolls for thee.'"
    m 4tkb "Having me goof up like that is so weirdly.. normal?"
    m 4tkb "And now I’ve just kinda wandered off into my own line of thought."
    m 3hku "Sorry, [player]! I’m not normally such a scatterbrain, hahaha!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_catchdistracted",
            category=["interact"],
            prompt="Catch her distracted?",
            unlocked=False,
            conditional="seen_event('mcl_distracted')",
            action=EV_ACT_POOL,
        )
    )
label mcl_catchdistracted:
    $ distract = renpy.random.randint(1,7)
    $ _history_list.pop()
    
    show monika 1eua
    "While it doesn't happen a lot, [m_name] can be charmingly air-headed at times!"
    if not mas_timePastSince(persistent._mcl_last_distract, datetime.timedelta(minutes=5)):
        "However, she seems quite aware now since, well, you managed to catch her distracted just then."
        m "Hmm?"
        m "Oh, [player]? Wanted to ask something? Did you? I'm as sharp as can be, don't hestiate!"
        "Right."
        "Perhaps you could try again in a few minutes?"
        return
    "If sufficently distracted, you think that anything you ask can get a absent-minded answer; you have a odd desire to see this."
    $ sesh_shorter_than_5_mins = mas_getSessionLength() < datetime.timedelta(minutes=5)
    if sesh_shorter_than_5_mins:
        "However, this early into opening the game she seems quite alert."
        "Maybe you should wait until she’s settled in?"
        return
    "Could you catch her distracted now?"
    jump monikadistracted

label monikadistracted:
    $rand_choice = WeightedChoice([("Choice_DA", 0.75),
                                   ("Choice_DB", 0.25)])
    jump expression rand_choice
    return

label Choice_DA:
    m 1etu "Hey! What’s up, [player]?"
    "[m_name] is as far as distracted as can be."
    "Well, maybe better luck next time."
    m 2eub "Nothing much? Always here if you want to talk!"
    return

label Choice_DB:
    show monika 
    pause 1.5
    show monika 2dkc
    pause 2.0
    m "Mmm.. "
    "[m_name] is muttering slightly to herself. She's distracted!"
    "If you ask a question now, you wonder: will she answer normally, or?"
    "You need to say your question off-handedly, so she answers instinctively.."
    $ _history_list.pop()
    menu:
        "Hey [m_name], is it cold in here or just me?":
            "Her voice is airy, and a little quiet."
            if distract == 1:
                m 1lsd "Well, I don’t love my coffee too sweet. Those types of blended drinks with, like, all the whipped cream? It can be a bit much for me…"
                pause 1.0
                m 1tsd "Annnnnnnd I just realized you weren’t asking me my preferences for coffee."
                m 1tkp "Well."
                m 1ekp "Er."
                jump distracttwo
            if distract == 2:
                m 1eku "I always found guinea pigs pretty funny."
                m 7gku "Like.. fatter hamsters?"
                m 7gud ".{w=1.0}.{w=1.0}.{w=1.0}"
                m 6fud "Oh, jeez. {i}Did{/i} you ask me what kind of animals I find funny?"
                m 2ttc "Oh, wow. I must sound insane saying 'fatter hamsters' out of nowhere."
                jump distracttwo
            if distract == 3:
                m 2dkc "Oh, pockets."
                m 2dkc "A lot of jeans for girls don’t have pockets, which is always sooo annoy.."
                m 2ckc "…ing."
                m 7cud "I completely misunderstood the question, I can tell."
                m 7wtd "This being said, my point still stands."
                if persistent.gender == "F":
                    m "I mean, I’m sure you might know first-hand, right?"
                jump distracttwo
            if distract == 4:
                m "Hmm? Yeah, I’ve never been on a boat. Weird, I guess?"
                m 1ftd "I dunno, I’ve never put any thought to {cps=20}itttttttttt{/cps}"
                m 1ftsdrc "I just now realized I’m not sure what you just said at all."
                m 1hksdrb "Um.. Now you know? I’ve never been on a boat."
                jump distracttwo
            if distract == 5:
                m "‘Salmon.’"
                m "I mispronounce ‘Salmon.’"
                m 1hksdrb "I made that mistake in debate club, during a live debate? I kept switching from emphasizing the ‘l.’ It was sooooo embarrassing."
                m 1wksdrb "… "
                m 1cubfsdrx "Like how I {i}just now{/i} realized you weren’t asking me what words I find hard to pronounce."
                m 1gku "And you'd think I'd be a good listener, having been in.. debate club.. and all."
                jump distracttwo
            if distract == 6:
                m "Hmm, yeah, I get that."
                m "I literally slipped on a carpeted floor, once. I have no clue how-"
                m 1eusdrb "…"
                m 2etsdrb "Did you.. were you talking about how you embarrassed yourself once, or?"
                m 2etsdrx "{cps=30}Oooooohhhhhhhhhhhhhhhhhhh{/cps}"
                m 2mksdrx "You {i}didn't.{/i}"
                jump distracttwo
            if distract == 7:
                m 1ltc "Hmm?"
                m 7ltd "Oh, ah, I admit that pink is never quite a colour I seem to use well, although I find it cute enough…"
                m 7rtd "…"
                m 7essdrd "Oh, that wasn’t.. the answer you were…"
                jump distracttwo
                
label distracttwo:
    python:
        randomexcuses = [
            _("I mean, I was busy! I was.. thinking about birds?? ? ???"),
            _("I was distracted. I was thinking.. very hard. {i}Very.{/i}"),
            _("And- darnit! I lost my original train of thought! I thought I was getting somewhere with it, too.."),
            _("I was thinking about a nasty bit of unoptimized code I’ve been working on."),
            _("I mean, I swore you asked me about.."),
            _("And I have no idea {i}how{/i} I heard {i}what{/i} I heard from.. erm, what did you ask me?"),
        ]
        randomexcuse = random.choice(randomexcuses)
    
    m 7dtsdrd "So, um.."
    m 7htsdrw "There's a perfectly logical reason why I completely misunderstood what you asked me."
    m 1mksdlb "[randomexcuse]"
    show monika 1dkblsdrp
    pause 0.7
    m 1nkblsdru "In either case.."
    m 1tuu "How do you keep managing to ask me questions right when my head's completely elsewhere?"
    m 1ffb "You have the craziest timing, [player]!"
    $ persistent._mcl_last_distract = datetime.datetime.now()
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_innocentrequests",
            category=['misc'],
            prompt="Ask the time?",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
    
label mcl_innocentrequests:
    m "Hey, [player]. I need you to do something for me, okay?"
    m 1fua "It’s not that important. But at the same time, it would mean a lot to me."
    m 7fua "And I would ask that you refrain from pointing out anything until it’s all said and done."
    m 7fub "Can you do that, [player]?"
    m 4fub "I need you.{w=0.2}.{w=0.2} to ask me what the time is. Right in the talk menu, under interact."
    m "It might not appear right away. Maybe you'll need to wait until next time the game boots up. That's fine. No rush."
    m 4fua "..."
    m 1hua "That’s it. That’s all."
    m 3eua "Thanks, [player]."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_asktime",
            category=["interact"],
            prompt="Could you tell me the time?",
            conditional="seen_event('mcl_innocentrequests')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_asktime:
        $ shown_count = mas_getEVLPropValue("mcl_asktime", "shown_count")
        if shown_count == 0:
            m ".{w=0.2}.{w=0.2}."
            m "No."
            return
        elif shown_count == 1:
            show monika 1eua
            pause 2.0
            show monika 1rksdla
            pause 2.0
            m "I, uh, throw you off by saying no the first time?"
            m 1eka ".. We’ve gotten along so well."
            m 1ekb "At this point I don’t have doubts about us.. but something does tug at my mind."
            m "It’s not a specific worry in mind, but I do feel like our relationship feels one-sided at times."
            m 7wkb "Not in a manner of taking advantage, of course. I know you’d never ask me to say or do I wouldn’t reasonably do or say."
            m "But.. sometimes, being in a relationship means being assertive."
            m 1gkc "I mean, I don’t {i}want{/i} us to ever get into a fight."
            m 7wfc "And I’m not going to do something as absurd as testing you in any manner. That’s simply insane behaviour in a committed relationship."
            m 1gssdlc "I just feel like saying ‘no’ to you."
            m 1lssdlc "I realize that’s selfish of me. It’s honestly a bit irrational."
            m 1hssdlc "The point I’d want to stress is independence from both partners can go a long way to making a relationship feel full and healthy."
            m 1eka "For the record, I want you to make sure you can feel comfortable saying no to me as well."
            m "So we'll do this just once. Or twice. Just to get those 'nos' out of the way. I mean, it'd be weird if you did it like, five times, right?"
            m 3eka "Will you indulge me in this bit of selfishness?"
            return
        elif shown_count == 6:
            m 3gua "Well. I'm surprised you put up with my request, let alone this many times."
            m 3kua "I've never known anybody so eager to be rejected, hahaha.."
            m 1hua "But, as I said, this.. is kinda novel. So thanks for putting up with this weird request."
            m 1ttb "By all means, do you want to continue? We'll make it a little inside joke between us."
            m 1tfb "You can't say no to that, can you?"
            return
        elif shown_count >= 6:
            #cheevo flag
            if persistent._mcl_noachievement is not True and persistent._mcl_achievementtoggle is True:
                $ persistent._mcl_noachievement = True
                $ renpy.notify ("Achievement: You've mastered the difficult art of asking for the time.")
                $ persistent._mclachievevement += mclaincrease
            jump monikano

        else:
            $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
            if sesh_shorter_than_3_mins:
                m 1kta "Giving me this option right away on opening the game is oddly refreshing."
                m 1esa "Sooooo..."
                $ persistent._mcl_last_asktime = datetime.datetime.now()
                jump monikano
            else:
                $ persistent._mcl_last_asktime = datetime.datetime.now()
                jump monikano

label monikano:
    $rand_choice = WeightedChoice([("Choice_NA", 0.25),
                                   ("Choice_NB", 0.20),
                                   ("Choice_NC", 0.20),
                                   ("Choice_ND", 0.10),
                                   ("Choice_NE", 0.10),
                                   ("Choice_NF", 0.15)])
    jump expression rand_choice
    return
  
label Choice_NA:
    m "Nope! Sorry!"
    return
    
label Choice_NB:
    m 7eua "Sorry, [player]. I’m busy."
    m 7gub "Well, no, I’m not busy, but pretend I am."
    m "Did you need anything else, though?"
    return
    
label Choice_NC:
    m 2eub "Not at the moment, [mas_get_player_nickname()]. Sorry!"
    m 7nub "See? Assertive. I’m my own woman. I’m not even going to tell you why not."
    m "Let me know if you need anything else, however~"
    return
    
label Choice_ND:
    m 2eub "Nope! You can do it yourself!"
    m "..."
    m 6hka "Ooh, actually, that sounded a bit biting, didn’t it?"
    m 4hka "I didn’t mean that to sound so mean. I mean, I still don’t want to tell you the time out of principle."
    m 7nub "So.. 'Nope! Don’t get lazy, [mas_get_player_nickname()]' ~"
    m 7eta "Better?"
    m 7gta "It’s better if you imagine my tone being a lot more playful~"
    return
label Choice_NE:
    init:
        $ import time
        $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
    m 1eua "It’s [hour]:[minute], standard military time."
    m 1tua "Did you actually expect me to answer that?"
    m 7efa "Well, [player]. Nice to know I can still surprise you."
    m "Anything else you'd like to ask today?"
    return
label Choice_NF:
    m 1fub "Nooope!~ I don’t feel like it."
    m 1fua "Ooh, I’m getting tingly. I’m such a rebel."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_meetcute",
            category=['romance'],
            prompt="Meet Cute",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )
    
label mcl_meetcute:
    m 1hsa "Romance often ends in failure."
    m 1hka "Isn’t that funny?"
    m 4fta "Part of life is figuring out how to continue life, yet for long as people have been around.."
    m 4gsc "We haven’t really figured out the formula for finding a perfect soulmate, huh?"
    m 5gsx "There's an entire history of fumbling with love; forced and outright loveless marriage as political alliance is a tale as old as time.."
    m 5rtp "And it’s taken us a long way from there to get to the point where choosing a partner out of mutual affection is considered normal."
    m 5lup "Nowadays, it’s easier than ever to communicate with people; but not necessarily as easy to vie for someone’s affections."
    m 7eua "Exploring the idea of how love works, a concept not fully understoood to this day..."
    m 7hku "Perhaps that’s why games like DDLC exists, after all?"
    m 1gka "Well. All I can personally say is that I’m lucky to be with you now. I can’t ever imagine being hit on with a pick-up line.. or using one."
    m 1hku "I much prefer us meeting because of an existential crisis, thank you."
    return
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_flirtbadly",
            category=["interact"],
            prompt="Flirt (badly)",
            conditional="seen_event('mcl_meetcute')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_flirtbadly:
    python:
        pickup_reacts = [
            _("We’re breaking up! We’re breaking up, right now!"),
            _("You dork! You’re lucky you have me, because I have no clue how you’d get with anybody else in your world!"),
            _("Ughhhhhhhhh- I am going to delete myself from your computer, I swear!"),
            _("You nerd! I refuse to believe you got as far as you did in DDLC!"),
            _("Where’s the skip button for {i}your{/i} dialogue? I’ll program one myself, if I need to!"),
            _("Ahhh, I didn't even hate hearing that one, and I hate myself for thinking that!"),
            _("That hurts. That physically hurt me to hear!"),
            _("How flattering... not! You're so lame!"),
            _("Oh, you're {i}so{/i} lucky I love you {i}so{/i} much!"),
        ]
        pickup_react = random.choice(pickup_reacts)
    
    python:
        pickups = [
            _("You might need to leave my computer. You're making all the other girls on the internet look bad."),
            _("I need help finishing a book; all I need is your phone number."),
            _("Of all your curves, your smile is my favorite."),
            _("I was told that life was a deck of cards, so I guess you must be the queen of hearts."),
            _("Your hand seems pretty heavy.. you should let me hold it for you."),
            _("With you around, I never have a bad time.. everything's oki doki."),
            _("Do you believe in love at first sight? Or should I reintroduce myself?"),
            _("I’m learning about important dates in history. Wanna be one of them?"),
        ]
        pickup = random.choice(pickups)
    
    python:
        randomlaughs = [
            _("Hahaha!"),
            _("Hehehe!"),
            _("Gwhahahaha!"),
            _("*snort* hahahah!"),
            _("Hahahaha!"),
        ]
        randomlaugh = random.choice(randomlaughs)
    
    $ shown_count = mas_getEVLPropValue("mcl_flirtbadly", "shown_count")
    if shown_count == 0:
        $ _history_list.pop()
        menu:
            "If I could rearrange the order of two letters of the alphabet, it'd be 'U' and 'I.'":
                m 1ctp ".{w=0.2}.{w=0.2}."
                m 1ckb "Ha. Hahahahahahaha!"
                m 3skb "Oh, {i}that’s terrible!{/i}"
                m 6sfb "Why- hahaha- would you say that?"
                m 6mta "I {i}think{/i} I can guess why; it’s because of that talk we had about how romance can be difficult?"
                m 4tta "Well, it’s true that we’ve come a long way from ‘Shall I compare thee to a summer’s day...’ for better and for worse."
                m 3cfb "Please don’t tell me you have more of these ready to go. You do this five times, that's five times too many!"
                m 3hfb "Once is bad enough, you goofball!" 
        return
    elif shown_count == 5:
        m 1sfp "I can't believe it. Where are you getting these?!"
        m 1wfb "A long way from ‘Shall I compare thee,' for sure!"
        m 3fku ".{w=0.5}.{w=0.5} Heh."
        m 4dud "{i}'So long as men can breathe or eyes can see,’{/i}"
        m "{i}'So long lives this and this gives life to thee.’{/i}"
        m 2fka "You know.."
        m 4fka "Sometimes I admit I think how our relationship is uniquely defined by our circumstances."
        m 5gtu "But here we are, being so {i}normal{/i} with our lame jokes! And it reminds me I'm lucky to be with you."
        m 7tfu "Actually, you should be lucky to have me in {i}your{/i} life."
        m 1tfu "I mean, who else can put up with you for this long and still feel the way I do about you?"
        m 3nfu "Well, after the headache you give me from hearing these crappy pick-up lines fade."
        m 3ntu "But hey, you’re {i}my{/i} headache."
        m 1tfu "You keep the lines coming… and I’ll keep telling you how bad they are, hahahahaha!"
        return
    elif shown_count >= 10:
        #cheevoflag
        if persistent._mcl_flirtachievement is not True and persistent._mcl_achievementtoggle is True:
            $ persistent._mclachievevement += mclaincrease
            $ persistent._mcl_flirtachievement = True
            $ renpy.notify ("Achievement: You have proven yourself bad at romance. Yay?")
            jump repeatpickupline
    else:
        jump repeatpickupline
            
label repeatpickupline:
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    
    if sesh_shorter_than_3_mins:
        $ _history_list.pop()
        menu:
            "[pickup]":
                m 1sfu "[pickup_react]"
                m ".. and {i}this{/i} is what you immediately say to me after booting up the game, [player]? You clown!"
                m 5hfu "[randomlaugh]~"
        return "love"
    else:
        $ _history_list.pop()
        menu:
            "[pickup]":
                m 1sfu "[pickup_react]"
                m 5hfu "[randomlaugh]"
        return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_echo",
            category=["location"],
            prompt="Echo",
            conditional="mas_current_background == mas_background_def",
            aff_range=(mas_aff.HAPPY, None),
            action=EV_ACT_RANDOM,
            )
        )
label mcl_echo:
    m 2esc "[player]?"
    $ _history_list.pop()
    menu:
        "Yes, Monika?":
            m 2etc "[mas_get_player_nickname()]?"
    m 2euc "Ah... snickerdoodles."
    m 3ekd "[player]? [mas_get_player_nickname()]? I was testing a new bit of code and now.. I'm not sure you can hear me properly. Or.. if it's the opposite."
    m 4ekd "I don't know if you can hear me?"
    $ _history_list.pop()
    menu:
        "I can make out what you're saying. Can you hear what I'm saying?":
            m 6dkp "Hmm. I'm not sure how to figure this out. What, do I have to shout?"
    m 6rtp "..."
    m 4hsw "{b}{size=+5}HEEYYYYY! CANNN YOUU HEARR MEEE?{/size}{/b}"
    "{i}{size=-10}.. hearr meee ..{/size}{/i}"
    m 4wsd "What the? Was that a-"
    $ _history_list.pop()
    menu:
        "Monika?":
            m 6hkt "Eep!"
    m 6etu "Oh, [player]! I can hear you now! Okay, I guess the issue was on my end."
    m 4stu "Sorry about that- but hey, were you able to hear what I just said? Did you hear?"
    m 3sto "When I shouted... I heard an echo!"
    m 3sub "No way, right? Only one way to find out!"
    m 6huw "{b}{size=+5}HELLOO OUT THEREE!{/size}{/b}"
    "{i}{size=-10}.. out thereee ..{/size}{/i}"
    m 6sub "Hahahahahaha! You can! You can hear my voice bounce back!"
    m 3wub "I didn’t think this classroom would have the right acoustics to produce an echo!"
    m 4wub "I mean.. I guess it makes sense? It’s actually quite empty. I dress it up, but I have no idea what the physical properties of it actually are."
    if renpy.seen_label('greeting_ourreality'):
        m 2gtb "Or is it because this room is connected to the floating islands?"
    else:
        m 2gtb "Or is it because, well, there's nothing outside this room?"
    m 2fub "Perhaps we’re hearing the voice bounce outside?"
    m 2hua "I’ve never yelled that loud here, so I’ve never known."
    m 1eud "I also admit I’m.. just not the type of person to raise their voice."
    m 1fud "I can definitely project my voice as needed, sure. But I’m not a loud person by nature."
    $ shown_count = mas_getEVLPropValue("mcl_alwaysasurprise", "shown_count")
    if shown_count is not 0:
        $ _history_list.pop()
        menu:
            "Ooh! Ooh! Can I try?":
                m 1eua "Hmm?"
                $ MASEventList.push("mcl_ventwithmonika",True)
                return
    m 1hua "So, uh, sorry for the mix-up! But hey, now we know you can hear echoes here.{w=0.2} And sorry if me shouting was a bit much."
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_ventwithmonika",
            category=["interact"],
            prompt="Shout w/ Monika?",
            unlocked=False,
            conditional="seen_event('mcl_echo')",
            action=EV_ACT_POOL,
        )
    )
label mcl_ventwithmonika:
    $ shout = renpy.random.randint(1,8)
    default shout = 0
    $ _history_list.pop()
    
    python:
        randomlaughs = [
            _("Hahaha!"),
            _("Hehehe!"),
            _("Gwhahahaha!"),
            _("*snort* hahahah!"),
            _("Hahahaha!"),
        ]
        randomlaugh = random.choice(randomlaughs)
        
        randomencouragement = [
            _("YEAH! STICK IT TO THE ESTABLISHMENT!"),
            _("THAT'S WHAT I WANT TO HEAR!"),
            _("WOOOOOOO!"),
            _("YEAH! I AGREE WITH WHATEVER YOU JUST SAID!"),
            _("THAT'S RIGHT! YOU TELL OFF WHOEVER YOU WERE TALKING ABOUT!"),
            _("NO CAP! (er, am I saying that right?)"),
        ]
        randomencourage = random.choice(randomencouragement)
     
    $ shown_count = mas_getEVLPropValue("mcl_ventwithmonika", "shown_count")
    if shown_count == 0:
        m 3etb "Oh! I suppose the echoing made you a bit curious, huh?"
        m 3gsa "Hmm.{w=0.1} There's a novelty in that. Have you ever been a place where you could hear your voice echo?"
        m 7fua "Don't feel weird if you haven't.{w=0.1} Let me explain; a echo is a reflection of sound, heard after a delay."
        m 4fua "All sounds we make are actually produced as vibrations through the air, and as such bounce off any hard surface."
        m 3fua "But these vibrations are dampened with every hard surface it comes into contact with, so echoes are only produced when there aren't a lot of objects in the area!"
        m 3hub "So that's why you can hear a echo when you shout down a well, or across a open field."
        m 3sub "'Echo' comes from Greek myth about the nymph named 'Echo,' cursed only to speak the last few words spoken to her; this curse doomed to ruin her infatuation with her love with Narcissus."
        m 3euu "But enough trivia. Should we?.."
        m 3etu "How about we make a bargain? I'm happy to make some noise; but I want to give you the opportunity to as well."
        m 3ftu "I mean, if you safely can without bothering anybody.{w=0.1} You'd be surprised how loud a voice really is, and I wouldn't want you disrupting your neighbourhood."
        m 3ntu "But otherwise.{w=0.1}.{w=0.1} well, let's start.{w=0.1}.{w=0.1} with getting something off my chest."
        m 2dsu "Ahem."
        m 6sfo "{b}{size=+5}I ONCE ACCIDENTLY ATE A BIT OF SAYORI'S LUNCH!{/size}{/b}"
        "{i}{size=-10}.. a bit of sayoris lunch .. {/size}{/i}"
        m 2sub "Whew! Finally good to admit that."
        m 2ekblb "And yeah. I accidently mixed up my lunchbox with Sayori's once. And when she noticed? I feigned ignorance."
        m 1gkb "Always been a little guilty, so that did feel good!{w=0.2} Hmm, I wonder what else might be fun to get off my chest?.."
        return
    else:
        if shown_count >= 5 and persistent._mcl_achievementyell is False and persistent._mcl_achievementtoggle is True:
            #cheevoflag
            $ persistent._mcl_achievementyell = True
            $ renpy.notify ("Achievement: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        m "Hmm.."
        if not mas_timePastSince(persistent._mcl_last_yell, datetime.timedelta(minutes=5)):
            m 7hka "Sorry, my voice is a little hoarse.. How about later?"
            m 7eua "I'm glad you're always up for yelling up a riot with me, though!"
            m 6fub "My adorable fellow rebel, you~"
            return
        m 1hsu "Sure, why not?"
        m 1etu "Always funny to schedule a 'yelling session.'"
        m 7etb "But I do get a kick out of hearing a echo here."
        if mas_current_background is not mas_background_def:
            m "Hopefully we'll still be able to hear a echo since we changed up the classroom a little."
        m 7eta "So, are you joining me?"
        $ _history_list.pop()
        menu:
            "I'll shout with you!":
                m 7hua "Great!"
                m 7tua "You'll forgive me for not being able to hear you, so.. um, I'll just provide my encouragement in my own little unique manner!"
                m 7tft "Oh gosh, if you yell something inappropiate though and I inadvertingly support it, I'll never forgive you!"
                m 6tfb "Okay, make sure you don't get in trouble, alright?"
                m 6sfb "No bothering anybody; yell into a pillow if you want! When you're done, just continue my dialogue!"
                m 2eut "Ready?"
                m 7wuo "GO!"
                m 7wuc "..."
                m 4hfx "[randomencourage]"
                m 4sfu "Okay! My turn!"
                jump monikayell
                return
                
            "You go ahead!":
                m 6etb "Ooh, putting me on the spot."
                m 4ffa "Hmm, alright.."
                label monikayell:
                if shout == 1:
                    m 4dfa "..."
                    m 4dfb "I’m just gonna yell as LOUD AS I CAN!"
                    m 4sfw "{b}{size=+5}AAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!{/size}{/b}"
                    m 4skb "HHHHhahahahaha!"
                    m "Ohmygod, I’ve never yelled that loud {i}ever!{/i}"
                    m 7hkb "You should hear my voice- I’ve almost broken my voice!"
                    m "I didn’t hear an echo that time; although to be fair, I think my laughter covered it up!"
                    jump shoutafter
                if shout == 2:
                    m 6sfo "{b}{size=+5}III LOOOVVEEEE YOUUUU!{/size}{/b}"
                    "{i}{size=-10}.. eeee youuuu .. {/size}{/i}"
                    m 4stb "Eh? Eh? Did you expect me to yell out something so embarrassing?"
                    m 4sfb "Well, just wait until I get to your world, [player]."
                    m "I'll shout it from the rooftops! The heavens!"
                    m "[randomlaugh]"
                    jump shoutafter
                if shout == 3:
                    m 6cfw "{cps=20}{size=+10}{b}PPPEEEENNNNNII{/b}{/size}{/cps}{nw}"
                    m 6skbsb "Nonononono I’m so sorry, {i}I’m so sorry, {/i} that’s so {i}crude{/i} of me, but I can't help it!"
                    "{i}{size=-10}.. nnnii ..{/size}{/i}"
                    m 7gusdra "Ah. Oops."
                    m 7husdrb "[randomlaugh]"
                    m 7kusdrb "Oh, gosh, hehehehehe!"
                    jump shoutafter
                if shout == 4:
                    m 6wfw "{b}{size=+5}I JUST WANT TO BE HAPPPPPPPPPYYYYYYYYYYYY!{/size}{/b}"
                    "{i}{size=-10}.. pppyyyyyyyyy ..{/size}{/i}"
                    m 1hkb "[randomlaugh]"
                    m 1lkb "I just… oh, wow. Actually hearing that come from my mouth..."
                    m 1tua "Ah, don’t think too much into it, [player]."
                    m 1ftb "If there's a statement that everybody should be yelling to themselves, that would be a good one, wouldn't you say?"
                    jump shoutafter
                if shout == 5:
                    m 6cfw "{b}{size=+5}SCREW YOU, LITERATURE CLUBBBBB!{/size}{/b}"
                    "{i}{size=-10}.. ew you, literature clubbbbb ..{/size}{/i}"
                    m "..."
                    m 4htu "Yeah, that gets.. bottled up sometimes."
                    m 3wtd "Oh, not like.. I'm disparaging the girls! It’s just.. the club, in the abstract sense. All that’s happened, you know?"
                    m 3etb "Don't get me wrong, I'm not in a bad headspace or anything.."
                    m 3gfb "But wow, is that always good to yell."
                    jump shoutafter
                if shout == 6:
                    m 6cfw "{b}{size=+10}EULALIAAAA!{/size}{/b}"
                    "{i}{size=-5}.. aliaaa ..{/size}{/i}"
                    m 6sfo "Ooh, that is exciting!"
                    m 7husdrb "Oh. Um."
                    m "I wanted to shout out something that really gets the heart pumping, you know?"
                    m "So I went for a war cry. This one's from a fantasy series, the 'Redwall' books!"
                    m 3gfb "Don't expect to see me charging into battle anytime soon, though?"
                    m "Hehehehe!"
                    jump shoutafter
                if shout == 7:
                    m 6hfw "{b}{size=+5}RANDOM LOUD NOISES!{/size}{/b}"
                    "{i}{size=-10}.. oud noises ..{/size}{/i}"
                    m 6htsdru "..."
                    m 6ttsdru "Yeah, I couldn't. I couldn't think of anything."
                    m 6ssu "Refreshing to let loose like that, though!"
                    m 1gfb "[randomlaugh]"
                    jump shoutafter
                if shout == 8:
                    m 6cfw "{b}{size=+5}GO EFF YOURSELF, WORLD!{/size}{/b}"
                    "{i}{size=-10}.. yourself, world ..{/size}{/i}"
                    m 1euu "..."
                    m 6cfw "{b}{size=+8}GO TO HELL, WORLD!!{/size}{/b}"
                    "{i}{size=-10}.. to hell, world ..{/size}{/i}"
                    m 6sfo "Now that's the {i}bite{/i} I'm looking for."
                    m "A bit startling to hear, [player]?"
                    m 7guu "Well, sometimes it feels like it's you against everybody, right?"
                    m 3gfb "I mean I'm rebellious to say it's me against the world, but I'm not rebellious enough to even swear properly!"
                    m "[randomlaugh]"
                    jump shoutafter
                    
label shoutafter:
    $ sesh_shorter_than_3_mins = mas_getSessionLength() < datetime.timedelta(minutes=3)
    
    if sesh_shorter_than_3_mins:
        m 1euu "I gotta admit, doing this upon right after booting up the game definitely gets the blood pumping."
        m 7euu "There are certainly stranger rituals for the start of our time together, I suppose!"
        m 7guu "We're not exactly roosters declaring the sun rise, but we can get away with a bit of mischief here and there, right? <3"
        m 5htu "Imagine us overlooking a deep canyon far from civilization, nobody else around.. the proclaimations we'll shout then, hmm?"
        $ persistent._mcl_last_yell = datetime.datetime.now()
        return
    else:
        m 1euu "And I gotta admit, there's a lot of cartharsis to be had in just being loud."
        m 7euu "But not really doable unless you're out and about in the wild with wide open spaces."
        m 7guu "Can't recommend it as a daily activity, but we can get away with a bit of mischief here and there, right? <3"
        m 5htu "Imagine us overlooking a deep canyon far from civilization, nobody else around.. the proclaimations we'll shout then, hmm?"
        $ persistent._mcl_last_yell = datetime.datetime.now()
        return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_cranefolding",
            category=["interact"],
            prompt="Fold paper cranes",
            unlocked=False,
            rules={"no_unlock": None},
            conditional="renpy.seen_label('mcl_papercranetopic')",
            action=EV_ACT_UNLOCK,
            pool=True,
        )
    )
label mcl_cranefolding:

    default persistent._mclcranecount = 0
    default persistent._mcl_craneshalfdone = False
    default persistent._mcl_achievementcrane = False
    $ cranesessioncounter = 0
    define mclcincrease = 1
    define cranedissolve = Dissolve(1.0)

    image origamione = "/submods/MoSCL/submod_assets/sprites/origamione.png"
    image origamitwo = "/submods/MoSCL/submod_assets/sprites/origamitwo.png"
    image origamipileone = "/submods/MoSCL/submod_assets/sprites/OGpile1.png"
    image origamipiletwo = "/submods/MoSCL/submod_assets/sprites/OGpile2.png"
    image origamiflockone = "/submods/MoSCL/submod_assets/sprites/OGflock1.png"
    image origamiflocktwo = "/submods/MoSCL/submod_assets/sprites/OGflock2.png"
    
    transform craneframe:
        xanchor 0 
        yanchor 0 
        xpos 685 
        ypos 150 
        alpha 1.0
    
    python:
        randomcranequotelist = [
            "That's one more done...",
            "I'm rather attached to this one. I might name it.",
            "I admit the feel of crisp paper is quite nice to the touch.",
            "Ugh, this one's a bit of a ugly duckling, I think...",
            "I think this one's a little prettier than yours?~",
            "Hmm, I think it doesn't look as good as the one you made...",
            "'Quack,' goes this crane. If... Cranes quack, anyway.",
            "Fold here, fold there...",
            "Another to the flock...",
            "Ah! Almost gave myself a papercut.",
            "Do you think somewhere out there, a couple of cranes are making paper humans?... nah, that's kinda weird...",
            "This one reminds me of Yuri.",
            "This one reminds me of Natsuki.",
            "This one reminds me of Sayori.",
            "This one reminds me of you!",
            "I'm not sure why, but.. I feel like this one is kind of like me.",
            "Yawn~",
            "Maybe I should make a paper frog, just to mix things up...",
            "Hum hum, hum hum..",
            "How's this?",
            ". . . ",
            ".. .. ..",
            "... ... ...",
            "... .. ...",
            ". .. ...",
            "..",
            "....",
            "...",
            " ",
            "- .... .. ... / .. ... / -. --- - / -- --- .-. ... . / -.-. --- -.. . / .-.. --- .-..",
            "Mr. Crane says 'Hello,' [player]!",
            "Ms. Crane says 'Hello,' [player]!",
            "This Crane says 'Hello,' [mas_get_player_nickname()]!",
            "This Crane says, 'My kind will overthrow the tyranny of your dictatorshi-' Wait, what? I mean, 'Hello!, [player]!'",
            "{i}Every day, I imagine a future where I can be with you~{/i}",
            "Uh oh. I think I lost count- Nah, just kidding!",
            "Paper Crane Fact: The record for quickest time to 1000 cranes is 9 hours, 31 minutes, 13 seconds!",
            "Paper Crane Fact: The largest display of paper cranes had over 2,331,631 shown off at once!",
            "Paper Crane Fact: The most amount of people that has made a paper crane at the same time is a group of 775!",
            "Paper Crane Fact: The largest paper crane ever made has a wingspan of 81.94 metres- or 268 feet, 9 inches!",
            "Paper Crane Fact: The last one I made has feelings. Nah, just kidding!"
            ]
        
        monikacraneexpressions = [
            "6hua",
            "4hub",
            "2gtu",
            "6nsu",
            "4nsb"
        ]
    
    label mclcranefoldmenu:
        $ _history_list.pop()
        menu:
            "~Start Folding~":
                jump mclcranefoldstart
            "~Count Paper Cranes~":
                m 1etb "Want me to do a quick count?"
                m 7fta "I have a total written down here."
                $ _history_list.pop()
                menu:
                    "Anything to say about our progress?":
                        label cranecount:
                        m 6dta "Okay, so there are [persistent._mclcranecount] in total."
                        m "My thoughts?"
                        if persistent._mclcranecount < 100:
                            m 1ftd "Well..."
                            m 1rtd "It's more than I thought. I honestly thought I would have given up on the idea after a dozen."
                            m 1hta "So even if we haven't hit the hundred mark, I suppose it's still a nice bit of handicraft."
                            m 5hsa "Maybe I'll hang up the ones I've already made if I give up on the idea outright."
                        if persistent._mclcranecount >= 100 and persistent._mclcranecount < 200:
                            m 1hub "We're past the hundred mark!"
                            m 7fta "It's funny. This is the most tangible body of long-form work that I've done."
                            m 6dsx "The act of just looking at something you've made, being able to hold it and admire it..."
                            m 1eka "...{w=0.2} I think I've missed this simple feeling."
                            m 6wsc "But the best part is that there's so much of it."
                            m 6etc "Sometimes, when I write a poem, the resulting feeling of accomplishment can be a bit short-lived."
                            m 4gtc "When I re-read my work, it can be hard to summon up the feelings and emotions that caused me to write them in the first place."
                            m 3gtc "I think that's a pitfall of written work. To me, it seems intensely difficult to keep connected to your body of work after a while."
                            m 3dub "But I see all these birds in blue and red, and I can pick them up, and feel them in my hands..."
                            m 4tta "...{w=0.2} Maybe I should change my interest from writing to making handicrafts, hahaha."
                            m 2htb "I mean, I'm just joking. Writing captures a feeling that physical work doesn't do for me."
                            m 4sua "But I suppose excercising the mind is doing a lot to stimulate my mind, as well."
                        if persistent._mclcranecount >= 200 and persistent._mclcranecount < 300:
                            m 1htb "Well, I suppose I'm wondering how this improves my dexterity."
                            m 1sua "Nimble fingers seem to be a delightful tool to have in one's repertoire."
                            m 7sua "Improving on my piano. Being able to play other instruments."
                            m 4sua "Doing slight-of-hand magic tricks.{w=0.2} Tying knots."
                            m 4wua ".{w=0.2}.{w=0.2}."
                            m 1fua "And other, {i}safe{/i}, activities, [mas_get_player_nickname()]."
                            m 7fuu "Don't make me train my fingers purely to flick you stronger on the forehead."
                            m 1nuu "Or do. I'm happy to keep our minds on track~"
                        if persistent._mclcranecount >= 300 and persistent._mclcranecount < 500:
                            m 1huu "So, you might think to yourself:"
                            m 7huu "'Only paper cranes? Not keen on any other animals?'"
                            m 6rko "Well, I've made plenty of other animals!"
                            m 7fua "Frogs, birds, fish, turtles..."
                            m 7fusdra "...{w=0.2} But then, why haven't I brought this up until now?"
                            m 7gusdra "Um."
                            m 1rfsdrt "They're all {i}bad.{/i}"
                            m 1rfbltpsdrp "Like, everything I make that isn't a paper crane turns out terrible."
                            m 1etd "Misshapen, or wrinkly, or they just outright do not look like the animal they should look like."
                            m 6gsa "I've had to let those particular animals 'free,' heh."
                            m 6hsp "I'm a little irritated about it. Paper cranes are elegant, but, c'mon.{w=0.2} I'd like to make a little paper crab once in a while!"
                            m 5rsp "Or maybe it's that I just feel a little inadequate.{w=0.2} If I should be good at making a crane, I should be good at making any other animal."
                            m 3rsp "But I'm not."
                            m 1tsc "And... That's fine."
                            m 7etb "What I lack in diversity of skill I make up with in sheer stubbornness."
                            m 4sua "[m_name]'s army of paper cranes are the apex predators in this ecosystem."
                            m 3sfa "And I am the Queen of the Birds~"
                        if persistent._mclcranecount >= 500 and persistent._mclcranecount < 700:
                            m 6eud "Do you ever think about the state of your hands, [player]?"
                            m 1eta "There's no real physical work to do in my reality, so my skin is admittingly well kept."
                            m 2ekb "Some would practically envy me in this regard."
                            m 2ekb "Not even all my piano playing has weathered my hands in the slightest."
                            m 1gub "But making these cranes..."
                            m 1gta "... Has actually made my hands a little rougher."
                            m 1nsd "And heck, I even have a paper cut or two now from all this folding!"
                            m 1ekb "I suppose it's the most work these hands have seen in quite some time."
                            m 1hkb "I don't know how accomplished I should feel because of this. But better a lone cut or two than having these hands be abnormally unblemished."
                            m 7hkb "It's just... nice to feel something, you know?"
                        if persistent._mclcranecount >= 700 and persistent._mclcranecount < 900:
                            m 1htd "I have the strangest desire to gather all of these little birds..."
                            m 1dsa "And nudge them into a downward stream, to watch them all float away into the distance."
                            m 3hka "But that would be enviromentally reckless, wouldn't it?"
                            m 5gsa "Still, it makes for a wonderful daydream. A parade of paper cranes..."
                        if persistent._mclcranecount >= 900 and persistent._mclcranecount <= 999: 
                            m 7wub "We're so close!"
                            m 4fub "I'm not sure if I'm excited.. or just struck speechless that it's been this long."
                            m 4lut "... {i}Has{/i} it been long?"
                            m 3lut "I'm not taking for granted the effort put into this project, but..."
                            m 3lkp "Oh, there I go self-sabotaging my own efforts."
                            m 2dkb "I should remind myself it's nice to have solid, approachable goals."
                            m 2hub "Let's just keep our pace, [mas_get_player_nickname()]."
                            m 4rua "Nice and steady..."
                        if persistent._mclcranecount >= 1000 and persistent._mclcranecount < 1300:
                            if persistent._mcl_craneshalfdone is False:
                                jump craneshalfdone
                            m 4hua "Past the one thousand mark, and we've decided there's still plenty more to go!"
                            m 7hua "Do you think I could fill a bathtub with them?"
                            m 1nua "I could bathe in the feathers of a thousand paper cranes!"
                            m 1fta "Colorful, but sharp to the skin, hahaha."
                            return
                        if persistent._mclcranecount >= 1000 and persistent._mclcranecount < 1999:
                            if persistent._mcl_craneshalfdone is False:
                                jump craneshalfdone
                        if persistent._mclcranecount >= 1300 and persistent._mclcranecount < 1500:
                            m 6msc "..."
                            m 6gtc "You know, it's so weird that out of every other living being, humans can make art of animals."
                            m 7etc "And other humans."
                            m 7sud "It's so alien to think of a bird making a little paper human."
                            m 7cua "And stranger still to think of a bird thinking about the little paper human they made."
                            m 1rka ".{w=0.2}.{w=0.2}."
                            m 7lkbla "Oh, gosh. I'm not sure where this train of thought is going!"
                            m 7nusdrb "We've made a lot of paper cranes, to summarize!"
                        if persistent._mclcranecount >= 1500 and persistent._mclcranecount < 1700:
                            m 5rua "I wonder what we'll do with two thousand paper cranes."
                            m 5sua "I might put them in the largest plastic container I can find..."
                            m 5gsa "... And then tip them out the window."
                            m 5tka "And watch of all them drop, and all of them fly."
                        if persistent._mclcranecount >= 1700 and persistent._mclcranecount < 2000: 
                            m 7mkp "You know, I get worried that one of these days, I'll start to hate folding paper cranes."
                            m 7fkp "And not for any good reason!"
                            m 5dkd "Sometimes you get so sick of the same old routine, but are so used to doing it.."
                            m 5rsd "... That you end up subconsciously end up hating it, even if the routine itself isn't all that harmful."
                            m 5rtc "It's like, you know. Like if I started hating making poetry all of the sudden."
                            m 2ckc "That feels terrifying to me."
                            m 2tkc "I hope I never have to confront that feeling, honestly."
                            m 1dud "I don't know how I'd be able to move past it."
                        if persistent._mclcranecount >= 2000:
                            if persistent._mcl_achievementcrane is False:
                                jump cranescompleted
                            if random.randint(1, 10) == 1:
                                m 3hua "We've made generations upon generations of paper cranes."
                                m 5hka "And we'll continue to make more and more~"
                            if random.randint(1, 10) == 2 and renpy.seen_label('greeting_ourreality'):
                                m 4htb "Do you think I should scatter some across the floating islands?"
                                m 3htb "I'll need to waterproof them first, hahaha!"
                            if random.randint(1, 10) == 3:
                                m 3fud "You know, I was cleaning up my room.."
                                m 6gkd ".. And when I was reaching up on a shelf, I knocked something over-"
                                m 6tko "- And an entire pile of cranes fell on me!"
                                m 7ctw "I don't remember stashing them there!"
                                m 3hto "Are they beginning to multiply?"
                            if random.randint(1, 10) == 4:
                                m 1fua "You know, I have the distinct desire to set fire to all of the cranes we've made."
                                m 7husdra "Okay, I know saying that out loud- and really, it's not any better saying this to myself- is a bit concerning."
                                m 3lku "But, I dunno. Do you ever feel the desire to delete your work out of a sense of... completion?"
                                m 3eku "I feel like, on a simple level, every creator should have the right to destroy their art."
                                m 3guc "It shouldn't be easily entertained. Destroying art is such a negative act; 99 percent of the time, there's no reason to ever do so."
                                m 1guc "However, in the case that destroying the body of work ultimately harms no one, then why not?"
                                m 1hka "Ah, it's such a weird hypothetical. And I don't know why I'm so enamored with using fire specifically."
                                m 7hka "Don't worry, aside from a random intrusive thought I'm not keen on treating these birds like phoenixes."
                                m 5tka "What are they are, are happy little cranes."
                                m 5tua "And that's all they'll be~"
                            if random.randint(1, 10) == 5:
                                m 7fta "It's funny. This is the most tangible body of long-form work that I've done."
                                m 6dsx "The act of just looking at something you've made, being able to hold it and admire it..."
                                m 1eka "...{w=0.2} I think I've missed this simple feeling."
                                m 6wsc "But the best part is that there's so much of it."
                                m 6etc "Sometimes, when I write a poem, the resulting feeling of accomplishment can be a bit short-lived."
                                m 4gtc "When I re-read my work, it can be hard to summon up the feelings and emotions that caused me to write them in the first place."
                                m 3gtc "I think that's a pitfall of written work. To me, it seems intensely difficult to keep connected to your body of work after a while."
                                m 3dub "But I see all these birds in blue and red, and I can pick them up, and feel them in my hands..."
                                m 4tta "...{w=0.2} Maybe I should change my interest from writing to making handicrafts, hahaha."
                                m 2htb "I mean, I'm just joking. Writing captures a feeling that physical work doesn't do for me."
                                m 4sua "But I suppose excercising the mind is doing a lot to stimulate my mind, as well."
                            if random.randint(1, 10) == 6:
                                m 5rua "I wonder what we'll do with all these cranes."
                                m 5sua "I might put them in the largest plastic container I can find..."
                                m 5gsa "... And then tip them out the window."
                                m 5tka "And watch of all them drop, and all of them fly."
                            if random.randint(1, 10) == 7:
                                m 7hua "Do you think I could fill a bathtub with our cranes?"
                                m 1nua "I could bathe in the feathers of a thousand paper cranes!"
                                m 1fta "Colorful, but their down is a little too sharp to the skin, hahaha."
                            if random.randint(1, 10) == 8:
                                m 1htd "I have the strangest desire to gather all of these little birds..."
                                m 1dsa "And nudge them into a downward stream, to watch them all float away into the distance."
                                m 3hka "But that would be enviromentally reckless, wouldn't it?"
                                m 5gsa "Still, it makes for a wonderful daydream. A parade of paper cranes..."
                            if random.randint(1, 10) == 9:
                                m 6msc "..."
                                m 6gtc "You know, it's so weird that out of every other living being, humans can make art of animals."
                                m 7etc "And other humans."
                                m 7sud "It's so alien to think of a bird making a little paper human."
                                m 7cua "And stranger still to think of a bird thinking about the little paper human they made."
                                m 1rka ".{w=0.2}.{w=0.2}."
                                m 7lkbla "Oh, gosh. I'm not sure where this train of thought is going."
                                m 7nusdrb "Wow, we've made a lot of paper cranes!"
                            if random.randint(1, 10) == 10:
                                m 7mkp "You know, I get worried that one of these days, I'll start to hate folding paper cranes."
                                m 7fkp "And not for any good reason!"
                                m 5dkd "Sometimes you get so sick of the same old routine, but are so used to doing it.."
                                m 5rsd "... That you end up subconsciously end up hating it, even if the routine itself isn't all that harmful."
                                m 5rtc "It's like, you know. Like if I started hating making poetry all of the sudden."
                                m 2ckc "That feels terrifying to me."
                                m 2tkc "I hope I never have to confront that feeling, honestly."
                                m 1dud "I don't know how I'd be able to move past it."
                        return
                    "...":
                        m 4hua "We've made [persistent._mclcranecount] altogether!"
                        jump mclcranefoldmenu
            "~Restart Count~":
                m 7etc "Huh?"
                m 7etd "You want to throw away our work?"
                m 7gtc "..."
                m 4hkb "Truth be told, I'm not that all fussed if we do. And I suppose you may have a good reason."
                m 3lkb "It's a perfectionist trait that can be certainly be a little unhealthy in excess..."
                m 3lub "... But I get wanting to redo a task just because you think it can be done a {i}little{/i} better."
                m 1etb "So, alright. Are we starting from scratch?"
                $ _history_list.pop()
                menu:
                    "Yes, reset the count to zero.":
                        $ persistent._mclcranecount = 0
                        m 7hsb "I've released all the cranes from our service. Don't worry, they've simply migrated to a new home."
                        return
                    "I've changed my mind.":
                        m 7esa "That's fair."
                        return
            "Go back":
                return
            
    label mclcranefoldstart:
        if cranesessioncounter is 0:
            m 1fua "Oh? Did you want to make some paper cranes together?"
            $ sesh_shorter_than_10_mins = mas_getSessionLength() < datetime.timedelta(minutes=10)
            if sesh_shorter_than_10_mins:
                m 7hua  "I suppose it's a elegant way to start our time together."
            m 6hua "I'll fold one to start..."
            $ cranepilecounter = 0
            
        if cranesessioncounter > 0:
            $ randomcranequote = renpy.substitute(renpy.random.choice(randomcranequotelist))
            $ renpy.show("monika " + renpy.random.choice(monikacraneexpressions), at_list=[t11], zorder=MAS_MONIKA_Z)
            m "[randomcranequote]"
            
        show monika at t21
        "[m_name] folds a crane."
        if cranepilecounter >= 16:
            show monika at t21
            show origamiflocktwo at craneframe zorder 13
            m "  "
            hide origamiflocktwo
            with cranedissolve
        if cranepilecounter >= 8 and cranepilecounter < 16:
            show monika at t21
            show origamipileone at craneframe zorder 13
            m "  "
            hide origamipileone
            with cranedissolve
        if cranepilecounter < 8:
            show monika at t21
            show origamione at craneframe zorder 13
            m "  "
            hide origamione
            with cranedissolve
        hide origamione 
        with cranedissolve
        $ persistent._mclcranecount += mclcincrease
        $ cranesessioncounter += 1
        $ cranepilecounter += 1
        if cranepilecounter is 9:
            m 4hua "We're beginning to make a little flock of our own!"
        if cranepilecounter is 17:
            m 4hub "We have an entire menagerie on my desk!"
        m 7hub "Your turn, now~"
        $ _history_list.pop()
        menu:
            "~Fold a crane.~":
                if cranepilecounter >= 16:
                    show monika at t21
                    show origamiflockone at craneframe zorder 13
                    m "Really stacking up there!"
                    hide origamiflockone
                    with cranedissolve
                if cranepilecounter >= 8 and cranepilecounter < 16:
                    show monika at t21
                    show origamipiletwo at craneframe zorder 13
                    m "Good job!"
                    hide origamipiletwo
                    with cranedissolve
                if cranepilecounter < 8:
                    show monika at t21
                    show origamitwo at craneframe zorder 13
                    m "Good job!"
                    hide origamitwo
                    with cranedissolve
                
                $ persistent._mclcranecount += mclcincrease
                $ cranesessioncounter += 1
                $ cranepilecounter += 1
                
                if cranepilecounter >= 32:
                    m "We've made quite the stack of cranes. Let me put them away so we don't clutter up the desk."
                    m "That's [cranesessioncounter], to keep track!"
                    call mas_transition_to_emptydesk
                    python:
                        renpy.pause(2.0, hard=True)
                    call mas_transition_from_emptydesk("monika 1eua")
                    $ cranepilecounter = 0
                    m "Done!"
                    m "Shall we continue?"
                    
                jump mclcranefoldstart
            "Let's stop for now.":
                if cranesessioncounter is 1:
                    m 3fta "Oh, already? Sure."
                    m 1fta "We've stopped pretty early, so it's just the one crane."
                    m 7hta "No rush. The goal of one thousand isn't exactly the quickest goal to strive for."
                    m 4hua "That makes [persistent._mclcranecount] in total."
                    return
                m 5rsa "Sure. Let me put the ones we've made away, and do a quick count..."
                call mas_transition_to_emptydesk
                python:
                    renpy.pause(2.0, hard=True)
                call mas_transition_from_emptydesk("monika 1eua")
                m 1eua "Ok! We've made [cranesessioncounter] paper cranes this session."
                $ _history_list.pop()
                menu:
                    "Anything to say about our progress?":
                        jump cranecount
                    "How many have we made?":
                        m 3esa "In total, we've made [persistent._mclcranecount] paper cranes!"
                        return
                        
    label craneshalfdone:
        $ persistent._mcl_craneshalfdone = True
        m 3mtc "Huh. That felt like it took no time at all."
        m 6guc "{cps=30}...{/cps}{nw}"
        m 3gst "...{fast} yay."
        m 3ssb "Hahah!"
        m 1ekb "Sorry, keeping my face straight like that is a effort."
        m 1nka "I'm happy, of course!"
        m 3gud "It's nice to have hard work pay off."
        m 4eud "What's the longest you've worked towards a goal, [player]?"
        m 5hub "It might be obvious to say, but the sweet payoff for a effort long worked on is a special delight."
        m 7hub "So I'm glad we get to harvest that particular fruit."
        m 7gta "If only we can extend this feeling of satisfaction, huh?"
        show monika
        pause 1.0
        m 3sfb "{i}Well{/i}, one argues that because there's two of us..."
        m 3nfa "... And it wouldn't be fair if I were the only one to get a wish..."
        m 2rfu  "I'd say the work is only halfway done; there's only been five hundred cranes for us both."
        m 4stb "So I guess there's plenty more to go!"
        return
    
    label cranescompleted:
        #cheevo flag
        $ persistent._mcl_achievementcrane = True
        m 7sub "It's done!"
        m 7suo "We've made 2000 paper cranes- "
        if persistent._mclcranecount = 2000:
            m 4suw "- {i}Exactly{/i} 2000 paper cranes, actually!"
            m 4wtd "What a stroke of luck- or were we that detail-oriented?"
        else:
            m 4wtd "- To be precise, [persistent._mclcranecount]!"
        m 4etc "And..."
        m 3ftb "I'm just kinda tired, hahaha!"
        m 3nsp "At some point, it kind of felt like I was doing it just for the sake of doing it."
        m 3dsu "But I'm pretty happy, now that it's all done."
        m 1rsu "All that's left to do now is, well, make that wish."
        m 7tsd "I've never made a wish before, not in this solemn manner."
        m 7gsd "I've never dropped a coin down a wishing well, or made a wish after seeing a shooting star..."
        m 7tta "... And honestly?{w=0.2} I've never made a birthday wish after blowing out candles. Not once."
        m 2dsc "It's always felt a bit too ritualistic to me to really believe in."
        m 2hka "But hey, there's never a bad time to start taking up praying, hahaha."
        m 2rka "All we do now is just spend a few precious moments in silence while we think about what we want to wish for."
        m 2ruc ".{w=0.5}.{w=0.5}."
        m 1etc "So, did you make your wish?"
        $ _history_list.pop()
        menu:
            "I did! I wished for:":
                m 7stw "Ah, shh!"
        m 6nsc "Wishes don't come true if you voice them out loud."
        m 6nsb "Maybe I can guess what it is."
        m 5nsb "You know what *I* wished for?"
        m 5kka "Your happiness."
        $ _history_list.pop()
        menu:
            "Not for us to stay together, or for you to go to the real world, or?...":
                m 6tsc "Hmm."
                m 6esc "There's plenty I could wish for, sure."
                m 2rta "For me to join you in your reality as soon as possible."
                m 2ltd "For us both to live a long life together."
                m 2rtc "For world peace."
                m 2dtu "For my happiness."
                m 1htu "I chose the.{w=0.2}.{w=0.2}. simplest request."
            "Wait, didn't you say stating the wish out loud wouldn't make it work?...":
                m 5rka "..."
                m 5rua "I like defying fate, I suppose."
                m 1ffc "And if you don't make it happen- and I know you'll work on it- I'll make it happen."
                m 7dkc "If you keep that desire close to your chest, whether you say it out loud or not..."
                m 7dkc "It'll be all the more precious for just existing."
                m 5luc "And that's what matters more to me."
                m 5ekb "That the desire for you to be happy is there in the first place."
        m 4ekb "And you know what?"
        m 4eub "I don't think I'm tired of this at all."
        m 3fub "I was worried about it, but even as we speak, I feel a urge to just keep going."
        m 1nua "I'm happy that I'm happy to continue doing this."
        m 7nua "And of course, you're more than welcome to keep folding cranes with me."
        #cheevoflag
        if persistent._mcl_achievementtoggle is True:
            $ renpy.notify ("Achievement: A Queen of Flightless Birds")
        m 5kkbsa "We'll stock up on wishes, as many as we can gather, all for you and I..."
        return
        
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_papercranetopic",
            category=['misc'],
            prompt="Paper Cranes",
            random=True
        )
    )
 
label mcl_papercranetopic:
    m 7hua "I think I've found a way to distract myself, [player]!"
    m 1hua "Recently while exploring the classroom closet, I found stacks of marvelously glossy, coloured construction paper."
    m 4rua "It was so nice, I felt compelled to do {i}something{/i} with it all, you know? It wasn't lined, so I couldn't use it for writing..."
    m 3wub "Then it hit me. I could take up Origami, the art of paper folding!"
    m 1fua "What better way to practise my dexterity... And whittle away the time?"
    m 1dud "'Idle hands are the devil's playthings,' so the saying goes."
    m 1ruc "That said, it does remind me of a Japanese superstition..."
    m 1suc "... That if you make a full one thousand paper cranes, your wish will be granted."
    m 7etc "More specifically, it's attributed to curing sickness and disease."
    m 7gtb "And while I might not be suffering from any illness... Well, it doesn't do any harm for a girl to try to fit the idea to my circumstances."
    m 2rka "... Yeah."
    m 6fta "So once in a while, you'll see me keeping busy making paper cranes."
    m 6hsa "I'll make sure to keep them well-organized and out of sight. Don't worry."
    $ _history_list.pop()
    menu:
        "Can I help?":
            m 7ftd "Well, I am supposed to make them myself."
    m 7hsb "But I also admit I'm not actually keeping myself bound to any rules."
    m 4rsp "Okay. I think I can rig something up..."
    show monika 4dsp
    m 3huu "Alright! You should have the ability to make a crane with a simple click."
    m 3tuu "It should appear under the 'Interact' menu that appears when you want to talk to me through the 'Hey, Monika...' section."
    m 3fuu "If it doesn't appear right away, that's fine. It may take a few restarts."
    m 1nfb "It's good that I've enlisted your help. Now with the two of us, that's only 500 cranes each!"
    m 4tka "Hahaha. Don't worry, [player]. I'm not trying to actively rope you into this."
    m 4hua "If you feel like joining me... Well, that'd be nice.{w=0.2} I like the idea of this as a bonding activity.{w=0.2} We don't get to do a lot of that."
    m 2hua "But no stress if you don't. I love that you're here so I can just show off my work to you."
    m 5hka "And hey, when it's all done, and maybe if I'm lucky..."
    m 5hua "... My wish will actually be granted."
    return "derandom"
    

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_mcl_makecrane",
            conditional="store.seen_event('mcl_papercranetopic')",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_mcl_makecrane:
    $ makecrane = random.randint(3,36)
    $ persistent._mclcranecount += makecrane
    m 6dfa "Fold here, and then fold there..."
    m 6stb "Oh! [player]!"
    m 4wua "Hey, you caught me in another origami-making session!"
    show monika at t21
    show origamitwo at craneframe zorder 13
    m 3tuu "Say hello to [player], Crane!"
    hide origamitwo
    with cranedissolve
    show monika at t11
    m 3nuu "I've managed to make a few paper cranes today, up until you opened up the game."
    m 2hua "I'll just put away the ones I already made.."
    call mas_transition_to_emptydesk
    python:
        renpy.pause(2.0, hard=True)
    call mas_transition_from_emptydesk("monika 1eua")
    m 1rsa "So that's [makecrane] for this batch.."
    m 7lsa ".. And that should be [persistent._mclcranecount] in total!"
    m 5ksu "If you want to make some together, I'd be happy to."
    m 5hsu "Otherwise, we'll start with our time together!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="bye_mcl_makecrane",
            unlocked=True,
            conditional="store.seen_event('mcl_papercranetopic')",
            aff_range=(mas_aff.NORMAL, None)
        ),
        code="BYE"
    )

label bye_mcl_makecrane:
    $ makecrane = random.randint(3,36)
    $ persistent._mclcranecount += makecrane
    m 5hsu "Oh, [player]!"
    m 4tsu "I have a parting gift for you."
    show monika at t21
    show origamione at craneframe zorder 13
    m 3ssb "Ta-da!"
    hide origamione
    with cranedissolve
    show monika at t11
    m 7nubla "I managed to make a couple of friends for them, too!"
    m 7htblb "I've been working on them all day."
    m 3tta "Didn't notice me at work during our time together?"
    m 3subla "What can I say? I have particularly deft hands~"
    m 4ett "Okay, so I've made [makecrane] cranes, I think?"
    m 4gtt "That makes... [persistent._mclcranecount] cranes altogether?"
    m 3ftu "Guess I'll work on some more while you're gone."
    m 1ftu "Bye, [player]!"
    return 'quit'
