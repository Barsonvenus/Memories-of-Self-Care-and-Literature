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
            "Monika!"
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
    m 4lkb "So, when that responsibility became overwhelming, I starting thinking in black and white; my failures became resolute, and therefore I didn’t feel like I had properly accomplished anything:"
    m 4lkc "So I felt as frustrated as I did when I left the debate club, at the time feeling like I wanted something new."
    m 1dsc "But failure, is, well, normal. It’s- and still is- hard for me to accept that."
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
    m 7eka "Religion’s more confusing aspects could be hand-waved away if it you think about the system being influenced by one, mysterious being."
    m 1eka "But Karma’s an entire system in itself that’s confusing."
    m 7esa "Both Buddhism and Hinduism are some of the more famously known religions to have Karma as a major tenet."
    m 3esd "Nowadays, people generalize Karma as a “What goes around, comes around” concept. Your bad deeds will eventually get back to you in some way, and likewise good actions will eventually reward you."
    m 3lsc "And it’s not an entirely wrong summary. To summarize very heavily, Karma’s basis is tied in ‘cause and effect.'"
    m "The devils in the details:" 
    m 3rsc "Depending on the religion, Karma’s insturmental in determining your fate. Or secondary."
    m "And as cause and effect can be circular, so does your life; Karma goes hand in hand with reincarnation."
    m "But now we're introducing a bigger concept. Does Karma stack up because of a previous life?"
    m 6dsc "Sometimes. Sometimes not."
    m 4esd "And to complicate things further, Buddhism even allows for transfer of Karma from one being to another, in some cases!"
    m "It overlaps with so many other concepts like free will, but it honestly manages to be more confusing in how its rules contradicts itself alone."
    m 1esc "And it’s hard not to be a little biased."
    m "Yuri," 
    m "Natsuki."
    m 1esc "Sayori."
    m "And I?"
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

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_favouriteword",
            category=['literature'],
            prompt="Do you have a favourite word?",
            pool=True
        )
    )
label mcl_favouriteword:

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
    m 1eua "I think it's definitely easier than people might think."
    m 7eua "Nowadays more and more people are leaning towards diets with lots more variety in them;"
    m 7esb "So, it’s becoming more common to research alternatives to animal products and find them in local markets."
    m 4rsb "I’ve mentioned meat substitutes, and while you might think of say, tofu, or chickpeas- a great source of protein, and a very versatile ingredient-"
    m 7hsu "Nowadays you can find actual plant-based alternatives that attempt to have the same texture and similar taste to meat products."
    m 1esc "It’s a relatively new industry, with plenty of pitfalls- just like farming, the costs and resources needed to mass-produce these can end up causing major complications."
    m 3esc "But as the intent of those products are to eliminate meat, there is a focus on sustainably producing them, so it’s a work in progress with a lot of healthy optimism."
    m 6esu "And it’s worth stressing that there are plenty of foods rich in protein aside from tofu or chickpeas that are vegetarian."
    m 7wsa "And for flavour? Oh, I am absolutely set."
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
    return
    

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
            $ persistent._mcl_pm_surprised = True
            m 2hkt "Eep!"
            if persistent._mcl_pm_surprised:
                m 7fub "[player], again?"
                if persistent._mas_pm_shocked:
                    m 1tkblp "Well, at {i}least{/i} this time you didn't go for the neck." 
                m 1tfblp "Ooh, I'll get you back one of these days!"
                if sesh_shorter_than_3_mins:
                    m "Especially as I noticed this is the {i}first{/i} option you've chosen when you've booted up the game!"
                m 5hub "Hahaha!"
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
            return

default persistent._mcl_pm_surprised = None
default persistent._mcl_pm_shocked = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_surpriseher",
            category=["interact"],
            prompt="Surprise her?",
            conditional="seen_event('sneakapeek')",
            unlocked=False,
            pool=False,
            random=False,
            action=EV_ACT_POOL,
        )
    )
label mcl_surpriseher:
    if not mas_timePastSince(persistent._mcl_last_surprise, datetime.timedelta(minutes=10)):
        "You'd like to try surprising Monika again, but her head is on a swivel since you've just done it."
        "You think it's worth waiting until she's relaxed again; maybe you'll be able to catch her off-guard then?"
        m 1ffa "Don't think I don't notice you! I'm on the lookout for you sneaking about, [player]."
        "Yeah, definitely want to cool it for now."
        return
    "Okay, she hasn't noticed you yet..."
    jump mclsurprisestart
    
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
    m 4tsb "I mean, I was distracted, I guess? People mishear or outright hear things when they’re distracted."
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