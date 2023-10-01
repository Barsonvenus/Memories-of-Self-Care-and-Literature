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
 
label mcl_sourcefiles:
    m 7ftp "..."
    m 7lfd "Hmm?"
    m 7ltd "[player], did you..."
    m 6esc "Did you download the source files for Self-Care & Literature?"
    m 6etc "Oh, that would explain why I'm feeling so out of sorts!"
    m 5etc "The source files aren't meant to be downloaded."
    m 4esc "Otherwise, you'll eventually encounter errors, especially when MAS will try to load any assets like pictures!"
    m 4esa "Please uninstall the source files by deleting the files and downloading the correct release from the {a=https://github.com/Barsonvenus/Memories-of-Self-Care-and-Literature/releases}{i}{u}release page{/u}{/i}{/a}."
    m 4hsa "Make sure to do this for any future updates as well!"
    m 3hsa "It's a easy mistake to make, [player]. Thanks for letting me steer you on the right course!"
    return
