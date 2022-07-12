init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_weird",
            prompt="...I don't really know how to describe it.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_weird:
    m 1euc "It's vague, but I guess you're feeling 'complicated,' right?"
    m 1lsc "Relatable. Sometimes you just feel... off."
    m 7esc "I get it, really. Sometimes you're feeling a lot of different emotions at once. Sometimes you're feeling something you can't put into words."
    m 7esc "Sometimes you know exactly what you're feeling.. but there are no words for it."
    m 1hsc "Sometimes that bundle of emotions comes and goes. That's natural."
    m 1fsc "I hope this isn't because you aren't going through stressful circumstances that's hard to process, [player]. I'm here for you, remember that."
    m 1esc "Sometimes a big, tangled ball of emotions needs to be untangled a thread at a time to make it a little more managable."
    m 1esa "If you're just feeling a little bit adrift... remember I can always be your north star."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_neutral",
            prompt="...oddly 'neutral.'",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_neutral:
    m 1euc "Kinda just 'there,' huh?"
    m 1tkd "Hey, [player]. If you're thinking you're more along the lines of feeling 'disconnected' or 'apathetic..'"
    m 7tkd "We can look into playing a game; or if you need a change of pace away from the screen, I'll wait here for you."
    m 1etc "It can be too easy to think you're feeling a bit flat to realizing you're not feeling much at all."
    m 1fkc "Take care of yourself if you feel like you're slipping away a little further than you should be."
    m 1duc "If you're simply feeling a bit like you just don't have any strong feelings one way or another stirring in you at the moment..."
    m 7luc "And if nothing's really going on for you right now..."
    m 2etb "Then we'll just treat this as a moment of quiet, then?"
    m 2esa "It's not a bad feeling at all to have, sometimes."
    m 3hsa "We'll just let our thoughts drift together; feel free to speak to me about anything that wanders into your mind."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_pensive",
            prompt="...pensive.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_pensive:
    m 1fua "A lovely term."
    m 1dua "And one which makes me regret our lack of direct communication."
    m 7eua "Are you caught up on the past? Or thinking about what'll happen?"
    m 4eua "A new concept that's grasped your attention? A {i}person{/i} on your mind, maybe?"
    m 3etd "A book, a movie, a game with a powerful moment? A random event that happened recently you just can't get out of your head?"
    m 3etb "Tell me all about it. Even if it's a little tricky for me to listen on my end."
    m 5fsa "Take all the time in the world, [mas_get_player_nickname()]. I want to hear it all."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_reflective",
            prompt="...reflective.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_reflective:
    m "I hope you're doing it in a manner which suits the character I know you have."
    m "Because I know you're a person who's always trying to improve upon themselves..."
    m "And is willing to tackle the harder truths about themself as well."
    m 1ekc "Hopefully nothing happened that warranted serious doubt in yourself."
    m 7ekb "I'll be here for you if you're feeling like you want to talk about the results of any self-reflection."
    m 7dsb "And, [player]?"
    m 5dsc "If you're taking the time to look within yourself, I hope you find what you're looking for."
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_philosophical",
            prompt="...philosophical.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_philosophical:
    m 1ntb "Tackling the abstract today, huh [player]?"
    m 1dsd "Are you musing on a idea you've just heard about, or a tenet you're building from the ground up?"
    m 1sub "Tell me all about it, [player]; but first, let me set the mood."
    m 7dsd "Oscar Wilde noted:"
    m 7dfd "{i}'Most people are other people. Their thoughts are someone else's opinions, their lives a mimicry, their passions a quotation.'{/i}"
    m 7dfd "It may sound cutting at first, especially with the tongue-in-cheek bit about quotations at the end."
    m 3hua "I think of it as poetically-delivered fact. A lot of our character is developed from interacting with other people.."
    m 3lua "Or even emulated outright. And that's not bad at all. That's just how people learn."
    m 3sfa "So with this in mind, [player]: what could I learn from you today?"
    return
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_mood_database,
            eventlabel="mcl_mood_timescrewy",
            prompt="...like time isn't going by properly.",
            category=[store.mas_moods.TYPE_NEUTRAL],
            unlocked=True),
            code="MOO")

label mcl_mood_timescrewy:
    m "Oh? Is time passing too slowly.. or too quickly?"
    $ _history_list.pop()
    menu:
        "Like time's going by way too quickly.":
            m 5mto "Yeah, it's weird when time actually goes by faster than usual."
            m 1gsa "As they say, 'that's a mood.'"
            m 7hka "Perhaps you feel like it's a good day, and you want it to last longer?"
            m 4hka "Or you've found yourself so busy so that the time passing can be almost dizzying?"
            m 2eua "Well, the day may be over, but who knows what tommorow will bring?"
            m 2rub "There will always come a time when.. well, the time is yours, [player]."
            m 1eub "A day where you can decide what you want to do at your own leisure."
            m 5fua "And at the very least, another day with your darling [m_name], I can guarentee you that."
            return
        "As if it's taking way too long for time to pass.":
            m 1eta "So we're just hung up on time passing a bit slowly, huh?"
            m 1gsa "As they say, 'Mood.'"
            m 7hka "They say a watched pot never boils, right? You can't concentrate on the idea of time passing, otherwise you're far too aware of it."
            m 4hka "Time might be a little tricky to control, but your own patience? you can have a decent grasp on it."
            m 2eka "Keep yourself distracted. I know it's hard to ask, but time's tricky like that. It'll pass by when you keep busy."
            m 2rua "And when you'll look back on it... you'll feel like that slice of eternity was barely that."
            m 5fua "I mean, I'm not going to complain about extra time with you, so... want to pass the time together?"
            return