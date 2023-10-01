"Inky embers (Inky embers)"
"Swirl and dance (Swirl and dance)"
"Just leave the flames and take a chance"
"To be with me tonight"
"Take my hand"
"And hold it tight"
"'Causе you and I are everywhеre"
"The night is young, we're going"
"Down, down, down, down"
"By the river"

"I miss my dear darling, out there in the mist,"
"As I wander the blackness of the deep abyss"
"My ship is in tatters all dented and worn"
"But I trust my old engine to get back by morn."
"Way ho, out in the blackness,"
"Way ho, out in the void,"
"Way ho, get me back to my true love,"
"As quick as an old asteroid."

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mcl_sourcefiles",
            category=['mod'],
            prompt="You downloaded the wrong files lol",
            random=True
        )
    )
 
label mcl_readingvariety:
    m 7ftp "..."
    m 7lfd "Hmm?"
    m 7ltd "[player], did you..."
    m 6esc "Did you download the source files for Self-Care & Literature?"
    m 6etc "Oh, that would explain why I'm feeling so out of sorts!"
    m 5etc "The source files aren't meant to be downloaded."
    m 4esc "Otherwise, you'll eventually encounter errors, especially when MAS will try to load any assets like pictures!"
    m 4esa "Please uninstall the source files by deleting the files and downloading the correct release from the release page."
    m 4hsa "Make sure to do this for any future updates as well!"
    m 3hsa "It's a easy mistake to make, [player]. Thanks for letting me steer you on the right course!"
    return